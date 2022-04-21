# Tony Leonard
# G00372842@gmit.ie
# 4th March 2022
# ***Update 20th April 2022***
# This script is not used in final Project.
# It was used in the testing and research of my project.


import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
myDB = client["StressCheck"]
myInfo = myDB["FineCount"]

multiDict = [{'x1': 'pycharm64', 'y1': 4, 'x2': 'Chrome', 'y2': 3, 'x3': 'Spotify', 'y3': 0.4, 'x4': 'File Navigation', 'y4': 0.7, 'x5': 'Discord', 'y5': 0.5, 'x6': 'Steam', 'y6': 1, 'x7': 'Apex Legends', 'y7': 6}]  # dummy values to check if connection works with MongoDB
myInfo.insert_many(multiDict)
print("Done")



