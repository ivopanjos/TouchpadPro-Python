import sys
from evdev import InputDevice
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from ImagesEnum import Images


class ShortcutsTab(QWidget):

    def __init__(self):
        self.dev = InputDevice("/dev/input/event6")
        super(ShortcutsTab, self).__init__()
        grid_main = QGridLayout()

        form_left = QFormLayout()
        form_right = QFormLayout()

        self.add_image(form_left)
        self.add_image(form_right)
        self.add_image(form_left)
        self.add_image(form_right)

        grid_main.addLayout(form_left, 0, 0)
        grid_main.addLayout(form_right, 0, 1)
        self.setLayout(grid_main)

    def add_image(self, v_box):
        image = QPixmap(Images.rotate.value)
        image = image.scaled(32, 32, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        imageLabel = QLabel()
        imageLabel.setPixmap(image)

        button_shortcuts = QPushButton("teste")
        button_shortcuts.clicked.connect(self.change_button_name)

        v_box.addRow(imageLabel, button_shortcuts)

    def change_button_name(self):
        button = self.sender()

        array = list()
        while (True):
            array = self.dev.active_keys()
            if 30 in array:
                break

        button.setText(str(array))


