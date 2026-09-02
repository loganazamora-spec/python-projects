# Imagine you are writing software to read data from a basic EEG cap. 
# The cap measures brain wave frequencies to see if a person is resting or actively focusing.

brain_waves = [
    {"time": "00:01", "frequency": 8, "state": "resting"},
    {"time": "00:02", "frequency": 14, "state": "focus"},
    {"time": "00:03", "frequency": 22, "state": "active"},
    {"time": "00:04", "frequency": 7, "state": "resting"},
    {"time": "00:05", "frequency": 19, "state": "active"}
]


# Mission 1: Add missing reading
brain_waves.append({"time":"00:06", "frequency":12, "state":"focus"})
    
# Mission 2: Remove unreliable reading
brain_waves.pop(0)

# Mission 3: Add 1 to a counter every time the state is active
active_counter = 0
frequencies = []
states = []

for row in brain_waves:
    state = row["state"].strip()

    if state == "active":
        active_counter += 1
    

# Mission 4: Lowest brain wave frequency recorded
    frequencies.append(row['frequency'])

    
# Mission 6: check if a reading's state is "focus". If it is, update that specific dictionary so the state says "deep focus" instead
    if row["state"] == "focus":
        row["state"] = "deep focus"

# Mission 5: Calculate average frequency
average_frequency = sum(frequencies)/len(frequencies)

# Mission 7: print activity count, lowest frequency, average, and brain waves list. 
print(f"Number of instances active: {active_counter}")
print(f"Lowest frequency is: {min(frequencies)}")
print(f"Average frequency rounded to 2 digits is: {float(round(average_frequency, 2))}")
print(f"List of brain wave data: {brain_waves}")
