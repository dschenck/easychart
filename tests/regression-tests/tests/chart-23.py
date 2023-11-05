import pytest


def regress(regression):
    import easychart
    import pandas as pd

    data = pd.DataFrame(
        [
            [107, 31, 635, 203, 2],
            [133, 156, 947, 408, 6],
            [814, 841, 3714, 727, 31],
            [1216, 1001, 4436, 738, 40],
        ],
        index=[1800, 1900, 2000, 2016],
        columns=["Africa", "America", "Asia", "Europe", "Oceania"],
    )

    chart = easychart.new("bar")
    chart.title = "Historic World Population by Region"
    chart.subtitle = "Source: <a href='https://en.wikipedia.org/wiki/World_population'>Wikipedia.org</a>"
    chart.categories = data.columns
    chart.yAxis.title = {"text": "Population (millions)", "align": "high"}
    chart.tooltip = "{value:.0f}m"
    for year in data.index:
        chart.plot(data.loc[year], name=year, datalabels=(year == 2016))

    regression.check(chart.serialize())
