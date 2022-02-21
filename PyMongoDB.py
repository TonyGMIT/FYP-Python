import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
myDB = client["SmartTabs"]
myInfo = myDB["MouseTracker"]

multiDict = [{'pycharm64': 4}, {'Chrome': 3}, {'Spotify': 0.4}, {'File Navigation': 0.7}, {'Discord': 0.5}, {'Steam': 1}] # dummy values to check if connection works with MongoDB
myInfo.insert_many(multiDict)
print("Done")



