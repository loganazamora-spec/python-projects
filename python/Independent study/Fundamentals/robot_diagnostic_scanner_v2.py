# Imagine you have built a small robot, and it has several sensors on it. 
# The robot sends you a batch of data containing the current readings from each sensor.

# The data that the sensor collects
sensor_data = [
    {"sensor_name": "temperature", "reading": 42},
    {"sensor_name": "battery_level", "reading": 15},
    {"sensor_name": "motor_speed", "reading": 88},
    {"sensor_name": "light_level", "reading": 76}
]

highest_reading = 0

for sensor in sensor_data:
    # Mission 1: print sensor data
    print(f"Sensor name: {sensor['sensor_name']}. Sensor reading: {sensor['reading']}")

    # Mission 2: check for critical values
    if sensor["reading"] < 20:
        print(f"WARNING: {sensor['sensor_name']} IS CRITICALLY LOW")

    # Mission 3: highest reading
    if sensor["reading"] > highest_reading:
        highest_reading = sensor["reading"]

print(f"Highest reading is: {highest_reading}")

