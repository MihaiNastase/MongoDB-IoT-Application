import pymongo
import json

client = pymongo.MongoClient("mongodb://localhost:27019/")
db = client['IoT_PropertyData']

query = db.Rooms.find({"area_id":"1"})

for i in query:
 print(i)