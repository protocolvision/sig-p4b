# Pattern-matching power check, v2

Addendum A.2, triangulation-design.md. Noise q = 0.3 per coder, two coders, 2000 runs per condition, seed 20261011; null reference 20000 presents, seed 20261012. Scores are mid-rank percentiles against each pattern's own null; margins are in percentile points.

Common feature set: observable-now features graded in at least 5 of 7 patterns. Not scored: N05 (4 of 7), N07 (3 of 7), N10 (3 of 7), N11 (2 of 7), N14 (3 of 7), N16a (3 of 7), N24 (2 of 7).

## Main result

Features scored (15): N01, N02, N03, N08, N09, N12, N13, N15, N19, N04a, N06a, N20, N21, N22, N23. Missing cells (NF in the pattern): SRE N04a; Mandated officer N23; Lead-industry diffusion N03, N13, N04a; Engineering absorption N12, N13, N21.

**Margin: 0.27** (percentile points, two coders; worst false-support rate 5.0%). Mean simulated coder disagreement when a pattern is the truth: 0.43.

| Truth | Supported when true | Top when true | False support: other truths (worst) | Average blend (worst pair) | Mixture blend (worst pair) | Null | Ideal gap | Nearest |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DevOps | 2% | 100% | 0.0% | 0.4% | 3.3% | 1.0% | 0.05 | Scarcity boom then specialisation |
| SRE | 11% | 100% | 0.0% | 0.8% | 2.6% | 1.0% | 0.09 | Scarcity boom then specialisation |
| Mandated officer | 34% | 100% | 0.0% | 1.3% | 3.9% | 2.6% | 0.21 | Lead-industry diffusion |
| Tool-operator fade | 2% | 100% | 0.0% | 0.2% | 1.1% | 0.4% | 0.09 | Scarcity boom then specialisation |
| Scarcity boom then specialisation | 0% | 100% | 0.0% | 0.0% | 0.2% | 0.1% | 0.04 | DevOps |
| Lead-industry diffusion | 14% | 100% | 0.0% | 0.4% | 3.5% | 0.8% | 0.16 | Scarcity boom then specialisation |
| Engineering absorption | 28% | 100% | 0.0% | 1.0% | 5.0% | 2.2% | 0.21 | Tool-operator fade |

**Families** (median noiseless percentile gap below the margin): DevOps with Scarcity boom then specialisation; SRE with Scarcity boom then specialisation; Mandated officer with Lead-industry diffusion; Tool-operator fade with Scarcity boom then specialisation; Scarcity boom then specialisation with DevOps; Lead-industry diffusion with Scarcity boom then specialisation; Engineering absorption with Tool-operator fade

**Null top shares** (10000 uniform random presents; 1/7 = 14.3%):

| Pattern | Percentile, one coder, no noise | Percentile, two coders with noise | Raw score (A.1 rule) |
| --- | --- | --- | --- |
| DevOps | 13.3% | 12.4% | 10.0% |
| SRE | 13.3% | 13.7% | 13.2% |
| Mandated officer | 16.1% | 22.2% | 27.6% |
| Tool-operator fade | 12.4% | 12.3% | 10.5% |
| Scarcity boom then specialisation | 11.1% | 8.5% | 6.9% |
| Lead-industry diffusion | 15.1% | 13.2% | 13.0% |
| Engineering absorption | 18.6% | 17.6% | 18.8% |

Sensitivity (not the pre-registered margin): if the truncation rule makes all five of N01, N04a, N08, N12, N23 "insufficient", the script recalibrates on the remaining 10 features, as follows.

## Sensitivity: truncation-exposed features insufficient

Features scored (10): N02, N03, N09, N13, N15, N19, N06a, N20, N21, N22. Missing cells (NF in the pattern): Lead-industry diffusion N03, N13; Engineering absorption N13, N21.

**Margin: 0.27** (percentile points, two coders; worst false-support rate 4.9%). Mean simulated coder disagreement when a pattern is the truth: 0.43.

| Truth | Supported when true | Top when true | False support: other truths (worst) | Average blend (worst pair) | Mixture blend (worst pair) | Null | Ideal gap | Nearest |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DevOps | 3% | 98% | 0.0% | 0.4% | 3.5% | 1.5% | 0.05 | SRE |
| SRE | 0% | 98% | 0.0% | 0.1% | 0.5% | 0.1% | 0.04 | DevOps |
| Mandated officer | 23% | 99% | 0.0% | 0.8% | 3.6% | 2.1% | 0.23 | Lead-industry diffusion |
| Tool-operator fade | 1% | 97% | 0.0% | 0.1% | 0.9% | 0.2% | 0.07 | Scarcity boom then specialisation |
| Scarcity boom then specialisation | 0% | 98% | 0.0% | 0.1% | 0.2% | 0.1% | 0.10 | Tool-operator fade |
| Lead-industry diffusion | 20% | 99% | 0.0% | 0.5% | 4.9% | 1.8% | 0.20 | SRE |
| Engineering absorption | 14% | 96% | 0.0% | 1.1% | 4.0% | 2.0% | 0.10 | Tool-operator fade |

**Families** (median noiseless percentile gap below the margin): DevOps with SRE; SRE with DevOps; Mandated officer with Lead-industry diffusion; Tool-operator fade with Scarcity boom then specialisation; Scarcity boom then specialisation with Tool-operator fade; Lead-industry diffusion with SRE; Engineering absorption with Tool-operator fade

**Null top shares** (10000 uniform random presents; 1/7 = 14.3%):

| Pattern | Percentile, one coder, no noise | Percentile, two coders with noise | Raw score (A.1 rule) |
| --- | --- | --- | --- |
| DevOps | 15.0% | 16.4% | 13.6% |
| SRE | 11.7% | 10.1% | 10.7% |
| Mandated officer | 14.3% | 19.0% | 19.7% |
| Tool-operator fade | 12.6% | 11.2% | 10.6% |
| Scarcity boom then specialisation | 10.6% | 8.0% | 6.2% |
| Lead-industry diffusion | 16.1% | 15.8% | 13.7% |
| Engineering absorption | 19.7% | 19.7% | 25.5% |
