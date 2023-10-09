def add_time(start, duration, starting_day=""):
    # Separate the start into hours and minutes
    start_time, end = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))

    # Calculate 24-hour clock format
    if end == "PM":
        start_hour += 12

    # Separate the duration into hours and minutes
    dur_hour, dur_minute = map(int, duration.split(':'))

    # Add hours and minutes
    new_hour = start_hour + dur_hour
    new_minutes = start_minute + dur_minute

    if new_minutes >= 60:
        hours_add = new_minutes // 60
        new_minutes -= hours_add * 60
        new_hour += hours_add

    days_add = 0
    if new_hour >= 24:
        days_add = new_hour // 24
        new_hour %= 24

    # Find AM and PM
    if new_hour >= 12:
        end = "PM"
        if new_hour > 12:
            new_hour -= 12
    else:
        end = "AM"
        if new_hour == 0:
            new_hour = 12

    # Handle days later
    if days_add > 0:
        if days_add == 1:
            days_later = " (next day)"
        else:
            days_later = f" ({days_add} days later)"
    else:
        days_later = ""

    # Define the week days
    week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

    if starting_day:
        weeks = days_add // 7
        i = (week_days.index(starting_day.lower().capitalize()) + days_add - 7 * weeks) % 7
        day = f", {week_days[i]}"
    else:
        day = ""

    new_time = f"{new_hour}:{new_minutes:02d} {end}{day}{days_later}"
    
    return new_time
