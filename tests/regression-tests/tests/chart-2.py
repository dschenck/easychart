import pytest


def regress(regression):
    import easychart

    # data is a pd.Series of the US unemployment rate
    data = easychart.datasets.load("unemployment")

    chart = easychart.new(datetime=True, title="US unemployment rate", zoom="x")
    chart.subtitle = "Source: Federal Reserve (FRED)"
    chart.yAxis.labels.format = "{value}%"
    chart.plot(data, name="unemployment rate")

    regression.check(chart.serialize())
