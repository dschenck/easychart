import pytest


def regress(regression):
    import easychart

    data = [10, 30, {"isIntermediateSum": True}, -4, -8, {"isSum": True}]

    chart = easychart.new("waterfall", legend=False)
    chart.categories = [
        "Opening stocks",
        "Production",
        "Total domestic supply",
        "Net exports",
        "Consumption",
        "Closing stocks",
    ]
    chart.plot(data)

    regression.check(chart.serialize())
