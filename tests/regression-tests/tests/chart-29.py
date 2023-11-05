import pytest


def regress(regression):
    import easychart

    data = [
        {"name": "Chrome", "y": 61.41, "sliced": True},
        {"name": "Internet Explorer", "y": 11.84},
        {"name": "Firefox", "y": 10.85},
        {"name": "Edge", "y": 4.67},
        {"name": "Safari", "y": 4.18},
        {"name": "Other", "y": 7.05},
    ]

    chart = easychart.new("pie")
    chart.title = "Browser market shares in January, 2018"
    chart.tooltip = "{point.name}: <b>{point.percentage:.1f}%</b>"
    chart.plot(data, name="browser")

    regression.check(chart.serialize())
