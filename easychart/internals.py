import datetime

def timestamp(date):
    try:
        return 1000 * date.timestamp()
    except: 
        if isinstance(date, datetime.date):
            return 1000 * datetime.datetime(date.year, date.month, date.day).timestamp()
    raise ValueError(f"'{date}' is not a datetime instance")

def flatten(*args):
    out = []
    for arg in args: 
        out.extend(arg) if isinstance(arg, (list, tuple)) else out.append(arg)
    return out