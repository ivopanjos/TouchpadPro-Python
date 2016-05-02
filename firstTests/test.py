from evdev import InputDevice, ecodes, UInput
import sys
from ewmh import EWMH


class MainClass:

    totalXDist = 2436
    totalYDist = 1044

    halfTotalXDist = totalXDist / 2
    halfTotalYDist = totalYDist / 2

    minSwipeXDist = 150     # 1/16 aproximate total distance
    minSwipeYDist = 20

    def __init__(self):
        self.dev = InputDevice('/dev/input/event2')
        self.ewmh = EWMH()

        # initialize normal variables and start reading
        self.x = -1
        self.y = -1

        # self.readInput(self.dev)
        # self.testMouse(self.dev)

        """
        ui = UInput()
        ui.write(ecodes.EV_KEY, ecodes.KEY_A, 1)  # KEY_A down
        ui.write(ecodes.EV_KEY, ecodes.KEY_A, 0)  # KEY_A up
        ui.syn()

        ui.close()
        """


    def test_mouse(self, dev):
        for event in dev.read_loop():
            print(event)
            
    def read_input(self, dev):
        first_time_x = True
        first_time_y = True
        double_tap = False
        x = -1
        y = -1

        for event in dev.read_loop():
            if event.type == ecodes.EV_KEY:
                if event.code == ecodes.BTN_TOOL_double_tap:        # catched a double tap
                    double_tap = True

            if event.type == ecodes.EV_ABS:     # absolute press

                # x event
                if event.code == ecodes.ABS_X:
                    if first_time_x:
                        x = event.value
                        first_time_x = False
                    self.x = event.value

                # y event
                if event.code == ecodes.ABS_Y:
                    if first_time_y:
                        y = event.value
                        first_time_y = False
                    self.y = event.value

                # maybe release touchpad event
                if event.code == ecodes.ABS_TOOL_WIDTH:
                    if event.value == 0:                                # release touchpad
                        self.print_pos(x, y, self.x,self.y, double_tap)
                        self.reset_variables()
                        x = -1
                        y = -1
                        first_time_x = True
                        first_time_y = True
                        double_tap = False
                        
    def print_pos(self, x1, y1, x2, y2, double_tap):
        # print ("first x: " + str(x1) + ", first y: " + str(y1))
        # print ("x: " + str(x2) + ", y: " + str(y2))

        if double_tap:      # swipe if its in double tap mode
            self.swipe(x1, y1, x2, y2)
        print()
    # self.test_window()

    def test_window(self):
        win = self.ewmh.getActiveWindow()
        print(win.get_wm_class()[0])
        print(win.get_wm_class()[1])

    def move_window_to_desktop(self, window, desktop):
        """
        Move the window to the given desktop number
        :param window
        :param desktop: number
        """
        self.ewmh.setWmDesktop(window, desktop)

    def move_to_desktop(self, desktop):
        """
        Change the current workspace to the given desktop number
        :param desktop: number
        """
        self.ewmh.setcurrent_desktop(desktop)
        
    def choose_desktop(self, swipe, current_desktop, total_desktop):
        """
        Calculate the desktop to move to.
        :param swipe: number (-1 or 1, swipe left or right)
        :param current_desktop: number
        :param total_desktop: total number of desktops
        """

        total = total_desktop - 1
        action = current_desktop + swipe
        if action < 0:
            return total
        elif action > total:
            return 0
        else:
            return action

    def swipe_move(self, x):
        """
        Given a swipe move changes to the respective desktop
        :param swipe: number (-1 or 1, swipe left or right)
        """

        win = self.ewmh.getActiveWindow()
        current_desktop = self.ewmh.getcurrent_desktop()
        total_desktops = self.ewmh.getNumberOfDesktops()
        desktop = self.choose_desktop(x, current_desktop, total_desktops)
        # self.move_window_to_desktop(win, desktop)
        self.move_to_desktop(desktop)
        self.ewmh.display.flush()

    def swipe(self, x1, y1, x2, y2):
        x = x2 - x1
        y = y2 - y1

        print("x1: " + str(x1) + ", x2: " + str(x2))
        self.swipe_horizontal(x)
    # self.swipe_vertical(y)

    def swipe_horizontal(self, x):
        if abs(x) < MainClass.minSwipeXDist:
            print(x)
            print("no swipe")
        elif x > 0:
            self.swipe_move(-1)
        # print(x)
        # print("swipe left to right")
        else:
            self.swipe_move(1)
        # print(x)
        # print("swipe right to left")
        pass

    def swipe_vertical(self, y):
        if abs(y) < MainClass.minSwipeYDist:
            print("no swipe")
        elif y > 0:
            print("swipe top to bottom")
        else:
            print("swipe bottom to top")


    def figure_out_pos_in_touchpad(self, x, y):
        if x < MainClass.halfTotalXDist:
            if y < MainClass.halfTotalYDist:
                print ("A")
            else:
                print ("C")
        else:   # x > MainClass.halfTotalXDist
            if y < MainClass.halfTotalYDist:
                print ("B")

            else:
                print ("D")

    def reset_variables(self):
        self.x = -1
        self.y = -1

    def emit_key_press(self, key):
        self.device.emit_click(key)
        # self.device.emit_click(uinput.KEY_B)

# Call main method
if __name__ == '__main__':
    app = MainClass()
    sys.exit(0)

