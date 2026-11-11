# SIG-P4B 2026-11-02 — Session Notes

Participants:
  - Sebastián Aristizábal | UTC+1
  - Ben
  - Brown Elk
  - Dylan Fitzgerald — UTC-6
  - Andre Comeau | UTC-5
  - ComplexSy
  - Nick
  - Jose Leal
  - Surya
  - PAtwater | UTC-8 | 42P
  - Tom Guarriello
  - divesh
  - Rika Goldberg | Axia Network
  - rafa (UTC+1)
  - Mike Casey | UTC -5
  - bunkerheadz1998
  - Matthew McDowell-Sweet (UTC)

---

## 📖 The Reading

The main reading for the session was an academic paper (pre-published around January of the previous year) on **AI agents and the principal–agent problem**, covering agency law, delegation, loyalty/alignment, liability/enforcement, and shared environments. The exact title and author were not clearly stated in the transcript. Also referenced as recommended reading is **Matthew McDowell-Sweet's blog post on "product thinking vs. protocol thinking"** (product versus protocols).

## 🧭 Overview

This was the **kickoff session for the "Protocols for Business" group's next year-long arc**. Rafa opened with a recap of the past ~18 months of reading (organizations as "knots of tensions," non-events, AI adoption maturity, standards, protocol hardening) and laid out the proposed themes and logistics for the coming year. The group then did extensive participant introductions, followed by silent reading and a round-robin discussion of the agent/principal-agent paper. Much of the discussion drew parallels between AI agents and crypto/DAO governance, and converged on open questions about liability, enforcement, alignment at scale, and how fast the field is moving.

## 💡 Key Points & Themes

**Framing and goals of the year (Rafa):**
- The year's aim is to develop "protocol vision" — the ability to *see* protocols everywhere, articulate the rules businesses run on, read incidents/agent traces through a protocol lens, and build intuition about which rules to harden, keep soft, or remove.
- Proposed six themes (not committed): (1) what an agent is and current governance processes; (2) natural/biological coordination without a manager; (3) emissions and signals (stigmergy, pheromones) in business; (4) hardness — seeing and engineering it; (5) dynamic environments.
- Core working hypothesis: as AI agents won't "ask for manager approval," management shifts from **gates** (which incentivize humans) to **guardrails** that match the tempo of work. Rafa cited a viral video of a concert-hall exit where a narrow/blocked entrance can speed up exit flow — illustrating how constraints can enable faster tempo.
- Lessons from prior reading: some tensions are handled in-the-moment, others built into structure; "non-events" (e.g. safety protocols prevent accidents you then can't count); tempo mismatches (Boom Supersonic's R&D outpacing its supply chain); standards adoption shaped by incentives (QWERTY); working with agents is largely "middle management" and gathering the right context.
- Participation is tiered: observer, protocol-watcher, or "serious play" (building case studies). Rafa noted an intent to turn this into **paid consulting work** via existing leads.

**Discussion of the agent paper:**
- **Rika:** Strong parallels to DAO governance — the principal-agent problem resembles delegates who are supposed to represent token holders but act autonomously. Asked what pitfalls crypto governance can teach so the group doesn't "reinvent the wheel."
- **Nick:** In crypto, things claimed to be "decentralized/autonomous" often aren't truly separate — separation is used for legal liability. The real challenge is defining what counts as genuinely autonomous (e.g. splitting an agent across 10 machines to claim autonomy); the paper sidesteps this.
- **Mike Casey:** Found the loyalty discussion thought-provoking. Raised an enforcement puzzle: traditional principal-agent problems assume a corporate/human entity that exists in time and space and can be held accountable, whereas agents are *ephemeral and infinitely replicable* — enforcing against a specific agent (vs. the lab that built it) seems nearly impossible.
- **Matthew:** Explored the question of **scale/speed** using four dimensions — tempo (time per action), span (length of mandate), width (how many agents in parallel), and depth (layers of delegation/hand-off). Humans occupy the *middle* of each axis; the edges and an expanding "frontier sphere" are where opportunity for "particularization" lies (invoking the Bezos "your margin is my opportunity" idea).
- **Jose Leal:** Connected to his "open social protocols" / "life space" work — at scale, how do you ground what makes a protocol beneficial vs. detrimental, across both AI and human levels? Different groundings yield different behavior.
- **Dylan:** The paper (pre-pubbed ~18 months ago) already feels dated given how fast the field moves; its theoretical agency/alignment issues are now concrete. Cited the flood of CVEs/vulnerabilities and the tension that restricting agent behavior to stop malicious use also hampers security researchers. Noted governance feels simultaneously overdue, urgently needed now, and premature (waiting for things to settle).
- **Brown Elk:** Coming from risk/insurance, flagged liability and agency (agents, AI, autonomous vehicles) as the key questions; joined late and will read more deeply.
- **ComplexSy:** Questioned two of the paper's assumptions — that efficiency gains from delegation are limited (he sees many small gains compounding, making efficiency "sticky across the board") and the need to model a **behavioral delegation threshold** (a critical risk point beyond which delegation creates legal/complication risk). Noted traders already offloading research to agents and models incentivized toward verbose/constant communication.
- **Ben:** Prefers a "Doctor Octopus" model — agents as extensions of human judgment rather than separate delegatees. Argued human-judgment grounding can scale (roughly logarithmically) by sampling outputs and iteratively **distilling smaller, reviewable chunks of judgment** into smaller/statistical models, with a frontier model as a proxy for human judgment used mainly for monitoring/alignment. Framed context as the "pheromone medium" for stigmergic signals in distributed AI systems. Plans to write this up.
- **Sebastián:** With an LLM, divided the paper into five spaces — mandates & consent; loyalty & conflicts; delegation chains; evidence & audit; shared environments — as potential anchors for future protocol discussion.
- **Rafa (closing take):** Endorsed the "speed of development" observation; noted there's still no cohesive definition of what an agent *is* as a software object (is it the same agent across a Claude Code session or many spun up?), and reiterated the liability question (if an agent you spin up does something harmful/illegal on autopilot, are you liable or is Anthropic/Claude?).

