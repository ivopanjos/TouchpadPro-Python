from enum import Enum


class GesturesEnum(Enum):
    # Two finger swipes
    TWO_SWIPE_LEFT = 1
    TWO_SWIPE_RIGHT = 2
    TWO_SWIPE_UP = 3
    TWO_SWIPE_DOWN = 4

    # Three finger swipes
    THREE_SWIPE_LEFT = 5
    THREE_SWIPE_RIGHT = 6
    THREE_SWIPE_UP = 7
    THREE_SWIPE_DOWN = 8

    # Pinch & Rotate (two fingers only)
    PINCH_IN = 9
    PINCH_OUT = 10
    ROTATE_CW = 11
    ROTATE_ACW = 12

    # Not defined gestures
    NOT_DEFINED = -1
    SINGLE_TOUCH = -1