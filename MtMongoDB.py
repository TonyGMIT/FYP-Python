# Tony Leonard
# G00372842@gmit.ie
# 20th March 2022
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
    if timeVar % 600 == 0:
        myInfo.delete_many({})
        newDict = [{'x1': 'Pycharm', 'y1': count1, 'x2': 'Chrome', 'y2': count2, 'x3': 'Code', 'y3': count3,'x4': 'File Navigation', 'y4': count4}]
        myInfo.insert_many(newDict)


