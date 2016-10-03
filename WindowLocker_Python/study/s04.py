import win32api
import win32con
import win32gui
from win32 import *


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

win32gui.FindWindow(None, "pydbg")

click(300, 300)
