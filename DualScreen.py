# Tony Leonard
# G00372842@gmit.ie
# 16th November 2021
import win32gui

T1 = 'Google' or 'Edge' or 'Fox'
T2 = 'YouTube'
T3 = '.py' or '.c' or '.java'
T4 = 'Teams'
T5 = 'File Explorer'


def get_title(title, none):
    if win32gui.IsWindowVisible(title):
        titles = (win32gui.GetWindowText(title))

        if T1 in titles:   # Web Engine Formatter
            print(titles)
            win = titles
            hwnd = win32gui.FindWindow(None, win)
            x0 = -7     # X-axis
            y0 = -5     # Y-axis
            x1 = 812    # Width
            y1 = 840    # Length
            win32gui.MoveWindow(hwnd, x0, y0, x1, y1, True)
        if T2 in titles:
            print(titles)
            win = titles
            hwnd = win32gui.FindWindow(None, win)
            x0 = 792
            y0 = -5
            x1 = 748
            y1 = 840
            win32gui.MoveWindow(hwnd, x0, y0, x1, y1, True)
        if T3 in titles:  # Coding IDE Formatter
            print(titles)
            win = titles
            hwnd = win32gui.FindWindow(None, win)
            x0 = 1530
            y0 = 0
            x1 = 1315
            y1 = 840
            win32gui.MoveWindow(hwnd, x0, y0, x1, y1, True)
        if T4 in titles:
            print(titles)
            win = titles
            hwnd = win32gui.FindWindow(None, win)
            x0 = 2830
            y0 = 0
            x1 = 1010
            y1 = 480
            win32gui.MoveWindow(hwnd, x0, y0, x1, y1, True)
        if T5 in titles:
            print(titles)
            win = titles
            hwnd = win32gui.FindWindow(None, win)
            x0 = 2830
            y0 = 500
            x1 = 1020
            y1 = 550
            win32gui.MoveWindow(hwnd, x0, y0, x1, y1, True)


win32gui.EnumWindows(get_title, None)
