# Agent lifecycle: what can be registered, identified and traced

Desk research, fetched 2026-10-11. Sources stored in corpus/b-raw/platforms/E/<id>.txt (first line URL, second line FETCHED). Quotes are verbatim (whitespace-normalised) and at most 40 words. Section 5 EU AI Act text is from the European Commission AI Act Service Desk; the Official Journal copy on EUR-Lex was blocked.

## 1. Agent definition versus runtime instance

Every platform separates a reusable definition (configuration, file, template) from a run (session, thread, task). The definition is a named object; the run is created by an invocation and ends by timeout, completion or stop. Run identifiers are mostly chosen or returned at run time.

- Claude subagents are defined as files or in code (a definition), and run in their own context.
  > "Each subagent runs in its own context window with a custom system prompt, specific tool access, and independent permissions." [claude-subagents]

- Claude Agent SDK: definitions are passed in code at query time or kept as files.
  > "Programmatically: use the agents parameter in your query() options. See the TypeScript and Python references Filesystem-based: define agents as markdown files in .claude/agents/ directories." [claude-sdk-subagents]

- Subagents can run concurrently and can create further subagents; depth and concurrency are capped by settings.
  > "Subagents can also spawn subagents of their own. To limit how deep that nesting goes, how many subagents run at once, and how much a query spends, see Cap subagent depth, concurrency, and spend." [claude-sdk-subagents]

- Default caps: 3 layers of nesting and 20 concurrent subagents.
  > "ConcurrencyCLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS20 subagents running at once" [claude-sdk-subagents]

- Each subagent run carries an identifier that can be captured; messages from inside a subagent carry the parent tool call id.
  > "Messages from within a subagent’s context include a parent_tool_use_id field. In TypeScript, each assistant and user message a subagent produces also carries agent_id" [claude-sdk-subagents]

- Subagent transcripts are stored separately and persist independently of the main conversation.
  > "Subagent transcripts are stored in separate files and persist independently of the main conversation." [claude-sdk-subagents]

- Claude Code exposes SubagentStart and SubagentStop hook events, so start and end can be logged.
  > "SubagentStartAgent type nameWhen a subagent begins execution SubagentStopAgent type nameWhen a subagent completes" [claude-subagents]

- OpenAI Agents SDK: an agent is a configured object; a handoff delegates to another agent and is exposed to the model as a tool.
  > "An agent is a large language model (LLM) configured with instructions, tools, and optional runtime behavior such as handoffs, guardrails, and structured outputs." [oai-agents]

- OpenAI handoffs are represented as tools.
  > "Handoffs are represented as tools to the LLM. So if there's a handoff to an agent named Refund Agent, the tool would be named transfer_to_refund_agent." [oai-handoffs]

- OpenAI: instructions can come from a callback evaluated at run time, so the effective definition can differ per run.
  > "System prompt or dynamic instructions callback." [oai-agents]

- Foundry Agent Service: an agent is a configuration; threads and runs are the conversation and execution records.
  > "An agent is a configurable orchestration component that uses AI models with instructions, tools, parameters, and optional safety and governance controls. At run time, an agent uses these components and a given thread's message history to respond to user inputs." [foundry-concepts]

- Foundry threads persist until deleted; the run is the invocation of an agent on a thread.
  > "Threads persist until explicitly deleted. In the Standard agent setup, threads are stored in your Azure Cosmos DB account." [foundry-concepts]

- Foundry offers three agent types: prompt agents (configuration only), voice-based prompt agents, and hosted agents (own code in a container).
  > "Hosted agents are code-based agents you build with Agent Framework, LangGraph, the OpenAI Agents SDK, the Anthropic Agent SDK, the GitHub Copilot SDK, or your own code" [foundry-agents]

- AgentCore Runtime: each session gets its own microVM, which is terminated when the session ends.
  > "Each session in AgentCore Runtime receives its own dedicated microVM with isolated compute, memory, and filesystem resources." [agentcore-sessions]

- AgentCore: session lifetime is hours to days; compute is ephemeral by default.
  > "Sessions last up to 8 hours for each lifecycle on microVMs, or up to 14 days on Instances." [agentcore-sessions]

- AgentCore: a session starts on the first invoke with an ID supplied by the customer's application.
  > "A new session is created on the first invoke with a unique runtimeSessionId provided by your application." [agentcore-sessions]

