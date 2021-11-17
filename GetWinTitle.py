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
