import sys
from PyQt5.QtWidgets import QWidget, QApplication, QInputDialog, QPushButton
from PyQt5.QtGui import *


class Example(QWidget):
    def __init__(self):
        global xi
        super().__init__()
        self.setWindowIcon(QIcon('Icon.jpg'))
        self.i, self.okBtnPressed = QInputDialog.getInt(self, "Choice", "Выберите сложность", 8, 1, 10, 1)
        xi = 1100 - self.i * 100


xi = 0
app = QApplication(sys.argv)
ex = Example()
