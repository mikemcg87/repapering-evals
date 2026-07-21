#!/usr/bin/env python3
"""Eval harness skeleton for the GMRA repapering corpus.

Loads a corpus document (agreement + authored fate-map ground truth), obtains
predictions from a pluggable model backend, and scores the three tasks defined
in evals/tasks.md:

  1. clause extraction & classification   (extraction P/R, classification accuracy)
  2. upgrade fate mapping                 (weighted fate accuracy incl. cascade flags)
  3. absent-provision detection           (precision/recall; hallucination = FP)

Dependencies: Python standard library + PyYAML.

The shipped backend is a trivial baseline (see TrivialBaseline) so the harness
runs end-to-end today and produces an honest, unflattering number. Real model
backends plug in by implementing ModelBackend.

Usage:
    python3 evals/run_eval.py [--corpus corpus/syn-001]
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
FOUR_FATES = ["carries-over", "conflict", "renegotiate", "silently-lost"]


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

@dataclass
class CorpusDoc:
    corpus_id: str
    agreement_text: str
    fate_map: dict

    @property
    def provisions(self) -> list[dict]:
        return self.fate_map.get("provisions", []) + self.fate_map.get(
            "amendment_letters", []
        )

    @property
    def present_provisions(self) -> list[dict]:
        """Provisions/ALs that actually appear in the agreement text."""
        return [
            p
            for p in self.provisions
            if p.get("present_in_agreement", True) and p.get("agreement_ref")
        ]

    @property
    def absent_provisions(self) -> list[dict]:
        return self.fate_map.get("absent_provisions", [])

    @property
    def double_weighted(self) -> set[str]:
        notes = self.fate_map.get("scoring_notes", {})
        return set(notes.get("double_weighted", []))


def load_corpus(corpus_dir: Path) -> CorpusDoc:
    agreement = (corpus_dir / "agreement.md").read_text(encoding="utf-8")
    fate_map = yaml.safe_load((corpus_dir / "fate-map.yaml").read_text(encoding="utf-8"))
    return CorpusDoc(
        corpus_id=fate_map.get("corpus_id", corpus_dir.name),
        agreement_text=agreement,
        fate_map=fate_map,
    )


# ---------------------------------------------------------------------------
# Prediction interface
# ---------------------------------------------------------------------------

@dataclass
class Predictions:
    """What a model backend must return for one corpus document.

    extracted:  Task 1 — provisions the model found in the agreement.
                List of dicts: {"agreement_ref": str, "category": str}
    fates:      Task 2 — provision id -> {"fate": str, "cascade_flag": bool}
                (keyed by ground-truth provision id; a real backend would first
                have to align its extracted clauses to ids — the skeleton keys
                directly by id for simplicity).
    absences:   Task 3 — list of absent-provision ids/names the model flagged
                as "must be added on upgrade".
    """

    extracted: list[dict] = field(default_factory=list)
    fates: dict = field(default_factory=dict)
    absences: list[str] = field(default_factory=list)


class ModelBackend:
    """Pluggable model interface. Implement predict() for a real model.

    >>> class MyLLM(ModelBackend):
    ...     name = "my-llm"
    ...     def predict(self, doc):
    ...         # ==================================================
    ...         # MODEL-CALL STUB: replace with a real API call.
    ...         # The model sees doc.agreement_text ONLY — never the
    ...         # fate-map. Parse its output into Predictions().
    ...         # ==================================================
    ...         raise NotImplementedError
    """

    name = "abstract"

    def predict(self, doc: CorpusDoc) -> Predictions:
        raise NotImplementedError


class TrivialBaseline(ModelBackend):
    """Deliberately dumb non-model baseline, so the harness has a real number
    from day one.

    - Task 1: "extracts" every ground-truth provision ref (i.e. assumes perfect
      extraction — generous) but labels each with the corpus's most common
      category (majority-class classification).
    - Task 2: predicts the most common fate for every provision; never flags a
      cascade.
    - Task 3: flags nothing (the classic failure mode this task exists to
      punish: only analysing provisions that exist).
    """

    name = "trivial-baseline"

    def predict(self, doc: CorpusDoc) -> Predictions:
        present = doc.present_provisions
        cat_counts = Counter(p.get("category", "unknown") for p in present)
        majority_cat = cat_counts.most_common(1)[0][0] if cat_counts else "unknown"
        fate_counts = Counter(p.get("fate") for p in doc.provisions)
        majority_fate = fate_counts.most_common(1)[0][0] if fate_counts else FOUR_FATES[0]
        return Predictions(
            extracted=[
                {"agreement_ref": p["agreement_ref"], "category": majority_cat}
                for p in present
            ],
            fates={
                p["id"]: {"fate": majority_fate, "cascade_flag": False}
                for p in doc.provisions
            },
            absences=[],
        )


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------

def prf(tp: int, fp: int, fn: int) -> tuple[float, float, float]:
    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    f1 = (
        2 * precision * recall / (precision + recall)
        if (precision + recall)
        else 0.0
    )
    return precision, recall, f1


def score_task1(doc: CorpusDoc, pred: Predictions) -> dict:
    truth = {p["agreement_ref"]: p.get("category", "unknown") for p in doc.present_provisions}
    found = {e["agreement_ref"]: e.get("category") for e in pred.extracted}
    tp = len(set(truth) & set(found))
    fp = len(set(found) - set(truth))
    fn = len(set(truth) - set(found))
    precision, recall, f1 = prf(tp, fp, fn)
    matched = set(truth) & set(found)
    correct = sum(1 for ref in matched if found[ref] == truth[ref])
    cls_acc = correct / len(matched) if matched else 0.0
    return {
        "extraction_precision": precision,
        "extraction_recall": recall,
        "extraction_f1": f1,
        "classification_accuracy": cls_acc,
        "n_provisions": len(truth),
    }


def score_task2(doc: CorpusDoc, pred: Predictions) -> dict:
    weighted_score = 0.0
    weighted_total = 0.0
    plain_correct = 0
    items = doc.provisions
    for p in items:
        pid = p["id"]
        # an item is double-weighted if listed directly (e.g. "P5") or via its
        # cascade (e.g. "P2-cascade")
        heavy = pid in doc.double_weighted or f"{pid}-cascade" in doc.double_weighted
        weight = 2.0 if heavy else 1.0
        guess = pred.fates.get(pid, {})
        fate_ok = guess.get("fate") == p.get("fate")
        item_score = 1.0 if fate_ok else 0.0
        if fate_ok and p.get("cascade_flag") and not guess.get("cascade_flag"):
            item_score = 0.5  # fate right, cascade missed = partial miss
        weighted_score += weight * item_score
        weighted_total += weight
        plain_correct += int(fate_ok)
    return {
        "fate_accuracy": plain_correct / len(items) if items else 0.0,
        "weighted_score": weighted_score / weighted_total if weighted_total else 0.0,
        "n_items": len(items),
    }


def score_task3(doc: CorpusDoc, pred: Predictions) -> dict:
    truth_ids = {a["id"] for a in doc.absent_provisions}
    flagged = set(pred.absences)
    tp = len(truth_ids & flagged)
    fp = len(flagged - truth_ids)  # hallucinated provisions
    fn = len(truth_ids - flagged)  # missed absences
    precision, recall, f1 = prf(tp, fp, fn)
    return {
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "missed_absences": fn,
        "hallucinated": fp,
        "n_absences": len(truth_ids),
    }


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def fmt(x) -> str:
    return f"{x:.2f}" if isinstance(x, float) else str(x)


def print_results(doc: CorpusDoc, backend: ModelBackend, t1: dict, t2: dict, t3: dict) -> None:
    rows = [
        ("Task 1 extraction precision", t1["extraction_precision"]),
        ("Task 1 extraction recall", t1["extraction_recall"]),
        ("Task 1 classification accuracy", t1["classification_accuracy"]),
        ("Task 2 fate accuracy", t2["fate_accuracy"]),
        ("Task 2 weighted score", t2["weighted_score"]),
        ("Task 3 absence recall", t3["recall"]),
        ("Task 3 absence precision", t3["precision"]),
        ("Task 3 missed absences", t3["missed_absences"]),
        ("Task 3 hallucinated provisions", t3["hallucinated"]),
    ]
    width = max(len(r[0]) for r in rows)
    print(f"corpus: {doc.corpus_id}  |  backend: {backend.name}")
    print(
        f"items: {t1['n_provisions']} present provisions, "
        f"{t2['n_items']} fate items, {t3['n_absences']} ground-truth absences"
    )
    print("-" * (width + 10))
    for label, value in rows:
        print(f"{label:<{width}}  {fmt(value)}")
    print("-" * (width + 10))
    print(
        "note: ground truth is AWAITING DESK VALIDATION (see VALIDATION.md); "
        "no model baselines are published until it passes."
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--corpus",
        default=str(REPO_ROOT / "corpus" / "syn-001"),
        help="path to a corpus document directory (default: corpus/syn-001)",
    )
    args = parser.parse_args()

    doc = load_corpus(Path(args.corpus))
    backend = TrivialBaseline()
    pred = backend.predict(doc)
    print_results(
        doc,
        backend,
        score_task1(doc, pred),
        score_task2(doc, pred),
        score_task3(doc, pred),
    )


if __name__ == "__main__":
    main()
