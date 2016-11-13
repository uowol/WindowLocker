import win32gui, win32con, time, sys
import pywintypes
import _thread
from PyQt4.QtGui import *
from PyQt4.QtCore import *

Actived = False
Stopped = False
password = ""
name = "공일_프라이버시"  # 이름바꾸는 메소드를 만들어야
mPassword = ""
passwords = ["'0'","'1'","'2'","'3'","'4'","'5'","'6'","'7'","'8'","'9'"]

"""
[setting.txt]
비밀번호
setting.txt, 프로그램이름1, 프로그램이름2, 프로그램이름3, 프로그램이름4, 프로그램이름5, ...

# \n으로 나눠서 두 줄을 읽어오고, ','으로 나눠서 잠그고자 하는 프로그램명 읽기
"""

# 위 기능 구현
text = ''
with open('setting.txt', encoding="utf-8") as f:
    text = f.read().split('\n')
print(text, type(text), len(text))
pw = text[0].split(',')
print(pw)
print(password)
for key in pw:
    password = password + "'" + key + "'"
print(password)
names = text[1].split(',')
print(names)
# 여기까지


def finding():
    global name
    global height, width

    while 1:
        try:
            mGround = win32gui.GetWindowText(win32gui.GetForegroundWindow())
            if mGround in names:
                print("finding:", mGround)
                name = mGround
                hwnd1 = win32gui.FindWindow(None, name)
                mPlacement = win32gui.GetWindowPlacement(hwnd1)
                width = mPlacement[4][2] - mPlacement[4][0] - 15.5
                height = mPlacement[4][3] - mPlacement[4][1] - 39

                return hwnd1, mPlacement
                break

        except pywintypes.error:
            print("finding...")


hwnd1 = finding()[0]
mPlacement = finding()[1]
width = mPlacement[4][2] - mPlacement[4][0] - 15.5
height = mPlacement[4][3] - mPlacement[4][1] - 39
print(hwnd1, mPlacement)

