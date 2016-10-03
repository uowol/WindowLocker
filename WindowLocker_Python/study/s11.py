import win32gui, win32con, time, sys
import pywintypes
import _thread
import pyHook
from PyQt4.QtGui import *
from PyQt4.QtCore import *
# import os
# import win32com.shell.shell as shell
# ASADMIN = 'asadmin'

mypassword = ""
password = "Numpad8Numpad5Numpad4Numpad6"
# password = "8546"
name = "사진"

# if sys.argv[-1] != ASADMIN:
#     script = os.path.abspath(sys.argv[0])
#     params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
#     shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)

try:
    hwnd1 = win32gui.FindWindow(None, name)
except pywintypes.error:
    sys.exit(0)

mPlacement = win32gui.GetWindowPlacement(hwnd1)
print(mPlacement)



def OnKeyboardEvent(event):
    if event.Ascii < 49 or event.Ascii > 57:
        hm.UnhookKeyboard()
        print("is canceled")
    global mypassword
    if(len(mypassword) >= 28):
        mypassword = ""
    mypassword = mypassword + str(event.Key)
    print(mypassword)
    return True


hm = pyHook.HookManager()

hm.KeyDown = OnKeyboardEvent

hm.HookKeyboard()


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
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

        vBoxLayout = QVBoxLayout()
        vBoxLayout.setAlignment(Qt.AlignCenter)

        label = QLabel(self)
        label.setMinimumSize(width, height)
        label.setAlignment(Qt.AlignCenter)
        # label.setFrameShape(QFrame.StyledPanel)
        image = QImage("locker.png")
        label.setPixmap(QPixmap.fromImage(image))
        vBoxLayout.addChildWidget(label)

        root = QWidget()
        root.setMinimumSize(width, height)
        root.setLayout(vBoxLayout)

        self.setCentralWidget(root)


# def enumHandler(hwnd, lParam):
#     if win32gui.IsWindowVisible(hwnd):
#         print(win32gui.GetWindowText(hwnd))
#         if 'SENDUP~1' in win32gui.GetWindowText(hwnd):
#             win32gui.MoveWindow(hwnd, 0, 0, 760, 500, True)
#
# win32gui.EnumWindows(enumHandler, None)

def start():
    # mPlacement = win32gui.GetWindowPlacement(hwnd1)
    # x = mPlacement[4][0] + 8
    # y = mPlacement[4][1] + 31
    # width = mPlacement[4][2] - mPlacement[4][0] - 15.5
    # height = mPlacement[4][3] - mPlacement[4][1] - 39
    # myWindow.setGeometry(x, y, width, height)

    while 1:
        global mypassword
        # global data
        if not password == mypassword:
            try:
                # print(data)
                # 야 시바 되으따아앙아ㅏ!!!
                mGround = win32gui.GetWindowText(win32gui.GetForegroundWindow())
                if not name in mGround:
                    win32gui.ShowWindow(hwnd1, win32con.SW_MINIMIZE)
                mPlacement = win32gui.GetWindowPlacement(hwnd1)
                x = mPlacement[4][0] + 8
                y = mPlacement[4][1] + 31
                width = mPlacement[4][2] - mPlacement[4][0] - 15.5
                height = mPlacement[4][3] - mPlacement[4][1] - 39
                myWindow.setGeometry(x, y, width, height)
                # myWindow.show()
                if mPlacement[1] == 2:
                    # myWindow.setWindowFlags(Qt.FramelessWindowHint)
                    # hm.UnHookKeyboard()
                    myWindow.hide()
                if mPlacement[1] == 1:
                    hm.HookKeyboard()
                    myWindow.show()
            except:
                # 비활성화 시 미니미즈
                # myWindow.setWindowFlags(Qt.FramelessWindowHint)
                print(BaseException)
                myWindow.hide()
                break
        else:
            myWindow.hide()
            # data = False
            break
    print("Canceled")


# def finish():
#     while 1:
#         global data
#         str = ""
#         for i in range(4):
#             str = str + input()
#             print(str)
#         if str == password:
#             data = True
#             myWindow.hide()
#             print("Success")
#         else:
#             print("Failed")


def push():
    import pythoncom
    pythoncom.PumpMessages()


if __name__ == "__main__":
    # global data
    # data = False
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    # finish = _thread.start_new_thread(finish, ())
    start = _thread.start_new_thread(start, ())
    push = _thread.start_new_thread(push, ())
    app.exec_()

    # time.sleep(1)
    # unlock = 0

#
# (961, 141, 1323, 861)
# (961, 141, 1323, 610)
# (770, 242, 1132, 711)
# (770, 262, 1132, 731)
#
#
