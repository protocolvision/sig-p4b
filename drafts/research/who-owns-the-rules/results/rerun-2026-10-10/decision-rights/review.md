# Decision rights: independent review

11 October 2026. Fresh Opus review. Only this file and `decide-recode.csv` were written.

## The pre-registered verdict is Mixed, and it is not close on condition 1

Condition 1 needed AGT below half the comparison median (under 4.5%) with its Wilson upper bound under 9.1%. AGT is 22.5% (12.3–37.5; 9 of 40), the highest of the nine domains, and 25.0% when the rest20 weights are applied. Not every domain is below 5%, so no genre effect. Under the binding rule the result is **Mixed**, whatever condition 2 says.

## The matching is valid in spirit, but AGT and the small domains are different populations

Of 20 seeded matched statements across all nine domains, all have the domain term correctly assigned and 14 are clearly about that domain's rules. Four are marginal (e.g. business-process "change management"). Two use the wrong sense of the term:
- TRD "portfolio risk limits" in a multifamily mortgage role, not trading;
- CLN "clinical protocols" for a pharma medical advisor, which means trial protocols, not hospital protocols.

Biases that matter:
- **AGT is a title-selected, senior-architect population.** 48 of 60 AGT items come from the `newtitle` stratum, and 53 of 60 have AI-type titles. Comparison domains are mostly the general `rest20` stratum (CRD 58/60). Three of AGT's 9 decide items are engineering standards, not rules governing an agent (X020, X124, X253); dropping them still leaves 6/37 = 16%.
- **CHG is polysemous.** "Change management" also catches regulatory, construction-scope and organisational change. About 30 of 46 CHG rule duties have no IT change-control marker.
- **TRD (n=7) and CLN (n=5) are too small to read.** CLN is mostly pharma employers, so it does not measure formularies or care pathways.
- **AI work leaks into comparison domains:** 21/60 ACC and 16/60 CHG items have AI titles.

## Exploratory re-code: every agent decide duty sets standards; comparison duties split

I coded all 35 decide items from spans only (ids shuffled, no domain field; domain words inside spans unavoidable), then unblinded with dr-key.json (all real items; domains match final.csv).

STANDARD | CHANGE: AGT 9 | 0; CHG 2 | 6; CRD 2 | 2; PRC 3 | 2; TRD 0 | 1; ACC 5 | 0; PRO 2 | 0; FRD 1 | 0; comparison pooled 15 | 11. AGT against pooled comparison: Fisher exact p = 0.033 (two-sided). The split holds, but it is fragile:
- Without CHG, p = 0.14 (AGT 9/0 against 13/5).
- Flipping the three borderline comparison CHANGE codes (X190, X359, X169) to STANDARD gives p = 0.08.
- ACC, the domain whose roles most resemble AGT (identity and security architects), is also 5/0 STANDARD.

It may reflect role type (architects set standards; operators approve changes) as much as agents.

## Part 2: the coding mostly holds, but Entra is mis-described

Eight rows checked against stored text (AGT-01, -02, -06, -07, -E2, CLN-01, PRC-05, FRD-02); all quotes present.

- **AGT-E2 (Entra) does name who approves changes to an agent's permissions.** Agent access requests go "to designated approvers based on the access package configuration"; **sponsors** are "human users accountable for making decisions about its lifecycle and access", and extensions "trigger a new approval cycle". So docs.md's "none names who approves changes to an agent's rules or permissions" holds for *rules* only. It is voluntary vendor documentation; since NIST AC-2's organisation-defined approver was coded no, only the sponsor role should carry the yes.
- **AGT-01 (OMB M-25-21)** is binding on agencies and lets the CAIO waive minimum practices "for a specific covered AI application". The strongest near-miss: an exception approver, not agent-specific.
- **AGT-07 (Ohio)** is an advisory council that establishes "the framework for evaluating and authorizing". It sets standards; the yes is generous.
- **AGT-02 and AGT-06** are correct as general AI governance.
- **PRC-05 (GSAM)** names contract parties agreeing a price relationship, not a pricing-rule approver; PRC's strongest level becomes firm-policy.
- **FRD-02** quotes a monitoring designee, which is apply, not decide. The same file says the program must be "approved by the national bank's or savings association's board of directors"; yes stands with that quote.
- **CLN-01** says a "formulary system must be established by the medical staff". That names who sets it, not who approves changes; weaker than CLN-03/04.

All 8 comparison domains still have at least one document naming a decider.

## Finding for the public report

> Job ads do not show a missing decider for AI agents. 22.5% of agent rule duties are decision duties (9 of 40; 95% CI 12–38%), against a median of 9.1% across eight other rule systems, so our pre-registered "agents are an exception" test failed. In an exploratory blind re-code, all nine agent decision duties set standards up front, such as "set the engineering standards that define how agentic AI gets deployed at scale". By contrast, 11 of 26 in other domains approve specific changes or exceptions, such as "Review and approve complex chargeback claims requiring managerial review due to … pricing exceptions" (p = 0.03, driven mostly by IT change management, in an agent sample drawn mainly from AI-titled senior roles). Written policies show the same gap: every comparison domain has a public document naming who approves rule changes. The agent documents name deciders for AI use in general, and the only one naming who approves a change to an agent's permissions is vendor product documentation (Microsoft Entra's agent "sponsor").

## Suggested figure

One row per domain, ordered by decide share: a dot with Wilson interval, a dashed line at the 9.1% median, and to its right a small bar splitting decide items into "sets standards" and "approves changes" (AGT 9 | 0, CHG 2 | 6). Grey out TRD (n = 7) and CLN (n = 5).

## Fixes before publishing

1. docs.md AGT note: Entra names deciders for an agent's *access*; none for its *rules*.
2. Mark AGT-07 advisory; fix PRC-05 and FRD-02.
3. Add the AGT stratum (48/60 `newtitle`) and CHG polysemy to the limits.
