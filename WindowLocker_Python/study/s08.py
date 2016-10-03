from PyQt4.QtGui import QLabel, QPainter
from PyQt4.QtCore import QSize
from PyQt4 import QtCore, QtGui
import sys

class MyLabel(QtGui.QWidget):
    def __init__(self, text=None):
        super(self.__class__, self).__init__()
        self.text = text

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setPen(QtCore.Qt.black)
        painter.translate(20, 100)
        painter.rotate(-90)
        if self.text:
            painter.drawText(0, 0, self.text)
        painter.end()

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        lbl1 = MyLabel('lbl 1')
        lbl2 = MyLabel('lbl 2')
        lbl3 = MyLabel('lbl 3')
        hBoxLayout = QtGui.QHBoxLayout()
        hBoxLayout.addWidget(lbl1)
        hBoxLayout.addWidget(lbl2)
        hBoxLayout.addWidget(lbl3) 
        self.setLayout(hBoxLayout)
        self.setGeometry(300, 300, 250, 150) 
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()