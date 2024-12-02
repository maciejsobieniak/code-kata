def time_period_length(time_period):
    time_parts = [part.split(":") for part in time_period.split("-")]
    time_first_minutes = int(time_parts[0][0]) * 60 + int(time_parts[0][1])
    time_second_minutes = int(time_parts[1][0]) * 60 + int(time_parts[1][1])
    total_length_minutes = time_second_minutes - time_first_minutes
    return total_length_minutes