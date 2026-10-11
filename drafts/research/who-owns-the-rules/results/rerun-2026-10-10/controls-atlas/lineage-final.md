# Lineage of control regimes: second coding and recomputed timing (Phase 4c)

11 October 2026. This file completes the two-coder step that `lineage.md` flagged as not done.

- **Coder 1** is the original collector (`lineage.csv`).
- **Coder 2** is a fresh Sonnet agent. It coded all 46 rows blind, from the milestone, status and quote only, without seeing the stage, the notes or this project's other files.
- **Adjudicator:** Opus.

Output: `lineage-final.csv`. It has both codes, the final stage, coder 2's rationale and an adjudication note on each disputed row.

## The two coders agree on 42 of 46 milestones (kappa 0.88)

Cohen's kappa is 0.88 (linear-weighted 0.88), with raw agreement 91%. Both coders used all five stages.

| Coder 1 \ Coder 2 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| 1 | 6 | 0 | 2 | 0 | 0 |
| 2 | 0 | 2 | 0 | 0 | 0 |
| 3 | 2 | 0 | 14 | 0 | 0 |
| 4 | 0 | 0 | 0 | 11 | 0 |
| 5 | 0 | 0 | 0 | 0 | 9 |

All four disagreements are between stages 1 and 3. Adjudication:
- **8, Amazon API Gateway launch (2015): 1 to 3.** The launch quote names authorization and access control per API, which means rules bound to the caller's identity.
- **15, S3 bucket policies (2010): 1 to 3.** These are conditions on the AWS account and on request attributes. One consequence follows: the cloud domain now has no sourced stage-1 milestone. Its baseline is the first sourced row, 2010-07-06, and it is censored. AWS account keys date from 2006, but that date is not sourced.
- **27, stateful inspection codified (NIST 2009): 3 to 1.** Tracking connection state is not a binding to identity, application, data labels or risk. The firewall rules are still fixed. Timing is unchanged, because network had already reached stage 3 and above earlier.
- **45, EPA memo withdrawal (2023): kept at 3.** The row records the withdrawn requirement. It stays excluded from timing, as before.

## Agents moved from static rules to central policy engines in about three years; APIs took 19 years and network security 31

Years from the first sourced stage-1 control. "Stage 5, product" counts only product features, not standards or laws, so a policy-language standard such as XACML does not count as a shipped engine. For agents, the dates come from `timeline-final.csv`, availability events only. Agent stage-5 "product" means generally available.

| Domain | Rows | Baseline (first stage 1) | Stage 3 or above | Stage 4 or above | Stage 5, any | Stage 5, product | First binding legal requirement |
|---|---|---|---|---|---|---|---|
| APIs | 14 | 1999-06 | +3.7 (2003) | +3.7 (2003) | +3.7 (2003, XACML standard) | +18.8 (2018, OPA) | +16.5 (2015, PSD2; sector-specific) |
| Cloud | 7 | 2010-07 (censored, no stage-1 row) | +0.0 (2010) | +0.2 (2010) | +6.6 (2017) | +6.6 (2017, SCPs) | +12.4 (2022, DORA; sector-specific) |
| Network | 10 | 1989-03 | +14.0 (2003) | +14.0 (2003) | +31.4 (2020, NIST 800-207) | n/a (no product row at stage 5) | +14.0 (2003, HIPAA; sector-specific) |
| Industrial | 7 | 1989-06 (censored) | +2.7 (1992) | n/a | n/a | n/a | +0.0 (1989) |
| Water | 7 | 1974 (censored) | +24.6 (1999) | +24.6 (1999) | n/a | n/a | +0.0 (1974) |
| Agents, all evidence | 289 | 2022-07-25 (archive) | −1.0 (2021, archive) | +1.8 (2024) | +3.3 (2025, preview) | +3.6 (2026-03, AWS AgentCore Policy GA) | +2.5 (2025-02, EU AI Act Art 4, general); +4.4 (2027-01, Colorado, scheduled) |
| Agents, primary only | 268 | 2023-03-13 | −0.3 (2022) | +1.2 (2024) | +2.6 (2025, preview) | +3.0 (2026) | +1.9 (2025-02, general); +3.8 (2027-01, scheduled) |

The agent dates rest on these events:
- first stage 1: A-002 (archive) and G-001 (primary);
- first stage 3: A-001 (Credo AI, archive) and A-003 (GitHub org policy, December 2022);
- first stage 4: P-027 (Bedrock guardrails on agents, May 2024);
- first stage 5: A-050 (GitHub Agent HQ preview, October 2025);
- first stage 5 GA: P-085 (AWS AgentCore Policy, March 2026).

The agent baseline is censored in the same way as cloud's. Stage-2 and stage-3 controls appear before the first sourced stage-1 control. Probable earlier stage-1 controls, such as the 2020 OpenAI API rate limits and content filter, are not in the record.

Counting instead from the first agent or model control of any stage on a primary source (the OpenAI Moderation endpoint, 2022-08-10):
- stage 3: +0.3;
- stage 4: +1.8;
- stage 5: +3.2;
- stage 5 GA: +3.6;
- EU AI Act Art 4: +2.5;
- Colorado: +4.4;
- EU Annex III (2 December 2027 under the Omnibus): +5.3.

Placing agents on the table:
- **Agents went from stage 1 to stage 5 faster than any other domain**, by a factor of about 2 against cloud and 5 to 10 against APIs and network security. The likely reason, which is an inference: agent controls reuse identity, policy-engine and gateway machinery those domains already built. The first stage-5 agent control in GA, AgentCore Policy, runs on Cedar, the API domain's 2023 stage-5 row.
- **The first binding rule came fast in date, but it is not a control rule.** EU AI Act Art 4 (February 2025) requires AI literacy, not any control in the timeline. Colorado (January 2027, scheduled) and EU Annex III (December 2027) require a designated human overseer. None of the 289 events is a binding rule, and `gaps.md` finds no law that requires any agent control. Measured as "first law requiring a control of the kind the vendors ship", agents have no date yet. That puts them where APIs, cloud and network stood for 12 to 16 years.
- **Agents follow the product-first path of APIs, cloud and network:** products, then standards, then sector-specific law. They do not follow the law-first path of industrial and water safety, where a statute is the baseline (+0.0).

## Limits

- The milestone sets are small (7 to 14 per domain) and were picked by one collector, so "first" means "first in the sourced record".
- Baselines are censored in cloud, industrial, water and agents.
- The agent row comes from a different instrument: 289 vendor events against hand-picked milestones. Its earliest dates are therefore more finely resolved than the other domains' dates.
- The stage scale was written for agents. Applying it to water and industrial safety, which have little stage 2 and no stage 5, compresses those domains.
