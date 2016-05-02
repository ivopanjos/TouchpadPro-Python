from ewmh import EWMH
from evdev import ecodes as e
import GesturesIdConst as GesturesId


class WindowManager:

    GOOGLE_CHROME = "google-chrome"

    def __init__(self):
        self.window_manager = EWMH()
        self.dict = dict()

        self.dict[GesturesId.THREE_SWIPE_LEFT] = [e.KEY_LEFTALT, e.KEY_RIGHT]
        self.dict[GesturesId.THREE_SWIPE_RIGHT] = [e.KEY_LEFTALT, e.KEY_LEFT]

    def get_active_window_class(self):
        window = self.window_manager.getActiveWindow()
        window_class = window.get_wm_class()[1]

        if window_class == self.GOOGLE_CHROME:
            return self.GOOGLE_CHROME

        return None

    def get_ecodes(self, gesture_code):
        return self.dict.get(gesture_code, None)