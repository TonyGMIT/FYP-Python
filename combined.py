# Tony Leonard
# G00372842@gmit.ie
# 16th November 2021
import win32gui


def get_title(title, none):
    if win32gui.IsWindowVisible(title):
        titles = (win32gui.GetWindowText(title))
        print(titles)
        if '-' in titles:
            win = titles
            hwnd = win32gui.FindWindow(None, win)
            x0, y0, x1, y1 = win32gui.GetWindowRect(hwnd)
            x0 = -7
            y0 = 0
            x1 = 812
            y1 = 830
            win32gui.MoveWindow(hwnd, x0, y0, x1, y1, True)
        elif '.' in titles:
            win = titles
            hwnd = win32gui.FindWindow(None, win)
            x0, y0, x1, y1 = win32gui.GetWindowRect(hwnd)
            x0 = 792
            y0 = 0
            x1 = 748
            y1 = 830
            win32gui.MoveWindow(hwnd, x0, y0, x1, y1, True)


win32gui.EnumWindows(get_title, None)
