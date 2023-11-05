import pytest


def regress(regression):
    import pandas as pd
    import easychart

    chart = easychart.new("line", datetime=True)
    chart.plot(
        [1, 3, 5, 4, 3, 5, 2],
        index=[pd.Timestamp(2022, 12, 8) + pd.Timedelta(days=i) for i in range(7)],
    )

    chart.xAxis.labels.format = "Midnight on {value:%d %b}"

    regression.check(chart.serialize())
