import datetime

DATETIME_TYPES = (datetime.date, datetime.datetime, datetime.time, datetime.timedelta)

def timestamp(date):
    try:
        return 1000 * date.timestamp()
    except Exception: 
        if isinstance(date, datetime.date):
            return 1000 * datetime.datetime(date.year, date.month, date.day).timestamp()
        if isinstance(date, datetime.time):
            return 1000 * datetime.datetime.combine(datetime.date(1970,1,1), date, datetime.timezone.utc).timestamp()
    raise ValueError(f"'{date}' is not a datetime instance")

def flatten(*args):
    out = []
    for arg in args: 
        out.extend(arg) if isinstance(arg, (list, tuple)) else out.append(arg)
    return out