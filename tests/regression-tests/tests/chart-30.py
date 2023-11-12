import pytest


def regress(regression):
    import easychart

    chart = easychart.new("pie")
    chart.plot(
        [
            ["Chrome", 58.9],
            ["Firefox", 13.29],
            ["Internet Explorer", 13],
            ["Edge", 3.78],
            ["Safari", 3.42],
            ["Safari", 7.61],
        ],
        innerSize="50%",
    )

    regression.check(chart.serialize())