from evdev import ecodes as e
import GesturesIdConst as GesturesId


class GesturesToEcodes:

    def __init__(self):
        self.dict = dict()

        # Two finger gestures
        self.dict[GesturesId.TWO_SWIPE_LEFT] = [e.KEY_LEFTMETA, e.KEY_RIGHT]
        self.dict[GesturesId.TWO_SWIPE_RIGHT] = [e.KEY_LEFTMETA, e.KEY_LEFT]
        self.dict[GesturesId.TWO_SWIPE_UP] = [e.KEY_LEFTMETA, e.KEY_UP]
        self.dict[GesturesId.TWO_SWIPE_DOWN] = [e.KEY_LEFTMETA, e.KEY_DOWN]

        # Three finger gestures
        self.dict[GesturesId.THREE_SWIPE_LEFT] = [e.KEY_LEFTMETA, e.KEY_LEFTCTRL, e.KEY_RIGHT]
        self.dict[GesturesId.THREE_SWIPE_RIGHT] = [e.KEY_LEFTMETA, e.KEY_LEFTCTRL, e.KEY_LEFT]
        # self.dict[GesturesId.THREE_SWIPE_UP] = [e.KEY_LEFTMETA, e.KEY_LEFTCTRL, e.KEY_UP] TODO maximize
        # self.dict[GesturesId.THREE_SWIPE_DOWN] = [e.KEY_LEFTMETA, e.KEY_LEFTCTRL, e.KEY_DOWN] TODO minimize

    def get_ecodes(self, gesture_code):
        """
        Get the list of ecodes for a certain gesture
        :param gesture_code:
        :return: list of ecodes
        """
        return self.dict.get(gesture_code, None)






