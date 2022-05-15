import pandas as pd

sensor_data = pd.read_csv('DataSetup\Data\SensorReading.csv').sample(1)

print(sensor_data)