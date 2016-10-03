import sys

from PyQt4.QtGui import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("s02")
        self.setGeometry(300, 300, 300, 400)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
