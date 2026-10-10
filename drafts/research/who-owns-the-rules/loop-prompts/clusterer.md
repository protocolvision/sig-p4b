# Clusterer prompt (filled per iteration: {K}, {POOL_PATH}, {OUTPUT_PATH})

You are an analyst. You have a pool of records, each describing a work activity that is changing as AI
agents and automation take on operational work in companies. Your task: find which activities bundle
together under one accountability, and infer what roles those bundles support.

Rules:
1. Read only `{POOL_PATH}`. Do not open any other file in this repository and do not search the web. Work
   from the records alone.
2. Group records into clusters using evidence of bundling, in this order of weight: the same `doc` (they
   appear together in one posting or framework); the same performer; the same decision or trade-off; the
   same knowledge; the same functions connected. Similar wording alone is weak evidence.
3. Every record gets exactly one cluster, or the label "unclustered" if no evidence ties it to others.
   Aim for 6 to 15 clusters; justify a number outside that range.
4. Name each cluster with a plain description of the work, not a job title.
5. For each cluster, infer: the role or roles that would hold it; whether that role exists today under a
   stable title (name it) or not; the likely seniority at which it would first be hired; whether the bundle
   looks lasting or transitional, and why; your confidence (low, medium, high).
6. Then answer: which clusters are most likely to become distinct roles by 2030, which will be absorbed into
   existing roles, and which will be automated away. Give reasons tied to record IDs.
7. Don't use these words unless they appear in a record: protocol, protocol vision, protocol engineering,
   BPM.

Write JSON to `{OUTPUT_PATH}`:
{"iteration": {K}, "clusters": [{"cluster_id": "C1", "description": "...", "record_ids": [...],
"bundling_evidence": "...", "roles": [{"role": "...", "exists_today": true, "existing_title": "...",
"seniority_at_first_hire": "...", "lasting_or_transitional": "...", "reason": "..."}], "confidence": "..."}],
"unclustered": [...], "outlook": {"distinct_roles_by_2030": [...], "absorbed": [...], "automated": [...],
"reasons": "..."}}

Validate that every record ID in the pool appears exactly once. Reply with a ten-line summary.
