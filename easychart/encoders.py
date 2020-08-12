import json
import numpy as np
import pandas as pd
import datetime

class Encoder(json.JSONEncoder):
    def default(self, value):
        if isinstance(value, (pd.Timestamp, datetime.datetime)):
            if value == value.replace(hour=0, minute=0, second=0): 
                return value.strftime("%Y-%m-%d")
            return value.strftime("%Y-%m-%d %H:%M:%S.%f")
        if isinstance(value, datetime.date):
            return value.strftime("%Y-%m-%d")
        if isinstance(value, np.datetime64):
            return self.default(pd.Timestamp(value.astype(int)))
        if isinstance(value, np.ndarray):
            return value.tolist()
        if isinstance(value, (np.int64, np.int32, np.int16, np.int8, np.int_)):
            return int(value)
        if isinstance(value, (np.double, np.float64, np.float_)):
            return float(value)
        if isinstance(value, (pd.DataFrame, pd.Series, pd.Index)): 
            return value.values.tolist()
        return super().default(value)
