import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
myDB = client["SmartTabs"]
myInfo = myDB["MouseTracker"]

multiDict = [{'x1': 'pycharm64', 'y1': 4, 'x2': 'Chrome', 'y2': 3, 'x3': 'Spotify', 'y3': 0.4, 'x4': 'File Navigation', 'y4': 0.7, 'x5': 'Discord', 'y5': 0.5, 'x6': 'Steam', 'y6': 1, 'x7': 'Apex Legends', 'y7': 6}]  # dummy values to check if connection works with MongoDB
myInfo.insert_many(multiDict)
print("Done")



