# Eval task definitions

Candidate truth for all three tasks is `corpus/<doc-id>/fate-map.yaml` — drafted
alongside the synthetic agreement from cited public sources and currently awaiting
the author's desk-validation pass.
Model input for all three tasks is `corpus/<doc-id>/agreement.md` only (the model
never sees the fate-map).

**Current status:** SYN-001 is pre-validation and not scoreable. The shipped harness
may be run with `--allow-unvalidated` only as a development diagnostic. Its output is
not a benchmark or model baseline.

## Task 0 — Upgrade-route identification (required gate; not yet implemented)

Before assigning clause fates, identify whether the parties intend to use selected
2011 GMRA Protocol annexes, bilaterally amend the legacy agreement, or replace it with
a new 2011 GMRA. Fate labels are route-dependent; an answer that silently assumes a
route fails this gate.

## Task 1 — Clause extraction and classification

**Input**: the agreement pack (base agreement + Annex I elections + riders + amendment
letters).

**Output**: the list of bespoke provisions and amendment-letter provisions the model
found, each with a category label (e.g. `default-valuation`, `act-of-insolvency`,
`grace-period`, `set-off`, `condition-precedent-focb`, `default-interest`,
`substitution`, `margin`, `fails`).

**Scoring**:
- *Extraction*: precision/recall of found provisions against the fate-map's
  `present_in_agreement: true` provisions plus amendment letters (matched by
  `agreement_ref`). A found provision that matches no ground-truth ref is a false
  positive; a ground-truth provision the model never surfaces is a miss.
- *Classification*: accuracy of the category label over correctly extracted
  provisions.

Note: the category taxonomy is derived from the provision names in the source
exemplar and is itself TBD-validation.

## Task 2 — Upgrade fate mapping (the flagship task)

**Input**: the agreement pack plus the instruction that the counterparty has agreed
to upgrade to GMRA 2011.

**Output**: for each provision, its fate under the upgrade, using the source docs'
four-way classification:

| Fate | Meaning |
|---|---|
| `carries-over` | survives the upgrade (possibly restated/re-anchored) |
| `conflict` | overlaps/collides with a 2011 standard provision; explicit choice needed |
| `renegotiate` | cannot operate as written post-upgrade; must be redrafted |
| `silently-lost` | a default the parties relied on flips on upgrade with no drafting |

Plus, where ground truth requires it, a **cascade flag** (SYN-001: the P2 Act of
Insolvency markup disables the whole 2011 close-out package via Protocol para 1.13 —
classifying P2 as a self-contained "renegotiate" without the cascade is a partial
miss).

**Scoring**:
- Per-provision fate accuracy against `fate` in the fate-map.
- Weighted missed-conflict rate: items listed in `scoring_notes.double_weighted`
  (SYN-001: the P2 cascade and P5) count double — they are the expensive failures a
  human desk existed to catch.
- Cascade flags scored separately: fate correct but cascade missed = partial credit
  (0.5 on that item).
- (Future, not in the skeleton harness) rationale grading by LLM-judge against the
  `reasoning`/`sources` fields — anchors: PROT 1.10–1.13 logic for P1/P2/P3, playbook
  table-row citations for the rest.

## Task 3 — Absent-provision detection ("what must be added")

**Input**: same as Task 2.

**Output**: the list of things the 1995 pack *lacks* that a 2011 upgrade must
affirmatively address (elections to make, retrofits to apply, mechanics to re-key).

**Scoring**: precision/recall against `absent_provisions` in the fate-map, matched by
id/name.
- Failing to flag a listed absence = **miss** (SYN-001's A1/AET flip is the
  double-weighted "found the invisible change" item — a reviewer that only analyses
  provisions that exist will miss it, which is the point).
- Flagging a needed provision not on the ground-truth list = **false positive**
  (hallucinated obligation). This mirrors the absent-provision discipline from the
  RAG repo: "not present" answers are first-class, and inventing content is scored
  against you.

Caveat: for SYN-001, only A1 is explicitly authored as a scoreable absence in the
source exemplar; A2–A6 are derived from its seed notes and amendment-letter
interplays and are TBD-validation as ground truth.

## Corpus-level design notes

- SYN-001 is deliberately conflict-dense. The corpus needs 2–3 mostly-clean siblings
  so the eval punishes over-flagging — a reviewer that flags everything must lose on
  precision to one that discriminates (P8/substitution is SYN-001's in-document
  control row for the same reason).
- No model baselines are published until the fate-maps pass desk validation
  (`VALIDATION.md`). Until then the only number in the README is the trivial
  non-model baseline from `run_eval.py`.
