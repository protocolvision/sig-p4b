# I5c: first dated community and tooling events (collected 2026-10-10)

## Method
- Rule (triangulation-design.md, Amendment A.2, point 7): date of each type = third-earliest record of that type. Inclusion: communities 3+ past events and 50+ members; tooling OSI licence, 1,000+ stars, README about building, running, monitoring or governing AI agents. Exclusions: academic multi-agent, games, trading/crypto bots.
- Tooling: GitHub API repos/{owner}/{repo} created_at (opened), plus GitHub search by function (guardrails, observability, authorization, governance policy). Candidates were chosen by function, then README checked for the word agent.
- Conferences: tech-conferences/conference-data JSON, 2023 to 2027, filtered on agent/agentic names. Dates are listing startDate; first edition and Internet Archive capture NOT confirmed.
- Communities: Meetup pages opened by WebFetch. Meetup pages as fetched do not show a founded date.
- Deviations: the section 4.2 filing phrases were not read (out of scope), so search terms were by function. The CSV uses the caller's columns, not the record_id/record_type/event_date schema of A.2; rename before pipeline use. I5-search-log.csv not written.

## Dates by the A.2 rule
- Open tooling, agent-README reading (Phoenix 2022-11-09, Langfuse 2023-05-18, AgentOps 2023-08-15): third-earliest = **2023-08-15**.
- Open tooling, lenient reading (LLM-app guardrails/observability: Phoenix, Guardrails AI 2023-01-29, Helicone 2023-01-31): third-earliest = **2023-01-31**. The choice of reading moves the date by about 6.5 months.
- Conferences (agent-named, confs.tech): third-earliest = **2025-12-11** (AgentCon Vancouver), preceded by 2025-05-16 and 2025-12-02. All are builder-oriented; none is clearly about running agents inside companies.
- Community (Meetup): **no date obtained**. Third-earliest cannot be computed.

## Gaps
- Meetup founded dates could not be read from the pages. Search-result snippets gave 2023-04-30 (Agentic Workflows group, whose URL returned not-found), 2024-11-26, 2025-07-11, 2026-04-12 (private NYC group, URL not-found); these are unverified and not used.
- confs.tech holds only listed events; older or lapsed conferences are likely missing, so conference dates may be late.
- GitHub licence field shows NOASSERTION for Phoenix, Langfuse, NeMo; OSI status not checked. Star counts are as of collection, not at inclusion.
- Search did not enumerate exhaustively; earlier qualifying repositories may exist. Policy/authorization frameworks aimed at agents appear only from 2026 in what I found.
- N13 community date input is therefore missing; N03 order cannot be settled on community vs tooling.
