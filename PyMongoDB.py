import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
myDB = client["SmartTabs"]
myInfo = myDB["MouseTracker"]

multiDict = [{'App': 'pycharm64', 'Duration': 4}, {'App': 'Chrome', 'Duration': 3}, {'App': 'Spotify', 'Duration': 0.4}, {'App': 'File Navigation', 'Duration': 0.7}, {'App': 'Discord', 'Duration': 0.5}, {'App': 'Steam', 'Duration': 1}]  # dummy values to check if connection works with MongoDB
myInfo.insert_many(multiDict)
print("Done")