- AgentCore does not map sessions to users; the customer must keep that mapping.
  > "AgentCore does not enforce session-to-user mappings - your client backend should maintain the relationship between users and their session IDs." [agentcore-sessions]

- AgentCore quotas: active session workloads and session creation rate per account.
  > "Active session workloads per account 5,000 in US East (N. Virginia) and US West (Oregon), and 2,500 in other AWS Regions." [agentcore-quotas]

- AgentCore session creation rate quota.
  > "New Runtime session creation rate 25 TPS" [agentcore-quotas]

- AgentCore session defaults: idle timeout 15 minutes, maximum duration 8 hours.
  > "Idle session timeout 15 minutes of inactivity" [agentcore-quotas]

- Google ADK: a Session is one conversation thread with an id, an app name and a user id.
  > "A Session represents a single conversation thread between a user and your agent" [adk-sessions]

- Google: Agent Registry gives an agent a globally unique, immutable identifier that stays constant when code or infrastructure changes.
  > "A globally unique, immutable Uniform Resource Name (URN) for an agent. This identifier provides a stable reference for consumers to look up and invoke the agent, remaining constant regardless of underlying infrastructure changes or code updates." [gcp-agent-registry]

- LangGraph: a node can have several outgoing edges whose destinations run in parallel; routing can be dynamic.
  > "If a node has multiple outgoing edges, all of those destination nodes will be executed in parallel as a part of the next superstep." [lg-overview]

- LangGraph orchestrator-worker: workers are chosen when subtasks cannot be predefined.
  > "Orchestrator-worker workflows provide more flexibility and are often used when subtasks cannot be predefined" [lg-workflows]

- LangGraph runs are tied to a thread_id and checkpoints.
  > "When you compile with a checkpointer, LangGraph saves checkpoints at super-step boundaries" [lg-overview]

## 2. Identity for agents

Identity is documented at three levels: a template or blueprint, an identity created from it, and a token that shows who acts for whom. Only Entra documents the template-to-identity-to-sponsor chain in agent terms.

- Entra Agent ID: agents are often created dynamically and can last minutes; identities are designed for that.
  > "An agent might exist for minutes during a specific task, or might be created and destroyed thousands of times per day" [entra-agentid]

- Entra: agent identities can be created in bulk and retired without leaving orphaned credentials.
  > "Organizations can create agent identities in bulk, apply consistent policies to all agents, and retire agents without leaving orphaned credentials" [entra-agentid]

- Entra: a blueprint is the template for agent identities, holding credentials and policies.
  > "An agent identity blueprint is an object in Microsoft Entra ID that serves as the template and authentication foundation for one or more agent identities." [entra-concepts]

- Entra: an agent identity is a special service principal created by a blueprint, without credentials of its own.
  > "An agent identity is a special service principal in Microsoft Entra ID. It represents an identity that the agent identity blueprint created and is authorized to impersonate. It doesn't have credentials on its own." [entra-agent-identities]

- Entra: a blueprint governs a class of agent identities and is used for lifecycle operations.
  > "A Microsoft Entra ID object that governs a class of agent identities and is used for lifecycle operations." [foundry-identity]

- Entra: at least one human sponsor is required for each agent identity and blueprint.
  > "At least one sponsor is required for each agent identity and agent identity blueprint." [entra-sponsor]

- Entra: owners are technical administrators; sponsors hold business accountability.
  > "Owners serve as technical administrators for agents, handling operational and configuration aspects. Sponsors provide business accountability for agents, making lifecycle decisions without technical administrative access." [entra-concepts]

- Entra: Copilot Studio agents each get an agent identity; the creator is recorded as sponsor.
  > "Each time an AI agent is created, the agent gets an agent identity in the Microsoft Entra tenant. The user who created the agent is recorded as its sponsor." [entra-agentid]

- Entra: delegated tokens name the user as subject and the agent identity as actor.
  > "The subject of the token is a user, while the actor is the agent identity." [entra-agent-identities]

- Entra: audit logs and sign-in reports show the agent identity as the acting client.
  > "Agent service principals maintain distinct identities in audit logs and sign-in reports." [entra-agent-id-faq]

- Foundry provisions a default blueprint and identity per project; unpublished agents share one identity.
  > "All unpublished or in-development agents within the same project share a common identity." [foundry-identity]

- RFC 8693: the act claim identifies the party to whom authority has been delegated.
  > "The "act" (actor) claim provides a means within a JWT to express that delegation has occurred and identify the acting party to whom authority has been delegated." [rfc8693]

