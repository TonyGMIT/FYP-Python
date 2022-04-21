# Tony Leonard
# G00372842@gmit.ie
# 20th November 2021
# ***Update 20th April 2022***
# This script is not used in final Project.
# It was used in the testing and research of my project.

import win32gui


def get_title(title, none):
    if win32gui.IsWindowVisible(title):
        titles = (win32gui.GetWindowText(title))
        if 'Google' in titles or 'Edge' in titles or 'Fox' in titles:
            print(titles)
            win = titles
            hwnd = win32gui.FindWindow(None, win)
            x0 = -7     # X-axis
            y0 = -5     # Y-axis
            x1 = 812    # Width
            y1 = 840    # Length
            win32gui.MoveWindow(hwnd, x0, y0, x1, y1, True)
        if '.py' in titles or '.c' in titles or '.java' in titles:
            print(titles)
            win = titles
            hwnd = win32gui.FindWindow(None, win)
            x0 = 792
            y0 = -7
            x1 = 748
            y1 = 830
            win32gui.MoveWindow(hwnd, x0, y0, x1, y1, True)


for x in range(3):
    win32gui.EnumWindows(get_title, None)
    if x == 2:
        break
        print("Done")
