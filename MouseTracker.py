# Not my own written code.
# Can be seen on: https://dev.to/tkkhhaarree/track-windows-app-usage-time-using-python-h9h


from win32gui import GetForegroundWindow
import psutil  # cross-platform library for receiving info on running processes
import time  # provides various functions to manipulate time values
import win32process  # GetWindowThreadProcessId: Retrieves the identifier of the thread and process that created the specified window.

usageTime = {}
timeStamp = {}

while True:
    currentApp = psutil.Process(win32process.GetWindowThreadProcessId(GetForegroundWindow())[1]).name().replace(".exe", "")
    timeStamp[currentApp] = int(time.time())
    time.sleep(1)  # delays for 1 second
    if currentApp not in usageTime.keys():  # .keys() not needed
        usageTime[currentApp] = 0
    elif 'explorer' in currentApp:
        usageTime[currentApp] = 0

    usageTime[currentApp] = usageTime[currentApp] + int(time.time()) - timeStamp[currentApp]
    print(usageTime)
