import win32gui, win32con, time, sys
import pywintypes
import _thread
import pyHook

name = "사진"
mypassword = ""


def OnKeyboardEvent(event):
    if event.Ascii < 49 or event.Ascii > 57:
        hm.UnhookKeyboard()
        print("is canceled")
    global mypassword
    if (len(mypassword) >= 28):
        mypassword = ""
    mypassword = mypassword + str(event.Key)
    print(mypassword)
    return True

try:
    hwnd1 = win32gui.FindWindow(None, name)
except pywintypes.error:
    sys.exit(0)

def push():
    while True:

        mGround = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        if not name in mGround:
            win32gui.ShowWindow(hwnd1, win32con.SW_MINIMIZE)

        mPlacement = win32gui.GetWindowPlacement(hwnd1)

        print(mPlacement)
        time.sleep(1)
#
#
#
# # if __name__ == "__main__":
push = _thread.start_new_thread(push, ())


hm = pyHook.HookManager()

hm.KeyDown = OnKeyboardEvent

hm.HookKeyboard()
import pythoncom
pythoncom.PumpMessages()
#


