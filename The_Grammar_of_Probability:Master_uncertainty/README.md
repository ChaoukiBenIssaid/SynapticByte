# 01 — Probability & Combinatorics, Visually Explained

> *The Logic of Uncertainty — Episode 1*
>
> **📺 Watch on YouTube:** https://www.youtube.com/watch?v=AZKP7mejviQ

Human intuition is notoriously bad at probability. This video builds the foundations from the ground up, from sample spaces to the birthday paradox, using a "pebble-based" visual metaphor.

---

## Scene breakdown

| # | Method | Topic |
|---|---|---|
| 1 | `scene_title` | Title card |
| 2 | `scene_birthday_hook` | The birthday paradox — what are the chances in a room of 23? |
| 3 | `scene_pebble_world` | Sample spaces and events, visualized as pebbles |
| 4 | `scene_naive_definition` | The naive definition of probability |
| 5 | `scene_fifty_fifty_fallacy` | Why "it either is or isn't" is not 50–50 |
| 6 | `scene_leibniz_dice` | Leibniz's dice mistake — labelling matters |
| 7 | `scene_problem_of_scale` | 2⁵² possible events — why we need combinatorics |
| 8 | `scene_multiplication_rule` | The multiplication rule |
| 9 | `scene_overcounting` | Adjusting for overcounting |
| 10 | `scene_binomial_coefficient` | Deriving the binomial coefficient |
| 11 | `scene_counting_matrix` | The master counting matrix (n^k, n!/(n−k)!, C(n,k), …) |
| 12 | `scene_story_proof` | Story proof: C(n,k) = C(n, n−k) |
| 13 | `scene_solving_birthday` | Solving the birthday paradox via the complement |
| 14 | `scene_math_no_matches` | The math of "no matches" |
| 15 | `scene_tipping_point` | The tipping point graph — 50% at k=23, 99% at k=57 |
| 16 | `scene_beyond_naive` | Beyond the naive definition |
| 17 | `scene_axioms` | The two axioms of probability |
| 18 | `scene_inclusion_exclusion` | Inclusion-exclusion |
| 19 | `scene_grand_synthesis` | Events ↔ Set theory ↔ Probability |
| 20 | `scene_blueprint` | The blueprint of uncertainty |

---

## Rendering

From the repo root:

```bash
# Full video at 1080p60
manim -pqh 01_logic_of_uncertainty/logic_of_uncertainty.py LogicOfUncertainty

# Fast preview
manim -pql 01_logic_of_uncertainty/logic_of_uncertainty.py LogicOfUncertainty
```

---

## Topics covered

Sample Space, Events, Naive Definition of Probability, The 50–50 Fallacy, Multiplication Rule, Permutations, Combinations, Binomial Coefficient, Story Proofs, The Birthday Paradox, Kolmogorov Axioms, Inclusion-Exclusion.
