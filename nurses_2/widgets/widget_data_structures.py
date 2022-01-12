from enum import Enum
from typing import NamedTuple

__all__ = "SizeHint", "PosHint", "Anchor", "Transition"


class SizeHint(NamedTuple):
    height: float | None
    width: float | None


class PosHint(NamedTuple):
    y: float | None
    x: float | None


class Anchor(str, Enum):
    CENTER = "CENTER"
    LEFT_CENTER = "LEFT_CENTER"
    RIGHT_CENTER = "RIGHT_CENTER"
    TOP_LEFT = "TOP_LEFT"
    TOP_CENTER = "TOP_CENTER"
    TOP_RIGHT = "TOP_RIGHT"
    BOTTOM_LEFT = "BOTTOM_LEFT"
    BOTTOM_CENTER = "BOTTOM_CENTER"
    BOTTOM_RIGHT = "BOTTOM_RIGHT"


class Transition(str, Enum):
    LINEAR = "linear"
    IN_QUAD = "in_quad"
    OUT_QUAD = "out_quad"
    IN_OUT_QUAD = "in_out_quad"
    IN_CUBIC = "in_cubic"
    OUT_CUBIC = "out_cubic"
    IN_OUT_CUBIC = "in_out_cubic"
    IN_QUART = "in_quart"
    OUT_QUART = "out_quart"
    IN_OUT_QUART = "in_out_quart"
    IN_QUINT = "in_quint"
    OUT_QUINT = "out_quint"
    IN_OUT_QUINT = "in_out_quint"
    IN_SINE = "in_sine"
    OUT_SINE = "out_sine"
    IN_OUT_SINE = "in_out_sine"
    IN_EXP = "in_exp"
    OUT_EXP = "out_exp"
    IN_OUT_EXP = "in_out_exp"
    IN_CIRC = "in_circ"
    OUT_CIRC = "out_circ"
    IN_OUT_CIRC = "in_out_circ"
    IN_ELASTIC = "in_elastic"
    OUT_ELASTIC = "out_elastic"
    IN_OUT_ELASTIC = "in_out_elastic"
    IN_BACK = "in_back"
    OUT_BACK = "out_back"
    IN_OUT_BACK = "in_out_back"
    IN_BOUNCE = "in_bounce"
    OUT_BOUNCE = "out_bounce"
    IN_OUT_BOUNCE = "in_out_bounce"
