import json
import collections
import numpy as np
import pandas as pd
import datetime
import easychart
import easytree

def default(value):
    """
    JSON default encoder function for non-standard objects

    Example
    -------------------------
    >>> json.dumps([pd.Timestamp(2020,4,20)], default=default)
    [2020-04-20]
    """
    if isinstance(value, (easychart.Chart, easytree.Tree)):
        return value.serialize()
    if isinstance(value, (pd.Timestamp, datetime.datetime)):
        if value == value.replace(hour=0, minute=0, second=0): 
            return value.strftime("%Y-%m-%d")
        return value.strftime("%Y-%m-%d %H:%M:%S.%f")
    if isinstance(value, datetime.date):
        return value.strftime("%Y-%m-%d")
    if isinstance(value, np.datetime64):
        return pd.Timestamp(value.astype(int))
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, (np.int64, np.int32, np.int16, np.int8, np.int_)):
        return int(value)
    if isinstance(value, (np.double, np.float64, np.float_)):
        return float(value)
    if isinstance(value, (pd.DataFrame, pd.Series, pd.Index)): 
        return value.values.tolist()
    if isinstance(value, (collections.abc.KeysView, collections.abc.ValuesView, collections.abc.ItemsView)): 
        return list(value)
    raise TypeError(f"Object of type '{type(value).__name__}' is not JSON serializable")

class Encoder(json.JSONEncoder):
    """
    JSON default encoder class

    Note
    -------------------------
    simplejson recommends passing a default function rather than
    a default encoding class

    Example
    -------------------------
    >>> json.dumps([pd.Timestamp(2020,4,20)], cls=Encoder)
    [2020-04-20]
    """
    def default(self, value):
        return default(value)
