import GesturesIdConst as GesturesId


class Gestures:

    # Values of touchpad definitions
    TOTAL_X_DIST = 2436
    TOTAL_Y_DIST = 1044

    MIN_SWIPE_X_DIST = 800
    MIN_SWIPE_Y_DIST = TOTAL_Y_DIST / 2.5   # 1/4 aproximate total distance

    MIN_SWIPE_X_SPEED = 1500
    MIN_SWIPE_Y_SPEED = 800

    def compute_events(self,
                       first_slot0_x, first_slot0_y,
                       first_slot1_x, first_slot1_y,
                       last_slot0_x, last_slot0_y,
                       last_slot1_x, last_slot1_y,
                       double_tap, triple_tap, start_time, end_time):

        if not any([double_tap, triple_tap]):
            return GesturesId.SINGLE_TOUCH

        delta_time = end_time - start_time
        value = self.swipe_horizontal(first_slot0_x, first_slot0_y, last_slot0_x, last_slot0_y, triple_tap, delta_time)
        if value in (GesturesId.TWO_SWIPE_LEFT, GesturesId.TWO_SWIPE_RIGHT,
                     GesturesId.THREE_SWIPE_LEFT, GesturesId.THREE_SWIPE_RIGHT):
            return value

        value = self.swipe_vertical(first_slot0_x, first_slot0_y, last_slot0_x, last_slot0_y, triple_tap, delta_time)
        if value in (GesturesId.TWO_SWIPE_UP, GesturesId.TWO_SWIPE_DOWN,
                     GesturesId.THREE_SWIPE_UP, GesturesId.THREE_SWIPE_DOWN):
            return value

        if double_tap and not triple_tap:
            value = self.pinch(first_slot0_x, first_slot0_y,
                               first_slot1_x, first_slot1_y,
                               last_slot0_x, last_slot0_y,
                               last_slot1_x, last_slot1_y, delta_time)

            if value in (GesturesId.PINCH_IN, GesturesId.PINCH_OUT):
                return value

            value = self.rotation(first_slot0_x, first_slot0_y,
                                  first_slot1_x, first_slot1_y,
                                  last_slot0_x, last_slot0_y,
                                  last_slot1_x, last_slot1_y, delta_time)

            if value in (GesturesId.ROTATE_CW, GesturesId.ROTATE_ACW):
                return value

        return GesturesId.NOT_DEFINED

    def swipe_horizontal(self, x1, y1, x2, y2, triple_tap, delta_time):
        delta_x = x2 - x1
        speed_x = abs(delta_x / delta_time)

        if abs(delta_x) < self.MIN_SWIPE_X_DIST:
            return GesturesId.NOT_DEFINED

        if speed_x < self.MIN_SWIPE_X_SPEED:
            return GesturesId.NOT_DEFINED

        if triple_tap:
            if delta_x < 0:
                return GesturesId.THREE_SWIPE_LEFT
            else:
                   return GesturesId.THREE_SWIPE_RIGHT
        else:
            if delta_x < 0:
                return GesturesId.TWO_SWIPE_LEFT
            else:
                return GesturesId.TWO_SWIPE_RIGHT

    def swipe_vertical(self, x1, y1, x2, y2, triple_tap, delta_time):
        delta_y = y2 - y1
        speed_y = abs(delta_y / delta_time)

        if abs(delta_y) < self.MIN_SWIPE_Y_DIST:
            return GesturesId.NOT_DEFINED

        if speed_y < self.MIN_SWIPE_Y_SPEED:
            return GesturesId.NOT_DEFINED

        if triple_tap:
            if delta_y < 0:
                return GesturesId.THREE_SWIPE_UP
            else:
                return GesturesId.THREE_SWIPE_DOWN
        else:
            if delta_y < 0:
                return GesturesId.TWO_SWIPE_UP
            else:
                return GesturesId.TWO_SWIPE_DOWN

    def pinch(self,
              first_slot0_x, first_slot0_y,
              first_slot1_x, first_slot1_y,
              last_slot0_x, last_slot0_y,
              last_slot1_x, last_slot1_y,
              delta_time):
        return GesturesId.NOT_DEFINED

    def rotation(self,
                 first_slot0_x, first_slot0_y,
                 first_slot1_x, first_slot1_y,
                 last_slot0_x, last_slot0_y,
                 last_slot1_x, last_slot1_y,
                 delta_time):
        return GesturesId.NOT_DEFINED

