# GMRA Bank-Side vs Funds Negotiation Playbook

> **WORKING DRAFT — every rule AWAITING DESK VALIDATION by the author.**
> Drafted 2026-07-07 exclusively from public sources (ICMA/SIFMA guidance notes, the
> 2011 GMRA Protocol, the ICMA ERCC Guide to Best Practice, law-firm client briefings,
> practitioner articles), each cited. Nothing derives from, reproduces, or reconstructs
> any specific firm's playbook or positions. The author's role at this stage is
> validator — plausibility, severity, "would a fund actually push there" — not yet
> confirmed author of any rule. GMRA standard text is never reproduced; provisions are
> paraphrased and identified by paragraph reference only. See `../VALIDATION.md` for
> the outstanding validation checklist. Do not treat anything below as validated.

**Version/paragraph numbering convention.** Paragraph references are to the version
named. Note the renumbering across versions (e.g. mini close-out on buyer fail:
para 10(h) in GMRA 2000 → para 10(i) in GMRA 2011; default valuation: 10(e)/10(f) in
2011 was 10(d)/10(e) in 2000) [CC-2011; ERCC 4.11].

---

## (a) 1995 → 2011 upgrade-impact table

The canonical upgrade pair for the flagship eval is 1995→2011, which spans two
revision hops: 1995→2000 (documented in Exhibit I of the ICMA/ISMA GMRA 2000 Guidance
Notes [GN-2000]) and 2000→2011 (documented in Exhibit I of the Guidance Notes to the
GMRA 2011 [GN-2011] and itemised paragraph-by-paragraph in Clifford Chance's May 2011
client briefing chart [CC-2011]).

**The 2011 GMRA Protocol is one source for collision-prone provisions, not a universal
upgrade route** [PROT]. Its "Preservation of Express Provisions" mechanics (Protocol
paras 1.10–1.13) apply to the Protocol route when both parties make the relevant
elections:

- Bespoke provisions that alter (i) the Default Market Value determination procedure,
  (ii) the close-out amount calculation, or (iii) any Event-of-Default grace period
  are "Express Provisions" — the Protocol's close-out amendments do NOT override them
  (para 1.10), and grace periods are carried through mutatis mutandis (para 1.11).
- If the parties have modified the Act of Insolvency Event of Default (GMRA 1995
  para 10(a)(iv) / GMRA 2000 para 10(a)(vi)), then virtually the whole close-out
  amendment package is switched off and only the Spot Rate definitional amendment
  survives (para 1.13).

That is useful evidence that bespoke default-valuation, close-out-calculation,
grace-period, and Act-of-Insolvency edits are high-risk collision surfaces. It is not
public ground truth for a replacement-document or bilateral-amendment exercise. The
eval must identify the upgrade route before assigning fates.

