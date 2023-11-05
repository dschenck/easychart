import pytest


def regress(regression):
    import easychart
    import pandas as pd

    data = pd.DataFrame(
        [[7, 16, 18], [11, 11, 13]],
        columns=["Gold", "Silver", "Bronze"],
        index=[2008, 2012],
    ).T

    chart = easychart.new("column")

    chart.title = "France Olympic medals"
    chart.subtitle = "by year and by medal class"
    chart.categories = data.index
    chart.yAxis.title.text = "medals"

    for column in data:
        chart.plot(data[column])

    regression.check(chart.serialize())
