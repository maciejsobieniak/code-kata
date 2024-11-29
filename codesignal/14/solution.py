def add_seconds_to_times(timePoints, seconds):
    time_part = []
    new_time = []
    for part_point in timePoints:
        time_part.append([int(part) for part in part_point.split(':')])
    for part in time_part:
        seconds_since_start = part[0] * 3600 + part[1] * 60 + part[2]
        total_seconds = (seconds_since_start + seconds) % (24 * 3600)
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds_new = divmod(remainder, 60)
        new_time.append(f"{hours:02d}:{minutes:02d}:{seconds_new:02d}")
    return new_time