def start():

    global hwnd1
    global Actived
    global mPassword
    global mPlacement
    myWindow.hideAll()
    myWindow.locker0.setVisible(True)
    while 1:
        if not password == mPassword:
            try:
                mGround = win32gui.GetWindowText(win32gui.GetForegroundWindow())  # 다수 처리할 때 이거 쓰면 될듯
                if not name == mGround:
                    Actived = False
                    print(mGround)
                    win32gui.ShowWindow(hwnd1, win32con.SW_MINIMIZE)
                    mPassword = ""
                    global Stopped
                    Stopped = True
                    myWindow.hide()
                    break
                mPlacement = win32gui.GetWindowPlacement(hwnd1)
                x = mPlacement[4][0] + 8
                y = mPlacement[4][1] + 31
                width = mPlacement[4][2] - mPlacement[4][0] - 15.5
                height = mPlacement[4][3] - mPlacement[4][1] - 39
                myWindow.backGround.setMinimumHeight(height)
                myWindow.backGround.setMaximumHeight(height)
                myWindow.backGround.setMinimumWidth(width)
                myWindow.backGround.setMaximumWidth(width)
                myWindow.locker0.setMinimumHeight(height)
                myWindow.locker0.setMaximumHeight(height)
                myWindow.locker0.setMinimumWidth(width)
                myWindow.locker0.setMaximumWidth(width)
                myWindow.locker1.setMinimumHeight(height)
                myWindow.locker1.setMaximumHeight(height)
                myWindow.locker1.setMinimumWidth(width)
                myWindow.locker1.setMaximumWidth(width)
                myWindow.locker2.setMinimumHeight(height)
                myWindow.locker2.setMaximumHeight(height)
                myWindow.locker2.setMinimumWidth(width)
                myWindow.locker2.setMaximumWidth(width)
                myWindow.locker3.setMinimumHeight(height)
                myWindow.locker3.setMaximumHeight(height)
                myWindow.locker3.setMinimumWidth(width)
                myWindow.locker3.setMaximumWidth(width)
                myWindow.locker4.setMinimumHeight(height)
                myWindow.locker4.setMaximumHeight(height)
                myWindow.locker4.setMinimumWidth(width)
                myWindow.locker4.setMaximumWidth(width)
                if mPlacement[1] == 2:
                    Actived = False
                    myWindow.hide()
                if mPlacement[1] == 1:
                    Actived = True
                    myWindow.setGeometry(x, y, width, height)
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


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        print(self)
        self.setupUI()

    def setupUI(self):
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(15, 30, 33))
        self.setPalette(palette)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        x = mPlacement[4][0] + 8
        y = mPlacement[4][1] + 31
        self.setGeometry(x, y, width, height)

        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.setAlignment(Qt.AlignCenter)

        self.backGround = QLabel(self)
        self.locker0 = QLabel(self)
        self.locker1 = QLabel(self)
        self.locker2 = QLabel(self)
        self.locker3 = QLabel(self)
        self.locker4 = QLabel(self)
        self.updateUI("back.jpg", self.backGround)
        self.updateUI("locker.png", self.locker0)
        self.updateUI("locker_1.png", self.locker1)
        self.updateUI("locker_2.png", self.locker2)
        self.updateUI("locker_3.png", self.locker3)
        self.updateUI("locker_4.png", self.locker4)
        self.hideAll()
        self.locker0.setVisible(True)
        root = QWidget()
        root.setMinimumSize(0, 0)
        root.setLayout(self.vBoxLayout)

        self.setCentralWidget(root)

    def updateUI(self, img, label):
        image = QImage(img)
        label.setMinimumSize(width, height)
        label.setMaximumSize(width, height)
        label.setAlignment(Qt.AlignCenter)
        label.setPixmap(QPixmap.fromImage(image))
        print(width, height)
        self.vBoxLayout.addChildWidget(label)

    def resizeUI(self, label):
        label.setMinimumSize(width, height)

    def hideAll(self):
        self.locker0.setVisible(False)
        self.locker1.setVisible(False)
        self.locker2.setVisible(False)
        self.locker3.setVisible(False)
        self.locker4.setVisible(False)


    def swapImg(self, i):
        if i == 0:
            self.locker0.setVisible(False)
            self.locker1.setVisible(True)
        if i == 1:
            self.locker1.setVisible(False)
            self.locker2.setVisible(True)
        if i == 2:
            self.locker2.setVisible(False)
            self.locker3.setVisible(True)
        if i == 3:
            self.locker3.setVisible(False)
            self.locker4.setVisible(True)
        if i == 4:
            self.locker4.setVisible(False)
            self.locker0.setVisible(True)


def nput():
    from pynput.keyboard import Key, Listener

    def on_press(key):
        if str(key) in passwords:
            print(str(key))
            global mPassword
            if Actived:
                if mPassword == "":
                    myWindow.swapImg(0)
                if len(mPassword) == 3:
                    myWindow.swapImg(1)
                if len(mPassword) == 6:
                    myWindow.swapImg(2)
                if len(mPassword) == 9:
                    myWindow.swapImg(3)
                    time.sleep(0.5)
                    myWindow.swapImg(4)

                if len(mPassword) >= 12:
                    myWindow.swapImg(0)
                    mPassword = ""


                mPassword = mPassword + str(key)
                print(mPassword)

    with Listener(on_press=on_press) as listener:
        listener.join()


def isStopped():
    import time
    global Stopped, mPlacement, hwnd1
    while (1):
        if (Stopped):
            mGround = win32gui.GetWindowText(win32gui.GetForegroundWindow())
            # print("부활대기중")
            # print(mGround, name)
            # time.sleep(5)  # 1분으로 설정하자. // 1분 넘게 그 화면에 있을 필요가 있을수도 ex) 카카오톡
            if(mGround != name):
                print("부!활!")
                Stopped = False
                hwnd1 = finding()[0]
                mPlacement = finding()[1]
                print(width, height)
                _thread.start_new_thread(start, ())
        time.sleep(0.5)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.type()
    myWindow = MyWindow()
    myWindow.show()

    _thread.start_new_thread(start, ())
    _thread.start_new_thread(nput, ())
    _thread.start_new_thread(isStopped, ())
    app.exec_()
    print("나왔다!")

print("종료")
