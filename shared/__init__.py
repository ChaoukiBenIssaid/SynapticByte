"""
Shared components used across all SynapticByte animations.

Public API:
    from shared import (
        # Colors
        DARK_BG, SOFT_WHITE, BLUE_3B, LIGHT_BLUE, YELLOW_3B, GOLD_3B,
        ORANGE_3B, GREEN_3B, RED_3B, PINK_3B, GREY_3B, DARK_GREY,
        TEAL_3B, CYAN_GLOW,
        # Components
        Pebble, section_title, golden_box, brace_label, make_node,
    )
"""

from .palette import (
    DARK_BG,
    SOFT_WHITE,
    BLUE_3B,
    LIGHT_BLUE,
    YELLOW_3B,
    GOLD_3B,
    ORANGE_3B,
    GREEN_3B,
    RED_3B,
    PINK_3B,
    GREY_3B,
    DARK_GREY,
    TEAL_3B,
    CYAN_GLOW,
)

from .components import (
    Pebble,
    section_title,
    golden_box,
    brace_label,
    make_node,
)

__all__ = [
    # Palette
    "DARK_BG",
    "SOFT_WHITE",
    "BLUE_3B",
    "LIGHT_BLUE",
    "YELLOW_3B",
    "GOLD_3B",
    "ORANGE_3B",
    "GREEN_3B",
    "RED_3B",
    "PINK_3B",
    "GREY_3B",
    "DARK_GREY",
    "TEAL_3B",
    "CYAN_GLOW",
    # Components
    "Pebble",
    "section_title",
    "golden_box",
    "brace_label",
    "make_node",
]
