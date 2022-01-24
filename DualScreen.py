# Tony Leonard
# G00372842@gmit.ie
# 16th November 2021
import win32gui


def get_title(title, none):
    if win32gui.IsWindowVisible(title):
        titles = (win32gui.GetWindowText(title))
        if 'Google' in titles or 'Edge' in titles or 'Fox' in titles:   # Web Engine Formatter
            print(titles)
            win = titles
            hwnd = win32gui.FindWindow(None, win)
            x0 = -7     # X-axis
            y0 = -5     # Y-axis
            x1 = 812    # Width
            y1 = 840    # Length
            win32gui.MoveWindow(hwnd, x0, y0, x1, y1, True)
        if 'YouTube' in titles:
            print(titles)
            win = titles
            hwnd = win32gui.FindWindow(None, win)
            x0 = 792
            y0 = -5
            x1 = 748
            y1 = 840
            win32gui.MoveWindow(hwnd, x0, y0, x1, y1, True)
        if '.py' in titles or '.c' in titles or '.java' in titles:  # Coding IDE Formatter
            print(titles)
            win = titles
            hwnd = win32gui.FindWindow(None, win)
            x0 = 1530
            y0 = 22
            x1 = 1315
            y1 = 815
            win32gui.MoveWindow(hwnd, x0, y0, x1, y1, True)
        if 'Teams' in titles:
            print(titles)
            win = titles
            hwnd = win32gui.FindWindow(None, win)
            x0 = 2830
            y0 = 22
            x1 = 780
            y1 = 480
            win32gui.MoveWindow(hwnd, x0, y0, x1, y1, True)
        if 'File Explorer' in titles:
            print(titles)
            win = titles
            hwnd = win32gui.FindWindow(None, win)
            x0 = 2830
            y0 = 520
            x1 = 780
            y1 = 550
            win32gui.MoveWindow(hwnd, x0, y0, x1, y1, True)


win32gui.EnumWindows(get_title, None)