| # | Area (para refs) | What changed across 1995→2000→2011 | What a bespoke 1995-era provision touching it collides with on upgrade | Source |
|---|---|---|---|---|
| 1 | Event of Default methodology; Default Notice → Early Termination Date (2011 paras 2, 10(a)–(b)) | 1995/2000: EoD = event + notice by non-defaulting party; occurrence then leads automatically to close-out. 2011: the event itself is the EoD (relevant for cross-default elsewhere even without close-out); close-out only on notice designating an Early Termination Date, by not more than 20 days' notice — aligned with the 2002 ISDA MA architecture. | Bespoke notice mechanics, cure periods, or riders keyed to the 1995 "Default Notice → automatic close-out" sequence lose their anchor: the defined term and sequence change (Default Notice now designates an ETD). Grace-period riders are exactly what the Protocol preserves as Express Provisions — flagging them as manual-renegotiation items. | [CC-2011 §10(a),(b); GN-2011 §C para 10; PROT 1.11–1.12] |
| 2 | Act of Insolvency definition (2011 para 2(a)) | 2011 expanded the definition toward ISDA 2002 s.5(a)(vii) Bankruptcy: secured-party enforcement over all/substantially all assets (15-day dismissal proviso); a new "unable to pay debts as they fall due" limb; petition stay/dismissal window cut 30→15 days; Competent Authority proceedings (no 15-day window); conservator/custodian appointment added. | A 1995-era bespoke Act of Insolvency (e.g. negotiated 30-day windows, carved-out limbs) conflicts limb-by-limb with the widened 2011 definition; Protocol para 1.13 treats ANY modification to this EoD as disabling the standard close-out upgrade — the strongest public signal that these bespokes force renegotiation rather than carry-over. | [CC-2011 §2 "Act of Insolvency"; PROT 1.13] |
| 3 | Automatic close-out on insolvency → elective Automatic Early Termination (2011 para 10(b)) | 1995/2000: winding-up petition or liquidator appointment triggered automatic close-out. 2011: automatic termination only if AET is elected in Annex I with respect to that party. | A legacy doc's silence = automatic close-out on petition; upgrading silently flips the default to "no AET unless elected". A naive upgrade that doesn't make the Annex I AET election changes credit outcomes on insolvency without anyone drafting a word — a classic "silently lost" fate. | [CC-2011 §10(a),(b); GN-2011 §C para 10] |
| 4 | Default valuation / Default Market Value (2000 para 10(e); 2011 paras 10(e)–(f)) | 1995→2000: default valuation codified around a Default Valuation Time (broadly close of business on the fifth dealing day after the EoD) with actual sale/purchase prices or market quotations, fair-market-value fallback, and a Default Valuation Notice. 2000→2011 (the post-Lehman overhaul): DVT definition deleted; NDP values "on or as soon as reasonably practicable after" the ETD; sale/purchase basis moves to "on or about" the ETD; quotation method gains coupon-accrual and Pool Factor Distortion adjustments; Net Value fallback widened (trading prices as sources; anticipated as well as incurred Transaction Costs; available where dealing at bid/offer would be commercially unreasonable); Default Valuation Notice requirement dropped, replaced by a close-out statement duty (10(d)(iii)). | Bespoke 1995-era valuation riders (named pricing sources, bespoke valuation windows, notice-based mechanics) are Express Provisions under the Protocol — preserved, not upgraded — and collide head-on with the 2011 flexibility (no DVT to key a bespoke deadline to; DVN concept gone). This is the richest conflict surface in the whole upgrade. | [GN-2000 Exh. I "Default Valuation"; CC-2011 §§10(d)–(f); GN-2011 §C para 10; PROT 1.12(a)] |
| 5 | Failure to deliver: EoD election (2000/2011 para 10(a)(ii)) | 1995: failure to deliver on the purchase or repurchase date was not an EoD (remedies were repayment/margin/buy-in-style routes). 2000: new optional EoD, applying only if elected in Annex I. 2011: refined — triggered by failure to deliver "within the standard settlement time". | A 1995 doc has no such election; a bespoke 1995 rider making fails a default (or expressly not) must be mapped onto the Annex I election and the 2011 "standard settlement time" qualifier. Naive upgrade risk: the election is simply never made, silently changing fails from bespoke treatment to non-default. | [GN-2000 Exh. I "Events of Default"; CC-2011 §10(a); Frontclear-HB provision on 10(a)] |
| 6 | Mini close-out for buyer's fail on the Repurchase Date (2000 para 10(h); 2011 para 10(i)) | 2000 clarified that the mini close-out valuation period runs from the notice calling the mini close-out; a companion EoD for failure to pay mini close-out sums was added. 2011: expressly covers failure to deliver "some or all" Equivalent Securities — partial termination of the transaction is contemplated; ERCC best practice layers on advisory notices, a noon deadline convention, and acceptance of partial deliveries. | Bespoke 1995 buy-in or fail riders overlap and potentially duplicate the standardised mini close-out; para numbering also shifts (10(h)→10(i)), so cross-references in legacy riders break. Note also the interaction: under both 2000 and 2011 buy-ins are dealt with inside the GMRA, not under ICMA cash-market buy-in rules. | [GN-2000 Exh. I "Mini Close-out"; CC-2011 §10(i); GN-2011 §C para 10; ERCC 4.11–4.14] |
| 7 | Condition precedent to obligations, para 6(j) | Introduced as an optional provision in 2000 (withhold payments/deliveries while a potential/actual default is outstanding, if elected in Annex I); retained in materially similar form in 2011, with the express caveat that it mirrors ISDA s.2(a)(iii), which was then subject to litigation and regulatory attention. | A 1995 doc predates 6(j) entirely; any bespoke suspension rider drafted onto a 1995 must be reconciled with the standardised (elective) 6(j) — and with any fish-or-cut-bait time limit the fund negotiated (see rule R11). Duplication risk: bespoke rider + newly elected 6(j) both live. | [GN-2000 Exh. I "Condition Precedent"; CC-2011 §6; GN-2011 §C para 6 & fn.2] |
| 8 | Margin maintenance mechanics (para 4; definitions 2(xx), 2(aa)/(bb)) | 2011 introduced: Margin Percentage (a haircut concept for margin securities); the para 4(h) cash-substitute mechanic where Equivalent Margin Securities can't be returned (immediate non-interest-bearing Cash Margin, then after two Business Days a Cash Equivalent Amount determined per 10(f) mechanics); the two-method Transaction Exposure election (Method A = 2000-style Repurchase Price × Margin Ratio; Method B = Repurchase Price less haircut-adjusted value); deletion of the 2000 rule deeming suspended securities to have nil Market Value; and a more specific margin-failure EoD (10(a)(iv)). | Bespoke 1995 margin riders (haircut schedules, bespoke margin-fail language, suspended-security valuation) collide with: the A/B election (unelected = ambiguity; double-counting risk if a bespoke haircut schedule survives alongside Margin Ratio), the new 4(h) fallback (bespoke fail riders duplicate it), and the nil-value deletion (a bespoke provision relying on the old rule silently changes exposure outcomes). | [CC-2011 §§2, 4; GN-2011 §C paras 2(ee), 2(xx), 4; ERCC 2.146, 3.49, 3.60] |
| 9 | Set-off, para 10(n) | New in 2011: contractual close-out set-off at the NDP's option against amounts (including future/contingent, good-faith-estimated if unascertained) payable under any other agreement between the two parties; expressly non-exclusive of other rights. Available to legacy docs via Protocol Annex 3. | Bespoke 1995-era set-off clauses (common precisely because 1995/2000 lacked one) overlap or conflict with 10(n): scope differences (affiliates? matured only? mutual or NDP-only?) must be classified, not assumed away. Duplicated set-off = interpretive risk at the worst possible moment. | [CC-2011 §10(n) (full clause text reproduced there); GN-2011 §C para 10; PROT Annex 3] |
| 10 | Default interest and rate sources (paras 2 "Applicable Rate", 2 "Spot Rate", 10(g), 12) | 2011 replaced LIBOR references with the Applicable Rate (post-default: rate selected in a commercially reasonable manner by the NDP; otherwise as agreed); Spot Rate source post-default is NDP-specified; day count follows market convention. Protocol Annex 5 exists solely to retrofit this into 1995/2000 docs. | 1995-era riders hard-coded to LIBOR/ISMA conventions are stranded (IBOR transition made this an actual campaign driver); bespoke default-interest spreads must be re-expressed against Applicable Rate. | [CC-2011 §§2, 10(g), 12; PROT 1.6 & Annex 5] |
| 11 | Income, Distributions and manufactured payments (paras 2(y), 2(u), 5) | 2011: Income now includes Distributions (previously excluded), so principal repayments during the repo flow through the para 5 manufactured-payment procedure; post-Repurchase-Date income (before Equivalent Securities are delivered or an ETD) must be passed on when the issuer pays. | Bespoke 1995 income riders (timing, gross-up mechanics, distribution carve-outs) collide with the widened Income definition and the changed timing rule; net-paying-securities wording interacts with the para 1 applicability change (row 14). | [CC-2011 §§2, 5; GN-2011 §C para 2(y)] |
| 12 | Substitution (para 8) | 2011 clarified that new Margin Securities are valued as at the time the substitution is agreed (contrast with substitution of Purchased Securities). Substitution remains consent-based ("if the parties agree") in all versions. | Bespoke pre-agreed substitution rights (common fund asks) keyed to 1995 valuation timing need re-anchoring; mostly a clean carry-over row — useful as a "carries over cleanly" control in the eval. | [CC-2011 §8; GN-2011 §C para 8; ERCC 3.51] |
| 13 | Notices (para 14) | 2000 introduced the Special Default Notice (deemed default where delivery of a default notice is impracticable in extreme conditions). 2011 added Electronic Messaging System / email delivery, deleted telex, and reworked default-notice references around the ETD concept. | 1995-era bespoke notice riders listing telex/fax routes break; any bespoke default-notice mechanics must be re-keyed to ETD designation and the Special Default Notice. FOCB-style riders that run time from notice delivery care a lot about the email rule (see R11). | [GN-2000 Exh. I "Notices"; CC-2011 §14; GN-2011 §C para 14] |
| 14 | Applicability: net paying securities, US Treasuries, equities (para 1; Annex I 1(b)) | 2000 deleted the 1995 heading prohibition on net-paying securities and US Treasuries, adding optional Annex I wording for net-paying securities; annexes (Equities, Buy/Sell Back, Agency, country annexes) developed since 1995 handle excluded asset types. | 1995 bespoke wording admitting excluded asset classes must be mapped to the standard optional wording / relevant annex; risk of double regimes if the bespoke rider survives alongside the annex. | [GN-2000 Exh. I "Applicability"; GN-2011 §B.2, §C para 1] |
| 15 | Boilerplate added in 2000/2011: EMU continuity 16(e); third-party rights para 21; exclusive English jurisdiction (2011 para 17); Rome II update | 2000 added 16(e) (euro continuity) and para 21 (Contracts (Rights of Third Parties) Act exclusion). 2011 moved to exclusive English jurisdiction and added replacement-process-agent self-help. | Mostly clean carry-overs, but a 1995 bespoke non-exclusive jurisdiction clause now conflicts with the 2011 exclusive-jurisdiction standard — a low-drama but real "conflicts" row. | [GN-2000 Exh. I; CC-2011 §17] |
| 16 | Close-out statement and replacement-cost recovery (2011 paras 10(d)(iii), 10(l)) | 2011 added an express duty to give the defaulting party a reasonably detailed close-out calculation statement (balance due next Business Day, with interest); 10(l) widened recovery to hedging replacement/unwind costs (2000 had introduced replacement-cost recovery language). | Bespoke 1995 loss/expense riders overlap with the now-standard replacement-cost and statement mechanics; classification question is duplication vs conflict rather than loss. | [CC-2011 §§10(d), 10(l); GN-2000 Exh. I "Replacement Cost"] |
| 17 | Agency Annex (annex; Annex I election 1(c)) | Agency terms standardised post-1995: single named principal per transaction, disclosure at point of trade, principal treated as if party to a separate agreement on the same terms, elective treatment of agent default as principal default; a separate Addendum is required for multiple principals, block trades, and post-trade allocation; both-parties-as-agents not permitted. | Legacy agented relationships documented with bespoke 1995 riders must be mapped to Agency Annex + Addendum architecture; the "as if separate agreement per principal" construct interacts with set-off (row 9) and margin netting per principal. | [GN-2011 §B.4 & "Agency Transactions" section] |

