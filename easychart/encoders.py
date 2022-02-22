import simplejson as json
import collections
import numpy as np
import pandas as pd
import datetime
import easychart
import easytree


def default(value):
    """
    JSON default encoder function

    Note
    ----
    timezone-naive datetime.datetime objects are localized to UTC, 
    not as of local machine time
    """
    if isinstance(value, (easychart.Chart, easytree.Tree)):
        return value.serialize()

    # naive pd.Timestamps are modeled as UTC
    # no further conversions needed
    if isinstance(value, pd.Timestamp):
        return 1000 * value.timestamp()

    if isinstance(value, np.datetime64):
        return 1000 * value.astype(float)

    if isinstance(value, datetime.datetime):
        return (
            1000
            * value.replace(tzinfo=(value.tzinfo or datetime.timezone.utc)).timestamp()
        )

    # naive datetime.datetime are localized as UTC
    if isinstance(value, datetime.date):
        return (
            1000
            * datetime.datetime.combine(
                value, time=datetime.time.min, tzinfo=datetime.timezone.utc
            ).timestamp()
        )

    # convert time to timestamp
    if isinstance(value, datetime.time):
        return (
            1000
            * datetime.datetime.combine(
                datetime.date(1970, 1, 1),
                value,
                tzinfo=(value.tzinfo or datetime.timezone.utc),
            ).timestamp()
        )

    if isinstance(value, np.ndarray):
        return value.tolist()

    if isinstance(value, (np.int64, np.int32, np.int16, np.int8, np.int_)):
        return int(value)

    if isinstance(value, (np.double, np.float64, np.float_)):
        return float(value)

    if isinstance(value, (pd.DataFrame, pd.Series, pd.Index)):
        return value.values.tolist()

    if isinstance(
        value,
        (
            range,
            zip,
            collections.abc.KeysView,
            collections.abc.ValuesView,
            collections.abc.ItemsView,
        ),
    ):
        return list(value)

    return json.JSONEncoder(ignore_nan=True).default(value)


class Encoder(json.JSONEncoder):
    """
    JSON default encoder class

    Note
    -------------------------
    simplejson recommends passing a default function rather than
    a default encoding class
    """

    def default(self, value):
        return default(value)
