import win32gui, win32con, time, sys
import pywintypes
import _thread
from PyQt4.QtGui import *
from PyQt4.QtCore import *

Actived = False
Stopped = False
password = "'8''5''4''6'"
name = "공일_프라이버시"
mPassword = ""


def finding():
    while 1:
        try:
            hwnd1 = win32gui.FindWindow(None, name)
            mPlacement = win32gui.GetWindowPlacement(hwnd1)
            return hwnd1, mPlacement
            break

        except pywintypes.error:
            print("finding...")


hwnd1 = finding()[0]
mPlacement = finding()[1]
print(hwnd1, mPlacement)


def start():
    global hwnd1
    global Actived
    global mPassword
    while 1:
        if not password == mPassword:
            try:
                mGround = win32gui.GetWindowText(win32gui.GetForegroundWindow())
                if not name in mGround:
                    win32gui.ShowWindow(hwnd1, win32con.SW_MINIMIZE)
                mPlacement = win32gui.GetWindowPlacement(hwnd1)
                x = mPlacement[4][0] + 8
                y = mPlacement[4][1] + 31
                width = mPlacement[4][2] - mPlacement[4][0] - 15.5
                height = mPlacement[4][3] - mPlacement[4][1] - 39
                myWindow.setGeometry(x, y, width, height)
                if mPlacement[1] == 2:
                    Actived = False
                    myWindow.hide()
                if mPlacement[1] == 1:
                    Actived = True
                    myWindow.show()
            except:
                print("Error")
                myWindow.hide()
                break
        else:
            mPassword = ""
            global Stopped
            Stopped = True
            myWindow.hide()
            break
    print("끝")
    hwnd1, mPlacement = finding()


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        print(self)
        self.setupUI()

    def setupUI(self):
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(19, 30, 33))
        self.setPalette(palette)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        x = mPlacement[4][0] + 8
        y = mPlacement[4][1] + 31
        width = mPlacement[4][2] - mPlacement[4][0] - 15.5
        height = mPlacement[4][3] - mPlacement[4][1] - 39
        self.setGeometry(x, y, width, height)

        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.setAlignment(Qt.AlignCenter)

        self.label = QLabel(self)
        self.label.setMinimumSize(width, height)
        self.label.setAlignment(Qt.AlignCenter)
        image = QImage("locker.png")
        self.label.setPixmap(QPixmap.fromImage(image))
        self.vBoxLayout.addChildWidget(self.label)

        root = QWidget()
        root.setMinimumSize(width, height)
        root.setLayout(self.vBoxLayout)

        self.setCentralWidget(root)

    def updateUI(self, img):
        image = QImage(img)
        self.label.setPixmap(QPixmap.fromImage(image))
        self.vBoxLayout.update()


def nput():
    from pynput.keyboard import Key, Listener

    def on_press(key):
        print(str(key))
        global mPassword
        if Actived:

            if len(mPassword) >= 12:
                mPassword = ""
            # if len(mPassword) >= 0:
            #     myWindow.updateUI("locker_1.png")

            mPassword = mPassword + str(key)
            print(mPassword)

    with Listener(
            on_press=on_press) as listener:
        listener.join()


def isStopped():
    import time
    global Stopped
    while (1):
        if (Stopped):
            print("부활대기중")
            time.sleep(5)
            print("부!활!")
            Stopped = False
            _thread.start_new_thread(start, ())
        time.sleep(5)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.type()
    myWindow = MyWindow()
    myWindow.show()
    _thread.start_new_thread(start, ())
    _thread.start_new_thread(nput, ())
    _thread.start_new_thread(isStopped, ())
    app.exec_()
    print("나왔다!")  # 안나와...

print("종료")
