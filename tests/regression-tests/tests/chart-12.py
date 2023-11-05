import pytest


def regress(regression):
    import easychart

    data = [
        [0, 15],
        [10, -50],
        [20, -56.5],
        [30, -46.5],
        [40, -22.1],
        [50, -2.5],
        [60, -27.7],
        [70, -55.7],
        [80, -76.5],
    ]

    chart = easychart.new()
    chart.title = "Atmosphere Temperature by Altitude"
    chart.subtitle = "According to the Standard Atmosphere Model"
    chart.chart = {"type": "spline", "inverted": True}

    with chart.xAxis as axis:
        axis.reversed = False
        axis.title.text = "Altitude"
        axis.labels.format = "{value} km"

    with chart.yAxis as axis:
        axis.labels.format = "{value}°"
        axis.title.text = "Temperature"
        axis.title.rotation = 0

    chart.tooltip.headerFormat = "<b>{series.name}</b><br/>"
    chart.tooltip.pointFormat = "{point.x} km: {point.y}°C"

    chart.legend.enabled = False
    chart.append(data, name="temperature")

    regression.check(chart.serialize())
