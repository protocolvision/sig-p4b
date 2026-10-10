# Pattern-matching power check, v3 (two-stage test)

Addendum A.3, triangulation-design.md. Noise q = 0.2 per coder, two coders, 2000 runs per condition, seed 20261011; percentile null 20000 presents, seed 20261012. Same 15 features, NF randomisation, noise, blends and null as A.2.

## Stage 1: families

Rule: two patterns are linked when their ideal distance (mean |difference| over the common features both grade) is at most half the median of the 21 pairwise distances; families are the connected components. Median 0.429, threshold 0.214.

Closest pairs: DevOps–Scarcity boom 0.300; Tool-operator fade–Scarcity boom 0.333; Tool-operator fade–Engineering absorption 0.333; DevOps–SRE 0.357; SRE–Scarcity boom 0.357; DevOps–Lead-industry diffusion 0.375.

Families: {DevOps}; {SRE}; {Mandated officer}; {Tool-operator fade}; {Scarcity boom}; {Lead-industry diffusion}; {Engineering absorption}.

**Stage 1 margin: 0.29** (percentile points; family score = best member's two-coder percentile). Worst false-support rate 5.0%.

| Family | Supported when a member is true (each member) | False: other truths | Average blend | Mixture blend | Null | Null top share |
| --- | --- | --- | --- | --- | --- | --- |
| DevOps | DevOps 0% | 0.0% | 0.1% | 3.1% | 1.0% | 12.0% |
| SRE | SRE 5% | 0.0% | 0.1% | 2.5% | 0.5% | 13.1% |
| Mandated officer | Mandated officer 29% | 0.0% | 0.1% | 2.3% | 2.4% | 19.8% |
| Tool-operator fade | Tool-operator fade 1% | 0.0% | 0.0% | 0.5% | 0.5% | 14.0% |
| Scarcity boom | Scarcity boom 0% | 0.0% | 0.0% | 0.0% | 0.0% | 7.6% |
| Lead-industry diffusion | Lead-industry diffusion 12% | 0.0% | 0.1% | 3.6% | 1.2% | 14.3% |
| Engineering absorption | Engineering absorption 24% | 0.0% | 0.1% | 5.0% | 1.9% | 19.2% |

## Stage 2: DevOps against Scarcity boom (all six features)

Features (6): N15, N04a, N20, N21, N22, N23. Statistic: per feature +1 if the coded value is closer to DevOps, −1 if closer to Scarcity boom, 0 if tied; summed per coder; mean of the two coders.

**k = 4.0**. Wrong-call rates: Scarcity call, DevOps true 0.0%; DevOps call, Scarcity true 0.0%; DevOps call, average blend 0.0%; Scarcity call, average blend 0.0%; DevOps call, mixture blend 3.4%; Scarcity call, mixture blend 3.5%.

| Truth | DevOps over Scarcity | Not distinguishable | Scarcity over DevOps |
| --- | --- | --- | --- |
| DevOps true | 73% | 27% | 0% |
| Scarcity true | 0% | 18% | 82% |
| average blend | 0% | 100% | 0% |
| mixture blend | 3% | 93% | 4% |

**H-DevOps "supported" under A.3 (all six features)**: DevOps true 0%; Scarcity true 0.0%; worst other truth 0.0%; worst average blend 0.1%; worst mixture blend 1.9%; null 0.1%. "Family only" when DevOps true: 0%.

## Stage 2: DevOps against Scarcity boom (truncation rule applied)

Features (4): N15, N20, N21, N22. Statistic: per feature +1 if the coded value is closer to DevOps, −1 if closer to Scarcity boom, 0 if tied; summed per coder; mean of the two coders.

**k = 3.0**. Wrong-call rates: Scarcity call, DevOps true 0.0%; DevOps call, Scarcity true 0.0%; DevOps call, average blend 0.0%; Scarcity call, average blend 0.0%; DevOps call, mixture blend 4.9%; Scarcity call, mixture blend 4.5%.

| Truth | DevOps over Scarcity | Not distinguishable | Scarcity over DevOps |
| --- | --- | --- | --- |
| DevOps true | 75% | 25% | 0% |
| Scarcity true | 0% | 33% | 67% |
| average blend | 0% | 100% | 0% |
| mixture blend | 5% | 91% | 4% |

**H-DevOps "supported" under A.3 (truncation rule applied)**: DevOps true 0%; Scarcity true 0.0%; worst other truth 0.0%; worst average blend 0.1%; worst mixture blend 2.4%; null 0.6%. "Family only" when DevOps true: 0%.

---

# Pattern-matching power check, v3 (two-stage test)

Addendum A.3, triangulation-design.md. Noise q = 0.3 per coder, two coders, 2000 runs per condition, seed 20261011; percentile null 20000 presents, seed 20261012. Same 15 features, NF randomisation, noise, blends and null as A.2.

## Stage 1: families

Rule: two patterns are linked when their ideal distance (mean |difference| over the common features both grade) is at most half the median of the 21 pairwise distances; families are the connected components. Median 0.429, threshold 0.214.

Closest pairs: DevOps–Scarcity boom 0.300; Tool-operator fade–Scarcity boom 0.333; Tool-operator fade–Engineering absorption 0.333; DevOps–SRE 0.357; SRE–Scarcity boom 0.357; DevOps–Lead-industry diffusion 0.375.

Families: {DevOps}; {SRE}; {Mandated officer}; {Tool-operator fade}; {Scarcity boom}; {Lead-industry diffusion}; {Engineering absorption}.

**Stage 1 margin: 0.27** (percentile points; family score = best member's two-coder percentile). Worst false-support rate 5.0%.

| Family | Supported when a member is true (each member) | False: other truths | Average blend | Mixture blend | Null | Null top share |
| --- | --- | --- | --- | --- | --- | --- |
| DevOps | DevOps 2% | 0.0% | 0.4% | 3.3% | 1.0% | 12.4% |
| SRE | SRE 11% | 0.0% | 0.8% | 2.6% | 1.0% | 13.7% |
| Mandated officer | Mandated officer 34% | 0.0% | 1.3% | 3.9% | 2.6% | 22.2% |
| Tool-operator fade | Tool-operator fade 2% | 0.0% | 0.2% | 1.1% | 0.4% | 12.3% |
| Scarcity boom | Scarcity boom 0% | 0.0% | 0.0% | 0.2% | 0.1% | 8.5% |
| Lead-industry diffusion | Lead-industry diffusion 14% | 0.0% | 0.4% | 3.5% | 0.8% | 13.2% |
| Engineering absorption | Engineering absorption 28% | 0.0% | 1.0% | 5.0% | 2.2% | 17.6% |

## Stage 2: DevOps against Scarcity boom (all six features)

Features (6): N15, N04a, N20, N21, N22, N23. Statistic: per feature +1 if the coded value is closer to DevOps, −1 if closer to Scarcity boom, 0 if tied; summed per coder; mean of the two coders.

**k = 4.0**. Wrong-call rates: Scarcity call, DevOps true 0.0%; DevOps call, Scarcity true 0.0%; DevOps call, average blend 0.0%; Scarcity call, average blend 0.0%; DevOps call, mixture blend 1.7%; Scarcity call, mixture blend 2.8%.

| Truth | DevOps over Scarcity | Not distinguishable | Scarcity over DevOps |
| --- | --- | --- | --- |
| DevOps true | 47% | 53% | 0% |
| Scarcity true | 0% | 40% | 60% |
| average blend | 0% | 100% | 0% |
| mixture blend | 2% | 96% | 3% |

**H-DevOps "supported" under A.3 (all six features)**: DevOps true 2%; Scarcity true 0.0%; worst other truth 0.0%; worst average blend 0.1%; worst mixture blend 1.1%; null 0.2%. "Family only" when DevOps true: 0%.

## Stage 2: DevOps against Scarcity boom (truncation rule applied)

Features (4): N15, N20, N21, N22. Statistic: per feature +1 if the coded value is closer to DevOps, −1 if closer to Scarcity boom, 0 if tied; summed per coder; mean of the two coders.

**k = 3.0**. Wrong-call rates: Scarcity call, DevOps true 0.0%; DevOps call, Scarcity true 0.0%; DevOps call, average blend 0.1%; Scarcity call, average blend 0.0%; DevOps call, mixture blend 4.3%; Scarcity call, mixture blend 3.0%.

| Truth | DevOps over Scarcity | Not distinguishable | Scarcity over DevOps |
| --- | --- | --- | --- |
| DevOps true | 55% | 45% | 0% |
| Scarcity true | 0% | 56% | 44% |
| average blend | 0% | 100% | 0% |
| mixture blend | 4% | 93% | 3% |

**H-DevOps "supported" under A.3 (truncation rule applied)**: DevOps true 2%; Scarcity true 0.0%; worst other truth 0.0%; worst average blend 0.1%; worst mixture blend 1.8%; null 0.5%. "Family only" when DevOps true: 0%.

---
