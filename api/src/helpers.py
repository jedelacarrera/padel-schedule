def time_to_float(time_string):
    int_time = int(time_string[:2])
    if int_time == 0:
        int_time = 24
    return int_time + 0.5 if time_string[3:5] == "30" else int_time
