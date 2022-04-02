import win32gui
from win32gui import GetForegroundWindow
import psutil  # cross-platform library for receiving info on running processes
import time  # provides various functions to manipulate time values
import win32process  # GetWindowThreadProcessId: Retrieves the identifier of the thread and process that created the specified window.
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
myDB = client["SmartTabs"]
myInfo = myDB["MouseTracker"]

usageTime = {}
timeStamp = {}

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0

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
            x0 = 2830
            y0 = 0
            x1 = 1010
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

while True:
    currentApp = psutil.Process(win32process.GetWindowThreadProcessId(GetForegroundWindow())[1]).name().replace(".exe", "")
    App = currentApp.replace("explorer", "File Navigation")  # changes explorer to file navigation to represent both file explorer and desktop navigation
    timeStamp[App] = int(time.time())
    time.sleep(1)  # delays for 1 second
    if App not in usageTime.keys():  # .keys() not needed
        usageTime[App] = 0

    timeVar2 = int(time.time()) - timeStamp[App]
    usageTime[App] = usageTime[App] + int(time.time()) - timeStamp[App]
    timeVar = usageTime[App]

    if timeVar % 360 == 0:
        if "pycharm64" in App:
            count1 += 0.10
            print(App, count1)
        if "chrome" in App:
            count2 += 0.10
            print(App, count2)
        if "Code" in App:  # Visual Studio Code
            count3 += 0.10
            print(App, count3)
        if "File Navigation" in App:
            count4 += 0.10
            print(App, count4)
        if "apex" in App:  # Games
            count5 += 0.10
            print(App, count5)
        if "Discord" in App:  # Visual Studio Code
            count6 += 0.10
            print(App, count6)
        if "Teams" in App:
            count7 += 0.10
            print(App, count7)
    if timeVar % 600 == 0:
        myInfo.delete_many({})
        newDict = [{'x1': 'Pycharm', 'y1': count1, 'x2': 'Chrome', 'y2': count2, 'x3': 'Code', 'y3': count3, 'x4': 'File Navigation', 'y4': count4, 'x5': 'Games', 'y5': count5, 'x6': 'Discord', 'y6': count6, 'x7': 'Teams', 'y7': count7}]
        myInfo.insert_many(newDict)