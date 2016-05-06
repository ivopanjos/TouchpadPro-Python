import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget

from ShortcutsTab import ShortcutsTab
from SpecialShortcutsTab import SpecialShortcutsTab
from AboutTab import AboutTab


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(500, 300)

        self.setWindowTitle("Touchpad Pro")
        self.setCentralWidget(self.add_tabs())

    def add_tabs(self):
        tab_widget = QTabWidget()

        tab_shortcuts = ShortcutsTab()
        tab_special_shortcuts = SpecialShortcutsTab()
        tab_about = AboutTab()

        tab_widget.addTab(tab_shortcuts, "Shortcuts")
        tab_widget.addTab(tab_special_shortcuts, "Special Shortcuts")
        tab_widget.addTab(tab_about, "About")
        return tab_widget


def run():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

run()