- RFC 8693: delegation and impersonation are distinct; under impersonation the recipient only sees the impersonated party.
  > "For all intents and purposes, when A is impersonating B, A is B within the context of the rights authorized by the token." [rfc8693]

- MCP authorization: servers must check that a token was issued for them; a token carries the client and user context, not an agent definition.
  > "MCP servers MUST validate that access tokens were issued specifically for them as the intended audience, according to RFC 8707 Section 2." [mcp-authz-latest]

- MCP: clients obtain a client ID via metadata documents, pre-registration or dynamic registration.
  > "MCP clients MUST obtain a client ID through one of three registration mechanisms" [mcp-authz-latest]

- MCP: token passthrough is forbidden.
  > "Token passthrough is explicitly forbidden" [mcp-security]

- SPIFFE: a SPIFFE ID identifies a workload, which may be as fine-grained as a process.
  > "A SPIFFE ID is a string that uniquely and specifically identifies a workload." [spiffe-concepts]

- SPIFFE: a workload may be a single process or span many nodes.
  > "a workload may often be more fine-grained than a physical or virtual node – often as fine grained as individual processes" [spiffe-concepts]

- Google: an agent principal can be a SPIFFE ID bound to the compute runtime.
  > "such as a SPIFFE ID, bound directly to the compute runtime of the agent." [gcp-agent-registry]

- AgentCore Identity: agent identities are implemented as workload identities.
  > "Agent identities are implemented as workload identities with specialized attributes that enable agent-specific capabilities while helping to maintain compatibility with industry-standard workload identity patterns." [agentcore-identity]

## 3. Tracing and provenance

Trace data records runs, not definitions. OpenTelemetry has agent-specific spans, but they are marked Development status and most attributes are conditional.

- OpenTelemetry GenAI: spans for create_agent, invoke_agent, execute_tool, invoke_workflow exist; status is Development.
  > "**Status**: [Development]" [otel-agent-spans]

- OTel: a create_agent span records the agent being created, with id, name, version.
  > "The `gen_ai.operation.name` SHOULD be `create_agent`." [otel-agent-spans]

- OTel: gen_ai.agent.id is the stable identifier of the agent.
  > "The stable unique identifier of the GenAI agent created during this operation." [otel-agent-spans]

- OTel: for hosted agents the id should be the provider's resource identifier.
  > "For hosted agents, this SHOULD be the provider-assigned stable identifier of the agent resource" [otel-agent-spans]

- OTel: invoke_agent spans are named per agent and can carry a conversation id.
  > "The `gen_ai.operation.name` SHOULD be `invoke_agent`." [otel-agent-spans]

- OTel: the conversation id groups a session or thread.
  > "The unique identifier for a conversation (session, thread), used to store and correlate messages within this conversation." [otel-agent-spans]

- OpenAI tracing: a trace is one workflow run; spans carry parent ids; a group id links traces of one conversation.
  > "Traces represent a single end-to-end operation of a "workflow". They're composed of Spans." [oai-tracing]

- OpenAI tracing: each agent run is wrapped in an agent span; handoffs in a handoff span.
  > "Each time an agent runs, it is wrapped in agent_span() LLM generations are wrapped in generation_span() Function tool calls are each wrapped in function_span() Guardrails are wrapped in guardrail_span() Handoffs are wrapped in handoff_span()" [oai-tracing]

- OpenAI tracing is unavailable under Zero Data Retention.
  > "Tracing is unavailable for organizations that use OpenAI's APIs under a Zero Data Retention (ZDR) policy." [oai-tracing]

- OpenAI tracing can be disabled per run or globally.
  > "You can disable tracing for a single run by setting agents.run.RunConfig.tracing_disabled to True" [oai-tracing]

- AgentCore Observability: telemetry is OpenTelemetry-compatible and stored in CloudWatch.
  > "AgentCore emits telemetry data in standardized OpenTelemetry (OTEL" [agentcore-obs]

- AgentCore: a trace belongs to a session and may include calls to other agents.
  > "A trace represents a detailed record of a single request-response cycle beginning from with an agent invocation and may include additional calls to other agents." [agentcore-obs-concepts]

- AgentCore: agent code must be instrumented to gather trace data.
  > "To gather trace data, you need to instrument your agent code using the AWS Distro for Open Telemetry (ADOT)." [agentcore-obs-concepts]