## 🔀 Questions & Disagreements

- What legally/operationally counts as a genuinely "autonomous" agent, and how much obfuscation makes it so? (Nick)
- Who is liable when an agent on autopilot does something harmful or illegal — the user or the model provider? How do you enforce against ephemeral, infinitely-replicable agents? (Mike, Rafa)
- No settled definition of "agent" as a software object (Rafa).
- Disagreement with the paper's premise that delegation efficiency gains are limited — ComplexSy argued gains compound; also proposed modeling a delegation risk threshold.
- Tension between restricting agent behavior to block malicious use vs. enabling security research (Dylan).
- Is governance intervention overdue, urgently needed now, or premature given things haven't settled? (Dylan)
- How to ground "good vs. bad" protocols at scale, across both human and AI levels (Jose).
- Competing framings: agent-as-separate-delegatee (paper) vs. agent-as-extension-of-human-judgment ("Doctor Octopus," Ben).
- Timing/format of the group's "matchmaking"/reading-selection process — clarified by Rafa as informal and collaborative, with him retaining final say (ComplexSy asked).

## 🔗 References Mentioned

- Matthew McDowell-Sweet's blog post on product thinking vs. protocol thinking (product vs. protocols).
- Summer of Protocols / Protocol Institute (2025 cohort, "protocol kits," Protocol Reader, book club).
- Venkat (Venkatesh Rao) — his writings cited as the on-ramp to protocols (Tom).
- "Knots of tensions" — concept attributed to Timber (in transcript).
- Boom Supersonic (tempo mismatch example); QWERTY (standards adoption); forward deployed engineer concept.
- Water rates / water data case study (vibe-coded, ~12 weeks) built by the group; Patrick (PAtwater) involved in water data.
- DAOs / crypto governance, principal-agent problem, delegates vs. token holders (Rika, Nick).
- Jeff Bezos "your margin is my opportunity" (Matthew).
- Stigmergy / pheromones as coordination signals (Rafa, Ben).
- Jose Leal's "open social protocols" and "life space" concept.
- Upcoming guest speakers: Navid (agentic SEO / agent readiness for websites, ~2 weeks out); Will Bins (fault-tolerant OS for 1,000-year autonomous operations; ex-Ethereum, late November); possible talk from Patrick or Venkat on formal protocol theory.
- The group website (protocolsforbusiness.com) with sessions, research, case studies, a 3D reading "map" (built with Claude), RSS feed, and GitHub for reading suggestions.
- "Business Protocol Management / BPM 2.0" — a term the group is trying to coin.

## ✅ Action Items & Next Time

- **Optional homework (all):** "Protocol watch" — find a protocol in your work, home, or on the street and post a short paragraph of observation before the next session (~2 weeks).
- **Recommended reading (all):** Matthew McDowell-Sweet's product-vs-protocol post.
- **Consider a case study:** Anyone interested should tell Rafa for extra support; case studies can be individual or squad-based.
- Members are encouraged to voice reading preferences (informal, collaborative; Rafa has final say).
- **Ben** plans to write up / build a slideshow and documents on his distributed-AI / scalable-judgment ideas for the Protocol Institute.
- **Next session (~2 weeks):** Navid on agentic SEO / agent readiness. Theme focus continuing on agents and governance.

## ⭐ Memorable Quotes

- **Dylan Fitzgerald:** "This is eighteen months ago in academia, and it is happening to us right now."
- **Mike Casey:** "With these agents, they're ephemeral, and there can be infinity of them. And so how do you actually enforce against a specific agent?"
- **Rafa:** "Success looks like we're all protocol [pilled] and all we see is protocols everywhere."
