# repapering-evals

Evaluating LLM performance on legal repapering — specifically, upgrading legacy
GMRA 1995 repo agreements to GMRA 2000/2011 terms — with authored ground truth.

Built by Michael McGlade: 7 years negotiating ISDA/GMRA documentation at Tier 1
investment banks, now an AI engineer.

## Why eval-first

You cannot measure whether a model can do repapering analysis without knowing the
right answers, and for legal documents nobody publishes the right answers. Scraped
agreements come with no ground truth: you'd be guessing what happens to each clause
on upgrade, then scoring a model against your guess.

So the corpus is built the other way round: **synthetic agreements whose upgrade
fate-maps are authored by a domain expert at the same time as the documents
themselves.** Every bespoke provision is written together with its ground-truth fate
under a 1995→2011 upgrade, anchored to public sources (the 2011 GMRA Protocol's
"Preservation of Express Provisions" mechanics, the ICMA guidance notes, the
Clifford Chance 2000→2011 change chart). No ICMA standard text is reproduced;
provisions are paraphrase-style with paragraph references only.

This is the same discipline as my RAG repo
([local-ai-legal-package-assistant](https://github.com/mikemcg87/local-ai-legal-package-assistant)):
authored fixtures, absent-provision questions where "not present" is the passing
answer, and honest baselines published even when unflattering.

## Where does ground truth come from? (the actual hard problem)

Authored ground truth needs an author who knows the answers — and GMRA
negotiation knowledge lives almost nowhere public: member-only ICMA
working-group minutes, a handful of practitioner books, and negotiators' heads.
The author is a former negotiator, 2.5 years off the desk. Rather than pretend
that's not a complication, this repo publishes its way through it:

- **`METHODOLOGY.md`** — expert elicitation as ground-truth authoring: every
  fact earns `CONFIRMED` (desk memory), `SOURCED` (public citation), or `OPEN`
  (flagged, cut from scoring, or contested). "Unsure but plausible" is not a
  grade.
- **`interviews/`** — the elicitation sessions themselves, published
  (anonymized). The provenance trail is part of the artifact, including the
  "I don't remember" answers.
- **`research/gmra-version-changes-sourced.md`** — the cited source pack:
  1995→2000→2011 change mechanics from primary sources, plus a census of where
  negotiation practice is actually documented (short answer: barely anywhere —
  which is why this corpus might matter).
- **`CONTRIBUTING.md`** — an open invitation to refutation: if you negotiated
  these documents and something here smells wrong, that issue is worth more
  than any star.

This method has already earned its keep once: the corpus's "FOCB" rider looked
like a candidate hallucination — unconfirmable from any ICMA or standard
material — until practitioner literature confirmed it as a real fund-side
markup term that simply never appears in standard text. Standard text versus
negotiated markup is exactly the distinction these evals test; the method
tripped over a live example in its own corpus.

## Corpus methodology

- Each corpus document is a synthetic legacy pack: a GMRA 1995 fact pattern with
  Annex I elections, bespoke riders, and amendment letters
  (`corpus/<id>/agreement.md`).
- Its ground truth is an authored fate-map (`corpus/<id>/fate-map.yaml`): per
  provision, its fate under upgrade — `carries-over` / `conflict` / `renegotiate` /
  `silently-lost` — with reasoning and public-source citations, plus an
  `absent_provisions` list of things a 1995 doc lacks that the upgrade must
  affirmatively address.
- The hardest ground-truth items are deliberately *invisible*: SYN-001's flagship
  item is the agreement's silence on automatic close-out, which the 2011 version
  flips into an elective AET — a reviewer that only analyses provisions that exist
  will miss it, which is the point.
- SYN-001 is deliberately conflict-dense; planned siblings are mostly-clean so the
  eval punishes over-flagging as well as under-flagging.

The negotiation playbook the corpus is seeded from lives in
`playbook/gmra-repapering-playbook.md` — a working draft built entirely from cited
public sources, every rule awaiting desk validation.

## Eval tasks

Defined precisely in `evals/tasks.md`; scored by `evals/run_eval.py`:

1. **Clause extraction & classification** — find the bespoke provisions, label them
   (extraction precision/recall; classification accuracy).
2. **Upgrade fate mapping** (flagship) — predict each provision's fate under the
   1995→2011 upgrade, scored against the fate-map, with double weighting on the
   expensive failures (SYN-001: the Act-of-Insolvency cascade and the invisible AET
   flip) and partial credit rules for fate-right-but-cascade-missed.
3. **Absent-provision detection** — list what must be *added* on upgrade. Failing
   to flag a listed absence is a miss; hallucinating a needed provision that isn't
   in the ground truth is a false positive.

`evals/run_eval.py` runs on the standard library + PyYAML, with a pluggable model
backend (the model-call stub is clearly marked). It ships with a trivial baseline —
majority-class everywhere, flag no absences — so there is a real number in this
README from day one.

## STATUS — read this before citing anything here

- **Corpus n=1.** SYN-001 is the only document. It is the quality template, not a
  benchmark.
- **Desk validation pending.** SYN-001's fate-map and the playbook were drafted
  from public sources; the author's red-pen pass (plausibility, severity grading,
  "would a fund actually push there") is tracked in `VALIDATION.md` and has not
  been completed. Every `AWAITING DESK VALIDATION` and `TBD-validation` marker in
  this repo means exactly that.
- **No model baselines published yet.** They land after validation — scoring models
  against unvalidated ground truth would just be scoring them against guesses,
  which is the failure mode this repo exists to avoid.
- The only number so far is the trivial (non-model) baseline, verbatim from
  `python3 evals/run_eval.py`:

```
corpus: SYN-001  |  backend: trivial-baseline
items: 9 present provisions, 10 fate items, 6 ground-truth absences
----------------------------------------
Task 1 extraction precision     1.00
Task 1 extraction recall        1.00
Task 1 classification accuracy  0.11
Task 2 fate accuracy            0.60
Task 2 weighted score           0.50
Task 3 absence recall           0.00
Task 3 absence precision        0.00
Task 3 missed absences          6
Task 3 hallucinated provisions  0
----------------------------------------
```

That baseline is generous on extraction (it is handed the ground-truth provision
list) and still scores 0.60 on fate accuracy just by answering "renegotiate" to
everything — which tells you the corpus needs its mostly-clean sibling documents
before fate accuracy means much. It misses all six absences, because it only looks
at provisions that exist. Both are exactly the honest numbers a trivial baseline
should produce.

## Repo layout

```
corpus/syn-001/agreement.md    synthetic GMRA 1995 pack (model input)
corpus/syn-001/fate-map.yaml   authored ground truth (model never sees this)
playbook/                      negotiation playbook draft (public-source, unvalidated)
evals/tasks.md                 task definitions and scoring rules
evals/run_eval.py              runnable harness, trivial baseline included
METHODOLOGY.md                 expert elicitation as ground-truth authoring
interviews/                    the elicitation sessions, published (anonymized)
research/                      cited source pack + practitioner-source census
VALIDATION.md                  the author's desk-validation checklist
CONTRIBUTING.md                refutation invitation for practitioners
```

## License

MIT — see `LICENSE`.
