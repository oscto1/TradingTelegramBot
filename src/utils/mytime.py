def td_minutes(timedelta) -> int:
    return (timedelta.seconds//60)%60

def td_hours(timedelta) -> int:
    return timedelta.seconds//3600