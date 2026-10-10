# Research design: who owns the rules when agents join the business?

Protocols for Business · version 1 · 10 October 2026 · status: ready for a first blind run

## 1. The problem

Companies are putting AI agents into sales, finance, operations and support. Agents act under rules:
who may approve a deal, how much can be spent, what data may leave, who may stop the work. Many of these
rules are unwritten; many are split across finance, security, legal and sales; and agents test them faster
than people do. When a rule needs to change, often nobody owns the change. Companies are already hiring
for related work (AI governance leads, agent managers, forward-deployed engineers, GRC engineers), and
earlier technology shifts produced roles that lasted (CISO, SRE, data scientist) and roles that faded
(webmaster, chief knowledge officer, prompt engineer).

A company deciding what to hire, and a research group deciding what to teach, need to know which of these
is happening.

## 2. Why a new design

The work so far is exploratory: four drafts in [`exploratory/`](exploratory/), written by one researcher and
one model, with sources found through search summaries and revised over several review rounds. It produced
hypotheses, not findings. Its weaknesses:

- **Selection.** We chose the role lineages and the frameworks, knowing what we hoped to find.
- **Stake.** The group builds Business Protocol Management (BPM). Every hypothesis that a role will form
  around protocol work flatters that work.
- **Sources.** Most claims rest on search-result summaries, marked (S), and some on memory, marked (M).
- **Drift.** Hypotheses were revised in response to challenges inside one conversation, so they fit the
  evidence we happened to gather.

This design states the questions and hypotheses before testing them, names what would refute each one,
fixes the methods and the evidence standard, and hands the work to an agent that has not read the
exploratory drafts. We then compare its results with ours.

## 3. Definitions

| Term | Meaning in this study |
| --- | --- |
| Protocol | A rule that people and agents act under and that others rely on: an approval, a limit, an access right, an interface, a right to stop the work. Can be written or unwritten, enforced in a system or remembered |
| Protocol work | Finding the rules a business actually runs on, deciding whether to change them, propagating changes into systems and agent configuration, checking the result, retiring rules that no longer serve |
| Business Protocol Management (BPM) | The practice the group proposes for protocol work, in three phases: See, Design, Evolve. Public guide: `src/research-bpm.html` |
| Role | A recognisable bundle of activities under one accountability, with its own job postings. A title alone is not a role |
| Distinct role | Postings in which protocol work is the primary duty (more than half the listed duties), under any title |
| Absorbed | Protocol work appears as a secondary duty in postings for existing roles (controller, revenue operations, GRC, security, privacy, platform engineering) |
| Lasting role | Still posted under a recognisable title, or holding an official occupation code, at least ten years after it first appeared |
| Faded role | Posting volume fell by more than half from its peak within five years, or the title folded into another role |
| Seniority at emergence | The level of the first ten documented holders or postings: entry, mid, senior, executive, or outside consultant |
| Institutional expression | The offices, roles, routines and standards through which a social movement's claims become ordinary organizational practice |
| Agent management | Supervising, configuring, prompting and quality-checking AI agents |

## 4. Research questions

- **RQ1. Emergence.** Historically, under what conditions did a new set of activities become one
  accountable role rather than being absorbed into existing roles, and at what seniority did such roles
  first appear?
- **RQ2. Application.** Do those conditions hold, or are they forming, for protocol work in companies
  deploying AI agents?
- **RQ3. Form.** If a distinct role forms between 2027 and 2030, what is its level, reporting line, source
  of authority and measure of success? How does it differ from agent management?
- **RQ4. Movement.** Is BPM, or protocol work generally, the institutional expression of the AI safety
  movement inside companies that deploy agents, or something else?
- **RQ5. Knowledge.** What tacit knowledge does protocol work need, and how much of it can be written down
  and taught?

## 5. Hypotheses and rivals

Each hypothesis states what would refute it. Rivals are the competing explanations the run must give equal
effort.

