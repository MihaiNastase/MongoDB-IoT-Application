import pymongo
import json

client = pymongo.MongoClient("mongodb://localhost:27019/")
db = client['IoT_PropertyData']
Consumption = db['Consumption']


#with open('./Json/Appliances.json') as f:
#with open('./Json/Rooms.json') as f:
with open('./Json/Appliances.json') as f:
    file_data = json.load(f)


#db.Consumption.insert_many(file_data)
#db.Rooms.insert_many(file_data)
db.Appliances.insert_many(file_data)


client.close()