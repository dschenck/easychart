import pytest


def regress(regression):
    import easychart

    data = [
        ["Chrome", 58.9],
        ["Firefox", 13.29],
        ["Internet Explorer", 13],
        ["Edge", 3.78],
        ["Safari", 3.42],
        ["Safari", 7.61],
    ]

    chart = easychart.new("pie")
    chart.plot(data)

    with chart.plotOptions.pie as options:
        options.startAngle = -90
        options.endAngle = 90

        # recenter the plot in the middle of the plot area
        options.center = ["50%", "75%"]

    regression.check(chart.serialize())
