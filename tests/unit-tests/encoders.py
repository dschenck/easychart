import pandas as pd
import datetime
import pytz

import easychart.encoders as encoders


def test_date():
    date = pd.Timestamp(2022, 1, 24)
    assert encoders.default(date) == 1642982400000

    date = datetime.date(2022, 1, 24)
    assert encoders.default(date) == 1642982400000


def test_datetime():
    # naive datetime
    date = datetime.datetime(2022, 1, 24)
    assert encoders.default(date) == 1642982400000

    date = datetime.datetime(2022, 1, 24, 9, 30)
    assert encoders.default(date) == 1643016600000

    date = pd.Timestamp(2022, 1, 24, 9, 30)
    assert encoders.default(date) == 1643016600000

    # localized datetime
    date = pytz.timezone("Europe/Paris").localize(
        datetime.datetime(2022, 1, 24, 10, 30)
    )
    assert encoders.default(date) == 1643016600000


def test_time():
    # naive time
    time = datetime.time(8, 30)
    assert encoders.default(time) == 1000 * (8 * 3600 + 30 * 60)

    # localized time
    date = pytz.timezone("Europe/Paris").localize(datetime.datetime(2022, 1, 24, 9, 30))
    time = date.time().replace(tzinfo=date.tzinfo)

    assert encoders.default(time) == 1000 * (8 * 3600 + 30 * 60)


def test_pandas_series():
    srs = pd.Series([1, 2, 3])
    assert encoders.default(srs) == [1, 2, 3]


def test_pandas_dataframe():
    df = pd.DataFrame([[1, 2, 3], [4, 5, 6]])
    assert encoders.default(df) == [[1, 2, 3], [4, 5, 6]]
