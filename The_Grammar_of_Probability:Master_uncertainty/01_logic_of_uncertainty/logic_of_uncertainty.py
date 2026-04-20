"""
The Logic of Uncertainty – Probability, Counting, and the Limits of Intuition
A Manim CE video in the spirit of 3Blue1Brown.

Render full video:
    manim -pqh logic_of_uncertainty.py LogicOfUncertainty

Render individual scenes:
    manim -pqh logic_of_uncertainty.py TitleScene
    manim -pqh logic_of_uncertainty.py BirthdayHook
    manim -pqh logic_of_uncertainty.py PebbleWorld
    ... etc.
"""

from manim import *
import numpy as np

# ─── 3B1B-style palette ─────────────────────────────────────────
DARK_BG       = "#1C1C2E"
SOFT_WHITE    = "#ECE6D0"
BLUE_3B       = "#58C4DD"
LIGHT_BLUE    = "#9CDCEB"
YELLOW_3B     = "#FFFF00"
GOLD_3B       = "#F4C95D"
GREEN_3B      = "#83C167"
RED_3B        = "#FC6255"
PINK_3B       = "#E48BC0"
GREY_3B       = "#888888"
DARK_GREY     = "#444444"
TEAL_3B       = "#5CD0B3"


# ─── Reusable Components ────────────────────────────────────────
class Pebble(Dot):
    """A glowing outcome dot — the 'pebble' metaphor."""
    def __init__(self, color=BLUE_3B, radius=0.1, glow=True, **kwargs):
        super().__init__(
            radius=radius, color=color,
            fill_opacity=0.9, stroke_width=0,
            **kwargs
        )
        if glow:
            halo = Dot(radius=radius * 2.5, color=color, fill_opacity=0.12, stroke_width=0)
            halo.move_to(self.get_center())
            self.add_to_back(halo)


def brace_label(mob, text, direction=DOWN, color=SOFT_WHITE, font_size=28):
    """Create a brace with centered label."""
    b = Brace(mob, direction, color=color, buff=0.15)
    l = MathTex(text, font_size=font_size, color=color)
    l.next_to(b, direction, buff=0.1)
    return VGroup(b, l)


def section_title(text, font_size=56):
    """Animate a section header in 3B1B style."""
    t = Text(text, font_size=font_size, color=SOFT_WHITE, weight=BOLD)
    ul = Underline(t, color=BLUE_3B, stroke_width=2, buff=0.15)
    return VGroup(t, ul)


