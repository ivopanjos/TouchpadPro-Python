import time
from ewmh import EWMH
ewmh = EWMH()

# get the active window

while True:

    win = ewmh.getActiveWindow()
    print(ewmh.getWmName(win))
    print(win.get_wm_class())
    time.sleep(2)

