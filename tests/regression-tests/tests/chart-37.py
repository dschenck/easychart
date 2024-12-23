import pytest


def regress(regression):
    import easychart
    import pandas as pd
    import requests

    # data is a pd.Series of the US unemployment rate
    data = easychart.datasets.load("unemployment")

    # recessions is a pd.DataFrame of the peak and trough dates
    # of US recessions since 1854, from the NBER
    res = requests.get("http://data.nber.org/data/cycles/business_cycle_dates.json")
    recessions = pd.DataFrame(res.json()).map(lambda d: pd.Timestamp(d))[1:]

    chart = easychart.new(datetime=True, title="US unemployment rate", zoom="x")
    chart.subtitle = "Source: Federal Reserve (FRED)"
    chart.yAxis.labels.format = "{value}%"
    chart.plot(data, name="unemployment rate")

    for i, recession in recessions.iterrows():
        chart.vband(recession.peak, recession.trough)

    regression.check(chart.serialize())
