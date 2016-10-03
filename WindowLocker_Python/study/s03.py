import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("s03")
        self.setGeometry(300, 300, 300, 400)

        btn1 = QPushButton("Click Meeeee", self)
        btn1.move(20, 20)
        btn1.clicked.connect(self.btn1_clicked)

    def btn1_clicked(self):
        QMessageBox.about(self, "sEEEs", "clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