- Foundry tracing: traces go to Application Insights; message content recording is off unless enabled.
  > "To trace the content of chat messages, set the AZURE_TRACING_GEN_AI_CONTENT_RECORDING_ENABLED environment variable to true" [foundry-trace]

- Foundry: multi-agent semantic conventions built on OpenTelemetry and W3C Trace Context.
  > "establish standardized practices for tracing and telemetry within multi-agent systems." [foundry-trace]

- A2A: an Agent Card is a JSON document describing identity, capabilities, skills, endpoint and authentication.
  > "Agent Card: A JSON metadata document published by an A2A Server, describing its identity, capabilities, skills, service endpoint, and authentication requirements." [a2a-spec]

- A2A: cards are served at a well-known URI.
  > "The standard path is https://{agent-server-domain}/.well-known/agent-card.json" [a2a-agentcard]

- A2A: cards may be signed with JWS.
  > "Agent Cards MAY be digitally signed using JSON Web Signature (JWS)" [a2a-spec]

- A2A: no standard registry API.
  > "The current A2A specification does not prescribe a standard API for curated registries." [a2a-agentcard]

- A2A: a contextId groups related tasks and messages; tasks end in terminal states.
  > "A contextId is an identifier that logically groups multiple related Task and Message objects" [a2a-spec]

- A2A: messages to a task in a terminal state are rejected.
  > "Messages sent to Tasks that are in a terminal state (TASK_STATE_COMPLETED, TASK_STATE_FAILED, TASK_STATE_CANCELED, TASK_STATE_REJECTED) cannot accept further messages." [a2a-spec]

## 4. Lifecycles, counts and retirement

Documented lifetimes are in hours to days for platform sessions and minutes for some agents. Retirement is documented for identities (Entra) and registry records, not for individual runs.

- AgentCore: a stopped session can be resumed with new compute; the session ID stays valid until the runtime is deleted.
  > "The session itself remains valid until the AgentCore Runtime ARN is deleted." [agentcore-sessions]

- AgentCore: stop reasons include inactivity, maximum lifetime, explicit stop, or failed health check.
  > "This can occur due to inactivity (default 15 minutes), reaching max compute lifetime (default 8 hours), an explicit stop by invoking the StopRuntimeSession API, or if the compute is deemed unhealthy based on health checks." [agentcore-sessions]

- AgentCore: memory and filesystem state vanish with compute unless persistence is configured.
  > "Any data stored in memory or written to disk persists only for the compute lifecycle." [agentcore-sessions]

- Foundry: threads are kept until the customer deletes them; retention is the customer's plan.
  > "Plan your thread retention strategy based on:" [foundry-concepts]

- Entra: sponsors decide on retention through access reviews; access packages expire.
  > "accountable for the agent's purpose and lifecycle decisions, including access reviews and agent retention" [entra-sponsor]

- Entra: sponsors and owners can disable and delete agent identities.
  > "Delete or disable the agent identity and modify its sponsors" [entra-sponsor]

- Entra governance: expiring access packages notify the sponsor.
  > "as the expiry date approaches, the sponsor receives notifications about the pending expiration." [entra-govern]

- AWS Agent Registry: records are published, approved and later deprecated.
  > "They also deprecate records no longer in use." [agentcore-registry]

- Workday: lifecycle from registration to retirement is marketed for agents.
  > "Manage your agents’ entire lifecycle—from registration to retirement" [workday-asor]

- Workday: stated aim of one hub for all agents.
  > "Manage and measure the impact of all your AI agents from one hub to mitigate agent sprawl." [workday-asor]

- Microsoft Agent 365: a single registry of agents in the organization.
  > "Admins can now view all their agents in a single, centralized registry" [ms-copilot-agent365]

- Google Agent Registry: registry covers agents, MCP servers, endpoints and skills; discovery differs from infrastructure discovery.
  > "categorizes agentic components into four primary types: agents, MCP servers, endpoints, and skills." [gcp-agent-registry]

- Claude Code: concurrent subagent cap blocks further creation until the count drops.
  > "Refuses to spawn another subagent, returning Concurrent subagent limit reached" [claude-sdk-subagents]

- Claude SDK: subagent transcripts are cleaned up on a retention period.
  > "See resume subagents in Claude Code for compaction behavior and the cleanupPeriodDays cleanup period." [claude-sdk-subagents]

