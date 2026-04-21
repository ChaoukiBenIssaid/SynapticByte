"""
The Soul of Statistics — A Masterclass in Conditional Probability.

A Manim Community Edition animation in the spirit of 3Blue1Brown.

Render from the repository root with:

    manim -pqh 02_soul_of_statistics/soul_of_statistics.py SoulOfStatistics

This script is the silent (animations-only) version. The voiceover heard on
the YouTube channel is generated separately and is not included in this repo.
"""

import sys
from pathlib import Path

# Make the repo-level `shared/` module importable when running from any cwd.
_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

import numpy as np
from manim import (
    Arrow,
    Circle,
    Create,
    Cross,
    CurvedArrow,
    DashedLine,
    Dot,
    Ellipse,
    FadeIn,
    FadeOut,
    Flash,
    GrowArrow,
    GrowFromCenter,
    GrowFromEdge,
    Group,
    Indicate,
    Intersection,
    LaggedStart,
    Line,
    MathTex,
    MobjectTable,
    ReplacementTransform,
    RoundedRectangle,
    Scene,
    Square,
    SurroundingRectangle,
    Tex,
    Text,
    TransformFromCopy,
    Uncreate,
    VGroup,
    Write,
    BOLD,
    ITALIC,
    DOWN,
    LEFT,
    RIGHT,
    UP,
    UR,
    UL,
    DR,
    DL,
    GREY_C,
    ORIGIN,
)

from shared.palette import (  # noqa: E402
    BLUE_3B,
    CYAN_GLOW,
    DARK_BG,
    DARK_GREY,
    GOLD_3B,
    GREEN_3B,
    GREY_3B,
    LIGHT_BLUE,
    ORANGE_3B,
    PINK_3B,
    RED_3B,
    SOFT_WHITE,
    TEAL_3B,
    YELLOW_3B,
)
from shared.components import (  # noqa: E402
    Pebble,
    golden_box,
    section_title,
)


