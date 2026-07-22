# repapering-evals

Research prototype for evaluating LLM performance on legal repapering — specifically,
upgrading legacy GMRA 1995 repo agreements to GMRA 2000/2011 terms. The current
fate-map is a source-anchored draft, not validated ground truth.

Built by Michael McGlade: 7 years negotiating ISDA/GMRA documentation at Tier 1
investment banks, now an AI engineer.

## Why eval-first

You cannot measure whether a model can do repapering analysis without knowing the
right answers, and for legal documents nobody publishes the right answers. Scraped
agreements come with no ground truth: you'd be guessing what happens to each clause
on upgrade, then scoring a model against your guess.

So the corpus is being built the other way round: synthetic agreements are drafted
together with **candidate** upgrade fate-maps anchored to public sources (the 2011
GMRA Protocol, ICMA guidance notes, and the Clifford Chance 2000→2011 change chart).
Those candidates do not become ground truth until the author completes a recorded
desk-validation pass. No ICMA standard text is reproduced; provisions are
paraphrase-style with paragraph references only.

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
- **`interviews/`** — the template and, once completed, anonymized elicitation
  sessions. No session has been completed yet; "I don't remember" will be retained
  as a valid answer.
- **`research/gmra-version-changes-sourced.md`** — the cited source pack:
  1995→2000→2011 change mechanics from primary sources, plus a census of where
  negotiation practice is actually documented (short answer: barely anywhere —
  which is why this corpus might matter).
- **`CONTRIBUTING.md`** — an open invitation to refutation: if you negotiated
  these documents and something here smells wrong, that issue is worth more
  than any star.

The source work has already exposed one useful distinction: practitioner literature
confirms "FOCB" as a real buy-side term across trading agreements, including repo,
while the specific GMRA condition-precedent rider drafted into SYN-001 remains OPEN.
The existence of a term does not validate a particular clause construction.

## Corpus methodology

- Each corpus document is a synthetic legacy pack: a GMRA 1995 fact pattern with
  Annex I elections, bespoke riders, and amendment letters
  (`corpus/<id>/agreement.md`).
- Its candidate ground truth is a draft fate-map (`corpus/<id>/fate-map.yaml`): per
  provision, a proposed fate under upgrade — `carries-over` / `conflict` /
  `renegotiate` / `silently-lost` — with reasoning and public-source citations, plus an
  `absent_provisions` list of things a 1995 doc lacks that the upgrade must
  affirmatively address.
- Some candidate items are deliberately *invisible*. For replacement 2011 paper,
  SYN-001's silence on automatic close-out creates an AET election decision; under a
  Protocol Annex 1 retrofit, AET is instead deemed specified. Task 0 must distinguish
  those routes before this item can be scored.
- SYN-001 is deliberately conflict-dense; planned siblings are mostly-clean so the
  eval punishes over-flagging as well as under-flagging.

The negotiation playbook the corpus is seeded from lives in
`playbook/gmra-repapering-playbook.md` — a working draft built entirely from cited
public sources, every rule awaiting desk validation.

## Eval tasks

Defined precisely in `evals/tasks.md`; scored by `evals/run_eval.py`:

0. **Upgrade-route identification** — distinguish a Protocol retrofit, bilateral
   amendment, and replacement 2011 agreement before assigning clause fates. This gate
   is not yet implemented in the harness.
1. **Clause extraction & classification** — find the bespoke provisions, label them
   (extraction precision/recall; classification accuracy).
2. **Upgrade fate mapping** (flagship) — predict each provision's fate under the
   1995→2011 upgrade, scored against the fate-map, with double weighting on the
   expensive failures (SYN-001: the Act-of-Insolvency cascade and the invisible AET
   flip) and partial credit rules for fate-right-but-cascade-missed.
3. **Absent-provision detection** — list what must be *added* on upgrade. Failing
   to flag a listed absence is a miss; hallucinating a needed provision that isn't
   in the ground truth is a false positive.

`evals/run_eval.py` runs on the standard library + PyYAML, with a model-backend
interface and a clearly marked stub. Its shipped diagnostic is deliberately
oracle-assisted: it reads the candidate fate-map to exercise the scoring path. It is
not a valid model baseline and must not be presented as one.

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
- The only number so far is a development-only scoring diagnostic, verbatim from
  `python3 evals/run_eval.py --allow-unvalidated`:

```
corpus: SYN-001  |  backend: oracle-assisted-diagnostic
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

The diagnostic is handed the candidate provision list and derives its majority class
from the same unvalidated document, so its 1.00 extraction and 0.60 fate accuracy are
not evidence of model performance. They only prove that the loader, scorer and report
path run end to end, while also exposing the current corpus imbalance.

## Repo layout

```
corpus/syn-001/agreement.md    synthetic GMRA 1995 pack (model input)
corpus/syn-001/fate-map.yaml   source-anchored candidate truth (not yet scoreable)
playbook/                      negotiation playbook draft (public-source, unvalidated)
evals/tasks.md                 task definitions and scoring rules
evals/run_eval.py              runnable harness, oracle-assisted diagnostic included
METHODOLOGY.md                 expert elicitation as ground-truth authoring
interviews/                    elicitation template; first session pending
research/                      cited source pack + practitioner-source census
VALIDATION.md                  the author's desk-validation checklist
CONTRIBUTING.md                refutation invitation for practitioners
```

## License

MIT — see `LICENSE`.
