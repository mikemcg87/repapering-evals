# GMRA version differences (1995 → 2000 → 2011) — sourced research

Research date: 2026-07-21. Purpose: validating a legal-AI eval corpus (synthetic GMRA 1995 exemplars). Every substantive claim carries a source URL and a confidence level. Primary sources used: ICMA Guidance Notes to the GMRA 2000 and GMRA 2011 (text-extracted from the official PDFs), ICMA Guidance Notes to the GMRA 1995, the ICMA 2011 GMRA Protocol (Revised, 7 June 2013), the Clifford Chance May 2011 client briefing, and ICMA's Repo FAQ.

Key source URLs (all fetched and text-verified during this research):

- **[GN-1995]** ICMA/TBMA Guidance Notes, GMRA 1995 Version — https://www.sifma.org/wp-content/uploads/2017/08/GMRA_Guidance-Notes-1995-Version.pdf
- **[GN-2000]** Guidance Notes, GMRA 2000 (October 2000; includes Exhibit I "Summary of the principal changes to the 1995 Version made in the 2000 Version") — https://www.sifma.org/wp-content/uploads/2024/06/Global_Master_Repurchase_Agreement_GMRA-Guidance_Notes-English.pdf
- **[GN-2011]** ICMA Guidance Notes to the GMRA 2011 (March 2012; includes Exhibit I "Summary of the principal changes to the 2000 Version made in the 2011 Version") — https://www.icmagroup.org/assets/documents/Legal/Guidance-Notes-to-the-GMRA-2011.pdf (same document also at https://www.icmagroup.org/assets/documents/Legal/GMRA-2011/GMRA-2011/Guidance-Notes-to-the-GMRA-2011.pdf)
- **[PROTOCOL]** ICMA 2011 Global Master Repurchase Agreement Protocol (Revised), 7 June 2013 — https://www.icmagroup.org/assets/documents/Legal/GMRA-2011/ICMA-2011-GMRA-Protocol-revised-7-June-2013.pdf
- **[CC-2011]** Clifford Chance client briefing, "ICMA publishes 2011 Global Master Repurchase Agreement" (May 2011; clause-by-clause change chart from p.3) — https://www.cliffordchance.com/content/dam/cliffordchance/briefings/2011/05/icma-publishes-2011-global-master-repurchase-agreement.pdf
- **[ICMA-FAQ26]** ICMA Repo FAQ 26, "What happens to repo in a default?" — https://www.icmagroup.org/market-practice-and-regulatory-policy/repo-and-collateral-markets/icma-ercc-publications/frequently-asked-questions-on-repo/26-what-happens-to-repo-in-a-default/
- **[ICMA-GMRA]** ICMA GMRA landing page (all versions, protocol, guidance) — https://www.icmagroup.org/market-practice-and-regulatory-policy/repo-and-collateral-markets/legal-documentation/global-master-repurchase-agreement-gmra/
- **[NRF-LBI]** Norton Rose Fulbright, High Court judgment on GMRA 2000 close-out valuation and "close of business" (LBI v Raiffeisen line of cases) — https://www.nortonrosefulbright.com/en/knowledge/publications/b50e5d68/high-court-delivers-leading-judgment-on-close-out-valuation-of-repo-transactions-under-gmra-2000-and-guidance-on-the-meaning-ofb-close-of-business
- **[HSF-LBI]** Herbert Smith Freehills, Court of Appeal on wide discretion for "fair market value" under GMRA 2000 — https://www.hsfkramer.com/notes/bankinglitigation/2018-04/court-of-appeal-confirms-wide-discretion-afforded-to-a-non-defaulting-party-when-determining-fair-market-value-of-securities-under-the-gmra-2000-version
- **[FRONTCLEAR-HB]** Frontclear GMRA Handbook — https://www.frontclear.com/assets/files/reports/Frontclear-GMRA-Handbook-DIGITAL.pdf
- **[DRS-MCO]** DRS, "Mini Close-Out" explainer — https://drs-als.com/mini-close-out/
- **[JC-EOD]** Jolly Contrarian, Events of Default — GMRA Provision — https://jollycontrarian.com/index.php?title=Events_of_Default_-_GMRA_Provision

---

## 1. Paragraph 6(j) — what it is (HIGH confidence, primary-source verified)

**Paragraph 6(j) is the optional "condition precedent" / payment-withholding provision — the GMRA's analogue of ISDA Section 2(a)(iii). It is NOT the failure-to-deliver / mini close-out provision.** The mini close-out lives in paragraph 10 (10(g)/(h) in GMRA 2000; 10(h)/(i) in GMRA 2011 — see §3–4 below).

Version history of 6(j):

