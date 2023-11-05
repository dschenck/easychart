import pytest


def regress(regression):
    import easychart

    labels = ["O", "A", "B", "AB"]
    values = [45, 40, 11, 4]

    chart = easychart.new("pie", title="Distribution of blood type in the US")
    chart.subtitle = "Source: American Red Cross"
    chart.tooltip = "{point.percentage:.0f}%"
    chart.plot(values, index=labels, labels="{point.name} ({point.y}%)")

    regression.check(chart.serialize())
