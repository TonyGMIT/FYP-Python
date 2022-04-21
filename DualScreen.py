# Tony Leonard
# G00372842@gmit.ie
# 16th November 2021
# ***Update 20th April 2022***
# This script is not used in final Project.
# It was used in the testing and research of my project.

import win32gui

C1 = '.py' or '.c' or '.java'
C2 = 'Google' or 'Edge' or 'Fox'
C3 = 'Visual'
C4 = 'Teams'
C5 = 'File Explorer'


def get_title(title, none):
    if win32gui.IsWindowVisible(title):
        titles = (win32gui.GetWindowText(title))
        if C1 in titles:  # Coding IDE Formatter
            win = titles
            hwnd = win32gui.FindWindow(None, win)
            x0 = 1530
            y0 = 0
            x1 = 1315
            y1 = 840
            win32gui.MoveWindow(hwnd, x0, y0, x1, y1, True)
        if C2 in titles:  # Web Engine Formatter
            win = titles
            hwnd = win32gui.FindWindow(None, win)
            x0 = -7  # X-axis
            y0 = -5  # Y-axis
            x1 = 812  # Width
            y1 = 840  # Length
            win32gui.MoveWindow(hwnd, x0, y0, x1, y1, True)
        if C3 in titles:
            win = titles
            hwnd = win32gui.FindWindow(None, win)
            x0 = 792
            y0 = -5
            x1 = 748
            y1 = 840
            win32gui.MoveWindow(hwnd, x0, y0, x1, y1, True)
        if C4 in titles:
            win = titles
            hwnd = win32gui.FindWindow(None, win)
            x0 = 2838
            y0 = 0
            x1 = 1000
            y1 = 480
            win32gui.MoveWindow(hwnd, x0, y0, x1, y1, True)
        if C5 in titles:
            win = titles
            hwnd = win32gui.FindWindow(None, win)
            x0 = 2830
            y0 = 500
            x1 = 1020
            y1 = 550
            win32gui.MoveWindow(hwnd, x0, y0, x1, y1, True)


for x in range(4):
    win32gui.EnumWindows(get_title, None)
    if x == 3:
        break
print("Done")
