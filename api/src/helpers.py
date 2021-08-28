def time_to_float(time_string: str) -> float:
    int_time = int(time_string[:2]) if len(time_string) == 5 else int(time_string[0])
    if int_time == 0:
        int_time = 24
    return int_time + 0.5 if time_string[-2:] == "30" else int_time
