def add_days(date, n):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date_part = [int(part) for part in date.split("-")]
    year = date_part[0]
    month = date_part[1]
    day = date_part[2]
    while n > 0:
        if month == 2 and is_leap_year(year):
            days_in_month[2] = 29
        else:
            days_in_month[2] = 28
        
        remaining_days_in_month = days_in_month[month] - day
        
        if n <= remaining_days_in_month:
            day += n
            n = 0
        else:
            n -= (remaining_days_in_month + 1)
            day = 1
            month += 1
            if month > 12:
                month = 1
                year += 1
    return f"{year:04d}-{month:02d}-{day:02d}"


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False