## 5. Regulation: what unit must be registered

The regulatory unit is the AI system (EU AI Act, NIST), the algorithm (PRA SS5/18) or the automated decision-making technology (Colorado). No retrieved text uses the agent as the unit to register.

- EU AI Act Art 49(1): providers register themselves and their high-risk system (Annex III) before placing on the market.
  > "the provider or, where applicable, the authorised representative shall register themselves and their system in the EU database referred to in Article 71." [euai-sd-art49]

- Art 49(2): providers register Annex III systems they judge not high-risk.
  > "that provider or, where applicable, the authorised representative shall register themselves and that system in the EU database referred to in Article 71." [euai-sd-art49]

- Art 49(3): public-authority deployers register themselves and their use of the system.
  > "deployers that are public authorities, Union institutions, bodies, offices or agencies or persons acting on their behalf shall register themselves, select the system and register its use in the EU database referred to in Article 71." [euai-sd-art49]

- Art 71: the Commission maintains the EU database; providers enter Sections A and B.
  > "The data listed in Sections A and B of Annex VIII shall be entered into the EU database by the provider or, where applicable, by the authorised representative." [euai-sd-art71]

- Annex VIII: the registered record is one system entry with trade name and a traceability reference, intended purpose, status.
  > "The AI system trade name and any additional unambiguous reference allowing the identification and traceability of the AI system;" [euai-sd-annex8]

- AI Act definition: the unit is an AI system, defined by function, not by instance.
  > "means a machine-based system that is designed to operate with varying levels of autonomy and that may exhibit adaptiveness after deployment" [euai-sd-art3]

- Art 12: high-risk systems must allow automatic recording of events over their lifetime.
  > "High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system." [euai-sd-art12]

- Art 26(6): deployers keep the logs under their control for at least six months.
  > "shall keep the logs automatically generated by that high-risk AI system to the extent such logs are under their control, for a period appropriate to the intended purpose of the high-risk AI system, of at least six months" [euai-sd-art26]

- NIST AI RMF GOVERN 1.6: mechanisms to inventory AI systems.
  > "GOVERN 1.6: Mechanisms are in place to inventory AI systems" [nist-rmf]

- NIST AI RMF GOVERN 1.7: decommissioning and phasing out AI systems.
  > "GOVERN 1.7: Processes and procedures are in place for decom- missioning and phasing out AI systems safely" [nist-rmf]

- PRA SS5/18: the inventory unit is the algorithm, with named ownership.
  > "assigning ownership for the inventory of algorithms and risk controls;" [pra-ss518]

- PRA SS5/18: a single, comprehensive inventory of algorithms.
  > "a single and comprehensive inventory of algorithms;" [pra-ss518]

- Colorado SB26-189: unit is automated decision-making technology used in consequential decisions; records kept 3 years; no register.
  > "Both developers and deployers are required to retain records necessary to demonstrate compliance with the act for at least 3 years." [colo-sb26189]

- Colorado SB26-189 repeals and replaces SB24-205.
  > "The act repeals and reenacts those provisions with new requirements regarding the use of automated decision-making technology in consequential decisions." [colo-sb26189]

- FINRA 2026 report: agents are a named emerging trend; firms may consider how to track agent actions and decisions.
  > "how to track agent actions and decisions; or" [finra-genai-2026]

- FINRA: auditability risk for multi-step agent tasks.
  > "Complicated, multi-step agent reasoning tasks can make outcomes difficult to trace or explain, complicating auditability." [finra-genai-2026]

## Synthesis

### The units, and which are registrable or traceable

