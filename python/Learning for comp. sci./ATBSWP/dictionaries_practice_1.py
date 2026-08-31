my_schedule = {
    "monday":"running",
    "tuesday":"biking",
    "wednesday":"swimming",
    "thursday":"running",
    "friday":"biking",
    "saturday":"swimming",
    "sunday":"stretching"
}

input_prompt = ("What day is it today? ")

print(f"Today you are: {my_schedule[input(input_prompt).strip().lower()]}")

