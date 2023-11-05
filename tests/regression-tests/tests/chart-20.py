import pytest


def regress(regression):
    import easychart

    chart = easychart.new("column")
    chart.stacked = True
    chart.title = "Total fruit consumption, grouped by gender"
    chart.categories = ["Apples", "Oranges", "Pears", "Grapes", "Bananas"]
    with chart.yAxis as axis:
        axis.allowDecimals = False
        axis.min = 0
        axis.title.text = "Number of fruits"
    chart.tooltip = "{value:.0f}"
    chart.plot([5, 3, 4, 7, 2], name="John", stack="male")
    chart.plot([3, 4, 4, 2, 5], name="Joe", stack="male")
    chart.plot([2, 5, 6, 2, 1], name="Jane", stack="female")
    chart.plot([3, 0, 4, 4, 3], name="Janet", stack="female")

    regression.check(chart.serialize())