# ═════════════════════════════════════════════════════════════════
#  MAIN SCENE — full video
# ═════════════════════════════════════════════════════════════════
class LogicOfUncertainty(Scene):
    def construct(self):
        self.camera.background_color = DARK_BG
        self.scene_title()
        self.scene_birthday_hook()
        self.scene_pebble_world()
        self.scene_naive_definition()
        self.scene_fifty_fifty_fallacy()
        self.scene_leibniz_dice()
        self.scene_problem_of_scale()
        self.scene_multiplication_rule()
        self.scene_overcounting()
        self.scene_binomial_coefficient()
        self.scene_counting_matrix()
        self.scene_story_proof()
        self.scene_solving_birthday()
        self.scene_math_no_matches()
        self.scene_tipping_point()
        self.scene_beyond_naive()
        self.scene_axioms()
        self.scene_inclusion_exclusion()
        self.scene_grand_synthesis()
        self.scene_blueprint()

    # ─────────────────────────────────────────────────────────────
    #  Transition helper
    # ─────────────────────────────────────────────────────────────
    def clear(self, fade_time=0.6):
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=fade_time)

    # ─────────────────────────────────────────────────────────────
    #  1. TITLE
    # ─────────────────────────────────────────────────────────────
    def scene_title(self):
        # Subtle grid
        grid = NumberPlane(
            x_range=[-8, 8, 1], y_range=[-5, 5, 1],
            background_line_style={
                "stroke_color": GREY_3B, "stroke_opacity": 0.08, "stroke_width": 1
            },
            axis_config={"stroke_opacity": 0},
            faded_line_ratio=0,
        )

        title = Text("The Logic of Uncertainty",
                      font_size=60, color=SOFT_WHITE, weight=BOLD)
        subtitle = Text("Probability, Counting, and the Limits of Intuition",
                        font_size=28, color=GREY_3B)
        subtitle.next_to(title, DOWN, buff=0.5)

        # Signature glowing dot
        dot = Dot(radius=0.25, color=BLUE_3B, fill_opacity=1)
        halo = Dot(radius=0.7, color=BLUE_3B, fill_opacity=0.15, stroke_width=0)
        glow = VGroup(halo, dot)
        glow.next_to(subtitle, DOWN, buff=0.7)

        self.play(FadeIn(grid, run_time=2))
        self.play(Write(title, run_time=2.5))
        self.play(FadeIn(subtitle, shift=UP * 0.3, run_time=1))
        self.play(GrowFromCenter(glow, run_time=0.8))

        # Pulse the dot
        self.play(
            halo.animate.scale(1.5).set_opacity(0),
            rate_func=smooth, run_time=1.5
        )
        self.wait(1)
        self.clear()

    # ─────────────────────────────────────────────────────────────
    #  2. THE BIRTHDAY HOOK
    # ─────────────────────────────────────────────────────────────
    def scene_birthday_hook(self):
        # 23 people as glowing dots in a circle
        people = VGroup()
        for i in range(23):
            angle = i * TAU / 23
            pos = 2.2 * np.array([np.cos(angle), np.sin(angle), 0])
            p = Pebble(color=BLUE_3B, radius=0.08)
            p.move_to(pos)
            people.add(p)
        people.shift(LEFT * 3)

        room_circle = Circle(radius=2.5, stroke_color=GREY_3B, stroke_width=1.5, stroke_opacity=0.4)
        room_circle.move_to(people.get_center())

        count_label = MathTex("23", font_size=48, color=BLUE_3B)
        count_label.move_to(people.get_center())
        count_sub = Text("people", font_size=22, color=GREY_3B)
        count_sub.next_to(count_label, DOWN, buff=0.1)

        # Question
        question = Text(
            "What are the chances\nthat at least two share\nthe exact same birthday?",
            font_size=26, color=SOFT_WHITE, line_spacing=1.4
        )
        question.move_to(RIGHT * 3 + UP * 1.5)

        # Options appearing one by one, then highlight answer
        opt_a = MathTex(r"\sim 1\%", font_size=36, color=GREY_3B)
        opt_b = MathTex(r"\sim 10\%", font_size=36, color=GREY_3B)
        opt_c = MathTex(r"> 50\%", font_size=36, color=GREY_3B)
        options = VGroup(opt_a, opt_b, opt_c).arrange(DOWN, buff=0.5)
        options.move_to(RIGHT * 3 + DOWN * 1.2)

        self.play(
            Create(room_circle, run_time=1),
            LaggedStart(*[GrowFromCenter(p) for p in people], lag_ratio=0.03, run_time=1.5),
        )
        self.play(Write(count_label), FadeIn(count_sub))
        self.wait(0.5)
        self.play(Write(question, run_time=1.5))
        self.play(
            LaggedStart(
                FadeIn(opt_a, shift=LEFT * 0.3),
                FadeIn(opt_b, shift=LEFT * 0.3),
                FadeIn(opt_c, shift=LEFT * 0.3),
                lag_ratio=0.4
            )
        )
        self.wait(1)

        # Reveal: highlight C, dim others
        box_c = SurroundingRectangle(opt_c, color=YELLOW_3B, buff=0.15, stroke_width=2)
        self.play(
            Create(box_c),
            opt_a.animate.set_opacity(0.25),
            opt_b.animate.set_opacity(0.25),
        )

        # Draw lines between random pairs to hint at why
        pair_lines = VGroup()
        np.random.seed(7)
        indices = list(range(23))
        for _ in range(12):
            i, j = np.random.choice(indices, 2, replace=False)
            line = Line(
                people[i].get_center(), people[j].get_center(),
                stroke_color=YELLOW_3B, stroke_width=1, stroke_opacity=0.3
            )
            pair_lines.add(line)

        self.play(LaggedStart(*[Create(l) for l in pair_lines], lag_ratio=0.05, run_time=1.5))

        punchline = Text(
            "Intuition says ~1%.  The math says > 50%.",
            font_size=24, color=RED_3B
        )
        punchline.to_edge(DOWN, buff=0.6)
        self.play(Write(punchline))
        self.wait(2)

        # Transition: zoom into "why?"
        why = Text("Why?", font_size=72, color=YELLOW_3B, weight=BOLD)
        self.play(
            *[FadeOut(m) for m in self.mobjects if m != why],
            run_time=0.6
        )
        self.play(Write(why))
        self.wait(1)
        self.play(FadeOut(why, scale=2, run_time=0.8))

    # ─────────────────────────────────────────────────────────────
    #  3. PEBBLE WORLD
    # ─────────────────────────────────────────────────────────────
    def scene_pebble_world(self):
        title = section_title("Welcome to Pebble World")
        title.to_edge(UP, buff=0.5)
        self.play(Write(title[0]), GrowFromEdge(title[1], LEFT), run_time=1.5)
        self.wait(0.5)

        # Shift the entire diagram left to leave room for the text on the right
        left_shift = LEFT * 1.5

        # Sample space S — a subtle rounded rectangle with a faint background fill
        s_box = RoundedRectangle(
            corner_radius=0.15, width=8, height=5, 
            stroke_color=GREY_3B, stroke_width=2, stroke_opacity=0.6,
            fill_color=DARK_GREY, fill_opacity=0.2
        )
        s_box.move_to(DOWN * 0.3 + left_shift)
        s_label = MathTex("S", font_size=36, color=SOFT_WHITE)
        s_label.next_to(s_box, UL, buff=0.1)

        # 9 pebbles arranged loosely
        np.random.seed(42)
        pebbles = VGroup()
        positions = [
            [-2.5, 1.0], [-1.0, 1.2], [0.5, 0.9],
            [-3.0, -0.3], [-1.2, -0.1], [0.8, -0.2],
            [-2.3, -1.5], [-0.5, -1.6], [1.2, -1.4],
        ]
        
        for x, y in positions:
            # Start pebbles dim/grey
            p = Pebble(color=DARK_GREY, radius=0.18)
            p.move_to([x, y - 0.3, 0])
            pebbles.add(p)
            
        pebbles.shift(left_shift)

        self.play(Create(s_box), Write(s_label))
        self.play(LaggedStart(*[GrowFromCenter(p) for p in pebbles], lag_ratio=0.06), run_time=1.5)

        # Define sample space neatly in a "sidebar" format
        s_def = VGroup(
            Text("Sample Space (S):", font_size=24, color=SOFT_WHITE, weight=BOLD),
            Text("The set of all possible outcomes.", font_size=20, color=GREY_3B),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        s_def.next_to(s_box, RIGHT, buff=0.8).align_to(s_box, UP).shift(DOWN * 0.5 + LEFT * 0.5)

        self.play(FadeIn(s_def, shift=LEFT * 0.3))
        self.wait(1)

        # Event A — ellipse with a subtle blue fill
        event_a = Ellipse(width=6.5, height=2.8, color=BLUE_3B, stroke_width=2.5, fill_opacity=0.1)
        event_a.move_to([-0.8, 0.3, 0]).shift(left_shift)
        a_label = MathTex("A", font_size=32, color=BLUE_3B)
        a_label.next_to(event_a, UR, buff=-0.4)

        a_def = VGroup(
            Text("Event (A):", font_size=24, color=BLUE_3B, weight=BOLD),
            Text("A subset of the sample space.", font_size=20, color=GREY_3B),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        a_def.next_to(s_def, DOWN, buff=0.8).align_to(s_def, LEFT)

        self.play(Create(event_a, run_time=1.5), Write(a_label))
        self.play(FadeIn(a_def, shift=LEFT * 0.3))

        # Light up pebbles inside A (changes their color to blue)
        in_a = pebbles[:6]
        self.play(
            *[p.animate.set_color(BLUE_3B) for p in in_a],
            run_time=0.8
        )

        # Event B — dashed ellipse overlapping, also with a subtle fill
        b_border = Ellipse(width=4.5, height=3.5, color=GOLD_3B, stroke_width=2)
        b_border.set_stroke(opacity=0.7)
        dash = DashedVMobject(b_border, num_dashes=35)
        
        # To fill a dashed object nicely, we put a borderless filled ellipse behind it
        b_fill = Ellipse(width=4.5, height=3.5, color=GOLD_3B, fill_opacity=0.1, stroke_width=0)
        
        event_b = VGroup(b_fill, dash)
        event_b.move_to([1.0, -0.6, 0]).shift(left_shift)
        
        b_label = MathTex("B", font_size=32, color=GOLD_3B)
        b_label.next_to(event_b, DR, buff=-0.3)

        self.play(Create(dash, run_time=1.5), FadeIn(b_fill), Write(b_label))
        self.wait(2)
        self.clear()

    # ─────────────────────────────────────────────────────────────
    #  4. NAIVE DEFINITION
    # ─────────────────────────────────────────────────────────────
    def scene_naive_definition(self):
        title = section_title("The Naive Definition")
        title.to_edge(UP, buff=0.5)
        self.play(Write(title[0]), GrowFromEdge(title[1], LEFT))

        # Build up the formula step by step
        frac = MathTex(
            r"P_{\text{naive}}(A)", r"=",
            r"\frac{|A|}{|S|}",
            font_size=52, color=SOFT_WHITE
        )
        frac.shift(UP * 0.8)

        self.play(Write(frac, run_time=2))
        self.wait(0.5)

        # Visual: 9 pebbles — 5 blue (in A), 4 grey (not in A)
        pebbles = VGroup()
        for i in range(9):
            color = BLUE_3B if i < 5 else DARK_GREY
            p = Pebble(color=color, radius=0.2, glow=(i < 5))
            pebbles.add(p)
        pebbles.arrange(RIGHT, buff=0.35)
        pebbles.shift(DOWN * 0.8)

        self.play(LaggedStart(*[GrowFromCenter(p) for p in pebbles], lag_ratio=0.06), run_time=1.2)

        # Braces
        fav = VGroup(*pebbles[:5])
        brace_fav = brace_label(fav, r"|A| = 5", UP, BLUE_3B, 26)
        brace_tot = brace_label(pebbles, r"|S| = 9", DOWN, SOFT_WHITE, 26)

        self.play(GrowFromEdge(brace_fav[0], LEFT), Write(brace_fav[1]))
        self.play(GrowFromEdge(brace_tot[0], LEFT), Write(brace_tot[1]))

        # Result
        result = MathTex(r"= \frac{5}{9}", font_size=52, color=YELLOW_3B)
        result.next_to(frac, RIGHT, buff=0.4)
        self.play(Write(result))
        self.wait(1)

        caveat = Text(
            "Requires a finite sample space where every pebble has equal mass.",
            font_size=20, color=RED_3B
        )
        
        caveat.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(caveat, shift=UP * 0.2))
        self.wait(2)
        self.clear()

    # ─────────────────────────────────────────────────────────────
    #  5. THE 50-50 FALLACY
    # ─────────────────────────────────────────────────────────────
    def scene_fifty_fifty_fallacy(self):
        title = section_title("Mental Trap: The 50-50 Fallacy")
        title.to_edge(UP, buff=0.5)
        self.play(Write(title[0]), GrowFromEdge(title[1], LEFT))

        # 1. Enhanced typography for the absurd claim
        claim = Tex(
            "``Life on Mars? It either is or isn't.\\\\",
            "So ", "$P = \\frac{1}{2}$", ".''",
            font_size=32, color=SOFT_WHITE
        )
        claim[2].set_color(YELLOW_3B) # Highlight the core assumption
        claim.shift(UP * 1.2)
        self.play(FadeIn(claim, shift=UP * 0.2, run_time=1.5))
        self.wait(0.5)

        # 2. Scale animation: two perfectly symmetric circles
        left_blob = Circle(radius=1.2, color=BLUE_3B, fill_opacity=0.2, stroke_width=3)
        left_blob.move_to(LEFT * 2.8 + DOWN * 0.8)
        left_label = Text("Life", font_size=28, color=BLUE_3B).move_to(left_blob)

        right_blob = Circle(radius=1.2, color=GREY_3B, fill_opacity=0.2, stroke_width=3)
        right_blob.move_to(RIGHT * 2.8 + DOWN * 0.8)
        right_label = Text("No Life", font_size=28, color=GREY_3B).move_to(right_blob)

        eq_sign = MathTex(r"\stackrel{?}{=}", font_size=48, color=YELLOW_3B)
        eq_sign.move_to(DOWN * 0.8)

        self.play(
            GrowFromCenter(left_blob), Write(left_label),
            GrowFromCenter(right_blob), Write(right_label),
            Write(eq_sign),
        )
        self.wait(1)

        # 3. The elegant cross-out (just the equal sign)
        cross = Cross(eq_sign, stroke_color=RED_3B, stroke_width=6, scale_factor=1.2)
        self.play(Create(cross, run_time=0.6))
        
        # 4. Show, don't just tell: Break the symmetry visually!
        self.play(
            left_blob.animate.scale(0.3).set_color(RED_3B),
            left_label.animate.scale(0.4).set_color(RED_3B),
            right_blob.animate.scale(1.3),
            right_label.animate.scale(1.2),
            run_time=1.5, rate_func=there_and_back_with_pause
        )
        # (It reverts to original size after the pause to make room for the bottom text)

        # 5. The reality text
        reality = Text(
            "The naive definition only applies with true physical symmetry.",
            font_size=22, color=BLUE_3B, weight=BOLD
        )
        reality.to_edge(DOWN, buff=0.5)

        # 6. Polished, visually appealing symmetric objects
        # High-quality Coin
        coin_bg = Circle(radius=0.45, color=GOLD_3B, fill_opacity=0.2, stroke_width=3)
        coin_inner = Circle(radius=0.35, color=GOLD_3B, stroke_width=1)
        coin_h = Text("H", font_size=22, color=GOLD_3B).move_to(coin_bg)
        coin = VGroup(coin_bg, coin_inner, coin_h)

        # High-quality Die
        die_bg = RoundedRectangle(
            corner_radius=0.15, width=0.9, height=0.9, 
            color=TEAL_3B, fill_opacity=0.2, stroke_width=3
        )
        die_dots = VGroup(*[
            Dot(radius=0.06, color=TEAL_3B).move_to(die_bg.get_center() + d)
            for d in [UL * 0.22, ORIGIN, DR * 0.22]
        ])
        die = VGroup(die_bg, die_dots)

        sym_group = VGroup(coin, die).arrange(RIGHT, buff=1.5)
        sym_group.next_to(reality, UP, buff=0.4)

        self.play(
            FadeOut(cross), FadeOut(eq_sign),
            left_blob.animate.shift(UP * 0.5).set_opacity(0.1),
            right_blob.animate.shift(UP * 0.5).set_opacity(0.1),
            left_label.animate.shift(UP * 0.5).set_opacity(0.2),
            right_label.animate.shift(UP * 0.5).set_opacity(0.2),
            run_time=1
        )
        self.play(
            FadeIn(sym_group, shift=UP * 0.2), 
            Write(reality),
            run_time=1.2
        )
        self.wait(2.5)
        self.clear()

    # ─────────────────────────────────────────────────────────────
    #  6. LEIBNIZ'S DICE MISTAKE
    # ─────────────────────────────────────────────────────────────
    def scene_leibniz_dice(self):
        title = section_title("Leibniz's Dice Mistake")
        title.to_edge(UP, buff=0.5)
        self.play(Write(title[0]), GrowFromEdge(title[1], LEFT))

        question = MathTex(
            r"\text{Are sums of 11 and 12 equally likely with two dice?}",
            font_size=28, color=GREY_3B
        )
        question.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(question))

        # WRONG reasoning: unlabelled
        wrong_header = Text("Unlabelled (wrong)", font_size=22, color=RED_3B, weight=BOLD)
        wrong_header.shift(LEFT * 3.5 + UP * 0.3)

        wrong_11 = MathTex(r"11: \{5,6\}", font_size=28, color=SOFT_WHITE)
        wrong_12 = MathTex(r"12: \{6,6\}", font_size=28, color=SOFT_WHITE)
        wrong_conc = MathTex(r"\Rightarrow P = \tfrac{1}{36} \text{ each}",
                             font_size=28, color=RED_3B)
        wrong_group = VGroup(wrong_11, wrong_12, wrong_conc).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        wrong_group.next_to(wrong_header, DOWN, buff=0.3)

        self.play(Write(wrong_header))
        self.play(LaggedStart(*[Write(m) for m in wrong_group], lag_ratio=0.4), run_time=1.5)
        self.wait(1)

        # Arrow
        arrow = MathTex(r"\longrightarrow", font_size=48, color=YELLOW_3B).move_to(ORIGIN)
        fix_text = Text("Label the dice!", font_size=20, color=YELLOW_3B, weight=BOLD)
        fix_text.next_to(arrow, UP, buff=0.15)
        self.play(Write(arrow), Write(fix_text))

        # CORRECT: labelled
        right_header = Text("Labelled (correct)", font_size=22, color=GREEN_3B, weight=BOLD)
        right_header.shift(RIGHT * 3.5 + UP * 0.3)

        # Die A and B as colored squares
        die_a = Square(side_length=0.5, color=BLUE_3B, fill_opacity=0.3, stroke_width=2)
        die_a_label = Text("A", font_size=16, color=BLUE_3B).move_to(die_a)
        die_b = Square(side_length=0.5, color=GOLD_3B, fill_opacity=0.3, stroke_width=2)
        die_b_label = Text("B", font_size=16, color=GOLD_3B).move_to(die_b)
        dice_display = VGroup(VGroup(die_a, die_a_label), VGroup(die_b, die_b_label))
        dice_display.arrange(RIGHT, buff=0.3)
        dice_display.next_to(right_header, DOWN, buff=0.3)

        right_11a = MathTex(r"11:", r"\; (A{=}5, B{=}6)", font_size=24, color=SOFT_WHITE)
        right_11b = MathTex(r"(A{=}6, B{=}5)", font_size=24, color=SOFT_WHITE)
        right_11b.next_to(right_11a, DOWN, aligned_edge=LEFT, buff=0.15).shift(RIGHT * 0.5)
        right_12 = MathTex(r"12:", r"\; (A{=}6, B{=}6)", font_size=24, color=SOFT_WHITE)
        right_12.next_to(right_11b, DOWN, aligned_edge=LEFT, buff=0.3).shift(LEFT * 0.5)

        right_stuff = VGroup(right_11a, right_11b, right_12)
        right_stuff.next_to(dice_display, DOWN, buff=0.3)

        conclusion = MathTex(
            r"\Rightarrow \text{11 is \textbf{twice} as likely!}",
            font_size=28, color=GREEN_3B
        )
        conclusion.next_to(right_stuff, DOWN, buff=0.4)

        self.play(Write(right_header))
        self.play(FadeIn(dice_display))
        self.play(Write(right_11a), Write(right_11b))
        self.play(Write(right_12))
        self.play(Write(conclusion))
        self.wait(2.5)
        self.clear()

    # ─────────────────────────────────────────────────────────────
    #  7. THE PROBLEM OF SCALE
    # ─────────────────────────────────────────────────────────────
    def scene_problem_of_scale(self):
        title = section_title("The Problem of Scale")
        title.to_edge(UP, buff=0.5)
        self.play(Write(title[0]), GrowFromEdge(title[1], LEFT))

        # Replaced SVG card with a basic rounded rectangle
        card = RoundedRectangle(corner_radius=0.1, width=0.9, height=1.3, color=DARK_GREY, fill_opacity=0.2)
        card.shift(LEFT * 4.5 + UP * 1)
        
        label_52 = Text("52-card deck", font_size=22, color=GREY_3B)
        label_52.next_to(card, DOWN, buff=0.2)

        self.play(FadeIn(card), FadeIn(label_52))
        self.wait(0.5)

        # Exponential explosion — spawn dots
        dots = VGroup()
        np.random.seed(10)
        for _ in range(200):
            d = Dot(
                radius=np.random.uniform(0.015, 0.06),
                color=interpolate_color(ManimColor(BLUE_3B), ManimColor(DARK_GREY), np.random.random()),
                fill_opacity=np.random.uniform(0.3, 0.8),
            )
            d.move_to([np.random.uniform(-4, 4), np.random.uniform(-3, -0.5), 0])
            dots.add(d)

        self.play(
            LaggedStart(*[FadeIn(d, scale=0.1) for d in dots], lag_ratio=0.003),
            run_time=2.5
        )

        # Count
        count = MathTex(r"2^{52}", r"\approx 4.5 \times 10^{15}", font_size=44, color=YELLOW_3B)
        count_label = Text("possible events", font_size=24, color=SOFT_WHITE)
        count_group = VGroup(count, count_label).arrange(DOWN, buff=0.2)
        count_group.shift(RIGHT * 3 + UP * 1)
        self.play(Write(count, run_time=1.5), FadeIn(count_label))
        self.wait(1)

        # CTA
        cta = Text(
            "We cannot count pebbles individually.\nWe must learn How to Count using combinatorics.",
            font_size=22, color=BLUE_3B, line_spacing=1.4, weight=BOLD
        )
        cta.to_edge(DOWN, buff=0.5)
        box = SurroundingRectangle(cta, color=BLUE_3B, stroke_width=1.5, buff=0.2, corner_radius=0.1)
        self.play(Write(cta), Create(box))
        self.wait(2)
        self.clear()

    # ─────────────────────────────────────────────────────────────
    #  8. THE MULTIPLICATION RULE
    # ─────────────────────────────────────────────────────────────
    def scene_multiplication_rule(self):
        title = section_title("The Multiplication Rule")
        title.to_edge(UP, buff=0.5)
        self.play(Write(title[0]), GrowFromEdge(title[1], LEFT))

        # 1. Formula
        rule = MathTex(
            r"a", r"\text{ outcomes}", r"\times",
            r"b", r"\text{ outcomes}", r"=",
            r"a \cdot b", r"\text{ total}",
            font_size=36, color=SOFT_WHITE
        )
        rule[0].set_color(BLUE_3B)
        rule[3].set_color(GOLD_3B)
        rule[6].set_color(GREEN_3B)
        rule.next_to(title, DOWN, buff=0.6)
        self.play(FadeIn(rule, shift=UP * 0.2))

        # 2. Helper function for organic flowing branches
        def create_branch(start, end, color):
            # Calculate control points for an S-curve
            dist = end[0] - start[0]
            ctrl_pt1 = start + RIGHT * (dist * 0.5)
            ctrl_pt2 = end + LEFT * (dist * 0.5)
            return CubicBezier(
                start, ctrl_pt1, ctrl_pt2, end, 
                stroke_color=color, stroke_width=3, stroke_opacity=0.7
            )

        # 3. Helper function for luminous glowing nodes
        def create_node(pos, color, radius=0.12):
            core = Dot(pos, radius=radius, color=color)
            glow1 = Dot(pos, radius=radius*2.5, color=color, fill_opacity=0.25, stroke_width=0)
            glow2 = Dot(pos, radius=radius*4.5, color=color, fill_opacity=0.08, stroke_width=0)
            return VGroup(glow2, glow1, core)

        # Tree layout parameters
        root_pos = LEFT * 5 + DOWN * 1.5
        root_node = create_node(root_pos, SOFT_WHITE, radius=0.1)
        
        cones = ["Cake", "Waffle"]
        flavors = ["Chocolate", "Vanilla", "Strawberry"]
        
        cone_x = -1.5
        cone_ys = [0.5, -2.2]
        
        flav_x = 2.0
        flav_y_offsets = [0.8, 0, -0.8]

        # Groups for staged animations
        l1_lines = VGroup()
        l1_nodes = VGroup()
        l2_lines = VGroup()
        l2_nodes = VGroup()
        
        # We will add both the dot AND the text to this group so the brace clears everything
        right_side_elements = VGroup() 

        for i, (cone, cy) in enumerate(zip(cones, cone_ys)):
            cone_pos = np.array([cone_x, cy, 0])
            c_node = create_node(cone_pos, BLUE_3B)
            
            c_text = Text(cone, font_size=26, color=SOFT_WHITE)
            # Position text above the top node and below the bottom node
            c_text.next_to(c_node, UP if i == 0 else DOWN, buff=0.2)
            
            c_line = create_branch(root_pos, cone_pos, BLUE_3B)
            
            l1_lines.add(c_line)
            l1_nodes.add(VGroup(c_node, c_text))

            for j, (flavor, fy_off) in enumerate(zip(flavors, flav_y_offsets)):
                fy = cy + fy_off
                flav_pos = np.array([flav_x, fy, 0])
                
                f_node = create_node(flav_pos, GREEN_3B)
                f_text = Text(flavor, font_size=22, color=SOFT_WHITE).next_to(f_node, RIGHT, buff=0.3)
                
                f_line = create_branch(cone_pos, flav_pos, GOLD_3B)
                
                # Add to animation groups
                l2_lines.add(f_line)
                flavor_group = VGroup(f_node, f_text)
                l2_nodes.add(flavor_group)
                
                # Add the entire flavor group (dot + text) to the brace target
                right_side_elements.add(flavor_group)

        # 4. Sequence the animations smoothly
        self.play(FadeIn(root_node, scale=0.5))
        
        # Level 1 (Cones)
        self.play(LaggedStart(*[Create(l) for l in l1_lines], lag_ratio=0.2), run_time=1.2)
        self.play(FadeIn(l1_nodes, shift=RIGHT * 0.2), run_time=0.8)
        
        # Level 2 (Flavors)
        self.play(LaggedStart(*[Create(l) for l in l2_lines], lag_ratio=0.08), run_time=1.5)
        self.play(FadeIn(l2_nodes, shift=RIGHT * 0.2), run_time=1)

        # 5. Attach the brace to the outermost elements
        br = Brace(right_side_elements, RIGHT, color=GREEN_3B, buff=0.2)
        br_tex = MathTex(r"2 \times 3 = 6", font_size=42, color=GREEN_3B)
        br_tex.next_to(br, RIGHT, buff=0.2)
        
        self.play(GrowFromEdge(br, UP), Write(br_tex))
        self.wait(3)
        self.clear()

    # ─────────────────────────────────────────────────────────────
    #  9. OVERCOUNTING
    # ─────────────────────────────────────────────────────────────
    def scene_overcounting(self):
        title = section_title("Adjusting for Overcounting")
        title.to_edge(UP, buff=0.5)
        self.play(Write(title[0]), GrowFromEdge(title[1], LEFT))

        # Explanation
        expl = Text(
            "Choosing a 2-person team from 4:\nordering gives 12, but (1,2) = (2,1).",
            font_size=22, color=GREY_3B, line_spacing=1.3
        )
        expl.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(expl))

        # Ordered pairs
        ordered_labels = [
            "(1,2)", "(2,1)", "(1,3)", "(3,1)",
            "(1,4)", "(4,1)", "(2,3)", "(3,2)",
            "(2,4)", "(4,2)", "(3,4)", "(4,3)"
        ]
        ordered = VGroup()
        for label in ordered_labels:
            box = VGroup(
                RoundedRectangle(width=0.85, height=0.5, corner_radius=0.05,
                                 stroke_color=GREY_3B, stroke_width=1,
                                 fill_color=DARK_GREY, fill_opacity=0.4),
                Text(label, font_size=14, color=SOFT_WHITE)
            )
            ordered.add(box)
        ordered.arrange_in_grid(rows=3, cols=4, buff=0.12)
        ordered.shift(LEFT * 3.2 + DOWN * 1.2)

        self.play(LaggedStart(*[FadeIn(b, scale=0.7) for b in ordered], lag_ratio=0.03), run_time=1)

        # Highlight duplicate pairs with brackets
        pair_highlights = VGroup()
        for i in range(0, 12, 2):
            rect = SurroundingRectangle(
                VGroup(ordered[i], ordered[i + 1]),
                color=BLUE_3B, stroke_width=1.5, buff=0.05, corner_radius=0.05
            )
            pair_highlights.add(rect)

        self.play(LaggedStart(*[Create(r) for r in pair_highlights], lag_ratio=0.08), run_time=1)

        # Arrow: divide by 2!
        arrow = Arrow(LEFT * 0.8 + DOWN * 1.2, RIGHT * 0.8 + DOWN * 1.2,
                      color=YELLOW_3B, stroke_width=3, buff=0)
        arrow_label = MathTex(r"\div 2!", font_size=32, color=YELLOW_3B)
        arrow_label.next_to(arrow, UP, buff=0.15)
        self.play(GrowArrow(arrow), Write(arrow_label))

        # Unordered sets
        sets_labels = ["{1,2}", "{1,3}", "{1,4}", "{2,3}", "{2,4}", "{3,4}"]
        unordered = VGroup()
        for label in sets_labels:
            box = VGroup(
                RoundedRectangle(width=0.85, height=0.5, corner_radius=0.05,
                                 stroke_color=BLUE_3B, stroke_width=1.5,
                                 fill_color=BLUE_3B, fill_opacity=0.1),
                Text(label, font_size=14, color=BLUE_3B)
            )
            unordered.add(box)
        unordered.arrange_in_grid(rows=2, cols=3, buff=0.12)
        unordered.shift(RIGHT * 3.2 + DOWN * 1.2)

        self.play(LaggedStart(*[FadeIn(b, scale=0.7) for b in unordered], lag_ratio=0.05), run_time=1)

        # Principle
        principle = MathTex(
            r"\text{If every outcome is counted } c \text{ times, divide by } c.",
            font_size=26, color=YELLOW_3B
        )
        principle.to_edge(DOWN, buff=0.5)
        self.play(Write(principle))
        self.wait(2.5)
        self.clear()

    # ─────────────────────────────────────────────────────────────
    #  10. THE BINOMIAL COEFFICIENT
    # ─────────────────────────────────────────────────────────────
    def scene_binomial_coefficient(self):
        title = section_title("The Binomial Coefficient")
        title.to_edge(UP, buff=0.5)
        self.play(Write(title[0]), GrowFromEdge(title[1], LEFT))

        desc = Text(
            "Choose k items from n, order doesn't matter, no replacement.",
            font_size=22, color=GREY_3B
        )
        desc.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(desc))

        # Build formula in stages
        step1 = MathTex(r"\frac{n!}{(n-k)!}", font_size=52, color=SOFT_WHITE)
        step1_note = Text("pick k (ordered)", font_size=18, color=GREY_3B)
        step1_note.next_to(step1, DOWN, buff=0.2)
        step1_group = VGroup(step1, step1_note)

        self.play(Write(step1), FadeIn(step1_note))
        self.wait(1)

        # Divide by k!
        step2 = MathTex(r"\frac{n!}{(n-k)! \cdot", r"k!", r"}", font_size=52, color=SOFT_WHITE)
        step2[1].set_color(YELLOW_3B)

        erase_label = Text("÷ k!  to erase order", font_size=18, color=YELLOW_3B)

        self.play(
            ReplacementTransform(step1, step2),
            FadeOut(step1_note),
            run_time=1.5
        )
        erase_label.next_to(step2[1], DOWN, buff=0.3)
        arr = Arrow(erase_label.get_top(), step2[1].get_bottom(),
                    color=YELLOW_3B, stroke_width=2, buff=0.05, max_tip_length_to_length_ratio=0.15)
        self.play(Write(erase_label), Create(arr))
        self.wait(1)

        # Final form
        binom = MathTex(r"\binom{n}{k}", r"=", r"\frac{n!}{(n-k)! \cdot k!}",
                        font_size=52, color=SOFT_WHITE)
        binom[0].set_color(BLUE_3B)
        binom.shift(DOWN * 0.5)

        self.play(
            FadeOut(erase_label), FadeOut(arr),
            ReplacementTransform(step2, binom[2]),
            Write(binom[0]), Write(binom[1]),
            run_time=1.5
        )

        # Glow effect on binom
        glow_rect = SurroundingRectangle(
            binom, color=BLUE_3B, stroke_width=2, buff=0.25, corner_radius=0.15
        )
        self.play(Create(glow_rect))
        self.wait(2.5)
        self.clear()

    # ─────────────────────────────────────────────────────────────
    #  11. THE MASTER COUNTING MATRIX
    # ─────────────────────────────────────────────────────────────
    def scene_counting_matrix(self):
        title = section_title("The Master Counting Matrix")
        title.to_edge(UP, buff=0.5)
        self.play(Write(title[0]), GrowFromEdge(title[1], LEFT))

        # Build the 2x2 grid data
        table_data = [
            [
                (r"n^k", "Mult. Rule", "(Passwords)", BLUE_3B),
                (r"\frac{n!}{(n-k)!}", "Permutations", "(Races)", GOLD_3B),
            ],
            [
                (r"\binom{n}{k}", "Binomial Coeff.", "(Committees)", GREEN_3B),
                (r"\binom{n+k-1}{k}", "Bose-Einstein", "(Particles)", PINK_3B),
            ],
        ]

        # 1. Create colored background panels for the 4 quadrants
        panels = VGroup()
        for i in range(2):
            for j in range(2):
                accent = table_data[i][j][3]
                panel = RoundedRectangle(
                    width=4.5, height=2.6, corner_radius=0.15,
                    fill_color=accent, fill_opacity=0.08,
                    stroke_color=accent, stroke_opacity=0.4, stroke_width=2
                )
                panels.add(panel)
        
        # Automatically align them into a neat grid
        panels.arrange_in_grid(rows=2, cols=2, buff=0.25)
        # Shift slightly right to make room for the row headers on the left
        panels.next_to(title, DOWN, buff=1.0).shift(RIGHT * 0.8)

        # 2. Create Row Headers
        row_headers = VGroup(
            Text("Order\nMatters", font_size=20, color=SOFT_WHITE, weight=BOLD, line_spacing=1.2),
            Text("Order\nDoesn't\nMatter", font_size=20, color=SOFT_WHITE, weight=BOLD, line_spacing=1.2)
        )
        # Align them to the left of the corresponding rows
        row_headers[0].move_to([panels.get_left()[0] - 1.2, panels[0].get_y(), 0])
        row_headers[1].move_to([panels.get_left()[0] - 1.2, panels[2].get_y(), 0])

        # 3. Create Column Headers
        col_headers = VGroup(
            Text("With Replacement", font_size=22, color=SOFT_WHITE, weight=BOLD),
            Text("Without Replacement", font_size=22, color=SOFT_WHITE, weight=BOLD)
        )
        # Align them above the corresponding columns
        col_headers[0].move_to([panels[0].get_x(), panels.get_top()[1] + 0.5, 0])
        col_headers[1].move_to([panels[1].get_x(), panels.get_top()[1] + 0.5, 0])

        # Animate headers and the grid structure first
        self.play(
            FadeIn(row_headers, shift=RIGHT * 0.2),
            FadeIn(col_headers, shift=DOWN * 0.2)
        )
        self.play(LaggedStart(*[Create(p) for p in panels], lag_ratio=0.1), run_time=1.5)

        # 4. Fill cells with high-contrast text and math
        cells = VGroup()
        for i in range(2):
            for j in range(2):
                idx = i * 2 + j
                formula_str, name, example, accent = table_data[i][j]
                
                # Make the math significantly larger
                f = MathTex(formula_str, font_size=48, color=accent)
                # Differentiate the name and example via weight and slant
                n = Text(name, font_size=18, color=SOFT_WHITE, weight=BOLD)
                e = Text(example, font_size=16, color=GREY_3B, slant=ITALIC)
                
                cell_content = VGroup(f, n, e).arrange(DOWN, buff=0.15)
                cell_content.move_to(panels[idx].get_center())
                cells.add(cell_content)

        # Pop the formulas in with a satisfying cascade
        self.play(LaggedStart(
            *[FadeIn(c, shift=UP * 0.2) for c in cells],
            lag_ratio=0.2
        ), run_time=2)
        
        self.wait(3)
        self.clear()

    # ─────────────────────────────────────────────────────────────
    #  12. STORY PROOFS
    # ─────────────────────────────────────────────────────────────
    def scene_story_proof(self):
        title = section_title("Story Proofs")
        title.to_edge(UP, buff=0.5)
        self.play(Write(title[0]), GrowFromEdge(title[1], LEFT))

        subtitle = Text("Proof by Interpretation", font_size=24, color=GREY_3B, slant=ITALIC)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(subtitle, shift=UP * 0.2))

        # Identity Equation
        identity = MathTex(
            r"\binom{n}{k}", r"=", r"\binom{n}{n-k}",
            font_size=64, color=SOFT_WHITE
        )
        identity[0].set_color(BLUE_3B)
        identity[2].set_color(GOLD_3B)
        identity.shift(UP * 0.5)
        self.play(Write(identity, run_time=2))
        self.wait(1)

        # Story: n people represented as dots
        people = VGroup()
        n_people = 7
        for i in range(n_people):
            # Fallback to standard Dot if Pebble class is acting up, 
            # but assuming Pebble works as defined in your setup:
            p = Pebble(color=GREY_3B, radius=0.15, glow=False)
            people.add(p)
        
        people.arrange(RIGHT, buff=0.6)
        people.shift(DOWN * 1.8)

        self.play(LaggedStart(*[GrowFromCenter(p) for p in people], lag_ratio=0.08))
        self.wait(0.5)

        # Indices for the two groups
        committee_indices = [1, 3, 5]
        left_behind_indices = [0, 2, 4, 6]
        
        comm_group = VGroup(*[people[i] for i in committee_indices])
        lb_group = VGroup(*[people[i] for i in left_behind_indices])

        # Action 1: Select k=3 for committee by shifting them UP
        self.play(
            comm_group.animate.shift(UP * 1.2).set_color(BLUE_3B),
            run_time=1.2, rate_func=smooth
        )

        # Brace and label for the Committee (now with plenty of space)
        comm_brace = Brace(comm_group, DOWN, color=BLUE_3B, buff=0.2)
        comm_label = Text("Committee (k)", font_size=20, color=BLUE_3B)
        comm_label.next_to(comm_brace, DOWN, buff=0.1)

        self.play(GrowFromEdge(comm_brace, LEFT), Write(comm_label))
        self.wait(0.8)

        # Action 2: Highlight the ones left behind
        self.play(
            lb_group.animate.set_color(GOLD_3B),
            run_time=0.8
        )

        # Brace and label for Left Behind
        lb_brace = Brace(lb_group, DOWN, color=GOLD_3B, buff=0.2)
        lb_label = Text("Left behind (n−k)", font_size=20, color=GOLD_3B)
        lb_label.next_to(lb_brace, DOWN, buff=0.1)

        self.play(GrowFromEdge(lb_brace, LEFT), Write(lb_label))
        self.wait(1)

        # Final Insight
        insight = Text(
            "Choosing who's IN is the same as choosing who's OUT.",
            font_size=24, color=YELLOW_3B, weight=BOLD
        )
        insight.to_edge(DOWN, buff=0.5)
        
        # Add a subtle background to the text so it pops out from the braces
        insight_bg = SurroundingRectangle(
            insight, color=DARK_BG, fill_opacity=0.8, stroke_width=0, buff=0.2
        )
        
        self.play(FadeIn(insight_bg), Write(insight))
        self.wait(3)
        self.clear()

    # ─────────────────────────────────────────────────────────────
    #  13. SOLVING THE BIRTHDAY PROBLEM — COMPLEMENT
    # ─────────────────────────────────────────────────────────────
    def scene_solving_birthday(self):
        title = section_title("Solving the Birthday Illusion")
        title.to_edge(UP, buff=0.5)
        self.play(Write(title[0]), GrowFromEdge(title[1], LEFT))

        # 1. Emphasize the word "nightmare" using Tex
        messy = Tex(
            'Counting "at least one match" is a ', 'nightmare', '.',
            font_size=32, color=SOFT_WHITE
        )
        messy[1].set_color(RED_3B)
        messy.next_to(title, DOWN, buff=0.6)
        self.play(Write(messy))

        # 2. Build a "Complete Graph" to show combinatorial explosion
        # Place 18 dots in a circle to represent people
        n_nodes = 18
        nodes = VGroup(*[
            Dot(radius=0.06, color=GREY_3B).move_to(
                1.8 * np.array([np.cos(a), np.sin(a), 0])
            ) for a in np.linspace(0, TAU, n_nodes, endpoint=False)
        ])
        nodes.shift(DOWN * 1)

        # Generate every possible pair connection
        lines = VGroup()
        for i in range(n_nodes):
            for j in range(i + 1, n_nodes):
                lines.add(Line(
                    nodes[i].get_center(), nodes[j].get_center(),
                    stroke_width=1, stroke_opacity=0.2, color=RED_3B
                ))

        # Add a subtle red warning glow behind it
        glow = Circle(radius=2.2, color=RED_3B, fill_opacity=0.1, stroke_width=0).move_to(nodes)

        self.play(FadeIn(nodes))
        # Drawing the lines rapidly creates a feeling of overwhelming complexity
        self.play(
            LaggedStart(*[Create(l) for l in lines], lag_ratio=0.02), 
            Succession(Wait(1), FadeIn(glow)), 
            run_time=2.5
        )
        self.wait(1)

        # 3. Clear the chaos to make way for the elegant solution
        self.play(
            FadeOut(VGroup(nodes, lines, glow)),
            FadeOut(messy),
            run_time=0.8
        )

        # 4. The elegant trick — centered and prominent
        trick = Text("The elegant trick: count the complement.", font_size=32, color=BLUE_3B, weight=BOLD)
        trick.shift(UP * 0.5)
        self.play(Write(trick))

        # 5. The Formula — scaled up and placed in a clean, highlighted dashboard
        formula = MathTex(
            r"P(\text{at least 1 match})", r"=", r"1", r"-", r"P(\text{no matches})",
            font_size=46, color=SOFT_WHITE
        )
        formula[0].set_color(YELLOW_3B)
        formula[4].set_color(BLUE_3B)
        formula.next_to(trick, DOWN, buff=0.8)

        # Create a premium background box
        box = RoundedRectangle(
            width=formula.width + 1.2, height=formula.height + 0.8,
            corner_radius=0.2, fill_color=DARK_GREY, fill_opacity=0.4,
            stroke_color=YELLOW_3B, stroke_width=2, stroke_opacity=0.8
        ).move_to(formula)

        self.play(Create(box))
        self.play(Write(formula, run_time=2))
        self.wait(2.5)
        self.clear()

    # ─────────────────────────────────────────────────────────────
    #  14. THE MATH OF NO MATCHES
    # ─────────────────────────────────────────────────────────────
    def scene_math_no_matches(self):
        title = section_title("The Math of No Matches")
        title.to_edge(UP, buff=0.5)
        self.play(Write(title[0]), GrowFromEdge(title[1], LEFT))

        setup = Text("For k people, assign birthdays one by one, no overlaps.",
                      font_size=22, color=GREY_3B)
        setup.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(setup))

        # Numerator — favorable: ordered, WITHOUT replacement
        num_label = Text("Favorable outcomes", font_size=18, color=GREEN_3B)
        num_label.shift(LEFT * 2 + UP * 0.3)
        num_note = Text("(Order matters, WITHOUT replacement)", font_size=16, color=DARK_GREY)

        numerator = MathTex(
            r"365", r"\times", r"364", r"\times", r"363",
            r"\times \cdots \times", r"(365 - k + 1)",
            font_size=32, color=GREEN_3B
        )

        # Denominator — sample space: ordered, WITH replacement
        den_label = Text("Sample space", font_size=18, color=BLUE_3B)
        denominator = MathTex(r"365^k", font_size=32, color=BLUE_3B)
        den_note = Text("(Order matters, WITH replacement)", font_size=16, color=DARK_GREY)

        # Build fraction
        frac_line = Line(LEFT * 3, RIGHT * 3, stroke_color=SOFT_WHITE, stroke_width=2)

        numerator.next_to(frac_line, UP, buff=0.25)
        denominator.next_to(frac_line, DOWN, buff=0.25)
        num_label.next_to(numerator, UP, buff=0.2)
        num_note.next_to(num_label, RIGHT, buff=0.3)
        den_label.next_to(denominator, DOWN, buff=0.2)
        den_note.next_to(den_label, RIGHT, buff=0.3)

        p_no = MathTex(r"P(\text{no match}) =", font_size=32, color=SOFT_WHITE)
        p_no.next_to(frac_line, LEFT, buff=0.4)

        frac_group = VGroup(p_no, numerator, frac_line, denominator,
                            num_label, num_note, den_label, den_note)
        frac_group.move_to(DOWN * 0.3)

        self.play(Write(p_no))
        self.play(Create(frac_line))
        self.play(Write(numerator), FadeIn(num_label), FadeIn(num_note))
        self.play(Write(denominator), FadeIn(den_label), FadeIn(den_note))
        self.wait(1.5)

        # Final complement
        final = MathTex(
            r"P(\text{match}) = 1 - P(\text{no match})",
            font_size=36, color=YELLOW_3B
        )
        final.to_edge(DOWN, buff=0.5)
        box = SurroundingRectangle(final, color=YELLOW_3B, stroke_width=1.5, buff=0.15, corner_radius=0.1)
        self.play(Write(final), Create(box))
        self.wait(2)
        self.clear()

    # ─────────────────────────────────────────────────────────────
    #  15. THE TIPPING POINT — ANIMATED GRAPH
    # ─────────────────────────────────────────────────────────────
    def scene_tipping_point(self):
        title = section_title("The Tipping Point")
        title.to_edge(UP, buff=0.5)
        self.play(Write(title[0]), GrowFromEdge(title[1], LEFT))

        # 1. Shift Axes UP to avoid text collisions at the bottom
        ax = Axes(
            x_range=[0, 100, 20],
            y_range=[0, 1.05, 0.5],
            x_length=9.5,
            y_length=4.5,
            axis_config={
                "color": GREY_3B, "stroke_width": 1.5,
                "include_ticks": True, "tick_size": 0.05
            },
            x_axis_config={
                "numbers_to_include": [0, 20, 40, 60, 80, 100],
                "font_size": 20, "color": GREY_3B
            },
            y_axis_config={
                "numbers_to_include": [0, 0.5, 1.0],
                "font_size": 20, "color": GREY_3B
            },
            tips=False,
        )
        ax.shift(UP * 0.1) # Moved up for breathing room
        
        x_lab = ax.get_x_axis_label(MathTex("k", font_size=28, color=GREY_3B), direction=RIGHT)
        y_lab = Text("P(match)", font_size=20, color=GREY_3B).next_to(ax.y_axis, UP, buff=0.15)

        self.play(Create(ax, run_time=1), Write(x_lab), FadeIn(y_lab))

        # 2. Continuous exponential approximation for a buttery smooth curve
        def bp_smooth(x):
            return 1.0 - np.exp(-x * (x - 1) / (2 * 365))

        # Animate the smooth curve being drawn
        graph = ax.plot(bp_smooth, x_range=[0, 100], color=BLUE_3B, stroke_width=4)

        # 50% dashed threshold line
        dashed = DashedLine(
            ax.c2p(0, 0.5), ax.c2p(100, 0.5),
            stroke_color=GREY_3B, stroke_width=1.5, dash_length=0.1, stroke_opacity=0.6
        )
        half_label = MathTex("0.5", font_size=20, color=GREY_3B).next_to(ax.c2p(0, 0.5), LEFT, buff=0.2)

        self.play(Create(dashed), FadeIn(half_label))
        self.play(Create(graph, run_time=2.5, rate_func=smooth))

        # 3. Add visual shading to the "Danger Zone" (Probability > 50%)
        danger_zone = ax.get_area(
            graph, x_range=[23, 100], 
            color=[YELLOW_3B, TEAL_3B], opacity=0.25
        )
        self.play(FadeIn(danger_zone, run_time=1))

        # Helper function for glowing markers
        def create_glow_dot(point, color):
            core = Dot(point, radius=0.08, color=color)
            glow = Dot(point, radius=0.25, color=color, fill_opacity=0.3, stroke_width=0)
            return VGroup(glow, core)

        # k = 23 marker
        k23_val = bp_smooth(23)
        k23_pt = ax.c2p(23, k23_val)
        k23_dot = create_glow_dot(k23_pt, YELLOW_3B)
        
        k23_vline = DashedLine(ax.c2p(23, 0), k23_pt, stroke_color=YELLOW_3B, stroke_width=2, dash_length=0.08)
        k23_hline = DashedLine(ax.c2p(0, k23_val), k23_pt, stroke_color=YELLOW_3B, stroke_width=2, dash_length=0.08)
        
        k23_label = MathTex(r"k=23", font_size=22, color=YELLOW_3B).next_to(ax.c2p(23, 0), DOWN, buff=0.2).shift(DOWN * 0.3)
        prob_label = MathTex(r"\approx 50.7\%", font_size=22, color=YELLOW_3B).next_to(k23_dot, UL, buff=0.15)

        self.play(
            Create(k23_vline), Create(k23_hline),
            FadeIn(k23_dot, scale=0.5),
            Write(k23_label), Write(prob_label),
            run_time=1.5
        )

        # k = 57 marker
        k57_val = bp_smooth(57)
        k57_pt = ax.c2p(57, k57_val)
        k57_dot = create_glow_dot(k57_pt, GREEN_3B)
        
        k57_vline = DashedLine(ax.c2p(57, 0), k57_pt, stroke_color=GREEN_3B, stroke_width=2, dash_length=0.08)
        
        k57_label = MathTex(r">99\%", font_size=22, color=GREEN_3B).next_to(k57_dot, UP, buff=0.15).shift(DOWN * 0.2)
        k57_klabel = MathTex(r"k=57", font_size=22, color=GREEN_3B).next_to(ax.c2p(57, 0), DOWN, buff=0.2).shift(DOWN * 0.3)

        self.play(
            Create(k57_vline), FadeIn(k57_dot, scale=0.5),
            Write(k57_label), Write(k57_klabel),
        )

        # 4. Insight (Safely placed below the axes)
        insight = MathTex(
            r"\binom{23}{2} = 253 \text{ pairs. Our brains miss this.}",
            font_size=32, color=SOFT_WHITE
        )
        insight.to_edge(DOWN, buff=0.4).shift(DOWN * 0.2)
        
        # Add a dark background box to ensure it stands out perfectly
        insight_bg = SurroundingRectangle(
            insight, color=DARK_BG, fill_opacity=0.8, stroke_width=0, buff=0.15
        )
        
        self.play(FadeIn(insight_bg), Write(insight))
        self.wait(3)
        self.clear()

    # ─────────────────────────────────────────────────────────────
    #  16. BEYOND THE NAIVE DEFINITION
    # ─────────────────────────────────────────────────────────────
    def scene_beyond_naive(self):
        title = section_title("Beyond the Naive Definition")
        title.to_edge(UP, buff=0.5)
        self.play(Write(title[0]), GrowFromEdge(title[1], LEFT))

        # Left: uniform pebbles
        uniform = VGroup()
        for i in range(6):
            for j in range(6):
                p = Dot(radius=0.1, color=BLUE_3B, fill_opacity=0.6)
                p.move_to([-4 + j * 0.5, 0.5 - i * 0.5, 0])
                uniform.add(p)
        u_label = Text("Naive: All equal", font_size=20, color=BLUE_3B, weight=BOLD)
        u_label.next_to(uniform, UP, buff=0.3)

        # Right: variable pebbles
        varied = VGroup()
        np.random.seed(77)
        for _ in range(30):
            r = np.random.exponential(0.12) + 0.03
            r = min(r, 0.45)
            opacity = min(1, 0.3 + r * 2)
            color = interpolate_color(ManimColor(BLUE_3B), ManimColor(RED_3B), np.random.random())
            d = Dot(radius=r, color=color, fill_opacity=opacity)
            d.move_to([np.random.uniform(1.5, 5), np.random.uniform(-2.2, 0.5), 0])
            varied.add(d)
        v_label = Text("Reality: Unequal masses", font_size=20, color=RED_3B, weight=BOLD)
        v_label.next_to(varied, UP, buff=0.3)

        # Divider
        divider = DashedLine(
            UP * 1.5, DOWN * 3,
            stroke_color=GREY_3B, stroke_width=1, dash_length=0.1
        )

        self.play(Create(divider))
        self.play(
            Write(u_label),
            LaggedStart(*[GrowFromCenter(p) for p in uniform], lag_ratio=0.008),
            run_time=1.5
        )
        self.play(
            Write(v_label),
            LaggedStart(*[GrowFromCenter(d) for d in varied], lag_ratio=0.02),
            run_time=2
        )

        need = Text(
            "We need a more general framework…",
            font_size=24, color=YELLOW_3B
        )
        need.to_edge(DOWN, buff=0.5)
        self.play(Write(need))
        self.wait(2)
        self.clear()

   # ─────────────────────────────────────────────────────────────
    #  17. THE TWO AXIOMS OF PROBABILITY (Side-by-Side Redesign)
    # ─────────────────────────────────────────────────────────────
    def scene_axioms(self):
        title = section_title("The Two Axioms of Probability")
        title.to_edge(UP, buff=0.5)
        self.play(Write(title[0]), GrowFromEdge(title[1], LEFT))

        # --- Base Panels ---
        panel_kwargs = {
            "width": 6.5,
            "height": 5.5,
            "corner_radius": 0.25,
            "stroke_width": 2.5,
            "fill_opacity": 0.05
        }
        
        # Left Panel (Axiom 1)
        left_panel = RoundedRectangle(color=BLUE_3B, **panel_kwargs)
        left_panel.move_to(LEFT * 3.4 + DOWN * 0.3)
        
        # Right Panel (Axiom 2)
        right_panel = RoundedRectangle(color=GOLD_3B, **panel_kwargs)
        right_panel.move_to(RIGHT * 3.4 + DOWN * 0.3)
        
        self.play(Create(left_panel), Create(right_panel), run_time=1.5)

        # ═════════════════════════════════════════════════════════
        #  AXIOM 1 (Left Side)
        # ═════════════════════════════════════════════════════════
        ax1_header = Text("Axiom 1", font_size=36, color=BLUE_3B, weight=BOLD)
        
        # Isolate substrings for easy coloring
        ax1_formula = MathTex(
            r"\mathbb{P}(", r"\emptyset", r") = ", r"0", 
            r"\quad \text{and} \quad", 
            r"\mathbb{P}(", r"S", r") = ", r"1",
            font_size=38, color=SOFT_WHITE
        )
        ax1_formula[1].set_color(RED_3B)
        ax1_formula[3].set_color(RED_3B)
        ax1_formula[6].set_color(GREEN_3B)
        ax1_formula[8].set_color(GREEN_3B)

        ax1_desc = Text(
            "Nothing has mass 0; the entire\n"
            "universe has mass 1.",
            font_size=22, color=SOFT_WHITE, line_spacing=1.1
        )
        
        ax1_text = VGroup(ax1_header, ax1_formula, ax1_desc).arrange(DOWN, buff=0.3)
        ax1_text.move_to(left_panel.get_top() + DOWN * 1.5)

        # Visuals for Axiom 1
        empty_tex = MathTex(r"\emptyset", font_size=28, color=RED_3B)
        empty_dot = Dot(radius=0.08, color=RED_3B)
        # Add a soft glow to the empty set dot
        empty_glow = Dot(radius=0.25, color=RED_3B, fill_opacity=0.3, stroke_width=0)
        empty_zero = MathTex("0", font_size=28, color=RED_3B)
        eg = VGroup(empty_tex, VGroup(empty_glow, empty_dot), empty_zero).arrange(DOWN, buff=0.2)
        eg.move_to(left_panel.get_bottom() + UP * 1.5 + LEFT * 1.5)

        full_circle = Circle(radius=0.8, color=GREEN_3B, fill_opacity=0.2, stroke_width=2.5)
        full_glow = Circle(radius=0.8, color=GREEN_3B, fill_opacity=0.1, stroke_width=8).set_stroke(opacity=0.2)
        full_tex = MathTex("S", font_size=28, color=GREEN_3B).move_to(full_circle)
        full_one = MathTex("1", font_size=28, color=GREEN_3B).next_to(full_circle, DOWN, buff=0.2)
        fg = VGroup(VGroup(full_glow, full_circle, full_tex), full_one)
        fg.move_to(left_panel.get_bottom() + UP * 1.6 + RIGHT * 0.8)

        self.play(Write(ax1_header))
        self.play(Write(ax1_formula), FadeIn(ax1_desc), run_time=1.5)
        self.play(FadeIn(eg, shift=UP*0.2), FadeIn(fg, shift=UP*0.2), run_time=1)

        # ═════════════════════════════════════════════════════════
        #  AXIOM 2 (Right Side)
        # ═════════════════════════════════════════════════════════
        ax2_header = Text("Axiom 2", font_size=36, color=GOLD_3B, weight=BOLD)
        
        ax2_formula = MathTex(
            r"\mathbb{P}\left(\bigcup A_j\right) = \sum \mathbb{P}(A_j)",
            font_size=38, color=SOFT_WHITE
        )
        
        ax2_desc_main = Text(
            "Disjoint events: the mass of the whole\n"
            "equals the sum of the parts.",
            font_size=22, color=SOFT_WHITE, line_spacing=1.1
        )
        ax2_desc_sub = Text("(if disjoint)", font_size=18, color=GREY_3B)
        ax2_desc = VGroup(ax2_desc_main, ax2_desc_sub).arrange(DOWN, buff=0.1)
        
        ax2_text = VGroup(ax2_header, ax2_formula, ax2_desc).arrange(DOWN, buff=0.25)
        ax2_text.move_to(right_panel.get_top() + DOWN * 1.6)

        # Visuals for Axiom 2
        bA = Ellipse(width=1.3, height=1.1, color=BLUE_3B, fill_opacity=0.25, stroke_width=2)
        lA = MathTex("A_j", font_size=26, color=BLUE_3B).move_to(bA)
        
        bB = Ellipse(width=0.9, height=1.2, color=GOLD_3B, fill_opacity=0.25, stroke_width=2)
        lB = MathTex("A_k", font_size=26, color=GOLD_3B).move_to(bB)
        
        plus = MathTex("+", font_size=32, color=SOFT_WHITE)
        eq_sign = MathTex("=", font_size=32, color=SOFT_WHITE)
        
        bU = Ellipse(width=2.4, height=1.4, color=GREEN_3B, fill_opacity=0.25, stroke_width=2)
        lU = MathTex(r"\bigcup A_j", font_size=26, color=GREEN_3B).move_to(bU)
        
        equation_visual = VGroup(
            VGroup(bA, lA), plus, VGroup(bB, lB), eq_sign, VGroup(bU, lU)
        ).arrange(RIGHT, buff=0.25)
        
        equation_visual.move_to(right_panel.get_bottom() + UP * 1.5)

        self.play(Write(ax2_header))
        self.play(Write(ax2_formula), FadeIn(ax2_desc), run_time=1.5)
        self.play(
            FadeIn(VGroup(bA, lA), shift=UP*0.2), 
            FadeIn(VGroup(bB, lB), shift=UP*0.2), 
            Write(plus), 
            Write(eq_sign), 
            FadeIn(VGroup(bU, lU), shift=UP*0.2),
            run_time=1.5
        )

        self.wait(3)
        self.clear()

    # ─────────────────────────────────────────────────────────────
    #  18. INCLUSION-EXCLUSION
    # ─────────────────────────────────────────────────────────────
    def scene_inclusion_exclusion(self):
        title = section_title("Inclusion-Exclusion")
        title.to_edge(UP, buff=0.5)
        self.play(Write(title[0]), GrowFromEdge(title[1], LEFT))

        # Formula
        formula = MathTex(
            r"P(A \cup B)", r"=", r"P(A)", r"+", r"P(B)", r"-", r"P(A \cap B)",
            font_size=40, color=SOFT_WHITE
        )
        formula[0].set_color(GREEN_3B)
        formula[2].set_color(BLUE_3B)
        formula[4].set_color(GOLD_3B)
        formula[6].set_color(RED_3B)
        formula.next_to(title, DOWN, buff=0.6)
        self.play(Write(formula, run_time=2))

        # Venn diagram — animated build
        cA = Circle(radius=1.3, color=BLUE_3B, fill_opacity=0.2, stroke_width=2.5)
        cA.shift(LEFT * 0.7 + DOWN * 1.5)
        cB = Circle(radius=1.3, color=GOLD_3B, fill_opacity=0.2, stroke_width=2.5)
        cB.shift(RIGHT * 0.7 + DOWN * 1.5)

        lA = MathTex("A", font_size=28, color=BLUE_3B).move_to(cA.get_center() + LEFT * 0.7)
        lB = MathTex("B", font_size=28, color=GOLD_3B).move_to(cB.get_center() + RIGHT * 0.7)

        self.play(Create(cA), Write(lA))
        self.play(Create(cB), Write(lB))

        # Highlight intersection
        inter = Intersection(cA, cB, fill_color=RED_3B, fill_opacity=0.35, stroke_width=0)
        inter_label = MathTex(r"A \cap B", font_size=20, color=RED_3B)
        inter_label.move_to(DOWN * 1.5)

        self.play(FadeIn(inter), Write(inter_label))

        # Annotation: "Counted twice!"
        ann = Text("Counted twice!", font_size=18, color=RED_3B, weight=BOLD)
        ann.next_to(inter_label, DOWN, buff=0.3)
        arrow = Arrow(ann.get_top(), inter_label.get_bottom(),
                      color=RED_3B, stroke_width=2, buff=0.05)
        self.play(Write(ann), Create(arrow))

        # Explanation
        expl = Text(
            "Subtract the overlap so it's only counted once.",
            font_size=22, color=SOFT_WHITE
        )
        expl.to_edge(DOWN, buff=0.4)
        self.play(Write(expl))
        self.wait(2.5)
        self.clear()

    # ─────────────────────────────────────────────────────────────
    #  19. THE GRAND SYNTHESIS
    # ─────────────────────────────────────────────────────────────
    def scene_grand_synthesis(self):
        title = section_title("The Grand Synthesis")
        title.to_edge(UP, buff=0.5)
        self.play(Write(title[0]), GrowFromEdge(title[1], LEFT))

        # Make subtitle slightly more stylized and italicized
        subtitle = Text("A Translation Guide", font_size=24, color=GREY_3B, slant=ITALIC)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(subtitle, shift=UP * 0.2))

        # 1. Create a border panel to anchor the table and its columns
        panel = RoundedRectangle(
            width=10.5, height=5.0, corner_radius=0.25,
            fill_color=DARK_GREY, fill_opacity=0.2, 
            stroke_color=GREY_3B, stroke_opacity=0.4, stroke_width=2
        )
        panel.next_to(subtitle, DOWN, buff=0.4)
        self.play(Create(panel), run_time=1)

        # 2. Setup Headers and arrange them as a group with larger text
        col1 = Text("Events", font_size=28, color=SOFT_WHITE, weight=BOLD)
        col2 = Text("Set Theory", font_size=28, color=BLUE_3B, weight=BOLD)
        col3 = Text("Probability", font_size=28, color=YELLOW_3B, weight=BOLD)
        headers = VGroup(col1, col2, col3).arrange(RIGHT, buff=2.2)
        headers.move_to(panel.get_top() + DOWN * 0.6)

        # Enhance arrows - slightly thicker flow lines and better buffing
        arr1 = Arrow(col1.get_right(), col2.get_left(), color=GREY_3B, stroke_width=3, buff=0.3)
        arr2 = Arrow(col2.get_right(), col3.get_left(), color=GREY_3B, stroke_width=3, buff=0.3)
        p_label = MathTex("P", font_size=24, color=YELLOW_3B).next_to(arr2, UP, buff=0.1)
        
        header_group = VGroup(headers, arr1, arr2, p_label)

        # Solid separator line below headers
        sep_line = Line(
            panel.get_left() + RIGHT * 0.5,
            panel.get_right() + LEFT * 0.5,
            stroke_color=GREY_3B, stroke_opacity=0.6, stroke_width=2
        ).next_to(header_group, DOWN, buff=0.3)

        self.play(
            FadeIn(headers, shift=DOWN * 0.2),
            GrowArrow(arr1), GrowArrow(arr2), FadeIn(p_label),
            Create(sep_line),
            run_time=1.5
        )

        # 3. Setup Rows dynamically arranged to headers
        rows_data = [
            ("A or B", r"A \cup B", r"P(A \cup B)"),
            ("not A", r"A^c", r"1 - P(A)"),
            ("Anything", r"S", r"P(S) = 1"),
        ]

        # Use arranging for cleaner positioning of the rows
        rows = VGroup()
        for ev, st, pr in rows_data:
            e = Text(ev, font_size=24, color=GREY_3B)
            # Make the math a little bigger for visibility
            s = MathTex(st, font_size=34, color=BLUE_3B)
            p = MathTex(pr, font_size=34, color=YELLOW_3B)
            
            # Snap X coordinates to header centers
            e.set_x(col1.get_x())
            s.set_x(col2.get_x())
            p.set_x(col3.get_x())
            
            row = VGroup(e, s, p)
            rows.add(row)

        rows.arrange(DOWN, buff=0.75)
        rows.next_to(sep_line, DOWN, buff=0.6)

        # 4. Subtle ledger lines between rows
        dashed_lines = VGroup()
        for i in range(len(rows) - 1):
            dl = DashedLine(
                panel.get_left() + RIGHT * 0.5,
                panel.get_right() + LEFT * 0.5,
                stroke_color=GREY_3B, stroke_opacity=0.2, stroke_width=1, dash_length=0.1
            )
            # Position at the vertical midpoint between row i and row i+1
            dl.set_y((rows[i].get_y() + rows[i+1].get_y()) / 2)
            dashed_lines.add(dl)

        self.play(Create(dashed_lines), run_time=1)

        # 5. Sequential "Translation" Reveal (Left to Right, then Down)
        # This forces the brain to watch the "translation" happen in order.
        for row in rows:
            self.play(FadeIn(row[0], shift=RIGHT * 0.2), run_time=0.4) # Event (English)
            self.play(FadeIn(row[1], shift=RIGHT * 0.2), run_time=0.4) # Set Theory (Math)
            self.play(FadeIn(row[2], shift=RIGHT * 0.2), run_time=0.4) # Probability (Applied)
            self.wait(0.2)

        self.wait(3)
        self.clear()

    # ─────────────────────────────────────────────────────────────
    #  20. THE BLUEPRINT (takeaways)
    # ─────────────────────────────────────────────────────────────
    def scene_blueprint(self):
        title = section_title("The Blueprint of Uncertainty")
        title.to_edge(UP, buff=0.5)
        self.play(Write(title[0]), GrowFromEdge(title[1], LEFT))

        takeaways = [
            ("1", "Label Everything", BLUE_3B),
            ("2", "Count Smart, Not Hard", TEAL_3B),
            ("3", "Probability is Mass", GOLD_3B),
        ]

        cards = VGroup()
        for num, heading, accent in takeaways:
            # 1. Shrink the bar to fit a single line of text
            bar = Rectangle(width=0.08, height=0.6, fill_color=accent,
                            fill_opacity=1, stroke_width=0)
            
            # 2. Increase font sizes slightly to fill the screen better
            n = Text(num, font_size=38, color=accent, weight=BOLD)
            h = Text(heading, font_size=34, color=SOFT_WHITE, weight=BOLD)
            
            # Group text together
            content = VGroup(n, h).arrange(RIGHT, buff=0.4)
            
            # Group bar and text (removed aligned_edge=UP so it centers vertically)
            row = VGroup(bar, content).arrange(RIGHT, buff=0.3)
            
            # 3. Create a subtle glowing background box for each item
            bg_box = RoundedRectangle(
                width=8.0, height=1.2, corner_radius=0.15,
                fill_color=accent, fill_opacity=0.08, 
                stroke_color=accent, stroke_opacity=0.4, stroke_width=1.5
            )
            
            # Align the text inside the left side of the box
            row.move_to(bg_box.get_left() + RIGHT * (row.width / 2 + 0.5))
            
            full_card = VGroup(bg_box, row)
            cards.add(full_card)

        # 4. Arrange the fully built cards and center them on screen
        cards.arrange(DOWN, buff=0.4)
        cards.next_to(title, DOWN, buff=1.0)

        for card in cards:
            # Fade in while slightly floating up for a smoother reveal
            self.play(FadeIn(card, shift=UP * 0.2), run_time=0.8)
            self.wait(0.5)

        self.wait(2)

        # Final signature dot
        self.play(*[FadeOut(m) for m in self.mobjects])
        dot = Dot(radius=0.25, color=BLUE_3B)
        halo = Dot(radius=0.8, color=BLUE_3B, fill_opacity=0.1, stroke_width=0)
        glow = VGroup(halo, dot)
        self.play(GrowFromCenter(glow))
        self.play(
            halo.animate.scale(2).set_opacity(0),
            run_time=2, rate_func=smooth
        )
        self.play(FadeOut(dot, run_time=0.8))