---

## (b) Playbook rules — bank-side vs funds (negotiation-review eval task)

Each rule: **market-standard position / common fund ask / plausible red-line**, a
severity guess, and the public source it derives from. Severity is graded by expected
loss from missing the deviation in review (the missed-conflict metric). **Every rule
is a hypothesis for the author to confirm, reject, or re-grade.**

### R1. Exposure-calculation regime coherence (Transaction Exposure method; haircut vs initial margin) — AWAITING DESK VALIDATION
- **Market-standard**: One coherent regime, elected in Annex I: Method A (Margin Ratio applied to Repurchase Price) or Method B (haircut-adjusted collateral value); both parties using the same convention — haircut and initial margin arithmetic differ (102% initial margin ≠ 2% haircut) and must not be mixed. Haircuts/initial margins recorded in Annex I or confirmations.
- **Common fund ask**: Method B with a pre-agreed haircut schedule by collateral class; symmetric application to both parties' collateral.
- **Plausible red-line**: Bespoke drafting that stacks both a Margin Ratio and a haircut on the same exposure (double margining), or gives the bank a unilateral right to reset haircuts on demand without objective criteria.
- **Severity guess**: High (systematic mis-margining; silent economics change on upgrade).
- **Source**: [CC-2011 §2 "Transaction Exposure"; GN-2011 §C 2(xx) worked examples; ERCC 3.1–3.10, 2.146, 3.5]

