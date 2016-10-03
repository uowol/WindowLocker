import win32gui, win32con, time, sys
import pywintypes
import _thread
from PyQt4.QtGui import *
from PyQt4.QtCore import *

Actived = False
Locking = True
password = "'8''5''4''6'"
name = "사진"
mPassword = ""

def lock():
    while Locking:
        try:

            hwnd1 = win32gui.FindWindow(None, name)

            mPlacement = win32gui.GetWindowPlacement(hwnd1)
            print(mPlacement)


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

            def start():
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
                            print(BaseException)
                            myWindow.hide()
                            break
                    else:
                        myWindow.hide()
                        break
                print("Canceled")
                Locking = False

            def nput():
                from pynput.keyboard import Key, Listener

                def on_press(key):
                    print(str(key))
                    global mPassword
                    if Actived:

                        if len(mPassword) >= 12:
                            mPassword = ""
                        if len(mPassword) >= 0:
                            myWindow.updateUI("locker_1.png")

                        mPassword = mPassword + str(key)
                        print(mPassword)

                with Listener(
                        on_press=on_press) as listener:
                    listener.join()


            if __name__ == "__main__":
                app = QApplication(sys.argv)
                myWindow = MyWindow()
                myWindow.show()
                start = _thread.start_new_thread(start, ())
                nput = _thread.start_new_thread(nput, ())
                app.exec_()

        except pywintypes.error:
            print("finding...")
    print("종료")
    lock()
lock()