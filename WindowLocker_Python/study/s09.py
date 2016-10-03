import win32gui, win32con, time, sys
import pywintypes
import ctypes
import _thread
from PyQt4.QtGui import *
from PyQt4.QtCore import *

def enumHandler(hwnd, lParam):
    if win32gui.IsWindowVisible(hwnd):
        print(win32gui.GetWindowText(hwnd))
        if 'SENDUP~1' in win32gui.GetWindowText(hwnd):
            win32gui.MoveWindow(hwnd, 0, 0, 760, 500, True)

win32gui.EnumWindows(enumHandler, None)