| ID | Hypothesis | Refuted if | Rival |
| --- | --- | --- | --- |
| H1 | A role lasts when three conditions hold together: (a) it owns a trade-off that stays permanent rather than a one-off migration; (b) no existing role already owns that trade-off; (c) an outside force renews the demand, with a number the role controls | Two or more lasting roles in the sample lacked one of (a)–(c), or two or more faded roles had all three | R1: lasting roles are explained by technology adoption volume alone |
| H2 | Lasting roles first appeared at entry or mid level, or as consultants, with authority from a written mandate (a policy, a law, a signed agreement), not from seniority | Most lasting roles in the sample first appeared as senior or executive hires | R2: new roles start senior and are later delegated |
| H3 | By end of 2029, most companies deploying agents absorb protocol work into existing roles; distinct roles appear in a minority (under 20% of such companies), concentrated in AI-native firms in dense labour markets | Distinct-role postings for protocol work are common outside AI-native firms by 2029, or no distinct postings appear at all | R3: it is all engineering; protocol work becomes policy code and disappears into platform teams |
| H4 | Agent management titles peak and fold into existing managers' jobs by 2028–29, as prompt engineering did; protocol work does not fold the same way, because it survives a swap of the agent technology | Agent management titles keep growing through 2029 as a distinct occupation, or protocol work shows the same fade pattern | R4: agent management is the durable role and protocol work is part of it |
| H5 | BPM matches the pattern of an institutional expression of the AI safety movement on mechanisms and business-case framing, but not on carriers, forcing lever or profession; it is a managerial translation of the agent-control strand, from a separate lineage | Movement organizations or people are found carrying BPM-like practice into deploying firms, or the mechanism overlap is weak | R5: privacy-led AI governance is the movement's institutional expression in firms, and BPM is unrelated |
| H6 | A distinct role forms only in a middle band: enough of the knowledge is written down to be claimed and taught (a rule register, an amendment rule, a metric), while judgment about trade-offs across functions stays with a person | Distinct roles form where nothing is written down, or persist where everything has become automated checks | R6: tacit knowledge is irrelevant; budgets and regulation decide |
| H7 | "Time to amend" (days from when a rule's overrides or workarounds cross a threshold to a recorded decision to change or keep it, counting open cases) can be measured from existing records and differs between firms with and without an owner | Needs field data; **out of scope for desk research** and left for a case study | — |

## 6. Methods

The run has four phases. Phases 1 and 2 are blind to BPM: the agent works only from this design's
definitions and does not read the group's materials. Phase 3 opens the BPM guide. Phase 4 synthesizes.

### Phase 1. Comparative role histories (RQ1; H1, H2)

1. **Sample.** At least twelve roles, chosen before any coding:
   - six that lasted, four that faded, two still contested;
   - at least four chosen by the agent from outside this list of examples (CISO, SRE, DevOps engineer,
     data scientist, product manager, social media manager, webmaster, chief knowledge officer, prompt
     engineer, Y2K coordinator, growth hacker, chief metaverse officer), using the O*NET New and Emerging
     occupations list, the Census occupation index, or LinkedIn emerging-jobs reports;
   - at least two that came from a social movement or a law rather than a technology (for example,
     privacy officer, safety engineer, sustainability manager).
2. **Coding sheet**, one row per role: first year the title appears; earliest job posting found (quote it);
   seniority of the first holders; the business question that led to the hiring; the trade-off it owned;
   the incumbent role it displaced or failed to displace; the outside force and the number; first
   association, certification and official occupation code (years); status today; evidence grade for each
   cell.
3. **Analysis.** Test H1 and H2 against the sheet, row by row, and report every exception.

### Phase 2. Framework triangulation (RQ2, RQ3, RQ5; H3, H4, H6)

1. Apply at least five established frameworks for how roles emerge, independently, each producing its own
   prediction for protocol work before the next is applied. Candidates: professional jurisdiction (Abbott);
   integration across units (Lawrence and Lorsch, Galbraith); task-based labour economics (Autor; Acemoglu
   and Restrepo); decision rights under cheap prediction (Agrawal, Gans and Goldfarb); professionalization
   markers (Wilensky); social movements into organizations (Dobbin; Edelman; Lounsbury). The agent may
   substitute frameworks it finds stronger, with reasons.
2. **Current signals.** Collect public data on postings and titles for 2023–2026: AI governance, agent
   operations or management, business rules analyst, GRC engineer, forward-deployed engineer, prompt
   engineer. Sources: Indeed Hiring Lab, LinkedIn Economic Graph, Lightcast, Revelio Labs, IAPP reports,
   regulators' texts.
3. Report where the framework predictions diverge and where they converge, and on what.

### Phase 3. The movement test (RQ4; H5)

1. Read the public BPM guide (`src/research-bpm.html`) and nothing else from the group.
2. Build the conditions for an institutional expression from the movement-to-organization literature (at
   least five cases, such as industrial safety, quality, environment, privacy, civil rights, trust and
   safety, responsible AI teams).
3. Map where the AI safety movement has institutionalized (labs, governments, standards, professions,
   deployer law).
4. Score BPM against each condition, with evidence. Score the rival (privacy-led AI governance) the same
   way.

### Phase 4. Synthesis

1. A verdict per hypothesis: supported, partly supported, not supported, or untestable with the evidence
   found; a confidence (low, medium, high); and the strongest evidence on each side.
2. Five to ten dated forecasts for 2027–2030, each with a probability and a named public source to check
   it against.
3. A list of what would most change the conclusions.

## 7. Evidence standard

- **Grades.** (P) primary source opened and read; (R) reputable secondary source opened and read;
  (S) supported only by a search-result summary; (M) from model memory. Load-bearing claims need (P) or
  (R); if only (S) or (M) is available, the claim is reported as unconfirmed.
- **Quotations** only when the exact words were seen; otherwise paraphrase and say so.
- **Every metric names its source document** and date.
- **Citations** in Chicago notes style.
- **Disconfirmation first.** For each hypothesis, search for counter-evidence before supporting evidence,
  and log both searches.

## 8. Controls for bias

| Risk | Control |
| --- | --- |
| Anchoring on our drafts | Blind phases 1 and 2; the agent must not open `exploratory/` |
| Sample chosen to fit | Agent-chosen roles, failed and contested roles, roles from movements and laws |
| Our stake in BPM | Rival hypotheses get equal effort; the review counts verdicts against BPM as well as for it |
| Search-summary drift | Grades for every claim; ten citations audited by hand in review |
| One model's view | Optional second run with a different model, compared with the first |

## 9. Outputs

The run writes to `results/run-YYYY-MM-DD/`:

- `report.md`: findings by research question, verdicts, forecasts, limitations;
- `role-sheet.csv`: the Phase 1 coding sheet;
- `frameworks.md`: Phase 2 predictions, divergence and convergence;
- `movement-test.md`: Phase 3 scoring;
- `sources.md`: every source with its grade;
- `search-log.md`: queries run, including the disconfirming ones.

## 10. Review after the run

1. **Compare** each verdict with the exploratory drafts' position. Record agreement, disagreement and new
   findings in `results/run-YYYY-MM-DD/review.md`.
2. **Audit sources**: check ten load-bearing citations by hand, chosen at random.
3. **Check the stake**: does the run's support for BPM rest on (P) and (R) evidence?
4. **Decide**: what changes in the BPM guide, the published job description, and the next design version.
   Revised hypotheses go into a new version of this file, not into the old one.

## 11. Limits

- Desk research cannot measure time to amend (H7) or observe how roles work inside firms; that needs case
  studies.
- Job-posting data for 2025–2026 is partly behind paywalls.
- The run's network access may block some sources; it must grade claims accordingly rather than fill gaps
  from memory.
- Forecasts can only be scored from 2027.
