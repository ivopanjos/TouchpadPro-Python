from evdev import ecodes, UInput


# TODO read keys to transform in ecodes, job for later
"""
dev = InputDevice('/dev/input/event6')
for event in dev.read_loop():
    print(event)
"""


class Keyboard:

    def __init__(self):
        self.ui = UInput()

    def press_key(self, list_ecodes):
        """
        Write events to keyboard based on a list of ecodes
        :param list_ecodes
        """

        # key down event (press)
        for code in list_ecodes:
            self.ui.write(ecodes.EV_KEY, code, 1)

        # key up event (release)
        for code in list_ecodes:
            self.ui.write(ecodes.EV_KEY, code, 0)

        # after all keys are writen sync
        self.ui.syn()

        #  close channel
        # self.ui.close() TODO close channel in the end of the execution



