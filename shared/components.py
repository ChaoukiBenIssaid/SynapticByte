"""
Reusable Manim components used across SynapticByte animations.

All helpers pull their default colors from :mod:`shared.palette` so that the
visual style stays consistent across videos.
"""

from manim import (
    Brace,
    Circle,
    Dot,
    MathTex,
    SurroundingRectangle,
    Text,
    Underline,
    VGroup,
    BOLD,
    DOWN,
)

from .palette import (
    BLUE_3B,
    GOLD_3B,
    GREY_3B,
    SOFT_WHITE,
)


class Pebble(Dot):
    """
    A glowing outcome dot — the 'pebble' metaphor for sample-space outcomes.

    Parameters
    ----------
    color : str
        Fill and glow color.
    radius : float
        Radius of the inner dot. The surrounding halo is 2.5x this radius.
    glow : bool
        If True, adds a soft halo behind the dot.
    **kwargs
        Forwarded to :class:`manim.Dot`.
    """

    def __init__(self, color=BLUE_3B, radius=0.1, glow=True, **kwargs):
        super().__init__(
            radius=radius,
            color=color,
            fill_opacity=0.9,
            stroke_width=0,
            **kwargs,
        )
        if glow:
            halo = Dot(
                radius=radius * 2.5,
                color=color,
                fill_opacity=0.12,
                stroke_width=0,
            )
            halo.move_to(self.get_center())
            self.add_to_back(halo)


def section_title(text, font_size=52, color=SOFT_WHITE, underline_color=BLUE_3B):
    """
    A bold section title with a colored underline.

    Used at the top of each major scene to establish context. Returns a
    :class:`VGroup` of (text, underline) so both elements can be animated
    independently — e.g. ``Write(title[0]), GrowFromEdge(title[1], LEFT)``.
    """
    t = Text(text, font_size=font_size, color=color, weight=BOLD)
    ul = Underline(t, color=underline_color, stroke_width=2, buff=0.15)
    return VGroup(t, ul)


def golden_box(mob, buff=0.25, color=GOLD_3B, stroke_width=2, corner_radius=0.1):
    """
    A glowing golden rectangle around a mobject, used to emphasize formulas
    and key results.
    """
    return SurroundingRectangle(
        mob,
        color=color,
        stroke_width=stroke_width,
        buff=buff,
        corner_radius=corner_radius,
    )


def brace_label(mob, text, direction=DOWN, color=SOFT_WHITE, font_size=28):
    """
    A brace with a LaTeX label attached in the given direction.

    Returns a :class:`VGroup` ``(brace, label)``.
    """
    b = Brace(mob, direction, color=color, buff=0.15)
    label = MathTex(text, font_size=font_size, color=color)
    label.next_to(b, direction, buff=0.1)
    return VGroup(b, label)


def make_node(
    label,
    radius=0.35,
    color=GREY_3B,
    label_color=SOFT_WHITE,
    fill_opacity=0.15,
    font_size=22,
):
    """
    Circular node for tree and graph diagrams.

    Returns a :class:`VGroup` ``(circle, label_text)``.
    """
    c = Circle(
        radius=radius,
        stroke_color=color,
        stroke_width=2,
        fill_color=color,
        fill_opacity=fill_opacity,
    )
    t = Text(label, font_size=font_size, color=label_color, weight=BOLD)
    t.move_to(c)
    return VGroup(c, t)
