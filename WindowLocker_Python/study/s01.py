import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

app = QApplication(sys.argv)
label = QLabel("Hello World")
label.show()
app.exec_()
