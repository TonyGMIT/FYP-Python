# Tony Leonard
# G00372842@gmit.ie
# 29th October 2021
# ***Update 20th April 2022***
# This script is not used in final Project.
# It was used in the testing and research of my project.

import win32gui

py1 = 'New Tab - Google Chrome'
ch1 = 'YouTube - Google Chrome'
ch2 = ''

hwnd1 = win32gui.FindWindow(None, py1)
hwnd2 = win32gui.FindWindow(None, ch1)

x0, y0, x1, y1 = win32gui.GetWindowRect(hwnd1)
x2, y2, x3, y3 = win32gui.GetWindowRect(hwnd2)

x0 = -7  # X-axis
y0 = -5  # Y-axis
x1 = 812  # Width
y1 = 840  # Length

x2 = 792  # 1530
y2 = 0
x3 = 748
y3 = 830

win32gui.MoveWindow(hwnd1, x0, y0, x1, y1, True)
win32gui.MoveWindow(hwnd2, x2, y2, x3, y3, True)
