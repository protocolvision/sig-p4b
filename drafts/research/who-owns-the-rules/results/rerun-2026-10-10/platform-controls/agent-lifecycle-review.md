# Agent lifecycle: fact-check

Checked 2026-10-11 against corpus/b-raw/platforms/E (all fetched 2026-10-11).

## Most claims hold; Claude agentId, AgentCore "max 8 hours", PRA scope and "human sponsor" need rewording

1. **Definition vs run: holds with caveat.** True for every platform in the corpus. Say "every platform we examined". Caveats: some definitions exist only in code at run time (OpenAI instructions callback; Claude `agents` in `query()` or `--agents`), so there may be nothing stored to list. And an AgentCore session "remains valid until the AgentCore Runtime ARN is deleted".

2. **AgentCore: partly overstated.** The microVM per session is verbatim, as is "After session completion, the entire microVM is terminated". But 8 hours is the default *compute* lifetime, adjustable via `maxLifetime`. A stopped session resumes on new compute "up to another 8 hours", and Instances run "up to 14 days", so "max 8 hours" per session is wrong. The 15-minute idle timeout is an adjustable default. The 5,000 figure covers US East (N. Virginia) and US West (Oregon), with 2,500 elsewhere. Both quotas are adjustable.

3. **Claude subagents: agentId overstated.** The 20-concurrent and 3-layer defaults are verbatim but version-dependent ("Claude Code v2.1.219 or later"). They also have an exception ("Sessions with ultracode active are never refused"). An agentId comes back only "When a subagent completes", and "built-in Explore and Plan agents … don't return an agentId". Say "most subagent runs return an ID".

4. **Entra Agent ID: holds with caveat.** Blueprints create identities: "the agent identity blueprint created". Sponsors are required: "At least one sponsor is required…". But sponsors can be "Users (including guest users) and groups", so write "a named person or group", not "a human". "Minutes" and "thousands of times per day" are design rationale ("An agent *might*…"), not measured counts. User-as-subject, agent-as-actor applies only to the user-delegated flow. In the agent's own flow, "The subject of the access token is the agent identity."

5. **Registries: holds with caveat; Agent 365 rests on a product overview.** AWS Agent Registry is a "discovery service" for *published* records behind an approval workflow, not an automatic inventory. Google "differs from infrastructure discovery", which finds "unregistered compute". The Agent 365 source is a marketing-register overview that also claims "activity, and agent health", so "not runs" is too strong for it. The draft also cites Workday, which is a marketing page; workday-pr.txt is a 187-byte failed fetch. The A2A quote is from a topics page, not the normative spec.

6. **OpenTelemetry: holds.** All four agent operations are Development status. `gen_ai.agent.id` is "Conditionally Required. If applicable", and for hosted agents should be the provider's resource ID (an ARN or a GCP registry ID). It identifies the definition, not the run. The source is the GitHub `main` branch, so cite it with the fetch date.

7. **Regulation: holds, except PRA (misapplied) and Colorado (summary only).**
   - EU AI Act Arts 49(1)–(3) and 71 are verbatim. The database covers Annex III systems only. Art 12 is a design duty ("shall technically allow"). Art 26(6) is qualified: logs are kept only "to the extent such logs are under their control", "unless provided otherwise", and financial institutions keep them inside financial-services documentation. The source is the Commission Service Desk text "as at 27 July 2026" with Digital Omnibus amendments, not the Official Journal. No application dates are in the corpus, so don't imply the duties apply now.
   - NIST AI RMF GOVERN 1.6 holds. The framework is "voluntary", and inventories are "resourced according to organizational risk priorities".
   - **PRA SS5/18 is "Algorithmic trading", June 2018.** Its "single and comprehensive inventory of algorithms" covers trading algorithms only. State that scope or drop it.
   - **Colorado SB26-189.** The stored file is the legislature's bill summary, not the statute. Signed 2026-05-14. The unit is a "covered ADMT" used in consequential decisions. Duties start January 1, 2027, and records are kept 3 years. "No register" only means the summary mentions none.
   - FINRA: the 2026 report is dated **9 December 2025**. Its line "Considerations may include: … how to track agent actions and decisions" is accurate and non-binding.

## "Agent" means three things across these sources

Vendors and OpenTelemetry use "agent" for a definition: an ARN, a URN, or `gen_ai.agent.id`. Entra uses it for an identity made from a blueprint, one of many "agent instances", possibly short-lived. Regulators register an "AI system" (EU, NIST), an "algorithm" (PRA) or a "covered ADMT" (Colorado), never an agent. Keep the draft's closing caveat.

## Proposed recommendation

> Keep one list of every AI system and agent design the firm uses, bought or built. For each, name an accountable owner, the systems and data it may access, and whose authority it acts on. Make sure every action an agent takes is recorded and can be traced to an entry on that list and to the person or team it acted for. Keep those records as long as regulators require: at least six months for EU high-risk uses. Individual agent runs come and go too quickly to list. List the designs, and keep the records of what they did.

Confidence: **medium-high**. Vendors, NIST, the EU AI Act and FINRA all support an inventory with owners and traceability. Retention periods vary by regime. The weak links are tracing a run back to its design, which depends on Development-status instrumentation, and agents created on the fly in code, which leave no stored design unless the firm requires one.