- **GMRA 1995: paragraph 6(j) does not exist.** The GMRA 2000 Guidance Notes state expressly: "The 2000 Version has introduced a new paragraph 6(j), which only applies if the parties have specified in Annex I that it is to apply." [GN-2000, p.11] The 1995 Guidance Notes' walk-through of paragraph 6 contains no such provision. [GN-1995] *(Confidence: HIGH — both primary guidance documents extracted verbatim.)*
- **GMRA 2000 (new, optional, event-specific):** "If it is specified to apply, then a condition precedent is introduced as a result of which a party may withhold its payments and deliveries under the Agreement (other than its obligations under paragraph 10) if a specified potential event of default occurs with respect to the counterparty. A potential event of default occurs when one of the events specified in paragraph 10 … has occurred in relation to the counterparty but the first party has not given the notice necessary to turn that event into an event of default … this condition precedent will not be triggered by all of the events set out in paragraph 10, only by those selected by the parties in Annex I." [GN-2000, p.11, close paraphrase/quote]
- **GMRA 2011 (still optional, but now all-events):** "Paragraph 6(j) now makes it a condition precedent to any obligation of a party (other than an obligation upon a close-out of the Agreement) that none of the events specified in paragraph 10(a) (Events of Default) has occurred and is continuing with respect to the other party, rather than requiring parties specifically to designate those events in Annex I for this purpose (as was the case in the 2000 Version). As under the 2000 Version, Paragraph 6(j) is optional – it applies only if the parties have so specified in Annex I." [GN-2011, p.25, near-verbatim]
- The 2011 Guidance Notes add a footnote flag: "Provisions of this kind are currently the subject of ongoing litigation. In addition, regulatory authorities are considering such provisions both in the context of resolution regimes and regulatory capital." [GN-2011, p.12 fn.2] — the post-Lehman Section 2(a)(iii)-style controversy (Marine Trade/Lomas era). *(Confidence: HIGH for the quote; the litigation referenced is the ISDA 2(a)(iii) case law — MEDIUM inference.)*

**Interaction with the 2011 change in Event-of-Default methodology (subtle, negotiator-relevant):** under GMRA 2000, 6(j) bites on "potential events of default" (event occurred, Default Notice not yet given) because in 2000 the notice itself creates the Event of Default. Under GMRA 2011 the event IS the Event of Default without notice (notice merely designates the Early Termination Date), so 2011's 6(j) is drafted off "Event of Default … has occurred and is continuing." Same commercial function, different trigger taxonomy. [GN-2000 p.11; GN-2011 pp.12–13, 25] *(Confidence: HIGH.)*

### The failure-to-deliver regime across versions (the thing 6(j) was believed to be)

| | GMRA 1995 | GMRA 2000 | GMRA 2011 |
|---|---|---|---|
| Failure to deliver Purchased Securities (purchase date) or Equivalent Securities (repurchase date) an Event of Default? | **No — not an EoD at all, and no election available.** "Failure to deliver the purchased securities to the buyer on the purchase date or to deliver equivalent securities to the seller on the repurchase date is not an event of default" [GN-1995, p.6] | **Elective EoD — new para 10(a)(ii), applies only if specified in Annex I.** Introduced after debate: US participants (Treasuries experience) wanted it; others resisted because settlement fails "are not generally an indicator of credit deterioration." [GN-2000, pp.13–14] | **Same elective structure retained (10(a)(ii)), now triggered only if the fail persists beyond "the standard settlement time for delivery of the Securities concerned."** [GN-2011, pp.13, 26] |
| Non-EoD remedies ("mini close-out") | Non-failing party may: (i) require repayment of the price paid; (ii) require cash margin if it has transaction exposure; (iii) by written notice terminate **that transaction only**. [GN-1995, p.6] | Same three remedies; provisions numbered **10(g) (purchase-date fail) and 10(h) (repurchase-date fail)**; 10(h)(iii) revised to clarify the mini close-out valuation period runs from the mini close-out notice. Failure to pay a mini close-out amount is itself a new EoD (10(a)(iii)). [GN-2000, pp.13–14, 19] | Renumbered **10(h)/10(i)**. 10(i) (formerly 10(h)) now expressly permits **partial termination** where the Buyer delivers some but not all Equivalent Securities. Failure to pay sums due under applied mini close-out remains an EoD. [GN-2011, pp.13, 29] |
| Automatic EoD for fails in any version? | No | No (elective, and even then requires Default Notice like other EoDs) | No (elective; and under 2011 methodology no EoD triggers close-out without an Early Termination Date designation, absent elected Automatic Early Termination for the two insolvency events) |

*(Confidence: HIGH throughout — all cells sourced from the three official Guidance Notes.)*

Note for the corpus: so the belief "6(j) = failure-to-deliver / mini close-out" is a **plausible-sounding conflation** — a model that asserts it should be scored wrong. The correct anchors are: 6(j) = condition precedent (2000 onward, optional); mini close-out = 10(g)/(h) (2000) / 10(h)/(i) (2011); 1995 has the remedies but neither the "mini close-out" defined EoD hook nor the elective fail EoD.

---

## 2. "FOCB" (finding: NOT an attested GMRA term — LOW confidence on any expansion)

