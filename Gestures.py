from math import hypot
from GesturesEnum import GesturesEnum as GesturesEnum
from Utils import delta, angle, average


class Gestures:

    # Values of touchpad definitions
    TOTAL_X_DIST = 2436
    TOTAL_Y_DIST = 1044

    MIN_SWIPE_X_DIST = 800
    MIN_SWIPE_Y_DIST = TOTAL_Y_DIST / 2.5   # 1/4 aproximate total distance

    MIN_SWIPE_X_SPEED = 1500
    MIN_SWIPE_Y_SPEED = 800

    MIN_PINCH_DIST = 1000
    MIN_ANGLE_DIST = 20

    def compute_events(self,
                       first_slot0_x, first_slot0_y,
                       first_slot1_x, first_slot1_y,
                       last_slot0_x, last_slot0_y,
                       last_slot1_x, last_slot1_y,
                       double_tap, triple_tap, start_time, end_time):

        if not any([double_tap, triple_tap]):
            return GesturesEnum.SINGLE_TOUCH

        delta_time = end_time - start_time

        if double_tap and not triple_tap:
            value = self.pinch(first_slot0_x, first_slot0_y,
                               first_slot1_x, first_slot1_y,
                               last_slot0_x, last_slot0_y,
                               last_slot1_x, last_slot1_y, delta_time)

            if value in (GesturesEnum.PINCH_IN, GesturesEnum.PINCH_OUT, GesturesEnum.ROTATE_CW, GesturesEnum.ROTATE_ACW):
                return value

        # no pinch or rotation gestures detected
        value = self.swipe_horizontal(first_slot0_x, first_slot0_y, last_slot0_x, last_slot0_y, triple_tap, delta_time)
        if value in (GesturesEnum.TWO_SWIPE_LEFT, GesturesEnum.TWO_SWIPE_RIGHT,
                     GesturesEnum.THREE_SWIPE_LEFT, GesturesEnum.THREE_SWIPE_RIGHT):
            return value

        value = self.swipe_vertical(first_slot0_x, first_slot0_y, last_slot0_x, last_slot0_y, triple_tap, delta_time)
        if value in (GesturesEnum.TWO_SWIPE_UP, GesturesEnum.TWO_SWIPE_DOWN,
                     GesturesEnum.THREE_SWIPE_UP, GesturesEnum.THREE_SWIPE_DOWN):
            return value

        return GesturesEnum.NOT_DEFINED

    def swipe_horizontal(self, x1, y1, x2, y2, triple_tap, delta_time):
        delta_x = x2 - x1
        speed_x = abs(delta_x / delta_time)

        if abs(delta_x) < self.MIN_SWIPE_X_DIST:
            return GesturesEnum.NOT_DEFINED

        if speed_x < self.MIN_SWIPE_X_SPEED:
            return GesturesEnum.NOT_DEFINED

        if triple_tap:
            if delta_x < 0:
                return GesturesEnum.THREE_SWIPE_LEFT
            else:
                return GesturesEnum.THREE_SWIPE_RIGHT
        else:   # double tap
            if delta_x < 0:
                return GesturesEnum.TWO_SWIPE_LEFT
            else:
                return GesturesEnum.TWO_SWIPE_RIGHT

    def swipe_vertical(self, x1, y1, x2, y2, triple_tap, delta_time):
        delta_y = y2 - y1
        speed_y = abs(delta_y / delta_time)

        if abs(delta_y) < self.MIN_SWIPE_Y_DIST:
            return GesturesEnum.NOT_DEFINED

        if speed_y < self.MIN_SWIPE_Y_SPEED:
            return GesturesEnum.NOT_DEFINED

        if triple_tap:
            if delta_y < 0:
                return GesturesEnum.THREE_SWIPE_UP
            else:
                return GesturesEnum.THREE_SWIPE_DOWN
        else:   # double tap
            if delta_y < 0:
                return GesturesEnum.TWO_SWIPE_UP
            else:
                return GesturesEnum.TWO_SWIPE_DOWN

    def pinch(self,
                 first_slot0_x, first_slot0_y,
                 first_slot1_x, first_slot1_y,
                 last_slot0_x, last_slot0_y,
                 last_slot1_x, last_slot1_y,
                 delta_time):

        delta_x_start = delta(first_slot1_x, first_slot0_x)
        delta_y_start = delta(first_slot1_y, first_slot0_y)

        delta_x_end = delta(last_slot1_x, last_slot0_x)
        delta_y_end = delta(last_slot1_y, last_slot0_y)

        # distance part - for pinch gesture
        distance_start = hypot(delta_x_start, delta_y_start)
        distance_end = hypot(delta_x_end, delta_y_end)
        distance_delta = delta(distance_end, distance_start)

        # angle part - for rotation gesture
        angle_start = angle(delta_x_start, delta_y_start)
        angle_end = angle(delta_x_end, delta_y_end)

        angle_delta = delta(angle_end, angle_start)

        if angle_delta > 180.0:
            angle_delta -= 360.0
        elif angle_delta < -180.0:
            angle_delta += 360.0

        print("Angle : ", angle_delta, " - Dist : ", distance_delta)

        # check for rotation gesture
        if abs(angle_delta) > self.MIN_ANGLE_DIST and abs(distance_delta) < self.MIN_PINCH_DIST:
            if angle_delta < 0:
                return GesturesEnum.ROTATE_ACW
            else:
                return GesturesEnum.ROTATE_CW

        # check for pinch gesture
        elif abs(distance_delta) > self.MIN_PINCH_DIST:
            if distance_delta < 0:
                return GesturesEnum.PINCH_IN
            else:
                return GesturesEnum.PINCH_OUT

        # gesture not defined
        else:
            return GesturesEnum.NOT_DEFINED

        # https://wayland.freedesktop.org/libinput/doc/latest/gestures.html
        # https://github.com/wayland-project/libinput/blob/master/src/evdev.c
        # https://github.com/wayland-project/libinput/blob/master/src/evdev-mt-touchpad-gestures.c
        # https://wayland.freedesktop.org/libinput/doc/latest/