- Platform. The service that hosts and runs agents (AgentCore Runtime, Foundry Agent Service, Claude Code or the Agent SDK in a customer process, Vertex/Gemini Enterprise Agent Platform). Persistent. Inventoriable by the firm as a contracted service and by cloud account/project.
- Definition or template. A configured agent: instructions, tools, model, handoff targets. Persistent when stored (a markdown file in .claude/agents/, a Foundry prompt or hosted agent, an AgentCore runtime ARN, an OpenAI Agent object in code). Registrable. Registries exist for this level: AWS Agent Registry, Google Agent Registry (immutable URN per agent), Microsoft Agent 365 registry. Gap: definitions created in code at run time (OpenAI dynamic instructions, SDK-supplied subagent definitions, LangGraph orchestrator-worker) have no stored object unless the firm's code writes one.
- Identity. Entra Agent ID has a blueprint (template/class, with owners and at least one sponsor) and agent identities created from it. Google and AWS describe agent principals as service accounts or workload identities (SPIFFE ID named by Google). Persistent until disabled or deleted. This is the level where a per-agent record is documented to exist with an accountable human.
- Permission or scope. Roles, scopes and access packages attach to the identity or blueprint, not to the run. Delegated tokens carry the user as subject and the agent as actor (Entra; RFC 8693 act claim). Persistent as assignments; the token itself is short-lived.
- Run or session. Created on invocation. Hours (AgentCore default 8 hours, up to 14 days on Instances), minutes for some agents (Entra), subagent runs inside one query (Claude, default cap 20 at once, 3 deep). Identifiers are chosen by the customer (AgentCore runtimeSessionId), returned by the platform (Claude agentId, Foundry run id) or generated by a framework (OpenAI trace_id). Ephemeral by design; the record that survives is the transcript, thread or trace.
- Trace. The durable evidence of a run. OpenTelemetry GenAI defines create_agent, invoke_agent and execute_tool spans with gen_ai.agent.id, name, version and conversation id. OpenAI, AgentCore and Foundry produce their own or OTel-compatible traces. Persistence depends on the firm's configuration (retention, content recording off by default in Foundry, unavailable under OpenAI Zero Data Retention).

### What is ephemeral and what persists

- Ephemeral: microVM and memory of a session, subagent context, token, tool-call connection. Trace and log records persist only if exported and retained.
- Persistent if the customer keeps it: definitions, identities and blueprints, threads (Foundry until deleted), subagent transcripts (Claude, subject to a cleanup period), registry records, traces in the firm's store.
- Counts: vendors publish quotas, not counts. AgentCore: 5,000 active session workloads per account in two regions, creation rate 25 per second. Claude: 20 concurrent subagents by default. The documented design intent in Entra is that agents may be created and destroyed thousands of times per day, so a run-level register would be a log, not an inventory.

### What a firm can realistically inventory and trace today

- Inventory: platforms in use; agent definitions per platform (via the platform registry or the firm's own code repository); blueprints and agent identities with named sponsor and owner; permissions per identity; MCP servers and tools each agent can reach (the registries cover MCP servers, endpoints and skills).
- Trace: which run used which definition (agent id, name, version in the span), under which session or conversation id, calling which tools, and with which parent run (parent_tool_use_id in Claude, parent span in OpenAI, trace context in OTel). For delegation: who it acted for, where the identity provider issues act or actor-style tokens (Entra) and where the firm links session ids to users itself (AgentCore does not).
- Retire: disable or delete the identity and blueprint (Entra), deprecate the registry record (AWS), delete threads (Foundry). Retiring a definition is not the same as ending runs already in flight.

### Gaps

- No cross-vendor standard for a definition register. A2A says it does not prescribe a registry API; the registries are vendor-specific.
- OpenTelemetry agent spans are Development status; attribute requirements are mostly conditional ("If applicable"), so lineage depends on instrumentation.
- "Created from what, by whom": documented as a chain only in Entra (blueprint creates identity; creator recorded as sponsor for Copilot Studio agents). For subagents created by a parent agent in code, the documented link is the parent tool call or span, not an identity or a registered definition.
- Session-to-user mapping is left to the customer on AgentCore; MCP authorization specifies client ID and token audience, and the retrieved text defines no agent-definition or agent-id field in the token.
- Third-party and shadow agents: registries list what is published to them; the Google text itself contrasts the registry with infrastructure discovery of unregistered compute.
- Regulation: the EU database is for providers' high-risk (and some non-high-risk Annex III) systems and for public-authority deployers; it records a system, not an agent run. Private-sector deployers have no registration duty in the retrieved text, but high-risk systems need automatic logs (Art 12) that deployers keep at least six months (Art 26(6)). NIST and PRA ask for inventories and ownership (AI systems; algorithms). Colorado SB26-189 requires records for three years, not a register. FINRA names agents and asks firms to consider how to track agent actions.

### Implication for the recommendation

"Keep a register of agents" is accurate only if "agent" means a registered definition with an identity and an accountable sponsor. A register of runs is not a practical or documented control. The documented controls are: an inventory of platforms and definitions, identities with named human sponsors and scoped permissions, a link from each run to its definition, identity and principal, and retained traces.
