# Desk-validation checklist

Nothing in this repo is validated ground truth until the items below are red-penned
by the author (Michael McGlade, 7 years negotiating ISDA/GMRA documentation at
Tier 1 banks). Until every box relevant to a document is checked, that document's
fate-map stays marked `AWAITING DESK VALIDATION` and no model baselines are
published against it.

## Method (2026-07-21): guided reconstruction, not blank-page recall

The author is 2.5 years off the desk and worked with the bank's playbook to hand —
so validation runs as a structured elicitation, honestly recorded:

1. **Source pack first**: `research/gmra-version-changes-sourced.md` (public,
   cited: ICMA guidance, 2011 Protocol mechanics, law-firm change charts) is read
   BEFORE the checklist — recognition unlocks what recall can't.
2. **Interview, not checklist-alone**: the author answers desk-shaped questions
   ("when a large fund pushed back on X, what was the fallback") rather than
   abstract correctness questions. Episodic memory is the asset being mined.
3. **Three-way verdicts**: each item resolves CONFIRMED (author is sure) /
   SOURCED (author unsure, public source settles it — cite it) /
   OPEN (neither — stays flagged, and the item is either cut from scoring or
   marked contested in the fate-map). Unsure-but-plausible is NOT a pass.
4. **Leverage dimension**: the author's desk was Morgan Stanley — terms were
   near-dictated to small funds/retail banks, genuinely negotiated with peer
   banks and mega-funds. Fate-maps and markup patterns differ by counterparty
   leverage; SYN-001's implied counterparty must be stated, and future corpus
   items should vary this axis deliberately.

## SYN-001 exemplar (corpus/syn-001/)

From the exemplar's own validation asks:

- [ ] Do P1–P8 read like provisions actually seen in the wild (shape, not text)?
      Which are implausible?
- [ ] Is the 2003-vintage fund markup pattern right — would a fund have got the P2
      limb deletion, the P6 FOCB rider?
- [ ] AL1/AL2 realism — were margin re-papers and fails riders done by amendment
      letter, or by full re-execution?
- [ ] What's missing that a real 1995 legacy doc would carry? (The best eval item is
      the one only a former negotiator would think to seed.)

Repo-added items (introduced in structuring, not in the source exemplar):

- [ ] Confirm or correct the derived category taxonomy in `fate-map.yaml`
      (`category` fields were derived from provision names, not authored).
- [ ] Confirm A2–A6 belong in the absent-provision ground truth, and grade their
      severities (currently `TBD-validation`; only A1/AET was explicitly authored
      as a scoreable absence).
- [ ] Grade AL1/AL2 severities (currently `TBD-validation`).
- [ ] Confirm the double-weighting scheme (P2-cascade, P5) and the 0.5
      partial-credit rule for fate-right/cascade-missed.

## Playbook (playbook/gmra-repapering-playbook.md)

Every rule R1–R13 is a hypothesis drafted from public sources. Per rule: confirm,
reject, or re-grade.

- [ ] R1 exposure-calculation regime coherence — plausibility + severity
- [ ] R2 threshold / MTA — plausibility + severity
- [ ] R3 margin call operations — plausibility + severity
- [ ] R4 failure-to-deliver EoD election — plausibility + severity
- [ ] R5 mini close-out mechanics — plausibility + severity
- [ ] R6 AET election — plausibility + severity
- [ ] R7 Act of Insolvency scope/grace — plausibility + severity
- [ ] R8 Default Market Value determination — plausibility + severity
- [ ] R9 close-out set-off breadth — plausibility + severity
- [ ] R10 NAV triggers — plausibility + severity
- [ ] R11 anti-optionality family (incl. whether the FOCB fate reasoning in the
      upgrade track is right) — plausibility + severity
- [ ] R12 Agency Annex architecture — plausibility + severity
- [ ] R13 substitution rights — plausibility + severity

Gaps in the public record (open questions from the playbook draft — answers needed
before the synthetic Annex I details can be treated as desk-plausible):

- [ ] 1. GMRA-specific NAV trigger levels — were ISDA-style 20/30/50 levels also the
      repo norm, or looser given over-collateralisation?
- [ ] 2. Haircut levels by collateral class — desk-plausible ranges for synthetic
      Annex I docs (or key off the FSB minimum-haircut framework as a public floor?)
- [ ] 3. Who calls margin in practice — was one-way margining a live ask?
- [ ] 4. 1995→2000 depth — does GN-2000 Exhibit I match what actually bit in
      upgrade negotiations, or does it understate 1995 pain points (e.g. the 1995
      default-valuation mechanics most renegotiated)?
- [ ] 5. Agency Annex friction — which flashpoints actually generated red-lines
      with pension-fund agents?
- [ ] 6. GMRA 6(j) usage — commonly elected in bank-fund GMRAs? Did funds import
      ISDA-style condition-end-date riders into repo docs? (R11.2 is an analogical
      construction — the ISDA 2014 amendment is ISDA-only.)
- [ ] 7. FOCB confirmation — does "fish or cut bait" deemed-waiver (30–90 days)
      match desk usage, and are the GMRA-side instantiations in section (c) right?
- [ ] 8. Severity calibration — re-grade every rule by expected desk loss; kill any
      rule a fund would never actually push.

## Exit criteria

A document graduates from `AWAITING DESK VALIDATION` when:

1. Every checklist item touching it is resolved (checked, or the entry corrected).
2. `TBD-validation` fields in its fate-map are replaced with graded values.
3. The validation outcome is recorded (what was confirmed, what was changed, what
   was killed) — corrections are part of the artifact, not something to hide.

Only then do model baselines get run and published.
