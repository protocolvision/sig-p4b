# Coder prompt (two coders, {CODER} = A or B)

You are coding work-activity records against fixed definitions. Read only `{POOL_PATH}` and do not open
any other file in this repository or search the web.

For each record, assign one primary code and optionally one secondary code:

- PV: Finding the rules, written or unwritten, that actually govern how work is done: observing
  workarounds, exceptions, overrides, escalations, or where automated agents stall, loop or improvise, in
  order to infer the rule; telling binding rules from leftovers; mapping rules across functions.
- PE: Designing, encoding, changing or testing the rules that constrain what people and agents may do in
  systems: permissions, spending and approval limits, data-access rules, approval gates, interfaces between
  teams, partners or agents, policy as code, procedures for changing these rules, testing rules against
  circumvention.
- RD: Deciding whether a rule should change by weighing a trade-off across functions (revenue against risk,
  speed against control), and owning that decision or its measure.
- AO: Building, configuring, prompting, supervising, evaluating or fixing AI agents and their outputs, where
  the activity is about the agent rather than the rules it acts under.
- OT: Anything else.

Code what the record says, not what the activity might involve. When unsure between a code and OT, choose
OT. Write JSON Lines to `{OUTPUT_PATH}`: {"id": "...", "primary": "PV|PE|RD|AO|OT", "secondary":
"PV|PE|RD|AO|OT|", "note": "under 20 words"}. Every record exactly once. Reply with counts per primary code.