# ═══════════════════════════════════════════════════════════════════
#  MAIN SCENE
# ═══════════════════════════════════════════════════════════════════
class SoulOfStatistics(Scene):
    """Top-level scene — calls each ``scene_*`` method in order."""

    def construct(self):
        self.camera.background_color = DARK_BG
        self.scene_title()
        self.scene_all_conditional()
        self.scene_renormalization()
        self.scene_relative_frequency()
        self.scene_lotp()
        self.scene_bayes_rule()
        self.scene_medical_test()
        self.scene_independence()
        self.scene_conditional_independence()
        self.scene_monty_hall_setup()
        self.scene_monty_hall_solution()
        self.scene_first_step_analysis()
        self.scene_prosecutor_fallacy()
        self.scene_defense_fallacy()
        self.scene_diagnostic_matrix()
        self.scene_simpsons_paradox()
        self.scene_resolving_simpson()
        self.scene_belief_toolkit()
        self.scene_closing()

    # ------------------------------------------------------------------
    def clear_scene(self, fade_time=0.6):
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=fade_time)

    # ─────────────────────────────────────────────────────────────
    #  1. TITLE
    # ─────────────────────────────────────────────────────────────
    def scene_title(self):
        pebbles = VGroup()
        np.random.seed(21)
        for _ in range(60):
            r = np.random.uniform(0.02, 0.12)
            p = Dot(
                radius=r, color=GREY_3B,
                fill_opacity=np.random.uniform(0.15, 0.5), stroke_width=0,
            )
            p.move_to([np.random.uniform(-7, 7), np.random.uniform(-4, 4), 0])
            pebbles.add(p)

        ring = Circle(radius=2.5, stroke_color=CYAN_GLOW, stroke_width=3, stroke_opacity=0.9)
        ring_glow = Circle(radius=2.5, stroke_color=CYAN_GLOW, stroke_width=12, stroke_opacity=0.08)

        title = Text("The Soul", font_size=64, color=SOFT_WHITE, weight=BOLD)
        of = Text("of", font_size=52, color=SOFT_WHITE, slant=ITALIC)
        stats = Text("Statistics", font_size=64, color=SOFT_WHITE, weight=BOLD)
        main_title = VGroup(title, of, stats).arrange(RIGHT, buff=0.2)

        subtitle = Text(
            "A Masterclass in Conditional Probability",
            font_size=26, color=GREY_3B, slant=ITALIC,
        )
        subtitle.next_to(main_title, DOWN, buff=0.4)

        self.play(
            LaggedStart(*[FadeIn(p, scale=0.3) for p in pebbles], lag_ratio=0.01),
            run_time=2,
        )
        self.play(Create(ring, run_time=2), Create(ring_glow, run_time=2))
        self.play(Write(main_title, run_time=2))
        self.play(FadeIn(subtitle, shift=UP * 0.2))
        self.wait(1)
        self.play(
            ring_glow.animate.scale(1.3).set_opacity(0),
            run_time=1.5,
        )
        self.clear_scene()

    # ─────────────────────────────────────────────────────────────
    #  2. ALL PROBABILITIES ARE CONDITIONAL
    # ─────────────────────────────────────────────────────────────
    def scene_all_conditional(self):
        statement = Tex(
            r"\textbf{All probabilities}\\",
            r"\textbf{are conditional.}",
            font_size=64, color=SOFT_WHITE,
        )
        statement.shift(UP * 1.5 + LEFT * 2)

        self.play(Write(statement, run_time=2.5))

        pab = MathTex(r"P(A \mid B)", font_size=60, color=GOLD_3B)
        pab_sub = Tex(
            r"The probability of A,\\given the new universe B.",
            font_size=24, color=GREY_3B,
        )
        pab_group = VGroup(pab, pab_sub).arrange(DOWN, buff=0.3)
        pab_group.shift(RIGHT * 3 + DOWN * 1.5)
        pab_box = golden_box(pab_group, buff=0.35)

        beam_lines = VGroup()
        box_left_edge = pab_box.get_left()
        beam_origin_center = statement.get_bottom() + DOWN * 0.5 + RIGHT * 1
        for angle in np.linspace(-0.6, 0.6, 8):
            start_point = beam_origin_center + UP * angle * 2.5 + LEFT * 1.5
            line = Line(
                start_point, box_left_edge,
                stroke_color=GOLD_3B, stroke_width=2, stroke_opacity=0.3,
            )
            beam_lines.add(line)

        self.play(
            LaggedStart(*[Create(l) for l in beam_lines], lag_ratio=0.05),
            run_time=1.5,
        )
        self.play(Create(pab_box), Write(pab), FadeIn(pab_sub, shift=UP * 0.2))
        self.wait(1.5)
        self.clear_scene()

    # ─────────────────────────────────────────────────────────────
    #  3. CONDITIONING AS RENORMALIZATION
    # ─────────────────────────────────────────────────────────────
    def scene_renormalization(self):
        title = section_title("Conditioning = Renormalization")
        title.to_edge(UP, buff=0.5)
        self.play(Write(title[0]), GrowFromEdge(title[1], LEFT))

        base_y = UP * 0.2
        s1_label = Tex(r"\textbf{Original Universe}", font_size=28, color=SOFT_WHITE)

        np.random.seed(33)
        all_pebbles = VGroup()
        pebble_data = []
        for _ in range(18):
            r = np.random.uniform(0.08, 0.25)
            x = np.random.uniform(-1.2, 1.2)
            y = np.random.uniform(-1.2, 1.2)
            p = Dot(radius=r, color=SOFT_WHITE, fill_opacity=0.85, stroke_width=0)
            p.move_to([x, y, 0])
            pebble_data.append((x, y, r))
            all_pebbles.add(p)

        s1_box = Rectangle_(3, 3, SOFT_WHITE, 1.5, 0.5)
        s1_group = VGroup(s1_box, all_pebbles).move_to(LEFT * 4.5 + base_y)
        s1_label.next_to(s1_group, UP, buff=0.3)
        mass_label = Tex(r"Total mass $= 1$", font_size=20, color=GREY_3B)
        mass_label.next_to(s1_group, DOWN, buff=0.3)

        self.play(
            Create(s1_box), Write(s1_label),
            LaggedStart(*[GrowFromCenter(p) for p in all_pebbles], lag_ratio=0.03),
            FadeIn(mass_label),
        )

        s2_label = Tex(r"\textbf{New Evidence (B)}", font_size=28, color=GOLD_3B)
        s2_box = Rectangle_(3, 3, SOFT_WHITE, 1.5, 0.3)
        evidence_circle = Circle(radius=1.1, stroke_color=GOLD_3B, stroke_width=2.5)

        s2_pebbles = VGroup()
        s2_dimmed = VGroup()
        for x, y, r in pebble_data:
            dist = np.sqrt(x ** 2 + y ** 2)
            if dist < 1.1:
                p = Dot(radius=r, color=SOFT_WHITE, fill_opacity=0.9, stroke_width=0)
                p.move_to([x, y, 0])
                s2_pebbles.add(p)
            else:
                p = Dot(radius=r, color=DARK_GREY, fill_opacity=0.15, stroke_width=0)
                p.move_to([x, y, 0])
                s2_dimmed.add(p)

        s2_group = VGroup(s2_box, s2_dimmed, evidence_circle, s2_pebbles).move_to(ORIGIN + base_y)
        s2_label.next_to(s2_group, UP, buff=0.3)
        discard = Tex(
            r"Outcomes contradicting\\evidence are discarded.",
            font_size=20, color=GREY_3B,
        ).next_to(s2_group, DOWN, buff=0.3)

        self.play(
            Create(s2_box), Write(s2_label), Create(evidence_circle),
            LaggedStart(*[FadeIn(p) for p in s2_pebbles], lag_ratio=0.03),
            LaggedStart(*[FadeIn(p) for p in s2_dimmed], lag_ratio=0.03),
            FadeIn(discard, shift=UP * 0.1),
        )

        s3_label = Tex(r"\textbf{Renormalization}", font_size=28, color=GOLD_3B)
        s3_label.move_to(RIGHT * 4.5 + base_y + UP * 1.8)
        renorm = Tex(
            r"Remaining evidence expands\\to become the new 100\%.",
            font_size=20, color=GREY_3B,
        ).move_to(RIGHT * 4.5 + base_y + DOWN * 1.8)

        s3_pebbles = s2_pebbles.copy()
        s3_circle = evidence_circle.copy()
        s3_group = VGroup(s3_circle, s3_pebbles)

        self.play(Write(s3_label), s3_group.animate.move_to(RIGHT * 4.5 + base_y))
        self.play(s3_group.animate.scale(1.35), FadeIn(renorm, shift=UP * 0.1))

        formula = MathTex(
            r"P(A \mid B)", r"=", r"\frac{P(A \cap B)}{P(B)}",
            font_size=48, color=SOFT_WHITE,
        )
        formula[0].set_color(GOLD_3B)
        formula.to_edge(DOWN, buff=0.4)
        fbox = golden_box(formula, buff=0.3)

        self.play(Write(formula), Create(fbox))
        self.wait(1.5)
        self.clear_scene()

    # ─────────────────────────────────────────────────────────────
    #  4. RELATIVE FREQUENCY
    # ─────────────────────────────────────────────────────────────
    def scene_relative_frequency(self):
        title = section_title("Relative Frequency").to_edge(UP, buff=0.4)
        self.play(Write(title[0]), GrowFromEdge(title[1], LEFT))

        np.random.seed(55)
        bits = []
        for _ in range(12 * 25):
            bit = str(np.random.randint(0, 2))
            color = TEAL_3B if np.random.random() < 0.3 else GREY_3B
            opacity = 0.7 if color == TEAL_3B else 0.25
            t = Tex(bit, font_size=18, color=color, fill_opacity=opacity)
            bits.append(t)

        matrix = VGroup(*bits).arrange_in_grid(rows=12, cols=25, buff=0.15)
        matrix.move_to([-3.5, -0.5, 0])

        self.play(FadeIn(matrix))

        circ_b = Circle(radius=1.4, stroke_color=LIGHT_BLUE, stroke_width=3)
        circ_b.move_to(matrix.get_center() + LEFT * 1.2 + UP * 0.3)
        label_b = MathTex("B", font_size=28, color=LIGHT_BLUE).next_to(circ_b, UP, buff=0.1)

        circ_a = Circle(radius=1.1, stroke_color=TEAL_3B, stroke_width=3)
        circ_a.move_to(circ_b.get_center() + RIGHT * 1.4 + DOWN * 0.6)
        label_a = MathTex("A", font_size=28, color=TEAL_3B).next_to(circ_a, RIGHT, buff=0.1)

        self.play(Create(circ_b), Write(label_b), Create(circ_a), Write(label_a))

        formulas = VGroup(
            MathTex(r"P(A) \approx \frac{n_A}{n}", font_size=36, color=TEAL_3B),
            MathTex(r"P(B) \approx \frac{n_B}{n}", font_size=36, color=LIGHT_BLUE),
            MathTex(r"P(A \cap B) \approx \frac{n_{AB}}{n}", font_size=36, color=SOFT_WHITE),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)

        insight = MathTex(
            r"P(A \mid B)", r"\approx",
            r"\frac{n_{AB}/n}{n_B/n}", r"=", r"\frac{n_{AB}}{n_B}",
            font_size=40, color=GOLD_3B,
        )
        ibox = golden_box(insight, buff=0.3)
        insight_bundled = VGroup(ibox, insight)

        note = Tex(
            r"\textbf{Restrict attention ONLY to trials where B occurs.}",
            font_size=20, color=GREY_3B,
        )

        right_panel = VGroup(formulas, insight_bundled, note).arrange(DOWN, buff=0.7).shift(DOWN * 0.2)
        right_panel.move_to([3.5, -0.5, 0])

        self.play(LaggedStart(*[Write(f) for f in formulas], lag_ratio=0.4))
        self.play(Write(insight), Create(ibox), FadeIn(note, shift=UP * 0.2))

        dim_animations = []
        for bit in matrix:
            dist = np.linalg.norm(bit.get_center() - circ_b.get_center())
            if dist > circ_b.radius:
                dim_animations.append(bit.animate.set_opacity(0.05))
            else:
                dim_animations.append(bit.animate.set_opacity(1))
        dim_animations.append(circ_a.animate.set_stroke(opacity=0.2))
        dim_animations.append(label_a.animate.set_opacity(0.2))

        self.play(*dim_animations)
        self.wait(1.5)
        self.clear_scene()

    # ─────────────────────────────────────────────────────────────
    #  5. LAW OF TOTAL PROBABILITY (LOTP)
    # ─────────────────────────────────────────────────────────────
    def scene_lotp(self):
        title = section_title("The Strategy of Wishful Thinking").to_edge(UP, buff=0.5)
        self.play(Write(title[0]), GrowFromEdge(title[1], LEFT))

        question = Tex(
            r"How do we find the probability of a complex event?\\",
            r"We condition on what we wish we knew.",
            font_size=28, color=GREY_3B,
        ).next_to(title, DOWN, buff=0.4)

        self.play(FadeIn(question))

        partition_colors = [BLUE_3B, GREEN_3B, "#9B59B6", RED_3B, GOLD_3B, TEAL_3B]
        strips = VGroup()
        strip_w = 1.2
        for i in range(6):
            strip = Rectangle_(strip_w, 4, SOFT_WHITE, 1, 0.4, fill_color=partition_colors[i], fill_opacity=0.08)
            strip.move_to([-3.8 + i * strip_w + strip_w / 2, -1, 0])
            label = MathTex(f"A_{i+1}", font_size=22, color=SOFT_WHITE).next_to(strip, DOWN, buff=0.15)
            strips.add(VGroup(strip, label))

        self.play(LaggedStart(*[FadeIn(s) for s in strips], lag_ratio=0.1))

        blob_b = Ellipse(width=5, height=2.5, color=GOLD_3B, stroke_width=2.5, fill_opacity=0.08)
        blob_b.move_to([-1.8, -0.8, 0])
        b_label = MathTex("B", font_size=28, color=GOLD_3B).next_to(blob_b, UP, buff=0.1)

        self.play(Create(blob_b), Write(b_label))

        intersections = VGroup()
        for i, s in enumerate(strips):
            inter = Intersection(
                blob_b, s[0],
                fill_color=partition_colors[i], fill_opacity=0.35, stroke_width=0,
            )
            intersections.add(inter)

        self.play(LaggedStart(*[FadeIn(inter) for inter in intersections], lag_ratio=0.15))

        lotp_header = Tex(
            r"\textbf{The Law of Total Probability (LOTP)}",
            font_size=26, color=GOLD_3B,
        )
        lotp_formula = MathTex(
            r"P(B) = \sum_i P(B \mid A_i) \, P(A_i)",
            font_size=36, color=SOFT_WHITE,
        )
        lotp_group = VGroup(lotp_header, lotp_formula).arrange(DOWN, buff=0.3)
        lotp_group.shift(RIGHT * 3.5 + DOWN * 1.5)
        lbox = golden_box(lotp_group, buff=0.3)

        self.play(Write(lotp_header), Write(lotp_formula), Create(lbox))

        arrows = VGroup()
        for i in range(4):
            start_point = strips[i][1].get_right()
            target_point = lbox.get_left() + UP * (0.3 - i * 0.2)
            arr = Arrow(
                start_point, target_point,
                color=partition_colors[i], stroke_width=2, buff=0.1,
                max_tip_length_to_length_ratio=0.08,
            )
            arrows.add(arr)

        self.play(LaggedStart(*[GrowArrow(arr) for arr in arrows], lag_ratio=0.15))
        self.wait(1.5)
        self.clear_scene()

    # ─────────────────────────────────────────────────────────────
    #  6. BAYES' RULE
    # ─────────────────────────────────────────────────────────────
    def scene_bayes_rule(self):
        title = section_title("Reversing the Conditionals").to_edge(UP, buff=0.5)
        self.play(Write(title[0]), GrowFromEdge(title[1], LEFT))

        subtitle = Tex(
            r"We know $P(B \mid A)$ but desperately need $P(A \mid B)$.",
            font_size=32, color=GREY_3B,
        ).next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(subtitle))

        posterior = MathTex(r"P(A \mid B)", font_size=60, color=GOLD_3B)
        equals = MathTex("=", font_size=60, color=SOFT_WHITE)
        likelihood = MathTex(r"P(B \mid A)", font_size=60, color=LIGHT_BLUE)
        prior = MathTex(r"P(A)", font_size=60, color=TEAL_3B)
        numerator = VGroup(likelihood, prior).arrange(RIGHT, buff=0.15)
        denominator = MathTex(r"P(B)", font_size=60, color=SOFT_WHITE)
        frac_width = max(numerator.width, denominator.width) + 0.2
        frac_line = Line(LEFT, RIGHT, stroke_width=2, color=SOFT_WHITE).set_width(frac_width)
        fraction = VGroup(numerator, frac_line, denominator).arrange(DOWN, buff=0.2)
        bayes = VGroup(posterior, equals, fraction).arrange(RIGHT, buff=0.25).shift(DOWN * 0.8)
        bbox = golden_box(bayes, buff=0.45)

        self.play(Write(bayes), Create(bbox))

        post_label = Tex(
            r"\textbf{The Posterior:}\\Our updated belief.",
            font_size=24, color=GOLD_3B,
        )
        post_box = SurroundingRectangle(
            post_label, color=GOLD_3B, stroke_width=1, buff=0.15,
            fill_color=DARK_BG, fill_opacity=0.9,
        )
        post_label.move_to(LEFT * 3.5 + DOWN * 2.5)
        post_box.move_to(post_label)
        post_arrow = CurvedArrow(
            post_label.get_top(), posterior.get_bottom() + DOWN * 0.1,
            color=GOLD_3B, stroke_width=2, angle=-0.3,
        )

        self.play(FadeIn(post_box), FadeIn(post_label), Create(post_arrow))

        like_label = Tex(
            r"\textbf{The Likelihood:}\\How well the evidence\\fits the belief.",
            font_size=24, color=LIGHT_BLUE,
        )
        like_box = SurroundingRectangle(
            like_label, color=LIGHT_BLUE, stroke_width=1, buff=0.15,
            fill_color=DARK_BG, fill_opacity=0.9,
        )
        like_label.move_to(LEFT * 4 + UP * 0.8)
        like_box.move_to(like_label)
        like_arrow = CurvedArrow(
            like_label.get_right(),
            likelihood.get_top() + UP * 0.1 + LEFT * 0.2,
            color=LIGHT_BLUE, stroke_width=2, angle=0.4,
        )

        self.play(FadeIn(like_box), FadeIn(like_label), Create(like_arrow))

        prior_label = Tex(
            r"\textbf{The Prior:}\\What we believed\\before.",
            font_size=24, color=TEAL_3B,
        )
        prior_box = SurroundingRectangle(
            prior_label, color=TEAL_3B, stroke_width=1, buff=0.15,
            fill_color=DARK_BG, fill_opacity=0.9,
        )
        prior_label.move_to(RIGHT * 4 + UP * 0.8)
        prior_box.move_to(prior_label)
        prior_arrow = CurvedArrow(
            prior_label.get_left(),
            prior.get_top() + UP * 0.1 + RIGHT * 0.2,
            color=TEAL_3B, stroke_width=2, angle=-0.4,
        )

        self.play(FadeIn(prior_box), FadeIn(prior_label), Create(prior_arrow))

        coherency = Tex(
            r"Coherency: Updating sequentially piece-by-piece yields\\",
            r"the exact same result as updating with all evidence simultaneously.",
            font_size=24, color=GREY_3B,
        ).to_edge(DOWN, buff=0.2)

        self.play(FadeIn(coherency))
        self.wait(1.5)
        self.clear_scene()

    # ─────────────────────────────────────────────────────────────
    #  7. MEDICAL / FACTORY TEST (FALSE POSITIVES)
    # ─────────────────────────────────────────────────────────────
    def scene_medical_test(self):
        title = section_title("The False Positive Trap").to_edge(UP, buff=0.4)
        self.play(Write(title[0]), GrowFromEdge(title[1], LEFT))

        TREE_SHIFT = DOWN * 0.5

        prompt = Tex(
            r"``A factory scanner tests microchips for defects (1\% failure rate). "
            r"The scanner is 95\% accurate. If a chip flags as defective, what is "
            r"the actual chance it's broken?''",
            font_size=28, color=GREY_3B,
        )
        prompt.next_to(title, DOWN, buff=0.3)

        self.play(FadeIn(prompt))

        def make_branch_node(icon_char, main_val, sub_text, color, radius=0.45):
            bg_circle = Circle(
                radius=radius, stroke_color=color, stroke_width=3,
                fill_color=DARK_BG, fill_opacity=1,
            )
            glow = Circle(
                radius=radius * 1.2, stroke_color=color,
                stroke_width=6, stroke_opacity=0.15,
            )
            icon = Text(icon_char, color=color)
            icon.width = radius * 1.1
            icon.move_to(bg_circle)
            icon_group = Group(glow, bg_circle, icon)
            val_tex = Tex(main_val, font_size=24, color=SOFT_WHITE).next_to(icon_group, UP, buff=0.15)
            label = Tex(sub_text, font_size=20, color=color).next_to(icon_group, DOWN, buff=0.15)
            return Group(icon_group, val_tex, label), icon_group

        def make_leaf_node(icon_char, main_val, sub_text, color, radius=0.35):
            bg_circle = Circle(
                radius=radius, stroke_color=color, stroke_width=3,
                fill_color=DARK_BG, fill_opacity=1,
            )
            glow = Circle(
                radius=radius * 1.2, stroke_color=color,
                stroke_width=6, stroke_opacity=0.15,
            )
            icon = Text(icon_char, color=color)
            icon.width = radius * 1.1
            icon.move_to(bg_circle)
            icon_group = Group(glow, bg_circle, icon)
            val_tex = Tex(main_val, font_size=22, color=color).next_to(icon_group, DOWN, buff=0.15)
            label = Tex(sub_text, font_size=22, color=color).next_to(icon_group, RIGHT, buff=0.4)
            return Group(icon_group, val_tex, label), icon_group, label

        root, root_icon = make_branch_node("🏢", "10,000", "Total Chips", SOFT_WHITE, radius=0.55)
        root.move_to(LEFT * 5.8 + DOWN * 1 + TREE_SHIFT)

        defective, def_icon = make_branch_node("📟", "100", r"Defective (1\%)", GREY_3B, radius=0.45)
        defective.move_to(LEFT * 3.0 + UP * 0.5 + TREE_SHIFT)

        perfect, perf_icon = make_branch_node("📟", "9,900", r"Perfect (99\%)", TEAL_3B, radius=0.45)
        perfect.move_to(LEFT * 3.0 + DOWN * 2.3 + TREE_SHIFT)

        line_d = Line(root_icon.get_right(), def_icon.get_left(), stroke_color=GOLD_3B, stroke_width=2)
        line_p = Line(root_icon.get_right(), perf_icon.get_left(), stroke_color=TEAL_3B, stroke_width=2)

        tp, tp_icon, tp_lbl = make_leaf_node("⚠️", "95", r"Flagged +\\(True Positives)", GOLD_3B)
        tp.move_to(LEFT * 0.5 + UP * 1.5 + TREE_SHIFT)
        line_tp = Line(def_icon.get_right(), tp_icon.get_left(), stroke_color=GOLD_3B, stroke_width=2)

        fn, fn_icon, fn_lbl = make_leaf_node("✔", "5", r"Passed -\\(False Negatives)", DARK_GREY, radius=0.3)
        fn.move_to(LEFT * 0.5 + UP * 0.1 + TREE_SHIFT)
        line_fn = Line(def_icon.get_right(), fn_icon.get_left(), stroke_color=DARK_GREY, stroke_width=1.5)

        fp, fp_icon, fp_lbl = make_leaf_node("⚠️", "495", r"Flagged +\\(False Positives)", ORANGE_3B)
        fp.move_to(LEFT * 0.5 + DOWN * 1.2 + TREE_SHIFT)
        line_fp = Line(perf_icon.get_right(), fp_icon.get_left(), stroke_color=ORANGE_3B, stroke_width=2)

        tn, tn_icon, tn_lbl = make_leaf_node("✔", "9,405", r"Passed -\\(True Negatives)", TEAL_3B)
        tn.move_to(LEFT * 0.5 + DOWN * 2.7 + TREE_SHIFT)
        line_tn = Line(perf_icon.get_right(), tn_icon.get_left(), stroke_color=TEAL_3B, stroke_width=1.5)

        self.play(FadeIn(root))
        self.play(Create(line_d), Create(line_p), FadeIn(defective), FadeIn(perfect))
        self.play(
            Create(line_tp), Create(line_fn), Create(line_fp), Create(line_tn),
            FadeIn(tp), FadeIn(fn), FadeIn(fp), FadeIn(tn),
        )

        reveal_title = Tex(r"\textbf{The Reveal}", font_size=32, color=SOFT_WHITE)
        reveal_formula = MathTex(
            r"\mathcal{P}(D \mid +) = \frac{95}{95 + 495} \approx 0.16",
            font_size=32, color=GOLD_3B,
        )
        reveal_note = Tex(
            r"Despite a 95\% accurate scanner, a flagged chip\\",
            r"only has a 16\% chance of being broken.\\",
            r"\textbf{Never ignore the prior.}",
            font_size=20, color=GREY_3B,
        )
        reveal = VGroup(reveal_title, reveal_formula, reveal_note).arrange(DOWN, buff=0.3)
        reveal.move_to(RIGHT * 4.6 + DOWN * 0.8 + TREE_SHIFT)
        rbox = golden_box(reveal, buff=0.3)
        reveal_group = VGroup(rbox, reveal)

        arrow_tp = Arrow(tp_lbl.get_right(), rbox.get_left() + UP * 0.5, color=GOLD_3B, stroke_width=2, buff=0.15)
        arrow_fn = Arrow(fn_lbl.get_right(), rbox.get_left() + UP * 0.1, color=DARK_GREY, stroke_width=1.5, buff=0.15)
        arrow_fp = Arrow(fp_lbl.get_right(), rbox.get_left() + DOWN * 0.3, color=ORANGE_3B, stroke_width=2, buff=0.15)
        arrow_tn = Arrow(tn_lbl.get_right(), rbox.get_left() + DOWN * 0.7, color=TEAL_3B, stroke_width=1.5, buff=0.15)

        self.play(
            FadeIn(reveal_group, shift=UP * 0.2),
            GrowArrow(arrow_tp), GrowArrow(arrow_fn),
            GrowArrow(arrow_fp), GrowArrow(arrow_tn),
        )
        self.play(
            fn.animate.set_opacity(0.15), line_fn.animate.set_opacity(0.15), arrow_fn.animate.set_opacity(0.15),
            tn.animate.set_opacity(0.15), line_tn.animate.set_opacity(0.15), arrow_tn.animate.set_opacity(0.15),
        )
        self.wait(1.5)
        self.clear_scene()

    # ─────────────────────────────────────────────────────────────
    #  8. INDEPENDENCE
    # ─────────────────────────────────────────────────────────────
    def scene_independence(self):
        title = section_title("Independence: When Evidence Changes Nothing", font_size=46)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title[0]), GrowFromEdge(title[1], LEFT))

        defn = Text(
            "Events A and B are independent if learning that B occurred\n"
            "gives us zero new information about A.",
            font_size=22, color=SOFT_WHITE, line_spacing=1.3,
        ).next_to(title, DOWN, buff=0.5)

        self.play(FadeIn(defn))

        f1 = MathTex(r"P(A \cap B) = P(A) \, P(B)", font_size=40, color=SOFT_WHITE)
        f2 = MathTex(r"\text{Implication: } P(A \mid B) = P(A)", font_size=36, color=GOLD_3B)
        formulas = VGroup(f1, f2).arrange(DOWN, buff=0.4).shift(DOWN * 0.2)
        fbox = golden_box(formulas)

        self.play(Write(f1), Write(f2), Create(fbox))

        warn1_title = Text("Independence ≠ Disjointness", font_size=20, color=GOLD_3B, weight=BOLD)
        warn1_text = Text(
            "If A and B are disjoint, knowing A\n"
            "means B definitely did not occur.\n"
            "Disjoint events are highly dependent!",
            font_size=16, color=GREY_3B, line_spacing=1.3,
        )
        warn1 = VGroup(warn1_title, warn1_text).arrange(DOWN, buff=0.15).shift(LEFT * 3.2 + DOWN * 2.5)
        w1box = SurroundingRectangle(
            warn1, color=GREY_3B, stroke_width=1, buff=0.15, corner_radius=0.08,
            fill_color=DARK_GREY, fill_opacity=0.4,
        )

        warn2_title = Text("Pairwise vs. Mutual", font_size=20, color=SOFT_WHITE, weight=BOLD)
        warn2_text = Text(
            "Events can be independent in isolated\n"
            "pairs, but dependent when viewed as\n"
            "a whole collective group.",
            font_size=16, color=GREY_3B, line_spacing=1.3,
        )
        warn2 = VGroup(warn2_title, warn2_text).arrange(DOWN, buff=0.15).shift(RIGHT * 3.2 + DOWN * 2.5)
        w2box = SurroundingRectangle(
            warn2, color=GREY_3B, stroke_width=1, buff=0.15, corner_radius=0.08,
            fill_color=DARK_GREY, fill_opacity=0.4,
        )

        self.play(FadeIn(w1box), FadeIn(warn1))
        self.play(FadeIn(w2box), FadeIn(warn2))
        self.wait(1.5)
        self.clear_scene()

    # ─────────────────────────────────────────────────────────────
    #  9. CONDITIONAL INDEPENDENCE
    # ─────────────────────────────────────────────────────────────
    def scene_conditional_independence(self):
        title = section_title("Conditional Independence").to_edge(UP, buff=0.5)
        self.play(Write(title[0]), GrowFromEdge(title[1], LEFT))

        scenario = Tex(
            r"\textit{Scenario: Why is the server crashing?}",
            font_size=32, color=GREY_3B,
        ).next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(scenario))

        def make_icon_node(letter, label_text, node_color):
            bg_circle = Circle(
                radius=0.6, stroke_color=node_color, stroke_width=3, fill_opacity=0.1,
            )
            glow = Circle(
                radius=0.75, stroke_color=node_color, stroke_width=5, stroke_opacity=0.2,
            )
            icon = Text(letter, font_size=40, color=node_color)
            icon.width = 0.6
            icon.move_to(bg_circle)
            label = Tex(label_text, font_size=24, color=SOFT_WHITE).next_to(bg_circle, DOWN, buff=0.2)
            return Group(glow, bg_circle, icon, label), bg_circle

        m_node_group, m_circle = make_icon_node("M", r"\textbf{M}: Memory Leak", GREY_C)
        m_node_group.move_to(LEFT * 5 + UP * 0.2)

        n_node_group, n_circle = make_icon_node("N", r"\textbf{N}: Network Spike", GREY_3B)
        n_node_group.move_to(LEFT * 5 + DOWN * 2.4)

        c_node_group, c_circle = make_icon_node("C", r"\textbf{C}: Crashing", ORANGE_3B)
        c_node_group.move_to(LEFT * 2 + DOWN * 1.1)

        arr_mc = Arrow(m_circle.get_right(), c_circle.get_top() + LEFT * 0.1, color=GOLD_3B, stroke_width=2, buff=0.15)
        arr_nc = Arrow(n_circle.get_right(), c_circle.get_bottom() + LEFT * 0.1, color=GOLD_3B, stroke_width=2, buff=0.15)

        indep_note = Tex(
            r"\textbf{Unconditionally Independent:}\\A memory leak is no more\\or less likely to cause a spike.",
            font_size=20, color=GREY_3B,
        ).move_to(LEFT * 5 + DOWN * 1.1)

        self.play(FadeIn(m_node_group), FadeIn(n_node_group), Write(indep_note))
        self.play(GrowArrow(arr_mc), GrowArrow(arr_nc), FadeIn(c_node_group))

        c_heavy_glow = Circle(
            radius=0.9, stroke_color=ORANGE_3B, stroke_width=8, stroke_opacity=0.3,
        ).move_to(c_circle)

        self.play(
            Create(c_heavy_glow),
            Flash(c_circle, color=ORANGE_3B, line_length=0.3, num_lines=12),
            c_circle.animate.set_fill(ORANGE_3B, opacity=0.3),
        )

        expl_title = Tex(
            r"\textbf{We observe a crash (condition on C).}",
            font_size=24, color=ORANGE_3B,
        )
        expl_text = Tex(
            r"Now, knowing there is NO memory leak\\",
            r"provides massive information: if it\\",
            r"is crashing without a leak, there MUST\\",
            r"be a network spike.",
            font_size=22, color=SOFT_WHITE,
        )
        expl_key = Tex(
            r"\textbf{M and N are suddenly dependent given C.}",
            font_size=24, color=GOLD_3B,
        )
        expl_formula = MathTex(
            r"P(M, N \mid C) < P(M \mid C) \, P(N \mid C)",
            font_size=32, color=SOFT_WHITE,
        )
        expl = VGroup(expl_title, expl_text, expl_key, expl_formula).arrange(DOWN, buff=0.3)
        expl.move_to(RIGHT * 3 + DOWN * 1.1)
        ebox = golden_box(expl, buff=0.35)
        expl_group = VGroup(ebox, expl)

        self.play(FadeIn(expl_group, shift=UP * 0.2))
        self.wait(1.5)
        self.clear_scene()

    # ─────────────────────────────────────────────────────────────
    #  10. MONTY HALL SETUP
    # ─────────────────────────────────────────────────────────────
    def scene_monty_hall_setup(self):
        title = section_title("The Monty Hall Problem").to_edge(UP, buff=0.5)
        self.play(Write(title[0]), GrowFromEdge(title[1], LEFT))

        doors = VGroup()
        for lbl in ["1", "2", "3"]:
            door = VGroup(
                RoundedRectangle(
                    width=1.5, height=2.5, corner_radius=0.08,
                    stroke_color=GREY_3B, stroke_width=2,
                    fill_color=DARK_GREY, fill_opacity=0.5,
                ),
                Text(lbl, font_size=36, color=SOFT_WHITE, weight=BOLD),
            )
            door[1].move_to(door[0].get_center() + DOWN * 0.5)
            doors.add(door)
        doors.arrange(RIGHT, buff=0.8).shift(UP * 0.3)

        goat1 = Text("🐐", font_size=28).next_to(doors[0], UP, buff=0.2).set_opacity(0.3)
        car = Text("🚗", font_size=28).next_to(doors[1], UP, buff=0.2).set_opacity(0.3)
        goat2 = Text("🐐", font_size=28).next_to(doors[2], UP, buff=0.2).set_opacity(0.3)
        icons = VGroup(goat1, car, goat2)

        self.play(LaggedStart(*[FadeIn(d, shift=UP * 0.3) for d in doors], lag_ratio=0.2))
        self.play(FadeIn(icons))

        steps = VGroup(
            Text("1. Contestant chooses Door 1.", font_size=20, color=SOFT_WHITE),
            Text("2. Monty (who knows everything) opens Door 2, revealing a goat.", font_size=20, color=SOFT_WHITE),
            Text('3. Monty asks: "Do you want to switch to Door 3?"', font_size=20, color=SOFT_WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).shift(DOWN * 1.8)
        steps_bg = SurroundingRectangle(
            steps, color=GREY_3B, stroke_width=1,
            fill_color=DARK_GREY, fill_opacity=0.5, buff=0.2, corner_radius=0.08,
        )

        self.play(FadeIn(steps_bg), LaggedStart(*[Write(s) for s in steps], lag_ratio=0.4))
        self.play(
            doors[0][0].animate.set_stroke(color=YELLOW_3B, width=3),
            doors[1][0].animate.set_fill(opacity=0.1).set_stroke(opacity=0.3),
            goat1.animate.set_opacity(0), car.animate.set_opacity(1), goat2.animate.set_opacity(0),
        )

        wrong = Text('"Two doors left, so it must be 50-50."', font_size=22, color=RED_3B).to_edge(DOWN, buff=0.5)
        cross = Cross(wrong, stroke_color=RED_3B, stroke_width=4)
        self.play(Write(wrong), Create(cross))
        self.wait(1.5)
        self.clear_scene()

    # ─────────────────────────────────────────────────────────────
    #  11. MONTY HALL SOLUTION
    # ─────────────────────────────────────────────────────────────
    def scene_monty_hall_solution(self):
        title = section_title("Demolishing Intuition").to_edge(UP, buff=0.4)
        self.play(Write(title[0]), GrowFromEdge(title[1], LEFT))

        tree_title = Text(
            "The Tree Strategy", font_size=22, color=SOFT_WHITE, weight=BOLD,
        ).shift(LEFT * 3.5 + UP * 1.2)
        summary = VGroup(
            Text("Car at 1 (1/3): switching loses", font_size=16, color=RED_3B),
            Text("Car at 2 (1/3): Monty MUST open 3 → switch wins", font_size=16, color=GREEN_3B),
            Text("Car at 3 (1/3): Monty MUST open 2 → switch wins", font_size=16, color=GREEN_3B),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(tree_title, DOWN, buff=0.3)
        win_prob = MathTex(
            r"\text{Win by switching} = \frac{2}{3}",
            font_size=32, color=YELLOW_3B,
        ).next_to(summary, DOWN, buff=0.4)

        self.play(Write(tree_title), FadeIn(summary[0], shift=RIGHT * 0.2))
        self.play(FadeIn(summary[1], shift=RIGHT * 0.2), FadeIn(summary[2], shift=RIGHT * 0.2))
        self.play(Write(win_prob))

        bayes_title = Text(
            "The Bayesian Proof", font_size=22, color=SOFT_WHITE, weight=BOLD,
        ).shift(RIGHT * 3 + UP * 1.2)
        bayes_setup = MathTex(
            r"P(C_1 \mid M_2) = \frac{P(M_2 \mid C_1) \, P(C_1)}{P(M_2)}",
            font_size=28, color=SOFT_WHITE,
        )
        bayes_calc = MathTex(
            r"= \frac{(1/2)(1/3)}{1/2} = \frac{1}{3}",
            font_size=28, color=GOLD_3B,
        )
        bayes_proof = VGroup(bayes_setup, bayes_calc).arrange(DOWN, buff=0.2).next_to(bayes_title, DOWN, buff=0.3)
        bpbox = golden_box(bayes_proof)

        self.play(Write(bayes_title), Write(bayes_setup), Write(bayes_calc), Create(bpbox))

        insight = Text(
            "Monty's choice breaks the symmetry.  Always switch.",
            font_size=24, color=YELLOW_3B, weight=BOLD,
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(insight))
        self.wait(1.5)
        self.clear_scene()

    # ─────────────────────────────────────────────────────────────
    #  12. FIRST-STEP ANALYSIS
    # ─────────────────────────────────────────────────────────────
    def scene_first_step_analysis(self):
        title = section_title("Strategy: First-Step Analysis").to_edge(UP, buff=0.5)
        self.play(Write(title[0]), GrowFromEdge(title[1], LEFT))

        scenario = Tex(
            r"Every millisecond, a rogue nanobot degrades (1/3), duplicates (1/3),\\",
            r"or remains idle (1/3). What is P(eradication)?",
            font_size=24, color=GREY_3B,
        ).next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(scenario))

        def make_nanobot(color=CYAN_GLOW, radius=0.2):
            bg_circle = Circle(
                radius=radius, fill_color=DARK_BG, fill_opacity=1,
                stroke_color=color, stroke_width=2,
            )
            glow = Circle(
                radius=radius * 1.4, fill_opacity=0,
                stroke_color=color, stroke_width=6, stroke_opacity=0.2,
            )
            icon = Text("N", font_size=24, color=color)
            icon.width = radius * 1.2
            icon.move_to(bg_circle)
            return Group(glow, bg_circle, icon), bg_circle

        def make_death_mark(radius=0.15):
            mark = VGroup(
                Line(UP * radius + RIGHT * radius, DOWN * radius + LEFT * radius),
                Line(UP * radius + LEFT * radius, DOWN * radius + RIGHT * radius),
            ).set_color(RED_3B).set_stroke(width=3)
            return mark

        nano_group, nano_core = make_nanobot(CYAN_GLOW)
        nano_group.shift(LEFT * 4 + DOWN * 0.3)

        die_mark = make_death_mark().move_to(LEFT * 2.0 + UP * 1.4)
        same_group, same_core = make_nanobot(CYAN_GLOW, radius=0.15)
        same_group.move_to(LEFT * 2.0 + DOWN * 0.3)
        split1_group, split1_core = make_nanobot(CYAN_GLOW, radius=0.15)
        split1_group.move_to(LEFT * 2.0 + DOWN * 1.4)
        split2_group, split2_core = make_nanobot(CYAN_GLOW, radius=0.15)
        split2_group.next_to(split1_group, RIGHT, buff=0.1)

        arr_die = Arrow(
            nano_core.get_right(), die_mark.get_bottom() + LEFT * 0.1,
            stroke_color=RED_3B, buff=0.1, max_tip_length_to_length_ratio=0.1,
        )
        arr_same = Arrow(
            nano_core.get_right(), same_core.get_left(),
            stroke_color=CYAN_GLOW, buff=0.1, max_tip_length_to_length_ratio=0.1,
        )
        arr_split = Arrow(
            nano_core.get_right(), split1_core.get_top() + LEFT * 0.1,
            stroke_color=CYAN_GLOW, buff=0.1, max_tip_length_to_length_ratio=0.1,
        )

        prob_die = MathTex(r"\frac{1}{3}", font_size=20, color=GREY_3B).next_to(arr_die, UP, buff=0.05)
        prob_same = MathTex(r"\frac{1}{3}", font_size=20, color=GREY_3B).next_to(arr_same, UP, buff=0.05)
        prob_split = MathTex(r"\frac{1}{3}", font_size=20, color=GREY_3B).next_to(arr_split, DOWN, buff=0.05)

        self.play(FadeIn(nano_group))

        math_title = Tex(r"\textbf{The Math Box (First-Step Strategy)}", font_size=22, color=GOLD_3B)
        math_let = Tex(r"Let $P(E)$ be the probability of eradication.", font_size=22, color=SOFT_WHITE)
        math_cond = Tex(
            r"\textit{Condition on the first millisecond using LOTP:}",
            font_size=20, color=GREY_3B,
        )

        eq_start = MathTex(r"P(E) =", font_size=32, color=SOFT_WHITE)
        eq_term1 = MathTex(r"\frac{1}{3}(1)", font_size=32, color=RED_3B)
        eq_plus1 = MathTex(r"+", font_size=32, color=SOFT_WHITE)
        eq_term2 = MathTex(r"\frac{1}{3}P(E)", font_size=32, color=CYAN_GLOW)
        eq_plus2 = MathTex(r"+", font_size=32, color=SOFT_WHITE)
        eq_term3 = MathTex(r"\frac{1}{3}P(E)^2", font_size=32, color=CYAN_GLOW)

        equation = VGroup(eq_start, eq_term1, eq_plus1, eq_term2, eq_plus2, eq_term3).arrange(RIGHT, buff=0.15)
        math_group = VGroup(math_title, math_let, math_cond, equation).arrange(DOWN, buff=0.3)
        math_group.shift(RIGHT * 2.5 + DOWN * 0.8)
        mbox = SurroundingRectangle(
            math_group, color=GREY_3B, stroke_width=2, buff=0.3, corner_radius=0.15,
            fill_color=DARK_BG, fill_opacity=0.8,
        )

        self.play(FadeIn(mbox), FadeIn(math_title), FadeIn(math_let), FadeIn(math_cond), FadeIn(eq_start))
        self.play(GrowArrow(arr_die), FadeIn(prob_die), FadeIn(die_mark), TransformFromCopy(prob_die, eq_term1))
        self.play(FadeIn(eq_plus1), GrowArrow(arr_same), FadeIn(prob_same), FadeIn(same_group), TransformFromCopy(prob_same, eq_term2))
        self.play(FadeIn(eq_plus2), GrowArrow(arr_split), FadeIn(prob_split), FadeIn(split1_group), FadeIn(split2_group), TransformFromCopy(prob_split, eq_term3))
        self.play(
            eq_term1.animate.set_color(SOFT_WHITE),
            eq_term2.animate.set_color(SOFT_WHITE),
            eq_term3.animate.set_color(SOFT_WHITE),
        )

        insight = Tex(
            r"Conditioning on the first step transforms an infinite recursive\\",
            r"nightmare into a simple quadratic equation.",
            font_size=24, color=YELLOW_3B,
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(insight))
        self.wait(1.5)
        self.clear_scene()

    # ─────────────────────────────────────────────────────────────
    #  13. PROSECUTOR'S FALLACY
    # ─────────────────────────────────────────────────────────────
    def scene_prosecutor_fallacy(self):
        title = section_title("The Prosecutor's Fallacy").to_edge(UP, buff=0.5)
        self.play(Write(title[0]), GrowFromEdge(title[1], LEFT))

        context = Tex(
            r"The tragic misapplication of probability in analyzing rare evidence.",
            font_size=24, color=GREY_3B,
        ).next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(context))

        def get_icon(fallback_text, color):
            icon = Text(fallback_text, color=color)
            icon.height = 0.8
            return icon

        fl_icon = get_icon("⚖", RED_3B)
        fl_title = Tex(r"\textbf{The Flawed Logic}", font_size=28, color=SOFT_WHITE)
        fl_header = VGroup(fl_icon, fl_title).arrange(DOWN, buff=0.2)
        fl_fact1 = Tex("1. DNA from a crime scene matches a suspect.", font_size=20, color=GREY_3B)
        fl_fact2 = Tex("2. Expert says P(Random Match) = 1 in 1 Billion.", font_size=20, color=GREY_3B)
        fl_conclusion_text = Tex(r"\textit{Prosecutor wrongly concludes:}", font_size=20, color=RED_3B)
        fl_conclusion_math = MathTex(
            r"P(\text{Innocent}) = \text{1 in 1 Billion}",
            font_size=28, color=RED_3B,
        )
        fl_conclusion = VGroup(fl_conclusion_text, fl_conclusion_math).arrange(DOWN, buff=0.15)
        fl_content = VGroup(fl_header, fl_fact1, fl_fact2, fl_conclusion).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        fl_content.shift(LEFT * 3.5 + DOWN * 0.5)

        mf_icon = get_icon("🧬", GOLD_3B)
        mf_title = Tex(r"\textbf{The Mathematical Fatal Flaw}", font_size=28, color=SOFT_WHITE)
        mf_header = VGroup(mf_icon, mf_title).arrange(DOWN, buff=0.2)
        mf_formula = MathTex(
            r"P(\text{Evidence} \mid \text{Innocence}) \neq P(\text{Innocence} \mid \text{Evidence})",
            font_size=28, color=GOLD_3B,
        )
        mf_text = Tex(
            r"A random match is rare, but if testing\\",
            r"a database of millions, finding AT LEAST\\",
            r"one random match is extremely likely.\\",
            r"\textbf{The expert completely ignored the prior.}",
            font_size=20, color=GREY_3B,
        )
        mf_content = VGroup(mf_header, mf_formula, mf_text).arrange(DOWN, buff=0.4)
        mf_content.shift(RIGHT * 3.5 + DOWN * 0.5)

        divider = DashedLine(
            UP * 1.5, DOWN * 3.5, stroke_color=GREY_3B, stroke_width=2, dash_length=0.1,
        )
        self.play(Create(divider))
        self.play(FadeIn(fl_header, shift=DOWN * 0.2), FadeIn(fl_fact1, shift=RIGHT * 0.2), FadeIn(fl_fact2, shift=RIGHT * 0.2))
        self.play(FadeIn(fl_conclusion, shift=UP * 0.2))

        strike_line = Line(
            fl_conclusion.get_left() + LEFT * 0.2, fl_conclusion.get_right() + RIGHT * 0.2,
            color=RED_3B, stroke_width=4,
        )
        self.play(Create(strike_line), fl_conclusion.animate.set_opacity(0.5))
        self.play(FadeIn(mf_header, shift=DOWN * 0.2), Write(mf_formula))
        self.play(FadeIn(mf_text, shift=UP * 0.2))
        self.wait(1.5)
        self.clear_scene()

    # ─────────────────────────────────────────────────────────────
    #  14. DEFENSE ATTORNEY'S FALLACY
    # ─────────────────────────────────────────────────────────────
    def scene_defense_fallacy(self):
        title = section_title("The Defense Attorney's Fallacy").to_edge(UP, buff=0.5)
        self.play(Write(title[0]), GrowFromEdge(title[1], LEFT))

        context = Text(
            "The danger of failing to condition on all available evidence.",
            font_size=24, color=GREY_3B,
        ).next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(context))

        def get_icon(fallback_text, color):
            icon = Text(fallback_text, color=color)
            icon.height = 0.8
            return icon

        fl_icon = get_icon("💼", RED_3B)
        fl_title = Text("The Flawed Logic", font_size=28, color=SOFT_WHITE, weight=BOLD)
        fl_header = VGroup(fl_icon, fl_title).arrange(DOWN, buff=0.2)
        fl_text = Text(
            "\"Only 1 in 10,000 brokers who sell early\n"
            "are guilty of insider trading. It's irrelevant.\"",
            font_size=20, color=GREY_3B, line_spacing=1.2,
        )
        fl_math = MathTex(
            r"P(\text{Guilty} \mid \text{Sold Early}) = \frac{1}{10{,}000}",
            font_size=32, color=RED_3B,
        )
        fl_content = VGroup(fl_header, fl_text, fl_math).arrange(DOWN, buff=0.5)
        fl_content.shift(LEFT * 3.5 + DOWN * 0.5)

        mf_icon = get_icon("🔍", GOLD_3B)
        mf_title = Text("The Fatal Flaw", font_size=28, color=SOFT_WHITE, weight=BOLD)
        mf_header = VGroup(mf_icon, mf_title).arrange(DOWN, buff=0.2)
        mf_text1 = Text(
            "They ignored the most critical evidence:\n"
            "An internal memo was on their computer.",
            font_size=20, color=RED_3B, line_spacing=1.2,
        )
        mf_math = MathTex(
            r"P(\text{Guilty} \mid \text{Sold} \cap \text{Has Memo})",
            font_size=32, color=GOLD_3B,
        )
        mf_box = golden_box(mf_math, buff=0.25)
        mf_math_bundled = VGroup(mf_box, mf_math)
        mf_text2 = Text(
            "When the leaked memo is factored in,\n"
            "the probability skyrockets to > 50%.",
            font_size=20, color=GREY_3B, line_spacing=1.2,
        )
        mf_content = VGroup(mf_header, mf_text1, mf_math_bundled, mf_text2).arrange(DOWN, buff=0.4)
        mf_content.shift(RIGHT * 3.5 + DOWN * 0.5)

        divider = DashedLine(
            UP * 1.5, DOWN * 3.5, stroke_color=GREY_3B, stroke_width=2, dash_length=0.1,
        )
        self.play(Create(divider))
        self.play(FadeIn(fl_header, shift=DOWN * 0.2), Write(fl_text), FadeIn(fl_math, shift=UP * 0.2))
        self.play(
            fl_content.animate.set_opacity(0.3),
            FadeIn(mf_header, shift=DOWN * 0.2),
            FadeIn(mf_text1, shift=RIGHT * 0.2),
        )
        self.play(Create(mf_box), Write(mf_math), FadeIn(mf_text2, shift=UP * 0.2))
        self.wait(1.5)
        self.clear_scene()

    # ─────────────────────────────────────────────────────────────
    #  15. DIAGNOSTIC MATRIX
    # ─────────────────────────────────────────────────────────────
    def scene_diagnostic_matrix(self):
        title = section_title("Diagnostic Matrix: Legal Fallacies").to_edge(UP, buff=0.5)
        self.play(Write(title[0]), GrowFromEdge(title[1], LEFT))

        def get_header_with_icon(text, fallback_char, color):
            icon = Text(fallback_char, color=color)
            icon.height = 0.5
            label = Tex(rf"\textbf{{{text}}}", font_size=28, color=SOFT_WHITE)
            return VGroup(icon, label).arrange(RIGHT, buff=0.2)

        col_headers = [
            get_header_with_icon("Prosecutor's Fallacy", "⚖", RED_3B),
            get_header_with_icon("Defense Attorney's Fallacy", "🔍", GOLD_3B),
        ]
        row_headers = [
            Tex(r"\textbf{The Error}", font_size=24, color=SOFT_WHITE),
            Tex(r"\textbf{The Math}", font_size=24, color=SOFT_WHITE),
            Tex(r"\textbf{The Danger}", font_size=24, color=SOFT_WHITE),
        ]
        rows_data = [
            [Tex(r"Transposing the\\Conditional", font_size=22, color=GREY_3B),
             Tex(r"Incomplete\\Conditioning", font_size=22, color=GREY_3B)],
            [MathTex(r"\text{Confusing } P(E \mid I)\\ \text{with } P(I \mid E)", font_size=26, color=RED_3B),
             MathTex(r"\text{Calculating } P(G \mid A)\\ \text{instead of } P(G \mid A \cap M)", font_size=26, color=GOLD_3B)],
            [Tex(r"Making rare evidence\\seem like proof of guilt", font_size=22, color=GREY_3B),
             Tex(r"Diluting evidence within\\an improperly large universe", font_size=22, color=GREY_3B)],
        ]

        table = MobjectTable(
            rows_data,
            row_labels=row_headers,
            col_labels=col_headers,
            include_outer_lines=False,
            line_config={"stroke_color": GREY_3B, "stroke_width": 1.5, "stroke_opacity": 0.5},
        ).scale(0.85).shift(UP * 0.1)

        footnote = Tex(
            r"$E$: Evidence \textbar\ $I$: Innocence \textbar\ $G$: Guilt \textbar\ $A$: Action (e.g., Sold Early) \textbar\ $M$: Memo",
            font_size=18, color=GREY_3B,
        ).to_edge(DOWN, buff=0.2)

        self.play(
            Create(table.get_horizontal_lines()), Create(table.get_vertical_lines()),
            FadeIn(table.get_col_labels()), FadeIn(table.get_row_labels()),
        )

        entries = table.get_entries_without_labels()
        self.play(FadeIn(entries[0], shift=UP * 0.15), FadeIn(entries[1], shift=UP * 0.15))
        self.play(FadeIn(entries[2], shift=UP * 0.15), FadeIn(entries[3], shift=UP * 0.15), FadeIn(footnote))
        self.play(FadeIn(entries[4], shift=UP * 0.15), FadeIn(entries[5], shift=UP * 0.15))
        self.wait(1.5)
        self.clear_scene()

    # ─────────────────────────────────────────────────────────────
    #  16. SIMPSON'S PARADOX
    # ─────────────────────────────────────────────────────────────
    def scene_simpsons_paradox(self):
        title = section_title("Simpson's Paradox").to_edge(UP, buff=0.5)
        self.play(Write(title[0]), GrowFromEdge(title[1], LEFT))

        subtitle = Tex(r"\textit{The Impossibility}", font_size=26, color=GREY_3B).next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(subtitle))

        def get_avatar(text, fallback_char, color):
            icon = Text(fallback_char, color=color)
            icon.height = 0.5
            label = Tex(rf"\textbf{{{text}}}", font_size=22, color=SOFT_WHITE)
            return VGroup(icon, label).arrange(DOWN, buff=0.15)

        col_labels = [
            get_avatar("Alice (Sr. Dev)", "A", TEAL_3B),
            get_avatar("Bob (Jr. Dev)", "B", GOLD_3B),
        ]
        row_labels = [
            Tex("Core Backend", font_size=22, color=SOFT_WHITE),
            Tex("UI Tweaks", font_size=22, color=SOFT_WHITE),
            Tex(r"\textbf{Total Success}", font_size=22, color=SOFT_WHITE),
        ]

        rows_data = [
            [Tex(r"70/90 (78\%)", font_size=22, color=TEAL_3B), Tex(r"2/10 (20\%)", font_size=22, color=GREY_C)],
            [Tex(r"10/10 (100\%)", font_size=22, color=TEAL_3B), Tex(r"81/90 (90\%)", font_size=22, color=GREY_C)],
            [Tex(r"80/100 (80\%)", font_size=24, color=GREY_C), Tex(r"\textbf{83/100 (83\%)}", font_size=24, color=GOLD_3B)],
        ]

        table = MobjectTable(
            rows_data,
            row_labels=row_labels,
            col_labels=col_labels,
            include_outer_lines=False,
            line_config={"stroke_color": GREY_3B, "stroke_width": 1},
        ).scale(0.9).shift(RIGHT * 1.5 + DOWN * 0.3)

        h_lines = table.get_horizontal_lines()
        if len(h_lines) > 3:
            h_lines[3].set_color(SOFT_WHITE).set_stroke(width=2)

        self.play(
            Create(table.get_horizontal_lines()), Create(table.get_vertical_lines()),
            FadeIn(table.get_col_labels()), FadeIn(table.get_row_labels()),
        )
        entries = table.get_entries_without_labels()
        self.play(FadeIn(entries[0], shift=UP * 0.1), FadeIn(entries[1], shift=UP * 0.1))
        self.play(FadeIn(entries[2], shift=UP * 0.1), FadeIn(entries[3], shift=UP * 0.1))

        ann1 = Tex(
            r"\textbf{Alice is better at\\BOTH types\\of tasks.}",
            font_size=22, color=TEAL_3B,
        )
        ann1.move_to(LEFT * 4.5 + UP * 0.2)
        target_y = (table.get_cell((2, 1)).get_y() + table.get_cell((3, 1)).get_y()) / 2
        arr1 = Arrow(
            ann1.get_right(),
            np.array([table.get_left()[0], target_y, 0]),
            color=TEAL_3B, buff=0.2,
        )
        self.play(FadeIn(ann1, shift=RIGHT * 0.2), GrowArrow(arr1))
        self.play(FadeIn(entries[4], shift=UP * 0.1), FadeIn(entries[5], shift=UP * 0.1))

        ann2 = Tex(
            r"\textbf{Bob has a better\\OVERALL success\\rate?!}",
            font_size=22, color=GOLD_3B,
        )
        ann2.move_to(LEFT * 4.5 + DOWN * 1.8)
        arr2 = Arrow(
            ann2.get_right(),
            np.array([table.get_left()[0], table.get_cell((4, 1)).get_y(), 0]),
            color=GOLD_3B, buff=0.2,
        )
        self.play(FadeIn(ann2, shift=RIGHT * 0.2), GrowArrow(arr2))

        q = Tex(
            r"\textbf{How can Alice be better at every individual task,\\but worse overall?}",
            font_size=26, color=YELLOW_3B,
        ).to_edge(DOWN, buff=0.4)

        self.play(
            table.animate.set_opacity(0.3),
            ann1.animate.set_opacity(0.3), arr1.animate.set_opacity(0.3),
            ann2.animate.set_opacity(0.3), arr2.animate.set_opacity(0.3),
            Write(q),
        )
        self.wait(1.5)
        self.clear_scene()

    # ─────────────────────────────────────────────────────────────
    #  17. RESOLVING SIMPSON'S PARADOX
    # ─────────────────────────────────────────────────────────────
    def scene_resolving_simpson(self):
        title = section_title("Resolving the Paradox").to_edge(UP, buff=0.5)
        self.play(Write(title[0]), GrowFromEdge(title[1], LEFT))

        def get_avatar(text, fallback_char, color):
            icon = Text(fallback_char, color=color)
            icon.height = 0.4
            label = Tex(rf"\textbf{{{text}}}", font_size=20, color=SOFT_WHITE)
            return VGroup(icon, label).arrange(DOWN, buff=0.15)

        def make_dot_grid(n_hard, n_easy, pos):
            hard_dots = VGroup()
            for i in range(n_hard):
                r, c = divmod(i, 10)
                d = Dot(radius=0.06, color=SOFT_WHITE, fill_opacity=0.9).move_to(
                    pos + np.array([c * 0.18, -r * 0.18, 0])
                )
                hard_dots.add(d)
            offset_y = -((n_hard - 1) // 10 + 1) * 0.18 - 0.2
            easy_dots = VGroup()
            for i in range(n_easy):
                r, c = divmod(i, 10)
                d = Dot(radius=0.06, color=GREY_3B, fill_opacity=0.6).move_to(
                    pos + np.array([c * 0.18, offset_y - r * 0.18, 0])
                )
                easy_dots.add(d)
            return hard_dots, easy_dots

        alice_hard, alice_easy = make_dot_grid(90, 10, np.array([-5.0, 1.2, 0]))
        bob_hard, bob_easy = make_dot_grid(10, 90, np.array([-1.5, 1.2, 0]))
        alice_grid = VGroup(alice_hard, alice_easy)
        bob_grid = VGroup(bob_hard, bob_easy)

        alice_lbl = get_avatar("Alice", "A", TEAL_3B).next_to(alice_grid, DOWN, buff=0.3)
        bob_lbl = get_avatar("Bob", "B", GOLD_3B).next_to(bob_grid, DOWN, buff=0.3)
        h_hard_label = Tex("Backend", font_size=18, color=SOFT_WHITE).next_to(alice_hard, LEFT, buff=0.3)
        h_easy_label = Tex("UI Tweaks", font_size=18, color=GREY_3B).next_to(alice_easy, LEFT, buff=0.3)

        self.play(
            FadeIn(h_hard_label), FadeIn(h_easy_label), FadeIn(alice_lbl), FadeIn(bob_lbl),
            LaggedStart(*[FadeIn(d, scale=0.5) for d in alice_hard], lag_ratio=0.01),
            LaggedStart(*[FadeIn(d, scale=0.5) for d in alice_easy], lag_ratio=0.01),
            LaggedStart(*[FadeIn(d, scale=0.5) for d in bob_hard], lag_ratio=0.01),
            LaggedStart(*[FadeIn(d, scale=0.5) for d in bob_easy], lag_ratio=0.01),
        )

        expl1_title = Tex(
            r"\textbf{The Confounding Variable: Task Difficulty}",
            font_size=22, color=GOLD_3B,
        )
        t_box = SurroundingRectangle(
            expl1_title, color=GOLD_3B, stroke_width=1.5, buff=0.15,
            fill_color=DARK_GREY, fill_opacity=0.4,
        )
        title_group = VGroup(t_box, expl1_title)

        expl1 = Tex(
            r"Alice takes on almost all the\\high-risk, difficult tasks (90 backend).",
            font_size=20, color=SOFT_WHITE,
        )
        e1_box = SurroundingRectangle(
            expl1, color=TEAL_3B, stroke_width=1.5, buff=0.15,
            fill_color=DARK_GREY, fill_opacity=0.4,
        )
        group1 = VGroup(e1_box, expl1)

        expl2 = Tex(
            r"Bob pads his statistics with\\trivial tasks (90 UI Tweaks).",
            font_size=20, color=SOFT_WHITE,
        )
        e2_box = SurroundingRectangle(
            expl2, color=GOLD_3B, stroke_width=1.5, buff=0.15,
            fill_color=DARK_GREY, fill_opacity=0.4,
        )
        group2 = VGroup(e2_box, expl2)

        expls = VGroup(title_group, group1, group2).arrange(DOWN, buff=0.4).shift(RIGHT * 3.5 + UP * 0.3)
        self.play(FadeIn(title_group, shift=UP * 0.2))

        alice_highlight = SurroundingRectangle(alice_hard, color=TEAL_3B, stroke_width=2, buff=0.1)
        self.play(
            FadeIn(group1, shift=UP * 0.2),
            Create(alice_highlight),
            alice_easy.animate.set_opacity(0.2),
            bob_grid.animate.set_opacity(0.2),
        )

        bob_highlight = SurroundingRectangle(bob_easy, color=GOLD_3B, stroke_width=2, buff=0.1)
        self.play(
            FadeIn(group2, shift=UP * 0.2),
            Uncreate(alice_highlight),
            alice_hard.animate.set_opacity(0.2),
            bob_easy.animate.set_opacity(1),
            Create(bob_highlight),
        )
        self.play(
            Uncreate(bob_highlight),
            alice_grid.animate.set_opacity(1),
            bob_grid.animate.set_opacity(1),
        )

        bottom = MathTex(
            r"P(A \mid B, \mathbf{C}) < P(A \mid B^c, \mathbf{C})",
            r"\text{ does NOT guarantee }",
            r"P(A \mid B) < P(A \mid B^c)",
            font_size=28, color=SOFT_WHITE,
            tex_to_color_map={r"\mathbf{C}": GOLD_3B},
        )
        bottom.to_edge(DOWN, buff=0.4)
        bbox = golden_box(bottom)
        self.play(Create(bbox), Write(bottom))
        self.wait(1.5)
        self.clear_scene()

    # ─────────────────────────────────────────────────────────────
    #  18. BELIEF UPDATING TOOLKIT
    # ─────────────────────────────────────────────────────────────
    def scene_belief_toolkit(self):
        title = section_title("The Belief Updating Toolkit").to_edge(UP, buff=0.5)
        self.play(Write(title[0]), GrowFromEdge(title[1], LEFT))

        col_headers = [
            Tex(r"\textbf{What you have}", font_size=36, color=SOFT_WHITE),
            Tex(r"\textbf{What you want}", font_size=36, color=LIGHT_BLUE),
            Tex(r"\textbf{The Tool}", font_size=36, color=GOLD_3B),
        ]
        rows_data = [
            [MathTex(r"A \cap B \text{ and } B", font_size=32),
             MathTex(r"P(A \mid B)", font_size=32, color=LIGHT_BLUE),
             Tex(r"\textbf{Formal Definition}", font_size=32, color=GOLD_3B)],
            [MathTex(r"P(B \mid A_i) \text{ and partitions}", font_size=32),
             MathTex(r"\text{The total } P(B)", font_size=32, color=LIGHT_BLUE),
             Tex(r"\textbf{Law of Total Probability}\\\textbf{(Wishful Thinking)}", font_size=28, color=GOLD_3B)],
            [MathTex(r"P(B \mid A)", font_size=32),
             MathTex(r"\text{The reverse } P(A \mid B)", font_size=32, color=LIGHT_BLUE),
             Tex(r"\textbf{Bayes' Rule}\\\textbf{(The Inversion Engine)}", font_size=28, color=GOLD_3B)],
            [Tex(r"Infinite recursive stages", font_size=32),
             Tex(r"The ultimate outcome", font_size=32, color=LIGHT_BLUE),
             Tex(r"\textbf{First-Step Analysis}", font_size=32, color=GOLD_3B)],
        ]

        table = MobjectTable(
            rows_data,
            col_labels=col_headers,
            include_outer_lines=False,
            line_config={"stroke_color": GREY_3B, "stroke_width": 1, "stroke_opacity": 0.6},
        ).scale(0.85).shift(DOWN * 0.3)
        from manim import Rectangle
        accent_bar = Rectangle(
            width=0.06, height=table.height,
            fill_color=TEAL_3B, fill_opacity=0.8, stroke_width=0,
        ).next_to(table, LEFT, buff=0.5)

        self.play(
            Create(table.get_horizontal_lines()),
            Create(table.get_vertical_lines()),
            FadeIn(accent_bar),
        )
        self.play(
            FadeIn(table.get_rows()[0]),
            LaggedStart(
                *[FadeIn(row, shift=RIGHT * 0.2) for row in VGroup(*table.get_rows()[1:])],
                lag_ratio=0.3,
            ),
        )
        self.wait(2)
        self.clear_scene()

    # ─────────────────────────────────────────────────────────────
    #  19. CLOSING
    # ─────────────────────────────────────────────────────────────
    def scene_closing(self):
        s1 = Text("All probabilities are conditional.", font_size=52, color=SOFT_WHITE, weight=BOLD)
        s2 = Text("We are always updating.", font_size=52, color=SOFT_WHITE, weight=BOLD)
        statement = VGroup(s1, s2).arrange(DOWN, buff=0.3)

        orb = Dot(radius=1.2, color=ORANGE_3B, fill_opacity=0.7, stroke_width=0)
        orb_glow = Dot(radius=2.5, color=ORANGE_3B, fill_opacity=0.08, stroke_width=0)

        self.play(GrowFromCenter(VGroup(orb_glow, orb)))
        self.play(Write(s1))
        self.play(Write(s2))
        self.wait(1.5)
        self.play(
            orb_glow.animate.scale(2).set_opacity(0),
            *[FadeOut(m) for m in self.mobjects],
        )


# ---------------------------------------------------------------------------
# Local helper (kept inside module scope to avoid leaking into `shared`)
# ---------------------------------------------------------------------------
def Rectangle_(width, height, stroke_color, stroke_width, stroke_opacity,
               fill_color=DARK_GREY, fill_opacity=0.0):
    """Shorthand for a Manim Rectangle with fill + stroke parameters."""
    from manim import Rectangle
    return Rectangle(
        width=width, height=height,
        stroke_color=stroke_color, stroke_width=stroke_width,
        stroke_opacity=stroke_opacity,
        fill_color=fill_color, fill_opacity=fill_opacity,
    )
