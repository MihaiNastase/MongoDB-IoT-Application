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

@app.route('/')
def welcome():
    return "Welcome to IoThing. The path you're looking for is /IoT/", 200

@app.route('/IoT/Rooms')
def findAllRooms():
    holder = list()
    result = db.Rooms.find()
    for i in result:
        holder.append(i)
    json_docs = parse_json(holder)
    return jsonify(json_docs), 200




if __name__ == '__main__':
    app.run(debug=True)