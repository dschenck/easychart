import pytest


def regress(regression):
    import easychart

    chart = easychart.new("column")

    chart.plotOptions.column = {"groupPadding": 0.10, "pointPadding": 0.05}

    chart.plot([1, 3, 2, 4, 3], name="Series A")
    chart.plot([8, 1, 0, 3, 1], name="Series B")

    regression.check(chart.serialize())
