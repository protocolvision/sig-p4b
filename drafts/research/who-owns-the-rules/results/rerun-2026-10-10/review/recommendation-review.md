# Review: recommendation.md (rerun 2026-10-10)

Fresh adversarial review against `findings.md`, `comparison.md`, `red-team.md`, `field-plan-scaffold.md` and `instruments/I4.md`. recommendation.md was not edited. Most numbers check: 123 posting codes, 771 spans, 5 of 34 speakers, the AI Act and Colorado quotes and dates, and the five forecasts. All required sections are present. No construction client is named. The problems are mostly confidence set too high and the security finding stated more firmly than the evidence allows.

## Critical fixes

**1. F4 confidence is inflated.** Findings give "high" only on what the texts say, and "medium" on the contrast: the AI-law denominator is 4, one coder did the coding, and under the PRA reading Art 17(1)(m) would make it 1 of 4. Line 15:
- Change: "Named change owners appear only in trading texts and AI labs' own policies (F4; high on the texts)."
- To: "In the 19 texts read, named change owners appear only in trading texts (8 of 12 from guidance) and AI labs' own policies (F4; high on the quotes, medium on the contrast)."

**2. Line 34 contradicts F4 on labs.** It says change owners "exist only in trading", but lab self-policies name them (3 of 3).
- Change: "Those exist only in trading: 15c3-5 CEO certification, Series 57 registration and the RTS 6 designated person."
- To: "Binding versions exist only in trading (15c3-5 CEO certification, Series 57 registration, the RTS 6 designated person). Labs name change owners in voluntary policies."

**3. The security home is stated as settled.** F3 is low. Cluster 111 holds only because of one Thrivent posting. The red team adds that rule wording appears in 20 of 30 AI postings "across engineering, content, consulting and security", that JLL sits in Facilities governance, and that the frame is mostly regulated finance. The red team's conclusion is that postings "do not show where it settles".
- Line 24, change: "**Designing rules (PE) belongs where it already forms: security and governance review.**"
- To: "**Designing rules (PE) is most visible in security and governance review (low).**" Then add after the I3 sentence: "Cluster 111 holds only because of one posting, and the frame is mostly regulated finance."
- Line 36 heading, change "rule design sits in security" to "rule design shows up most in security review".

**4. Recommendations carry "medium" with no tested evidence behind them.** The comparison says the rerun "does not test whether the alternative works better."
- Line 22: change "(`comparison.md` claim 21; medium)" to "(claim 21; low to medium: vendors ship registries, but firm ownership is untested)".
- Line 24: change "held where the firm can change it across vendors (medium)" to "(low to medium; rests on the trading analogy and the vendor relabelling in F6)".
- Line 30: change "(medium for register and owner; low for the pilot)" to "(low to medium for register and owner; low for the pilot)".

**5. The F2 summary hides that existing-job duties are mostly technical.** Line 14:
- Change: "Existing staff inside functions often run agents (F2; low to medium)."
- To: "Agent duties sit in existing jobs about as often as under new AI titles (0.86, 0.63–1.15), but about 53% of those jobs are computing or engineering. The evidence that business staff run agents inside functions is 6 of 10 speakers, single-coded (F2; low to medium)."

**6. Gatekeeper citation overreaches.** I4 coded only a forum notice of Amazon's policy. Mastercard's guide was not acquired.
- Change: "Amazon's policy (from 4 March 2026) requires agents to identify themselves and stop when asked. Neither names a role inside the firm (`comparison.md` claim 18; I4)."
- To: "A forum notice of Amazon's policy (from 4 March 2026) requires agents to identify themselves and stop when asked, and names no role inside the firm. Mastercard's guide was not read (claim 18; I4)."

**7. Wrong citation for "direct and exclusive control" (line 53).** Claim 14 does not contain the phrase. It comes from comparison §4 "Survive" (IN).
- Change "(claim 14; medium)" to "(`comparison.md` §4, IN; medium). The rerun did not test whether firm-held rules work better."

This is also the one surviving warning that favours BPM, so it needs that caveat.

**8. RD has no artefact.** The by-layer brief asks for an artefact for each layer, and line 26 gives none for RD.
- Add: "The artefact is a written statement of the council's decision rights and a dated log of its decisions on agent rules (low; not observed)."

## Minor fixes

- Line 12: add "on a weak test, because the earliest recordings were missing" after "tested and failed" (H8 per findings).
- Line 22: "No posting or speech span describes reviewing exceptions" overstates. Postings carry PV 2 of 123 codes, and only speech is checked for exception reviews. Write "No speech span describes reviewing exceptions or overrides, and PV is 2 of 123 posting codes."
- Line 22: share handled and interaction scores are measures of running agents, not of rule-finding. Say so before offering them as a PV starting point.
- Line 24, on seniority: the posting that carries cluster 111 is a Principal Engineer, and IQVIA's role is an architect. "Practitioner or senior-practitioner" fits, but note that the observed holders are senior individual contributors.
- Line 38: the function counts are pooled spans (862), including untimestamped pages, and recall is about 0.5. The "medium" for "with existing staff" leans on single-coded speech. Use "medium for dispersion; low to medium for existing staff."
- Line 50 heading says "two supported warnings" but lists three. The third is a reporting rule. Use "three warnings".
- Line 52: "No such posting exists in 25,512 postings" should add "from crawlable boards; 59% of frame employers, including the adoption leaders, are not visible".
- Line 60: no field claim tests PV directly. C7 covers RD and C9 covers public visibility. PV appears only as probes under C6 and the R-D interviews. Write "(C7, C9; PV through C6 probes)".
- Lines 78–82: the scaffold sets no schedule, so "field work ends by mid-2027" is the memo's assumption. Say so. Predictions 6–8 restate the C7, C8 and C6 thresholds correctly, but their probabilities are new here. Mark them as the authors' priors. Reword prediction 7: "decided no episode recorded in the window".
- Line 65: good as it stands. It correctly cites the lab-policy fact against the draft's framing advice.
- Vocabulary: the training section follows the rule ("training for the capability", "not the method"). Line 1's "how protocol vision and Business Protocol Management spread" reads as advocacy. Consider "who should own agent rules: what the rerun supports".

## Tilt check

The stake paragraph (line 18) and the bet labels are honest. What remains of the tilt is in fixes 3, 4 and 7. Firm-owned registers, written limits held across vendors and the security home all carry more confidence than the rerun gives. Each of them points toward an artefact BPM would supply.