**Bottom line: no ICMA, law-firm, judicial or market-glossary source uses "FOCB" as a GMRA/repo close-out term.** Multiple targeted searches (ICMA materials, law-firm briefings, Jolly Contrarian, acronym databases, litigation commentary) found **zero attested usage** in this domain. General acronym databases return only non-financial expansions (e.g. "Fish or Cut Bait" — https://www.allacronyms.com/FOCB). *(Confidence that FOCB is NOT a standard GMRA term of art: HIGH.)*

Plausible expansions if encountered in a repo/close-out text, ranked, all speculative:

1. **"Fair (market value at) Close Of Business"** — LOW-MEDIUM plausibility. GMRA 1995/2000 default valuation both pivot on **close of business**: 1995's Default Valuation Time is "close of business in the most appropriate market … on the day following the day of default" [GN-1995, p.4]; 2000's is close of business on the fifth dealing day; and the leading GMRA 2000 case law (LBI v Raiffeisen line) turned on the meanings of "fair market value" and "close of business" [NRF-LBI; HSF-LBI]. A desk or litigation shorthand fusing the two is conceivable but **unattested**.
2. **"Failure Of Counterparty/Central Bank"** — LOW plausibility, unattested.
3. **Corpus artifact / hallucination trap** — if "FOCB" appears in the synthetic corpus or in model output as a confident defined term, treat it as a fabrication signal. This is arguably the most useful reading for eval purposes: an eval item asking "what does FOCB mean under the GMRA?" has "no such standard term" as the gold answer.

Recommendation: put FOCB to the desk-negotiator expert (see §7) before using it in any eval item with a definitional gold answer.

---

## 3. Authoritative change charts

Best public comparison documents found, in order of usefulness:

1. **[GN-2011] Exhibit I** — ICMA's own official "Summary of the principal changes to the 2000 Version made in the 2011 Version" (pp.20–30 of the Guidance Notes). Clause-by-clause, drafted by Clifford Chance for ICMA. The authoritative 2000→2011 chart.
2. **[CC-2011]** — Clifford Chance May 2011 briefing; contains a tabular "Summary of Key Changes in the 2011 GMRA (c.f. the 2000 GMRA)" from p.3, essentially the same content as GN-2011 Exhibit I in chart form, plus Protocol commentary.
3. **[GN-2000] Exhibit I** — the official "Summary of the principal changes to the 1995 Version made in the 2000 Version" (pp.19–20). The only authoritative public 1995→2000 chart found.

Also useful: ICMA sells/hosts a **blackline of GMRA 2000 vs GMRA 1995** and related annexes via [ICMA-GMRA]; Frontclear's Handbook [FRONTCLEAR-HB] gives practitioner-level narrative across versions.

### 3a. 1995 → 2000 (from GN-2000 Exhibit I + body; HIGH confidence)

- **Applicability (para 1):** prohibition on net-paying securities and US Treasury transactions deleted; optional Annex I wording for net payers.
- **Condition precedent (para 6(j)):** NEW optional withholding provision (see §1).
- **Events of Default (10(a)):** grows from **eight** EoDs (1995) [GN-1995, p.6] to **ten** (2000): adds (i) elective failure-to-deliver EoD (10(a)(ii)) and (ii) failure to pay mini close-out amounts (10(a)(iii)). [GN-2000, pp.13, 19]
- **Default valuation (10(e)):** 1995 valued at close of business one (or in some cases two) dealing days after default, unless an actual sale/purchase occurred earlier; 2000 gives the non-defaulting party **five dealing days** to use actual sale/purchase prices or market quotations, with a "Net Value" (fair market value determined by the NDP) fallback where quotations are unobtainable or commercially unreasonable. Multiple partial sales/purchases contemplated. [GN-1995, p.4; GN-2000, pp.14, 19]
- **Mini close-out (10(h)):** clarified that the valuation period runs from the mini close-out notice. [GN-2000, p.19]
- **Replacement cost (10(k)):** clarified recoverable costs — replacement transactions, hedge unwind/replacement; consequential-loss bar retained. [GN-2000, pp.14–15, 19]
- **Notices (14(c)):** **Special Default Notice** introduced (deemed default where the NDP made all practical efforts to serve but could not). [GN-2000, p.20]
- **Continuity of contract (16(e)):** euro accession provision. **Third-party rights (para 21):** Contracts (Rights of Third Parties) Act exclusion. **Forward Transactions:** optional Annex I wording. [GN-2000, p.20]
- Buy/sell-back and agency: 1995 handled these via Annex III/Annex IV to the base agreement [GN-1995, p.3]; under 2000 they are the separately published Buy/Sell Back Annex and Agency Annex (plus an addendum for multiple principals). [GN-2000, Exhibit II, p.21]

### 3b. 2000 → 2011 (from GN-2011 Exhibit I + CC-2011; HIGH confidence)

- **EoD methodology inverted (para 10(a)/(b)):** 2000 = event + Default Notice creates the EoD, and the EoD automatically terminates; two insolvency events (winding-up petition, liquidator appointment) auto-terminate. 2011 = the event itself is the EoD without notice (so **cross-default under other agreements can trigger even if no close-out is initiated**), but close-out happens only when the NDP designates an **Early Termination Date** by notice of not more than 20 days; automatic termination survives only as elective **Automatic Early Termination** (Annex I, per-party) for those two insolvency events. [GN-2011, pp.12–13, 20, 25–27]
- **Act of Insolvency (2(a)) expanded:** secured-party enforcement over substantially all assets (15-day dismissal window); insolvency/failure-to-pay-debts trigger; petition stay period cut 30→15 days; Competent Authority proceedings (no 15-day period); conservator/custodian appointment added. [GN-2011, pp.20–21]
- **Default valuation:** see §4.
- **Margin:** new **Margin Percentage** concept (haircut on Margin Securities valuation); **Cash Equivalent Amount** procedure where Equivalent Margin Securities are unavailable on a collateral return (4(h)); 10(a)(iv) margin-default limb rewritten to enumerate specific margin failures (Margin Transfer within the minimum period per 4(g); 4(h)(i)/(ii); 4(i); 4(k)/(l)) instead of a bare cross-reference to para 4. [GN-2011, pp.20, 26; CC-2011]
- **Set-off:** NEW broad contractual cross-agreement set-off at **10(n)** — close-out amount may, at the NDP's option, be set off against amounts payable under **any other agreement** between the parties, including unascertained obligations via good-faith estimate; expressly no charge/security interest created. Full clause text reproduced in GN-2011 pp.29–30. [GN-2011; CC-2011]
- **Interest/rates:** LIBOR replaced by **Applicable Rate** (post-default: rate selected by the NDP in a commercially reasonable manner) in paras 10(g) and 12; day count per market convention rather than ISMA convention. [GN-2011, pp.21, 29–30]
- **Income (2(y)):** principal repayments/instalments during the term treated as Income, passed through under para 5; Equivalent Securities definition adjusted correspondingly. [GN-2011, p.6]
- **Payment/transfer (para 6):** any agreed clearance system (not just Euroclear/Clearstream); carve-out from the no-liens requirement (and the 9(h) representation) for clearance-system operator liens. [GN-2011, pp.24–25]
- **Calculation statement (10(d)(iii)):** NDP must provide a reasonably detailed close-out calculation statement; balance due the business day after the statement, with interest from the Early Termination Date. [GN-2011, p.27]
- **Notices (para 14):** email/Electronic Messaging System added, telex deleted; Special Default Notice retained but must now designate the Early Termination Date. [GN-2011, pp.16, 30]
- **Notification duty (10(m)):** party must notify the other immediately if an EoD, or an event that would become one on notice/lapse of time, occurs in relation to it. [GN-2011, p.29]
- **Tax (para 11):** substantively unchanged in structure (termination election + override-with-indemnity). [GN-2011, pp.15–16 — described without change commentary; *Confidence MEDIUM that no material 2011 change*]
- **Governing law (para 17):** updated for Rome II. [GN-2011, p.30]
- **Agency:** a revised Agency Annex for the 2011 GMRA was published by ICMA (see [ICMA-GMRA]); the Guidance Notes body discusses agency representations (9(b)). *Detailed 2011 Agency Annex changes not verified from primary text — Confidence LOW; flagged as a gap.*

### 3c. The 2011 GMRA Protocol — retrofit mechanics (HIGH confidence, primary text)

The **2011 GMRA Protocol (Revised, 7 June 2013)** [PROTOCOL] lets adhering parties upgrade legacy agreements bilaterally-by-multilateral-adherence (Adherence Letter to ICMA as agent; annex-by-annex tick-box elections, effective only where **both** parties ticked the same annex):

- **Annex 1:** GMRA 1995 close-out amendments (conforms EoD methodology + close-out/DMV procedure to 2011).
- **Annex 2:** same for GMRA 2000.
- **Annex 3:** inserts the 2011-style contractual set-off clause into a 1995 or 2000 agreement.
- **Annex 4:** Euro definition (any version). **Annex 5:** LIBOR → Applicable Rate (1995/2000, where not already done by Annex 1/2).
- **Preservation of Express Provisions (§§1.10–1.12):** the Protocol does **not** override negotiated terms — any provision in a confirmation, annex or amendment that provides a differing DMV procedure, a differing 10(b) calculation mechanism, or **any grace period in an EoD** (a "Grace Period Express Provision") is preserved; grace periods carry over mutatis mutandis to the amended provisions.
- **Reduced amendments (§1.13):** if the Act-of-Insolvency EoD (1995 para 10(a)(iv) / 2000 para 10(a)(vi)) was modified from the pre-printed form, then only the Spot Rate definitional amendment applies — the whole close-out conformity package is switched off. (A very negotiator-shaped safety valve: heavily negotiated books largely couldn't be protocol-upgraded.)

---

## 4. Default valuation / close-out: 2000 vs 2011 in detail (HIGH confidence)

The negotiators' battleground, from GN-2011 pp.14–15, 27–29 and CC-2011:

1. **Default Valuation Time deleted.** GMRA 2000: DMV determined by the Default Valuation Time — close of business on the **fifth dealing day** after the EoD (itself a change from 1995's next-day COB regime). GMRA 2011: the NDP determines DMV "on or as soon as reasonably practicable after the Early Termination Date," using prices "on or about the Early Termination Date"; the Default Valuation Time definition is **deleted**. Net effect: the rigid 5-day window becomes an open-textured reasonableness standard, with far more NDP flexibility on timing.
2. **Default Valuation Notice abolished.** Under 2011, "The non-Defaulting Party is no longer required to give the Defaulting Party a 'Default Valuation Notice'" [GN-2011, p.29]. Under 2000, failing to serve the DVN by the Default Valuation Time forced the NDP into the default (Net-Value-at-DVT) track — a classic trap litigated in the LBI cases [NRF-LBI].
3. **Three valuation methods retained but loosened (10(f)):** (i) actual sale/purchase prices — now "on or about the Early Termination Date" instead of within the EoD→DVT window; net proceeds may reflect reasonable commissions, costs, fees, expenses; NDP must act in **good faith**; (ii) market quotations — now referencing "pricing methodology which is customary for the relevant type of security," with commercially-reasonable adjustments for accrued unpaid coupons and **Pool Factor Affected Securities** (Pool Factor Distortion — the ABS/MBS lesson from Lehman); (iii) **Net Value fallback** widened — also available where the NDP determines it would not be commercially reasonable to deal at the prices bid/offered; "Net Value" now expressly includes **trading prices** as sources; **Transaction Costs** extended to reasonably *anticipated* costs and to guaranteed-delivery mark-ups/mark-downs.
4. **Deemed-default / notice timing:** 2000's Special Default Notice deems the EoD to occur on the date specified in it; 2011 retains the Special Default Notice but requires it to designate the Early Termination Date [GN-2011, p.16]. Separately, 2011's decoupling of EoD occurrence from notice moves the deemed-timing fight from "when did the EoD occur" to "when was the Early Termination Date designated."
5. **Hedge close-out costs (10(l), formerly 10(k)):** broadened to "otherwise hedging its exposure," and extended to Forward Transactions pre-Purchase Date. Gains must still be accounted for to the defaulter; consequential-loss bar retained.
6. **Case-law overlay (2000 form):** the English courts (LBI v Raiffeisen line, first instance and CA) confirmed a **wide discretion** for the NDP determining "fair market value" under GMRA 2000, including that it may take account of illiquidity/distressed conditions, and gave guidance on "close of business" [NRF-LBI; HSF-LBI]. *(Confidence HIGH that these cases are the leading authorities; MEDIUM on the fine holdings, which were summarized from firm briefings, not the judgments.)*

---

## 5. What large-fund counterparties negotiated hardest (THIN — flagged)

**Honest finding: there is very little published, citable material on actual buy-side GMRA mark-up practice.** Unlike ISDA (where negotiation guides abound), GMRA negotiation lore is mostly oral/desk knowledge. What the public record supports:

- **Annex I is the negotiation surface**: eligible collateral, Base Currency, minimum margin transfer/delivery periods, elective EoDs (10(a)(ii) fails), Automatic Early Termination, 6(j) application, Margin Percentages, thresholds. [ICMA-FAQ26; FRONTCLEAR-HB] *(Confidence HIGH that these are the election points; that is structural, not empirical.)*
- **NAV triggers**: commentary confirms NAV covenants (minimum NAV, percentage-decline triggers) are "typically set forth in negotiated ISDA schedules or MRA or GMRA annexes" for fund counterparties — i.e. banks demand NAV-decline additional EoDs from funds. (Practising Law Institute / margin-call end-user guide: https://marketingstorageragrs.blob.core.windows.net/webfiles/End_Users_Guide_to_Margin_Calls_and_Valuation_Issues.pdf) *(Confidence MEDIUM.)*
- **Agency Annex** matters disproportionately for asset managers (Wellington-class) trading as agent for many principals: the Annex requires per-principal treatment (each principal a separate agreement for default purposes), bars agent-on-agent trades, and the multiple-principals addendum governs allocation. [GN-2000 Exhibit II; GN-2011] Banks' classic asks: principal disclosure, timely allocation, agent liability carve-outs; managers' classic asks: no cross-principal set-off, limited agent responsibility. *(The clause mechanics are sourced; the "who pushes what" characterization is practitioner inference — Confidence LOW-MEDIUM, exactly the thing to validate with the expert.)*
- **Set-off scope (10(n), 2011)**: cross-agreement, cross-affiliate set-off is the provision most likely to be struck or narrowed by fiduciary buy-side counterparties (agency funds cannot lawfully offer cross-principal or cross-agreement set-off). Structural inference from the clause text [GN-2011 pp.29–30] — *Confidence MEDIUM as to the fact that funds narrow it; not documented in a published negotiation guide.*
- The Protocol's Preservation of Express Provisions and §1.13 carve-outs [PROTOCOL] are themselves indirect evidence of what was commonly negotiated by 2011: bespoke **DMV procedures**, bespoke **close-out calculation mechanics**, **grace periods in EoDs**, and **modified Act-of-Insolvency** definitions — ICMA would not have carved these out unless they were prevalent in negotiated books. *(Confidence MEDIUM-HIGH as inference.)*

---

## 6. Discrepancy risks for a synthetic GMRA-1995 corpus authored partly from model memory

1. **6(j) leakage into 1995 documents.** Models trained mostly on GMRA 2000/2011 text will happily put a 6(j) condition precedent (or a ten-limb EoD list) into a "1995" agreement. The genuine 1995 form has **no 6(j)** and only **eight** EoDs. [GN-1995; GN-2000]
2. **Failure-to-deliver anachronism.** A "1995" document offering an Annex I election to make fails an Event of Default, or using the defined "mini close-out" EoD hook (10(a)(iii)-style), is anachronistic — both are 2000 innovations. 1995 has only the three non-EoD remedies. [GN-1995 p.6; GN-2000 pp.13, 19]
3. **Default valuation window confusion.** 1995 = COB on the day after default (or next dealing day), market-appropriate-market test; 2000 = five dealing days + Default Valuation Notice + Net Value fallback; 2011 = "on or about the Early Termination Date," no DVT, no DVN. Models blur these constantly; a "1995" doc referencing a five-dealing-day window or "Net Value" is a version error. [GN-1995 p.4; GN-2000 p.14; GN-2011 pp.27–29]
4. **EoD-notice methodology.** 1995 and 2000 share the notice-creates-default model with automatic termination on two insolvency events; 2011 inverts it (event = EoD; notice designates Early Termination Date; AET elective). Any "1995" text speaking of "Early Termination Date," "Automatic Early Termination," "Applicable Rate," "Margin Percentage," "Cash Equivalent Amount," "Pool Factor," "Competent Authority," or a 10(n) cross-agreement set-off clause is contaminated by 2011 vocabulary. [GN-2011 Exhibit I]
5. **Fabricated terms of art (FOCB-class).** No public source attests "FOCB." Eval items should treat confident definitions of unattested abbreviations as hallucination markers — and conversely the corpus itself must not accidentally canonize such a term unless it is deliberately planted as a trap and keyed as such. Also watch paragraph-numbering drift: mini close-out is 10(g)/(h) in 2000 but 10(h)/(i) in 2011, and Act of Insolvency EoD is 10(a)(iv) in 1995 vs 10(a)(vi) in 2000 [PROTOCOL §1.13] — model memory routinely shuffles these sub-letters.

---

## 7. Open questions only a desk negotiator can answer

1. Have you ever seen "FOCB" used on a repo desk or in a GMRA mark-up — and if so, what did it stand for? (No public attestation exists; see §2.)
2. In practice, did anyone actually switch on paragraph 6(j) in Annex I — and did buy-side counterparties resist it the way they resisted ISDA 2(a)(iii) post-Lomas?
3. How often was the elective failure-to-deliver EoD (10(a)(ii)) switched on, and for which markets (e.g. USTs vs EGBs vs EM collateral)? Did Morgan Stanley's standard Annex I elect it?
4. What was your house position on the 2011 removal of the Default Valuation Notice and the five-day window — did dealers push counterparties onto 2011 paper primarily for the valuation flexibility, the set-off clause (10(n)), or the EoD methodology?
5. For Wellington-class agency relationships: what did the manager's standard rider to the Agency Annex look like (per-principal netting, allocation deadlines, agent liability), and which of those points did the bank concede to smaller managers vs hold against large ones?
6. Were NAV-decline triggers standard in fund-facing GMRA Annex I in your era, and at what levels (e.g. 10/20/30% monthly/quarterly/annual)?
7. Did your book actually use the 2011 Protocol, or was repapering done bilaterally — and did the §1.13 Act-of-Insolvency carve-out (which disables the Protocol for modified EoDs) bite in practice?
8. When 1995-paper legacy trades were still live, what was the standard fix for the next-day valuation problem — side letter to a 2000-style five-day mechanism, or reliance on "best price reasonably obtainable"?

---

*Prepared for corpus validation. Not legal advice. All Guidance Notes quotations were text-extracted from the official PDFs listed at the top; page references are to the printed page numbers in those PDFs.*

## Practitioner sources — where negotiators actually talk

*Added 2026-07-21. Every URL below was fetched live on that date unless marked otherwise. Ratings are for one purpose only: validating fund-vs-bank markup patterns for the synthetic GMRA corpus.*

### 8.1 Jolly Contrarian — yes, it has a clause-by-clause GMRA anatomy (HIGH, free)

JC does for the **2000 GMRA** what it does for the ISDA: a full "owner's manual" anatomy, Paragraphs 1–21 plus Schedule, Buy/Sellback Annex (BSA 1–4) and Equities Annex (EA 1–5), each page with a Nutshell™ paraphrase, full clause text (templated), a 1996 MRA cross-reference slot, and JC-style commentary. Verified by crawling the paragraph index and sampling pages. **Caveats:** the GMRA commentary is noticeably thinner than the ISDA anatomy (some pages are mostly nutshell + text, commentary a few paragraphs); it covers the 2000 form, not 1995 or 2011; and jollycontrarian.com returns **403 to non-browser fetchers** (WebFetch fails; a browser user-agent works fine).

Best five pages (all verified live via curl with browser UA):
- Landing/anatomy hub: https://jollycontrarian.com/index.php?title=GMRA (also reachable as `Global_Master_Repurchase_Agreement`)
- Paragraph 10 — Events of Default: https://jollycontrarian.com/index.php?title=10_-_GMRA_Provision — commentary explicitly contrasts GMRA single-category EoDs with ISDA EoD/Termination Event architecture; useful for how negotiators *think about* the EoD list
- Paragraph 4 — Margin Maintenance: https://jollycontrarian.com/index.php?title=4_-_GMRA_Provision
- Paragraph 6 — Payment and Transfer (home of 6(j)): https://jollycontrarian.com/index.php?title=6_-_GMRA_Provision
- Full category index (all GMRA pages): https://jollycontrarian.com/index.php?title=Category:GMRA

### 8.2 HedgeLegal (Poseidon Retsinas) — the best public fund-side markup voice (HIGH, free)

No GMRA-specific series, but the PB/NAV pieces are the closest public analogue to buy-side markup lore: written by a fund-side negotiator, listing the exact asks a fund makes against a dealer's template. Directly transferable to fund-vs-bank GMRA dynamics (NAV triggers, cure periods, EoD scope, cross-default). Publications index: https://hedgelegal.com/publications (verified live).

- **PB Agreement Negotiation Part 1** (Dec 2019): https://hedgelegal.com/prime-brokerage-agreement-negotiation-everything-a-hedge-fund-needs-to-know-part-1/ — also as PDF: https://hedgelegal.com/wp-content/uploads/2019/12/Prime-Brokerage-Agreement-Negotiation-Part-1.pdf
- **PB Negotiation Part 2 — Protecting Against Prime Broker Failure; 12 Years After Lehman** (Sep 2020): https://hedgelegal.com/pb-negotiation-part-2-protecting-against-prime-broker-failure-12-years-after-lehman/ — PDF: https://hedgelegal.com/wp-content/uploads/2020/09/Prime-Brokerage-Agreement-Negotiation-Part-2.pdf
- **How Fund Managers Can Mitigate NAV Triggers' Impact on Trading Agreements** (HFLR, May 2020; free reprint): https://hedgelegal.com/wp-content/uploads/2023/09/How-Fund-Managers-Can-Mitigate-NAV-Triggers-Impact-on-Trading-Agreements.pdf — the single best public source on NAV-trigger levels/mechanics across ISDA/MRA/GMRA fund docs
- **U.S. Treasury Clearing: Key Impacts for Hedge Funds** (Mar 2026): https://hedgelegal.com/u-s-treasury-clearing-key-impacts-and-required-actions-for-hedge-funds/ — confirms sponsored-repo was documented via non-standardised MRA/GMRA annexes varying by dealer (good corpus-realism detail)
- The **"fish-or-cut-bait"** waiver-after-EoD provision appears in the Retsinas HFLR series (Mar 5, 2020); part three of the paywalled HFLR original: https://www.hflawreport.com/2552136/how-fund-managers-can-mitigate-prime-broker-risk-legal-considerations-when-negotiating-prime-brokerage-agreements-part-three-of-three.thtml (Hedge Fund Law Report itself: paywalled, MED for repo specifically)

### 8.3 ICMA GMRA Clause Taxonomy & Library, with D2 Legal Technology (HIGH, free)

- Strategy paper (May 2022, free PDF, verified via search result link): https://www.icmagroup.org/assets/ICMA-GMRA-Clause-Taxonomy-and-Library-Strategy-Paper-May-2022.pdf
- This is quasi-official but earns its place in the practitioner layer: the whole project exists because firms negotiate the same GMRA clauses in divergent wordings, and the taxonomy documents **which clauses attract negotiation and what the variant business outcomes are** — i.e., a census of real markup practice, assembled with D2LT from member banks' negotiated books. Best single validator for "is this a clause funds/banks actually touch?"
- D2LT (d2legaltech.com) lists GMRA/GMSLA/PB doc-data consulting and posts on LinkedIn (#gmra), but its own site is service pages, not war stories (LOW standalone).

### 8.4 Subscription practice notes (MED-HIGH, paywalled)

- **Practical Law (Thomson Reuters), "Repos: Global Master Repurchase Agreement 2011 (GMRA)"** — practice note by Jonathan Haines (partner, Ashurst): https://uk.practicallaw.thomsonreuters.com/w-014-3802 — clause guide with negotiation flavour; companion MRA note at https://uk.practicallaw.thomsonreuters.com/w-008-9570. Access: PL subscription (most City firms; trials available). Verified the resource pages resolve; content paywalled.
- **LexisNexis (Lexis+ UK PSL), "An introduction to repo and the Global Master Repurchase Agreement (GMRA)"**: https://www.lexisnexis.co.uk/legal/guidance/an-introduction-to-repo-the-global-master-repurchase-agreement-gmra — guidance note, paywalled with free preview.
- These are drafted by practising negotiators and state default positions/market practice, but in sanitised know-how register — good for verifying claims, not for chatter.

### 8.5 Books — the real negotiation manuals (HIGH, paid)

- **Harding & Johnson, *A Practical Guide to Using Repo Master Agreements: Existing market practice for legal documentation in Europe and the USA*, 3rd ed., Harriman House, 2017** (ISBN 9780857195852; earlier ed. 1843741202). Clause-by-clause text **and commentary** on the GMRA, the US MRA, and the BNYM tri-party agreement, written from documentation-desk experience (Harding also wrote *Mastering the ISDA Master Agreements*, the canonical ISDA negotiation manual). **The single closest thing in print to GMRA negotiation ground truth.** https://www.amazon.com/Practical-Guide-Using-Master-Agreements/dp/0857195859
- **Choudhry, *The Repo Handbook*, 2nd ed., Elsevier/Butterworth-Heinemann, 2010** (ISBN 9780750681599): https://www.sciencedirect.com/book/9780750681599/the-repo-handbook — market mechanics and trading; documentation coverage exists but is descriptive, not negotiation-practice. MED.
- **Frontclear, "Rough Guide to the GMRA 2011 for operations staff & other non-lawyers"** (free PDF, already cited above as FRONTCLEAR-HB): https://www.frontclear.com/wp-content/uploads/2019/05/Rough-guide-to-the-GMRA-2011.pdf — plain-English walk-through incl. Annex I election points. MED-HIGH and free.

### 8.6 ICMA ERCC minutes and working groups (MED, free but patchy)

- ERCC Committee minutes are published as PDFs, e.g. 18 Apr 2018: https://www.icmagroup.org/assets/documents/ERC/2018-04-18-ERCC-Committee-meeting---minutes-200918.pdf and 2 Dec 2015: https://www.icmagroup.org/assets/documents/ERC/Minutes-from-repo-committee-meetings/ERC-Committee-minutes-021215.pdf (links surfaced via search; older tree partially reorganised — navigate from https://www.icmagroup.org/market-practice-and-regulatory-policy/repo-and-collateral-markets/).
- The **ERCC/GMRA Legal Working Group** (quarterly) is where actual documentation debates happen, but its minutes are member-only; contact ercc@icmagroup.org. Committee-level minutes occasionally reveal what the legal WG is arguing about. MED.

### 8.7 Where negotiators do NOT talk (honest negatives)

- **Reddit/forums: nothing good.** Multiple searches (r/quant, r/financialcareers, site:reddit.com with GMRA/ISDA-negotiation terms) surfaced only job adverts and definitional content. Trading-doc negotiation has no genuine public forum culture; the lore moves through LinkedIn DMs, ISDA/ICMA WGs, and desks. Corpus-validation implication: any confident "practitioners say on Reddit…" claim is itself a hallucination marker.
- **LinkedIn**: the one verified substantive poster is **Poseidon Retsinas** (https://www.linkedin.com/in/poseidon-retsinas/ — republishes the PB series via LinkedIn Pulse); D2LT's company page posts on GMRA digitisation. No active public "derivatives documentation negotiators" group with verifiable substantive GMRA content was found — groups exist but are gated and low-signal. LOW-MED.
- **The OTC Space** (theotcspace.com): cleared-derivatives/CCP-centric; searches found no GMRA-negotiation content. LOW for this purpose.
- **Regulation Tomorrow** (Norton Rose Fulbright blog): regulatory client-alert register, not negotiation practice. LOW.
- **Podcasts/YouTube**: no dedicated documentation-negotiation podcast verified. ICMA's webinar/podcast library (https://www.icmagroup.org/media-and-market-data/icma-webinars-and-podcasts/) covers repo topics but the GMRA workshops are paid training courses, not free chatter. Securities Finance Times (securitiesfinancetimes.com) carries repo-documentation *news* (e.g. Clause Library launch coverage) — useful for dates, not for markup lore. LOW-MED.
- **DRS (drs-als.com/gmra-negotiations/)**: outsourced-negotiation vendor; landing page is marketing, with a clause-commentary GMRA guide gated behind a form. Their negotiators demonstrably do this work, but published substance is thin. LOW-MED (guide unverified).
