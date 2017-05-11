import datetime

def add_gigasecond(day):
    gs = datetime.timedelta(seconds=10**9)
    return day + gs