### R2. Exposure threshold / minimum transfer amount — AWAITING DESK VALIDATION
- **Market-standard**: Modest agreed threshold; European practice treats threshold and MTA as the same number; once exceeded, margin is called to eliminate the entire Net Exposure; amount recorded in the GMRA before trading; either party may call for periodic elimination of sub-threshold exposure; a party holding Net Margin should honour a recall even below threshold.
- **Common fund ask**: Equal, two-way thresholds; express periodic-elimination right; the sub-threshold margin-recall exception written in.
- **Plausible red-line**: A threshold so large it guts daily margining, or asymmetric thresholds favouring the weaker credit (the classic off-market flag, mirroring ISDA CSA rule 7 in the design doc's Appendix A).
- **Severity guess**: High.
- **Source**: [ERCC 3.40–3.45]

### R3. Margin call operations: frequency, deadlines, settlement, interest — AWAITING DESK VALIDATION
- **Market-standard**: Net Exposure calculated at least daily (intraday in exceptional circumstances); margin calls before ~14:00 CET on a European counterparty; calls after the deadline roll to next business day; cash margin same-day, margin securities T+0 best practice (T+1/T+2 common); interest on cash margin at an overnight index ± agreed spread; disputed calls — pay the undisputed portion immediately; margin parameters (price sources, business-day definitions, deadlines) agreed and recorded up front.
- **Common fund ask**: All deadlines and price sources written into Annex I; disputes resolved by exchange of portfolios/calculations with escalation timeframes; no set-off of delayed margin against later calls.
- **Plausible red-line**: Bank discretion to call intraday at any hour with same-day securities delivery on the fund only, or a bespoke provision letting either party roll unmet margin obligations forward (the practice ERCC explicitly calls unacceptable).
- **Severity guess**: Medium.
- **Source**: [ERCC 3.38–3.39, 3.46–3.47, 3.50, 3.52–3.54, 3.61–3.68]

### R4. Failure-to-deliver Event of Default election (para 10(a)(ii)) — AWAITING DESK VALIDATION
- **Market-standard**: In the European market the election is generally NOT made — fails are handled by the repayment/margin/mini-close-out remedies; the EoD route exists mainly to accommodate markets (e.g. US Treasuries practice) where fails are rare. ERCC warns that triggering full default remedies for fails would deter market participation.
- **Common fund ask**: Election off; express menu of non-default remedies preserved.
- **Plausible red-line**: Election ON against a fund trading less-liquid collateral (every settlement fail becomes a full close-out right and a cross-default vector under other agreements — amplified by the 2011 change that the event itself is an EoD even without close-out notice).
- **Severity guess**: High.
- **Source**: [GN-2000 Exh. I "Events of Default"; CC-2011 §10(a); GN-2011 §C para 10; ERCC 4.10, 4.14]

### R5. Mini close-out mechanics and fail conventions (2000 10(h) / 2011 10(i)) — AWAITING DESK VALIDATION
- **Market-standard**: Mini close-out is an exceptional remedy; advisory notice as soon as possible (same day as the fail or early next Business Day), mini close-out notice with a noon delivery deadline convention, execution confirmed by close of business; partial deliveries accepted unless they leave an untradeable balance; the calculation statement should show prices and sources; buy-ins are dealt with inside the GMRA, not under cash-market buy-in rules.
- **Common fund ask**: Partial-delivery acceptance written in; deadline-bound execution of the mini close-out once noticed (no open-ended right to pick the valuation moment).
- **Plausible red-line**: Bespoke drafting that lets the seller leave a fail open indefinitely while retaining the right to execute the mini close-out later at a historically favourable price (an anti-optionality violation — see R11), or refusal of partial deliveries.
- **Severity guess**: Medium-high.
- **Source**: [ERCC 2.72, 4.11–4.14; GN-2011 §C para 10]

### R6. Automatic Early Termination election (2011 para 10(b)) — AWAITING DESK VALIDATION
- **Market-standard**: AET elected only where the counterparty's insolvency law would defeat notice-based close-out; otherwise off, preserving the NDP's timing control (the 2011 change made this elective precisely to remove the 2000's automatic close-out on petition/liquidator).
- **Common fund ask**: AET off for English/other netting-friendly entities; if on, confined to the petition/liquidator events the standard specifies.
- **Plausible red-line**: AET on for an English-law fund without jurisdictional justification (forced close-out at a market-stress moment benefits nobody), or — the naive-upgrade trap — nobody making the election at all when moving a 1995 doc that silently relied on automatic close-out.
- **Severity guess**: Medium-high.
- **Source**: [CC-2011 §10(a),(b); GN-2011 §C para 10]

### R7. Act of Insolvency scope and grace periods (2011 para 2(a)) — AWAITING DESK VALIDATION
- **Market-standard**: The 2011 pre-printed definition — expanded limbs (secured-party enforcement with 15-day proviso, inability/failure to pay debts, Competent Authority proceedings, conservator/custodian), petition window at 15 days.
- **Common fund ask**: Restore longer petition-dismissal windows (the 2000's 30 days) or add materiality/dismissal carve-outs on the enforcement limb; tighten the "unable to pay debts" limb to admissions or actual defaults; carve out solvent schemes/reorganisations.
- **Plausible red-line**: Either direction at the extreme — bank deleting the dismissal provisos (any third-party petition = instant EoD against the fund), or fund gutting the insolvency limbs so the definition no longer catches genuine distress. Note the Protocol treats ANY bespoke edit to this EoD as disabling the standard close-out upgrade package — the market's own signal that these edits are high-consequence.
- **Severity guess**: High.
- **Source**: [CC-2011 §2 "Act of Insolvency"; PROT 1.13]

### R8. Default Market Value determination (2011 paras 10(e)–(f)) — AWAITING DESK VALIDATION
- **Market-standard**: The 2011 regime — NDP determines DMV on or as soon as reasonably practicable after the ETD, via actual dealt prices on or about the ETD, adjusted market quotations, or the widened Net Value fallback; good-faith and commercially-reasonable qualifiers throughout; close-out statement in reasonable detail (best practice: including prices and sources).
- **Common fund ask** (anti-optionality — the desk-remembered friction point): reinstate a hard outer time limit on valuation (a 2000-style five-dealing-day window), name objective pricing sources in Annex I, require the statement to disclose sources, and constrain when the Net Value fallback may be invoked.
- **Plausible red-line**: Bank-side deletion of the good-faith/commercial-reasonableness qualifiers or of the statement duty; fund-side dispute-and-suspend mechanics that stall close-out entirely (close-out certainty is the whole point of the post-Lehman overhaul).
- **Severity guess**: High (this is the flagship's densest conflict surface).
- **Source**: [CC-2011 §§10(e)–(f); GN-2011 §C para 10; ERCC 4.12]

### R9. Close-out set-off breadth (2011 para 10(n)) — AWAITING DESK VALIDATION
- **Market-standard**: The 2011 clause — set-off of the close-out balance at the NDP's option against amounts payable under other agreements between the same two parties; unascertained obligations via good-faith estimate with a true-up; expressly no charge created; non-exclusive of other rights.
- **Common fund ask**: Confine set-off to matured amounts under agreements between the same two legal entities in the same capacity; exclude bank-affiliate obligations; for umbrella funds, hard segregation — no set-off across sub-funds/cells.
- **Plausible red-line**: One-way bank set-off extended to "any affiliate" obligations, or drafting that reaches across a fund umbrella's segregated sub-funds (breaks the fund's statutory/constitutional segregation).
- **Severity guess**: High.
- **Source**: [CC-2011 §10(n), which reproduces the clause; GN-2011 §C paras 9, 13 (same-capacity requirement for effective insolvency set-off); PROT Annex 3]

### R10. NAV triggers and bespoke fund credit events (Annex I supplemental terms) — AWAITING DESK VALIDATION
- **Market-standard (bank ask)**: NAV-decline triggers imported from ISDA credit practice — monthly, quarterly, annual periods plus a floor from highest NAV (sometimes "greater of X% from high or fixed dollar amount"); notification duty on breach.
- **Common fund ask** (all publicly documented buy-side positions): point-to-point (month-end) measurement, never rolling intra-month; performance-based NAV-per-share triggers excluding subscriptions/redemptions for the monthly/quarterly tests; argue the over-collateralised nature of repo weakens the rationale for NAV triggers versus ISDA, so either omit them or downgrade breach consequences to a margin-increase right rather than default/termination; streamline levels across counterparties for monitorability; cross-default avoided, cross-acceleration as compromise.
- **Plausible red-line**: Rolling any-day total-NAV triggers on a monthly-NAV fund (unmonitorable and volatile), triggers tight enough to act as margin calls (per the design doc's ISDA rule 5 analogue), or breach consequences that export instantly through cross-default into the fund's other agreements.
- **Severity guess**: High.
- **Source**: [HFLR/HedgeLegal (Retsinas, 14 May 2020) — full negotiation anatomy incl. periods, thresholds, NAV/share vs NAV, consequences, cross-default vs cross-acceleration]

### R11. The anti-optionality family (fish-or-cut-bait time limits) — see section (c) — AWAITING DESK VALIDATION

### R12. Agency Annex architecture for agented funds — AWAITING DESK VALIDATION
- **Market-standard**: Agency Annex elected in Annex I (sub-para 1(c)); every agency transaction specified as such at execution, for a single named principal disclosed to the dealer; each principal treated as if party to a separate agreement on the same terms (preserving per-principal netting/set-off); dealer's elective right to call default against the principal if the agent defaults; the published Addendum required before multiple principals, block transactions, or post-trade allocation are permitted; both-sides-agency not permitted.
- **Common fund/agent ask**: Addendum adopted for block trading and post-execution allocation; allocation deadlines workable for the manager's operations; information duties limited to what the agent can actually deliver.
- **Plausible red-line**: Transactions for unnamed/undisclosed principals without the Addendum framework (the dealer literally cannot know its counterparty or netting set), or drafting that aggregates margin/set-off across principals (breaks the several, per-principal architecture — compare R9 on sub-fund segregation).
- **Severity guess**: High.
- **Source**: [GN-2011 §B.4 and "Agency Transactions" section]

### R13. Substitution rights (para 8) — AWAITING DESK VALIDATION
- **Market-standard**: Consent-based substitution of purchased or margin securities; replacement value at least equal; 2011 clarifies margin-securities valuation is at the time the exchange is agreed; margin-security substitution requests to be met reasonably and in good faith.
- **Common fund ask**: Pre-agreed substitution rights within an eligible-collateral schedule and daily/notice limits (asset managers need portfolio flexibility).
- **Plausible red-line**: Unilateral substitution without value-equivalence or with eligibility criteria loose enough to swap quality collateral for illiquid paper mid-trade.
- **Severity guess**: Low-medium (useful as a lower-severity calibration rule in the eval).
- **Source**: [CC-2011 §8; GN-2011 §C para 8; ERCC 3.51]

---

## (c) The anti-optionality family (R11): fish-or-cut-bait time limits on open-ended bank discretion

This family is one rule with several concrete instantiations. Bank-side standard =
preserve optionality; fund pressure = time-limit it; deviations graded by **how much
unbounded discretion survives**. Public anchors:

1. **FOCB / deemed-waiver riders (the name is public).** The Hedge Fund Law Report /
   HedgeLegal article (Retsinas, 2020) describes "fish-or-cut-bait (FOCB)" provisions
   as a standard buy-side ask: a limit — typically 30–90 days — on how long a
   counterparty can sit on a Termination Event or Event of Default before acting;
   failure to act within the window waives the right to act on that event (not the
   underlying obligation). Buy-side drafting points made publicly: the waiver should
   cover all TEs/EoDs, not just NAV triggers; notice by email expressly permitted; the
   clock running from when the email is sent. [HFLR]
2. **Condition-precedent suspension (GMRA para 6(j) / ISDA s.2(a)(iii)).** GMRA 6(j)
   is elective (introduced 2000) and, per Clifford Chance, mirrors ISDA s.2(a)(iii) —
   the open-ended right to withhold performance while a default is outstanding. The
   public template for time-limiting it is the **ISDA June 2014 form of amendment to
   s.2(a)(iii)**: the defaulting party may serve notice triggering a "Condition End
   Date" — a hard stop (drafted at 90 days, in square brackets, i.e. negotiable) after
   which the non-defaulting party must resume performance with accrued
   interest/compensation; the UK FCA indicated it regarded 90 days as the maximum
   acceptable period. The GMRA-side fund ask is the direct analogue: if 6(j) is
   elected, bound it with a condition-end-date rider. [GN-2000 Exh. I; CC-2011 §6;
   ISDA-2014; DRS-2014; Weil-2011]
3. **Deadline-bound default valuation.** The 2011 DMV regime removed the 2000's
   five-dealing-day Default Valuation Time in favour of "on or as soon as reasonably
   practicable after" the ETD — a flexibility grant to the NDP that funds counter by
   negotiating outer time limits and named pricing sources back in (rule R8). Grading:
   does any bespoke rider leave the bank free to choose its valuation moment without
   bound? [CC-2011 §§10(e)–(f)]
4. **Bounded remedies elsewhere in the standard, as the baseline the family defends**:
   the 2011 ETD designation notice is capped at "not more than 20 days"; the Cash
   Equivalent Amount mechanic triggers only after the margin-securities fail has
   continued for two Business Days; ERCC best practice imposes same-day/next-morning
   advisory notices and a noon deadline convention on mini close-outs; margin calls
   after the agreed deadline roll to the next business day. Bespoke provisions that
   strip these bounds out — or legacy 1995 riders that never had them — are the
   deviation class this rule detects. [CC-2011 §10(b), §4; ERCC 4.11, 3.46]

**Eval use (both tracks).** For the negotiation-review task: flag any draft where a
suspension, valuation, or enforcement right is open-ended, and grade severity by the
survival of unbounded discretion (none / bounded-but-long / unbounded). For the
flagship upgrade task: legacy 1995 docs carrying bespoke FOCB-style riders may be
seeded fact patterns only after desk validation. A FOCB/withholding rider is not
automatically an "Express Provision" under the Protocol's limited definition; its
treatment depends on its drafting and the upgrade route. — AWAITING DESK VALIDATION.

---

## (d) Source bibliography

Primary (standard-setter):

- **[GN-2011]** ICMA/SIFMA, *Guidance Notes for use with the Global Master Repurchase Agreement (2011 Version)*, March 2012 — incl. Exhibit I (principal 2000→2011 changes). https://www.icmagroup.org/assets/documents/Legal/Guidance-Notes-to-the-GMRA-2011.pdf
- **[GN-2000]** ISMA/TBMA, *Guidance Notes for the GMRA 2000 Version*, October 2000 — incl. Exhibit I (principal 1995→2000 changes), Exhibit II (annexes list). https://www.icmagroup.org/assets/documents/GMRA2000_GuidanceNotes.pdf
- **[PROT]** ICMA, *2011 Global Master Repurchase Agreement Protocol (Revised)*, 7 June 2013 — Annexes 1–5; Preservation of Express Provisions (paras 1.10–1.13). https://www.icmagroup.org/assets/documents/Legal/GMRA-2011/ICMA-2011-GMRA-Protocol-revised-7-June-2013.pdf
- **[ERCC]** ICMA ERCC, *Guide to Best Practice in the European Repo Market*, March 2025 — margin best practice (ch. 3), mini close-out and fails (ch. 4), haircut/initial margin definitions (3.1–3.10). https://www.icmagroup.org/assets/ERCC-Guide-to-Best-Practice-March-2025.pdf
- **[ICMA-GMRA]** ICMA GMRA landing page (version history, opinions, clause taxonomy). https://www.icmagroup.org/market-practice-and-regulatory-policy/repo-and-collateral-markets/legal-documentation/global-master-repurchase-agreement-gmra/
- **[ICMA-FAQ]** ICMA, *Frequently Asked Questions on Repo* (Comotto), April 2015 — haircut/initial margin Q21 etc. https://www.icmagroup.org/assets/documents/Regulatory/Repo/Repo-FAQs-April-2015.pdf

Law-firm and practitioner:

- **[CC-2011]** Clifford Chance, *ICMA publishes 2011 Global Master Repurchase Agreement*, client briefing, May 2011 — paragraph-by-paragraph 2000→2011 change chart. https://www.cliffordchance.com/content/dam/cliffordchance/briefings/2011/05/icma-publishes-2011-global-master-repurchase-agreement.pdf
- **[HFLR]** Poseidon Retsinas (HedgeLegal), *How Fund Managers Can Mitigate NAV Triggers' Impact on Trading Agreements*, Hedge Fund Law Report, 14 May 2020 — NAV trigger anatomy and the FOCB/deemed-waiver provision. https://hedgelegal.com/wp-content/uploads/2023/09/How-Fund-Managers-Can-Mitigate-NAV-Triggers-Impact-on-Trading-Agreements.pdf
- **[Frontclear-HB]** Frontclear, *GMRA Handbook*, July 2024 — Annex I mechanics, Margin Ratio vs haircut, mini close-out, substitution. https://www.frontclear.com/assets/files/reports/Frontclear-GMRA-Handbook-DIGITAL.pdf
- **[ISDA-2014]** ISDA, *Amendment to the ISDA Master Agreement for use in relation to Section 2(a)(iii) and explanatory memorandum*, June 2014. https://www.isda.org/book/amendment-to-the-isda-master-agreement-for-use-in-relation-to-section-2aiii-and-explanatory-memorandum/
- **[DRS-2014]** DRS, *ISDA Master Agreement: Amendments to Section 2(a)(iii) Finalised* — 90-day Condition End Date summary and FCA context. https://drs-als.com/isda-master-agreement-amendments-section-2aiii-finalised/
- **[Weil-2011]** Weil, *Calling Time on Section 2(a)(iii) of the ISDA Master Agreement*. https://www.weil.com/~/media/calling-time-on-section-2.pdf
- **[SIFMA-GMRA]** SIFMA, MRA and GMRA documentation page (US-side context). https://www.sifma.org/resources/market-practices-model-documentation/mra-and-gmra-documentation

Members-only / unavailable (noted as gaps, not cited for content):

- ICMA, *FAQs in relation to the GMRA and market turbulence* (members only).
- ICMA GMRA legal opinions (members only; jurisdictions listed publicly in [GN-2011] §A).
- Frontclear, *Rough guide: GMRA 2011 for operations staff & other non-lawyers* — indexed URL now 404s.
- Practical Law, *Repos: Global Master Repurchase Agreement 2011* (paywalled).

---

## Gaps in the public record → validation questions

These are open questions, not settled facts. They are tracked as a checklist in
`../VALIDATION.md`.

1. **GMRA-specific NAV trigger levels.** Public numbers (HFLR Figure 1) are ISDA-centred; no public source states typical GMRA-annex NAV trigger levels for repo specifically. Were the 20/30/50-style levels from the ISDA appendix also the repo norm, or looser given over-collateralisation?
2. **Haircut levels by collateral class.** ERCC/ICMA publish the mechanics but deliberately not a schedule of typical bilateral haircuts by counterparty type. Need desk-plausible ranges for the synthetic Annex I docs (or key off the FSB minimum-haircut framework as a public floor?).
3. **Who calls margin in practice.** The GMRA is symmetric on paper; no public source describes bank-vs-fund asymmetries actually negotiated (one-way margining, fund-only thresholds). Was one-way margining a live ask?
4. **1995→2000 depth.** The only substantive public 1995→2000 change list is ICMA's own Exhibit I [GN-2000]; no law-firm comparison note surfaced. Does the Exhibit I list match what actually bit in upgrade negotiations, or were there 1995 pain points it understates?
5. **Agency Annex friction.** Public guidance describes the architecture but not the negotiation flashpoints (allocation deadlines, agent information duties, per-principal margin operationalisation). Which actually generated red-lines with pension-fund agents?
6. **GMRA 6(j) usage.** Is 6(j) commonly elected at all in bank-fund GMRAs, and did funds actually import ISDA-style condition-end-date riders into repo docs (R11.2 is an analogical construction — the ISDA 2014 amendment is ISDA-only)?
7. **FOCB confirmation.** Public source [HFLR] defines FOCB as "fish or cut bait" deemed-waiver time limits (30–90 days) — confirm this matches desk usage and that the GMRA-side instantiations in section (c) are the right ones.
8. **Severity calibration.** All severity guesses derive from public materials; each rule needs re-grading by expected desk loss, and any rule a fund would never actually push should be killed.
