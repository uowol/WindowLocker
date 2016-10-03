import win32gui, win32con, time, sys
import pywintypes
import _thread

try:
    hwnd1 = win32gui.FindWindow(None, '카카오톡')
except pywintypes.error:
    print('파라미터를 똑바로 넣으시오…')
    sys.exit()
else:
    try:
        eslapetime = int(input('화면이 변하는 시간 간격을 입력해라: '))
    except ValueError:
        print('숫자를 입력해 주시기 바라네..')

    else:
        if eslapetime == 0 or eslapetime is None:
            eslapetime = 1
        win32gui.ShowWindow(hwnd1, win32con.SW_HIDE)


def MaxMin():
    while 1:
        win32gui.ShowWindow(hwnd1, win32con.SW_MINIMIZE)
        time.sleep(eslapetime)
        # win32gui.ShowWindow(hwnd1, win32con.SW_MINIMIZE)
        # win32gui.ShowWindow(hwnd2, win32con.SW_RESTORE)
        # win32gui.ShowWindow(hwnd2, win32con.SW_SHOWMAXIMIZED)
        # time.sleep(eslapetime)


mRect = win32gui.GetWindowRect(hwnd1)
print(mRect)

thread1 = _thread.start_new_thread(MaxMin, ())
code = input('프로세스를 종료하고 싶으면 "비밀번호"를 입력하시오..!')
if code == 'znwlfkrtm':
    win32gui.ShowWindow(hwnd1, win32con.SW_RESTORE)
    win32gui.ShowWindow(hwnd1, win32con.SW_SHOW)
    sys.exit()
