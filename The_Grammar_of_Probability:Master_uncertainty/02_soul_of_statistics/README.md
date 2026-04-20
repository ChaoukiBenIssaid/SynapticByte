# 02 — Conditional Probability: The Soul of Statistics

> *The Soul of Statistics — Episode 1*
>
> **📺 Watch on YouTube:** *(coming soon)*

A visual masterclass in conditional probability, Bayes' rule, and the ways belief gets updated (and misused) in the real world.

---

## Scene breakdown

| # | Method | Topic |
|---|---|---|
| 1 | `scene_title` | Title card |
| 2 | `scene_all_conditional` | All probabilities are conditional |
| 3 | `scene_renormalization` | Conditioning as renormalization |
| 4 | `scene_relative_frequency` | Relative frequency view |
| 5 | `scene_lotp` | Law of Total Probability |
| 6 | `scene_bayes_rule` | Bayes' rule: prior, likelihood, posterior |
| 7 | `scene_medical_test` | The false positive trap (factory chip example) |
| 8 | `scene_independence` | Independence ≠ disjointness |
| 9 | `scene_conditional_independence` | Explaining away — when observing an effect couples independent causes |
| 10 | `scene_monty_hall_setup` | The Monty Hall problem |
| 11 | `scene_monty_hall_solution` | Why switching doubles your odds |
| 12 | `scene_first_step_analysis` | First-step analysis for infinite stochastic processes |
| 13 | `scene_prosecutor_fallacy` | The prosecutor's fallacy |
| 14 | `scene_defense_fallacy` | The defense attorney's fallacy |
| 15 | `scene_diagnostic_matrix` | Diagnostic matrix of legal fallacies |
| 16 | `scene_simpsons_paradox` | Simpson's paradox — how data can lie |
| 17 | `scene_resolving_simpson` | Resolving Simpson's paradox with confounders |
| 18 | `scene_belief_toolkit` | The belief updating toolkit |
| 19 | `scene_closing` | Closing card |

---

## Rendering

From the repo root:

```bash
# Full video at 1080p60
manim -pqh 02_soul_of_statistics/soul_of_statistics.py SoulOfStatistics

# Fast preview
manim -pql 02_soul_of_statistics/soul_of_statistics.py SoulOfStatistics
```

---

## Assets used

Scene methods reference the following SVG files in `assets/`. All are currently **placeholders** — scenes fall back to geometric primitives when an SVG is missing, so the video renders cleanly either way.

| File | Used in scene |
|---|---|
| `factory.svg` | Medical/factory test |
| `chip.svg` | Medical/factory test |
| `alert.svg` | Medical/factory test |
| `check.svg` | Medical/factory test |
| `memory.svg` | Conditional independence |
| `network.svg` | Conditional independence |
| `crash.svg` | Conditional independence |
| `nanobot.svg` | First-step analysis |
| `skull.svg` | First-step analysis |
| `scales.svg` | Prosecutor fallacy / diagnostic matrix |
| `dna_database.svg` | Prosecutor fallacy |
| `briefcase.svg` | Defense fallacy |
| `magnifying_glass.svg` | Defense fallacy / diagnostic matrix |
| `alice.svg` | Simpson's paradox |
| `bob.svg` | Simpson's paradox |

Replace with your own properly-licensed SVGs. Recommended free sources:
- [Feather Icons](https://feathericons.com/)
- [Heroicons](https://heroicons.com/)
- [Tabler Icons](https://tabler-icons.io/)

---

## Topics covered

Conditional Probability, Renormalization, Law of Total Probability, Bayes' Rule, Prior/Likelihood/Posterior, Base Rate Fallacy, Independence, Conditional Independence, Explaining Away, The Monty Hall Problem, First-Step Analysis, The Prosecutor's Fallacy, The Defense Attorney's Fallacy, Simpson's Paradox, Confounding Variables.
