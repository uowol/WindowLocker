import pyHook

def Log(logStr):
    print(str(logStr))
    # hm.UnhookKeyboard()


def OnKeyboardEvent(event):
    # global data
    # if len(data) == 4:
    #     data = 0
    # s = ""
    # Log('MessageName:' + str(event.MessageName))
    # Log('Message:' + str(event.Message))
    # Log('Time:' + str(event.Time))
    # Log('Window:' + str(event.Window))
    Log('Window:' + str(event.Ascii))
    Log('Window:' + str(event.Key))
    # if str(event.Key) == 'Numpad8':

    #     Log("이야 시바 되뜨라아앙")
    return True

hm = pyHook.HookManager()

hm.KeyDown = OnKeyboardEvent

hm.HookKeyboard()

if __name__ == '__main__':
    import pythoncom
    pythoncom.PumpMessages()