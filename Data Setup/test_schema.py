import pymongo
import json

client = pymongo.MongoClient("mongodb://localhost:27019/")
db = client['IoT_PropertyData']