# ═════════════════════════════════════════════════════════════════
#  INDIVIDUAL SCENES (inherit to get all methods)
# ═════════════════════════════════════════════════════════════════
class TitleScene(LogicOfUncertainty):
    def construct(self):
        self.camera.background_color = DARK_BG
        self.scene_title()

class BirthdayHook(LogicOfUncertainty):
    def construct(self):
        self.camera.background_color = DARK_BG
        self.scene_birthday_hook()

class PebbleWorld(LogicOfUncertainty):
    def construct(self):
        self.camera.background_color = DARK_BG
        self.scene_pebble_world()

class NaiveDefinition(LogicOfUncertainty):
    def construct(self):
        self.camera.background_color = DARK_BG
        self.scene_naive_definition()

class FiftyFiftyFallacy(LogicOfUncertainty):
    def construct(self):
        self.camera.background_color = DARK_BG
        self.scene_fifty_fifty_fallacy()

class LeibnizDice(LogicOfUncertainty):
    def construct(self):
        self.camera.background_color = DARK_BG
        self.scene_leibniz_dice()

class ProblemOfScale(LogicOfUncertainty):
    def construct(self):
        self.camera.background_color = DARK_BG
        self.scene_problem_of_scale()

class MultiplicationRule(LogicOfUncertainty):
    def construct(self):
        self.camera.background_color = DARK_BG
        self.scene_multiplication_rule()

