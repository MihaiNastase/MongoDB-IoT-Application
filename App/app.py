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
INTERVAL_TASK_ID = 'read_sensors    '


def parse_json(data):
    return json.loads(json_util.dumps(data))

@app.route('/IoT/Rooms')
def findAllRooms():
    holder = list()
    result = db.Rooms.find()
    for i in result:
        holder.append(i)
    json_docs = parse_json(holder)
    return jsonify(json_docs)

if __name__ == '__main__':
    app.run(debug=True)