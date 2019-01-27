from PyQt5 import uic
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Table.ui', self)
        self.initui()

    def initui(self):
        self.move(100, 100)
        self.setWindowTitle('Выбор цвета')
        self.setWindowIcon(QIcon('Icon.jpg'))
        a1, a2, a3, a4, a5, a6, a7, a8 = '#FFFFDC', '#CC6666', '#66CC66', '#6666CC', '#CCCC66', '#CC66CC', '#66CCCC', '#DAAA00'

        self.p00.setStyleSheet("background-color: {}".format(a6))
        self.p00.clicked.connect(self.run6)
        self.p10.setStyleSheet("background-color: {}".format(a6))
        self.p10.clicked.connect(self.run6)
        self.p20.setStyleSheet("background-color: {}".format(a8))
        self.p20.clicked.connect(self.run8)
        self.p30.setStyleSheet("background-color: {}".format(a8))
        self.p30.clicked.connect(self.run8)
        self.p40.setStyleSheet("background-color: {}".format(a8))
        self.p40.clicked.connect(self.run8)
        self.p01.setStyleSheet("background-color: {}".format(a6))
        self.p01.clicked.connect(self.run6)
        self.p11.setStyleSheet("background-color: {}".format(a6))
        self.p11.clicked.connect(self.run6)
        self.p21.setStyleSheet("background-color: {}".format(a8))
        self.p21.clicked.connect(self.run8)
        self.p31.setStyleSheet("background-color: {}".format(a5))
        self.p31.clicked.connect(self.run5)
        self.p12.setStyleSheet("background-color: {}".format(a2))
        self.p12.clicked.connect(self.run2)
        self.p22.setStyleSheet("background-color: {}".format(a5))
        self.p22.clicked.connect(self.run5)
        self.p32.setStyleSheet("background-color: {}".format(a5))
        self.p32.clicked.connect(self.run5)
        self.p42.setStyleSheet("background-color: {}".format(a5))
        self.p42.clicked.connect(self.run5)
        self.p13.setStyleSheet("background-color: {}".format(a2))
        self.p13.clicked.connect(self.run2)
        self.p23.setStyleSheet("background-color: {}".format(a2))
        self.p23.clicked.connect(self.run2)
        self.p33.setStyleSheet("background-color: {}".format(a4))
        self.p33.clicked.connect(self.run4)
        self.p04.setStyleSheet("background-color: {}".format(a3))
        self.p04.clicked.connect(self.run3)
        self.p14.setStyleSheet("background-color: {}".format(a3))
        self.p14.clicked.connect(self.run3)
        self.p24.setStyleSheet("background-color: {}".format(a2))
        self.p24.clicked.connect(self.run2)
        self.p34.setStyleSheet("background-color: {}".format(a4))
        self.p34.clicked.connect(self.run4)
        self.p05.setStyleSheet("background-color: {}".format(a7))
        self.p05.clicked.connect(self.run7)
        self.p15.setStyleSheet("background-color: {}".format(a3))
        self.p15.clicked.connect(self.run3)
        self.p25.setStyleSheet("background-color: {}".format(a3))
        self.p25.clicked.connect(self.run3)
        self.p35.setStyleSheet("background-color: {}".format(a4))
        self.p35.clicked.connect(self.run4)
        self.p06.setStyleSheet("background-color: {}".format(a7))
        self.p06.clicked.connect(self.run7)
        self.p16.setStyleSheet("background-color: {}".format(a7))
        self.p16.clicked.connect(self.run7)
        self.p26.setStyleSheet("background-color: {}".format(a7))
        self.p26.clicked.connect(self.run7)
        self.p36.setStyleSheet("background-color: {}".format(a4))
        self.p36.clicked.connect(self.run4)
        self.p9.setStyleSheet("background-color: {}".format(a1))
        self.p9.clicked.connect(self.run9)
        self.show()

    def run2(self):
        color = QColorDialog.getColor()
        if color.isValid():
            x = color.name()
            x = x.upper()
            NUM_COLORS[1] = int('0x' + x[1:], 16)
            self.p12.setStyleSheet("background-color: {}".format(x))
            self.p13.setStyleSheet("background-color: {}".format(x))
            self.p23.setStyleSheet("background-color: {}".format(x))
            self.p24.setStyleSheet("background-color: {}".format(x))

    def run3(self):
        color = QColorDialog.getColor()
        if color.isValid():
            x = color.name()
            x = x.upper()
            NUM_COLORS[2] = int('0x' + x[1:], 16)
            self.p04.setStyleSheet("background-color: {}".format(x))
            self.p14.setStyleSheet("background-color: {}".format(x))
            self.p15.setStyleSheet("background-color: {}".format(x))
            self.p25.setStyleSheet("background-color: {}".format(x))

    def run4(self):
        color = QColorDialog.getColor()
        if color.isValid():
            x = color.name()
            x = x.upper()
            NUM_COLORS[3] = int('0x' + x[1:], 16)
            self.p33.setStyleSheet("background-color: {}".format(x))
            self.p34.setStyleSheet("background-color: {}".format(x))
            self.p35.setStyleSheet("background-color: {}".format(x))
            self.p36.setStyleSheet("background-color: {}".format(x))

    def run5(self):
        color = QColorDialog.getColor()
        if color.isValid():
            x = color.name()
            x = x.upper()
            NUM_COLORS[4] = int('0x' + x[1:], 16)
            self.p22.setStyleSheet("background-color: {}".format(x))
            self.p32.setStyleSheet("background-color: {}".format(x))
            self.p42.setStyleSheet("background-color: {}".format(x))
            self.p31.setStyleSheet("background-color: {}".format(x))

    def run6(self):
        color = QColorDialog.getColor()
        if color.isValid():
            x = color.name()
            x = x.upper()
            NUM_COLORS[5] = int('0x' + x[1:], 16)
            self.p00.setStyleSheet("background-color: {}".format(x))
            self.p10.setStyleSheet("background-color: {}".format(x))
            self.p01.setStyleSheet("background-color: {}".format(x))
            self.p11.setStyleSheet("background-color: {}".format(x))

    def run7(self):
        color = QColorDialog.getColor()
        if color.isValid():
            x = color.name()
            x = x.upper()
            NUM_COLORS[6] = int('0x' + x[1:], 16)
            self.p05.setStyleSheet("background-color: {}".format(x))
            self.p06.setStyleSheet("background-color: {}".format(x))
            self.p16.setStyleSheet("background-color: {}".format(x))
            self.p26.setStyleSheet("background-color: {}".format(x))

    def run8(self):
        color = QColorDialog.getColor()
        if color.isValid():
            x = color.name()
            x = x.upper()
            NUM_COLORS[7] = int('0x' + x[1:], 16)
            self.p21.setStyleSheet("background-color: {}".format(x))
            self.p20.setStyleSheet("background-color: {}".format(x))
            self.p30.setStyleSheet("background-color: {}".format(x))
            self.p40.setStyleSheet("background-color: {}".format(x))

    def run9(self):
        color = QColorDialog.getColor()
        if color.isValid():
            x = color.name()
            x = x.upper()
            NUM_COLORS[0] = int('0x' + x[1:], 16)
            self.p9.setStyleSheet("background-color: {}".format(x))

NUM_COLORS = [0xFFFFDC, 0xCC6666, 0x66CC66, 0x6666CC,
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]
a = QApplication(sys.argv)
e = MyWidget()
e.show()
