import pandas as pd
from datetime import datetime

def read_random():

    sensor_data = pd.read_csv('DataSetup\Data\SensorReading.csv').sample(1)
    sensor_readings = list()

    sensor1 = {
        "timeStamp": datetime.now(),
        "sensor_id": "temp1",
        "reading": sensor_data.iloc[0]['temperature']
    }
    sensor2 = {
        "timeStamp": datetime.now(),
        "sensor_id": "atm1",
        "reading": sensor_data.iloc[0]['pressure']
    }
    sensor3 = {
        "timeStamp": datetime.now(),
        "sensor_id": "ldr1",
        "reading": sensor_data.iloc[0]['visibility']
    }

    sensor_readings.append(sensor1)
    sensor_readings.append(sensor2)
    sensor_readings.append(sensor3)

    return sensor_readings