class Overcounting(LogicOfUncertainty):
    def construct(self):
        self.camera.background_color = DARK_BG
        self.scene_overcounting()

class BinomialCoefficient(LogicOfUncertainty):
    def construct(self):
        self.camera.background_color = DARK_BG
        self.scene_binomial_coefficient()

class CountingMatrix(LogicOfUncertainty):
    def construct(self):
        self.camera.background_color = DARK_BG
        self.scene_counting_matrix()

class StoryProof(LogicOfUncertainty):
    def construct(self):
        self.camera.background_color = DARK_BG
        self.scene_story_proof()

class SolvingBirthday(LogicOfUncertainty):
    def construct(self):
        self.camera.background_color = DARK_BG
        self.scene_solving_birthday()

class MathNoMatches(LogicOfUncertainty):
    def construct(self):
        self.camera.background_color = DARK_BG
        self.scene_math_no_matches()

class TippingPoint(LogicOfUncertainty):
    def construct(self):
        self.camera.background_color = DARK_BG
        self.scene_tipping_point()

class BeyondNaive(LogicOfUncertainty):
    def construct(self):
        self.camera.background_color = DARK_BG
        self.scene_beyond_naive()

class AxiomsScene(LogicOfUncertainty):
    def construct(self):
        self.camera.background_color = DARK_BG
        self.scene_axioms()

class InclusionExclusion(LogicOfUncertainty):
    def construct(self):
        self.camera.background_color = DARK_BG
        self.scene_inclusion_exclusion()

class GrandSynthesis(LogicOfUncertainty):
    def construct(self):
        self.camera.background_color = DARK_BG
        self.scene_grand_synthesis()

class Blueprint(LogicOfUncertainty):
    def construct(self):
        self.camera.background_color = DARK_BG
        self.scene_blueprint()