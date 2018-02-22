import sys
from evdev import InputDevice, ecodes
from Gestures import Gestures
from Keyboard import Keyboard
from GesturesToEcodes import GesturesToEcodes
from WindowManager import WindowManager


class MainClass:

    def __init__(self, input_event):
        input_device = "/dev/input/event" + input_event
        self.dev = InputDevice(input_device)

        # initialize helper classes
        self.gestures = Gestures()
        # self.keyboard = Keyboard()
        self.gestures_to_ecodes = GesturesToEcodes()
        self.window_manager = WindowManager()

        self.read_input(self.dev)

    def read_input(self, dev):
        first_time_slot0_x = True
        first_time_slot0_y = True
        first_time_slot1_x = True
        first_time_slot1_y = True
        double_tap = False
        triple_tap = False

        get_slot1_values = False

        first_slot0_x = -1
        first_slot0_y = -1
        first_slot1_x = -1
        first_slot1_y = -1

        last_slot0_x = -1
        last_slot0_y = -1
        last_slot1_x = -1
        last_slot1_y = -1

        start_time = 0

        for event in dev.read_loop():
            # read start time of event
            if event.type != 0 and start_time == 0:
                start_time = event.timestamp()

            if event.type == ecodes.EV_ABS:
                # is there a second slot
                if event.code == ecodes.ABS_MT_SLOT:
                    if event.value == 1:
                        get_slot1_values = True
                    else:
                        get_slot1_values = False

                # get x position
                elif event.code == ecodes.ABS_MT_POSITION_X:
                    if get_slot1_values:
                        if first_time_slot1_x:
                            first_time_slot1_x = False
                            first_slot1_x = event.value
                        else:
                            last_slot1_x = event.value
                    else:
                        if first_time_slot0_x:
                            first_time_slot0_x = False
                            first_slot0_x = event.value
                        else:
                            last_slot0_x = event.value

                # get y position
                elif event.code == ecodes.ABS_MT_POSITION_Y:
                    if get_slot1_values:
                        if first_time_slot1_y:
                            first_time_slot1_y = False
                            first_slot1_y = event.value
                        else:
                            last_slot1_y = event.value
                    else:
                        if first_time_slot0_y:
                            first_time_slot0_y = False
                            first_slot0_y = event.value
                        else:
                            last_slot0_y = event.value

                # maybe touchpad released
                elif event.code == ecodes.ABS_TOOL_WIDTH:
                    if event.value == 0:    # touchpad released

                        self.interpret_values(first_slot0_x, first_slot0_y,
                                              first_slot1_x, first_slot1_y,
                                              last_slot0_x, last_slot0_y,
                                              last_slot1_x, last_slot1_y,
                                              double_tap, triple_tap, start_time, event.timestamp())

                        # reset all variables
                        first_time_slot0_x = True
                        first_time_slot0_y = True
                        first_time_slot1_x = True
                        first_time_slot1_y = True
                        double_tap = False
                        triple_tap = False

                        get_slot1_values = False

                        first_slot0_x = -1
                        first_slot0_y = -1
                        first_slot1_x = -1
                        first_slot1_y = -1

                        last_slot0_x = -1
                        last_slot0_y = -1
                        last_slot1_x = -1
                        last_slot1_y = -1

                        start_time = 0

            elif event.type == ecodes.EV_KEY:
                if event.code == ecodes.BTN_TOOL_DOUBLETAP:     # caught a double tap
                    if event.value == 1:
                        double_tap = True
                    else:
                        get_slot1_values = False

                elif event.code == ecodes.BTN_TOOL_TRIPLETAP:   # caught a triple tap
                    if event.value == 1:
                        triple_tap = True

    def interpret_values(self,
                         first_slot0_x, first_slot0_y,
                         first_slot1_x, first_slot1_y,
                         last_slot0_x, last_slot0_y,
                         last_slot1_x, last_slot1_y,
                         double_tap, triple_tap, start_time, end_time):

        value = self.gestures.compute_events(first_slot0_x, first_slot0_y,
                                             first_slot1_x, first_slot1_y,
                                             last_slot0_x, last_slot0_y,
                                             last_slot1_x, last_slot1_y,
                                             double_tap, triple_tap, start_time, end_time)

        print(value.name)
        """
        window_class = self.window_manager.get_active_window_class()

        if window_class is not None and triple_tap:
            list_ecodes = self.window_manager.get_ecodes(value)

        else:
            list_ecodes = self.gestures_to_ecodes.get_ecodes(value)

        if list_ecodes is not None:
            self.keyboard.press_key(list_ecodes)
        """


# Call main method
if __name__ == '__main__':
    app = MainClass(sys.argv[1])
    sys.exit(0)


