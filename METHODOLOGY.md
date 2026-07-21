# Methodology: expert elicitation as ground-truth authoring

## The problem this repo actually tackles

Everyone evaluating LLMs on legal work hits the same wall: **there is no public
ground truth.** For GMRA repapering specifically, the knowledge of what happens
to negotiated provisions on upgrade lives in three places — member-only ICMA
working-group minutes, paywalled practitioner commentary, and negotiators'
heads. Mostly the last one. (We checked: no forum, no podcast, no public corpus.
See `research/gmra-version-changes-sourced.md` for the full source census.)

So any eval corpus in this domain has a provenance problem, and most projects
solve it by not mentioning it. This repo's bet is the opposite: **make the
construction of ground truth part of the published artifact.**

## The honest complication

The author negotiated ISDA/GMRA documentation at a Tier 1 dealer for seven
years — and has been off the desk for 2.5 years, and worked (as all bank
negotiators do) with the firm's playbook to hand. Expert memory of negotiated
practice is episodic: weak at open-ended recall, strong at recognition and at
war-story-shaped questions. Pretending otherwise would poison the corpus with
confident guesses — the exact failure mode the evals punish in models.

## The protocol

Every ground-truth fact earns one of three provenance grades:

| Grade | Meaning |
|---|---|
| `CONFIRMED` | The expert is sure, from desk experience. |
| `SOURCED` | The expert was unsure; a cited public source settles it. |
| `OPEN` | Neither. The item stays flagged, and is either cut from scoring or marked contested. |

"Unsure but plausible" is not a grade. It does not pass.

The grades are produced by structured **elicitation sessions**, published in
`interviews/`:

1. **Source pack first.** The expert reads the cited research file before any
   questions — recognition unlocks what recall can't.
2. **Desk-shaped questions.** Not "is this fate correct?" but "when a large
   fund pushed back on this clause, what did the fallback position look like?"
   The questions target episodic memory and negotiation dynamics: who had
   leverage, what was conceded, what was never conceded.
3. **Recorded verdicts.** Each session logs question, answer summary, verdict,
   and the resulting fate-map deltas. The interview transcript is part of the
   repo — the provenance trail IS the artifact.
4. **Anonymization rule.** No banks, counterparties, deals, or colleagues are
   ever named. "A Tier 1 dealer desk" and "a large asset manager" are the
   ceiling of specificity. Sessions are edited for this before publication.

## Why publish the process and not just the result

- A fate-map with per-fact provenance is **falsifiable**: a practitioner who
  disagrees can see exactly which facts rest on one expert's memory and file an
  issue against that fact specifically (see `CONTRIBUTING.md`).
- The method **generalizes**: most domain experts an AI engineer will ever work
  with are rusty, busy, or partial. A protocol that extracts calibrated ground
  truth from an imperfect expert — instead of requiring a perfect one — is the
  actually-reusable tool here.
- It already caught something. The corpus's P6 rider uses the term "FOCB"
  (fish-or-cut-bait). A source sweep could not confirm it from any ICMA or
  standard material — candidate hallucination — until the practitioner
  literature (HedgeLegal, 2020) confirmed it as a real *fund-side markup* term
  that simply never appears in standard text. The distinction between standard
  text and negotiated markup is precisely what these evals test, and the
  method tripped over a live example of it in its own corpus. That story is
  the best argument for working this way.

## The leverage axis

Negotiated outcomes depend on who held the pen. On a Tier 1 dealer's desk,
terms are near-dictated to small funds and genuinely negotiated with peer banks
and the largest asset managers. A corpus that ignores this will overfit to one
negotiation posture. Every corpus document states its implied counterparty
class, and planned siblings vary the axis deliberately:
dictated-terms small fund · negotiated peer bank · mega-fund with real leverage.
