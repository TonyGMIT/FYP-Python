# Tony Leonard
# G00372842@gmit.ie
# 3rd November 2021
# ***Update 20th April 2022***
# This script is not used in final Project.
# It was used in the testing and research of my project.

import win32gui


def get_title(title, none):
    if win32gui.IsWindowVisible(title):
        titles = (win32gui.GetWindowText(title))
        if '-' in titles:
            print(titles)
        elif '.' in titles:
            print(titles)
        elif '|' in titles:
            print(titles)


win32gui.EnumWindows(get_title, None)
