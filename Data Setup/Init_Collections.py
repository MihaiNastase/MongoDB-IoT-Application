import pymongo
import json


def init_database(db_uri):
    client = pymongo.MongoClient(db_uri)
    db = client['IoT_PropertyData']

    db.Consumption.drop()
    db.Rooms.drop()
    db.Appliances.drop()
    db.Sensors.drop()
    db.ApplianceUsage.drop()
    db.SensorReadings.drop()
    db.History.drop()

    db.create_collection("Consumption")
    db.create_collection("Rooms")
    db.create_collection("Appliances")
    db.create_collection("Sensors")
    db.create_collection("ApplianceUsage")
    db.create_collection("SensorReadings")
    db.create_collection("History")


    try:
        with open('./Json/Consumption.json') as f:
            file_data = json.load(f)
            db.Consumption.insert_many(file_data)
    except:
        print("Using relative path!")
        with open('DataSetup\Json\Consumption.json') as f:
            file_data = json.load(f)
            db.Consumption.insert_many(file_data)
        
    try:
        with open('./Json/Rooms.json') as f:
            file_data = json.load(f)
            db.Rooms.insert_many(file_data)
    except:
        print("Using relative path!")
        with open('DataSetup\Json\Rooms.json') as f:
            file_data = json.load(f)
            db.Rooms.insert_many(file_data)

    try:
        with open('./Json/Appliances.json') as f:
            file_data = json.load(f)
            db.Appliances.insert_many(file_data)
    except:
        print("Using relative path!")
        with open('DataSetup\Json\Appliances.json') as f:
            file_data = json.load(f)
            db.Appliances.insert_many(file_data)


    client.close()


init_database("mongodb://localhost:27019/")