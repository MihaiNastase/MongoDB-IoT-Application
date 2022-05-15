from flask import Flask
from flask import g
from flask import jsonify
from flask import json
from flask import request
from flask import url_for
from flask import redirect
from flask import render_template
from flask import make_response
from flask_apscheduler import APScheduler
from simulate_sensors import read_random
import pymongo
from bson import BSON
from bson import json_util


app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27019/IoT_PropertyData'

client = pymongo.MongoClient(app.config['MONGO_URI'])
db = client['IoT_PropertyData']

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()
INTERVAL_TASK_ID = 'read_sensors'

def interval_task():
    sensor_readings = read_random()
    db.SensorReadings.insert_many(sensor_readings)

scheduler.add_job(id=INTERVAL_TASK_ID, func=interval_task, trigger='interval', seconds=15)

def parse_json(data):
    return json.loads(json_util.dumps(data))

@app.route('/IoT/TEST/')
def test_endpoint():
    #interval_task()
    return "Test", 200

@app.route('/pause-interval-task')
def pause_interval_task():
    scheduler.pause_job(id=INTERVAL_TASK_ID)
    return 'Interval task paused', 200
 
@app.route('/resume-interval-task')
def resume_interval_task():
    scheduler.resume_job(id=INTERVAL_TASK_ID)
    return 'Interval task resumed', 200

@app.route('/', methods=['GET'])
def welcome():
    return "Welcome to IoThing. The path you're looking for is /IoT/", 200


#THE ROOMS ENDPOINT
@app.route('/IoT/Rooms', methods=['GET'])
def findAllRooms():
    holder = list()
    result = db.Rooms.find()
    for i in result:
        holder.append(i)
    json_docs = parse_json(holder)
    return jsonify(json_docs), 200

@app.route('/IoT/Rooms', methods=['POST'])
def addNewRooms():
    payload = request.json
    db.Rooms.insert_many(payload)
    return {"Success":"Room(s) registered!"}, 200

@app.route('/IoT/Room/<area_id>', methods=['GET'])
def findRoomById(area_id):
    try:
        id = int(area_id)
        holder = list()
        result = db.Rooms.find({"area_id":id})
        for i in result:
            holder.append(i)
        if len(holder):
            json_docs = parse_json(holder)
            return jsonify(json_docs), 200
        else:
            return {"Error": "Room with specified area Id does not exist!"}, 404
    except Exception as e:
        return {"Error":str(e)}, 400

@app.route('/IoT/Room/<area_id>', methods=['DELETE'])
def deleteRoomById(area_id):
    try:
        id = int(area_id)
        holder = list()
        result = db.Rooms.find({"area_id":id})
        for i in result:
            holder.append(i)
        if len(holder):
            db.Rooms.delete_one({"area_id":id})
            json_docs = parse_json(holder)
            return jsonify(json_docs), 200
        else:
            return {"Error": "Room with specified area Id does not exist!"}, 404
    except Exception as e:
        return {"Error":str(e)}, 400

@app.route('/IoT/Room/<area_id>', methods=['PUT'])
def updateRoomById(area_id):
    payload = request.json
    try:
        id = int(area_id)
        holder = list()
        result = db.Rooms.find({"area_id":id})
        for i in result:
            holder.append(i)
        if len(holder):
            db.Rooms.delete_one({"area_id":id})
            db.Rooms.insert_one(payload)
            result = db.Rooms.find({"area_id":id})
            for i in result:
                holder.append(i)
            json_docs = parse_json(holder)
            return jsonify(json_docs), 200
        else:
            return {"Error": "Room with specified area Id does not exist!"}, 404
    except Exception as e:
        return {"Error":str(e)}, 400





#THE APPLIANCES ENDPOINT
@app.route('/IoT/Appliances', methods=['GET'])
def findAllAppliances():
    holder = list()
    result = db.Appliances.find()
    for i in result:
        holder.append(i)
    json_docs = parse_json(holder)
    return jsonify(json_docs), 200

@app.route('/IoT/Appliances/<area_id>', methods=['GET'])
def findAllAppliancesByArea(area_id):
    try:
        id = int(area_id)
        holder = list()
        result = db.Appliances.find({"area_id":id})
        for i in result:
            holder.append(i)
        json_docs = parse_json(holder)
        return jsonify(json_docs), 200
    except Exception as e:
        return {"Error":str(e)}, 400

@app.route('/IoT/Appliance/<label>', methods=['GET'])
def findAllAppliancesByLabel(label):
    holder = list()
    result = db.Appliances.find({"label":label})
    for i in result:
        holder.append(i)
    if len(holder):
        json_docs = parse_json(holder)
        return jsonify(json_docs), 200
    else:
        return {"Error": "Appliance with specified area Id does not exist!"}, 404

@app.route('/IoT/Appliances', methods=['POST'])
def addNewAppliances():
    payload = request.json
    db.Appliances.insert_many(payload)
    return {"Success":"Appliance(s) registered!"}, 200

@app.route('/IoT/Appliances/<area_id>', methods=['DELETE'])
def deleteAppliancesByArea(area_id):
    try:
        id = int(area_id)
        holder = list()
        result = db.Rooms.find({"area_id":id})
        for i in result:
            holder.append(i)
        if len(holder):
            db.Appliances.delete_many({"area_id":id})
            return "Appliances unregistered!", 200
        else:
            return {"Error": "Room with specified area Id does not exist!"}, 404
    except Exception as e:
        return {"Error":str(e)}, 400

@app.route('/IoT/Appliance/<label>', methods=['DELETE'])
def deleteApplianceByLabel(label):
        holder = list()
        result = db.Appliances.find({"label":label})
        for i in result:
            holder.append(i)
        if len(holder):
            db.Appliances.delete_one({"label":label})
            return "Appliance unregistered!", 200
        else:
            return {"Error": "Appliance with specified area Id does not exist!"}, 404

@app.route('/IoT/Appliance/<label>', methods=['PUT'])
def updateApplianceByLabel(label):
    payload = request.json
    holder = list()
    result = db.Appliances.find({"label":label})
    for i in result:
        holder.append(i)
    if len(holder):
        db.Appliances.delete_one({"label":label})
        db.Appliances.insert_one(payload)
        result = db.Appliances.find({"label":label})
        for i in result:
            holder.append(i)
        json_docs = parse_json(holder)
        return jsonify(json_docs), 200
    else:
        return {"Error": "Room with specified area Id does not exist!"}, 404



if __name__ == '__main__':
    app.run(debug=True)