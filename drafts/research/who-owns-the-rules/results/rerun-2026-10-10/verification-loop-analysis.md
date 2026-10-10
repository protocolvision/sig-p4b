Phase 2 verification of the loop analysis (analysis.md, exploratory-analysis.md): 127 claims, 122 confirmed, 4 corrected, 1 not found, 0 unverifiable.
1. Method: reran loop-tools/analyze.py on results/loop-2026-10-10; output is byte-identical to analysis.md. Kappa, agreement and disagreements also recounted independently from the coder files (298 records, 0.98, 0.95).
2. All 106 analysis.md claims (agreement, stability, per-code tables, verdicts, 14 cluster rows) and all exploratory tables (secondary-code counts, stratum-by-cluster) recompute exactly.
3. Corrected: exploratory line 13 quotes R1848 as "reviewing AI conversations weekly..."; the Vanta posting (C85ecc82f) says "Review Fin conversations weekly...". The ledger quote carries the same alteration.
4. Corrected: exploratory line 14 says both coders noted R9984 is not a cross-functional rule trade-off; only coder B did (coder A: "tools, not rules"). Source posting is Zip GTM Engineer (C64bee26b).
5. Corrected: analysis.md C12 role title "AI risk officer" is not attested (corpus has "Head of AI Governance"); C2 titles "HR service representative" and "help desk agent" are not attested verbatim.
6. Not found: analysis.md C9 role "Senior Manager, Accounting Operations" is absent from the acquired Built In SF listing (Cfecea488); it came from a search summary.
7. Confirmed from corpus: AI steward as a ServiceNow role (AI Control Tower guide, Cf7d364f5); R8231 Replit postmortem (C05737488).
8. Caveat on method, not a number: analyze.py applies only the final-iteration share; loop-design.md s7 also requires 60% in 3 of 5 iterations. PE (46%) fails either way, so verdicts hold.
9. Role/cluster descriptions are model-written labels; checked against iter-5.json and corpus titles, not as independent facts about companies.
10. Detail per claim: verification-loop-analysis.csv. Round-one files untouched; nothing committed.
