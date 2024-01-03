import pytest


def regress(regression):
    import easychart

    data = [
        [-9.9, 10.3],
        [-8.6, 8.5],
        [-10.2, 11.8],
        [-1.7, 12.2],
        [-0.6, 23.1],
        [3.7, 25.4],
        [6.0, 26.2],
        [6.7, 21.4],
        [3.5, 19.5],
        [-1.3, 16.0],
        [-8.7, 9.4],
        [-9.0, 8.6],
    ]

    chart = easychart.new("columnrange")
    chart.title = "Temperature variation by month"
    chart.subtitle = "Observed in Vik i Sogn, Norway, 2017"
    chart.tooltip = "{value}&deg;C"
    chart.yAxis.title.text = "Temperature ( &deg;C )"
    chart.legend = False
    chart.inverted = True
    chart.categories = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]
    chart.plot(data, name="Temperature")

    regression.check(chart.serialize())
