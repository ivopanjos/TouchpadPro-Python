import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class AboutTab(QWidget):

    def __init__(self):
        super(AboutTab, self).__init__()
        grid_main = QGridLayout()
        self.setLayout(grid_main)

