# Imagine you have built a small robot, and it has several sensors on it. 
# The robot sends you a batch of data containing the current readings from each sensor.


sensor_data = [
    {"sensor_name": "temperature", "reading": 42},
    {"sensor_name": "battery_level", "reading": 15},
    {"sensor_name": "motor_speed", "reading": 88},
    {"sensor_name": "light_level", "reading": 76}
]

readings = []

for data_point in sensor_data:
    reading_value = data_point['reading']

    readings.append(reading_value)

reading_max = max(readings)



for sensor in sensor_data:
    print(f"Sensor name: {sensor['sensor_name']}. Sensor reading: {sensor['reading']}")

    if sensor["reading"] < 20:
        print(f"WARNING: {sensor['sensor_name']} IS CRITICALLY LOW")
 
print(f"Max reading is: {reading_max}")