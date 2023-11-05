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
    chart.plot(
        [5, 3, 4, 7, 2],
        name="John",
        stack="male",
        labels="{point.y} fruits <br /> ({point.percentage:.0f}%)",
    )
    chart.plot([3, 4, 4, 2, 5], name="Joe", stack="male", labels="{point.series.name}")
    chart.plot([2, 5, 6, 2, 1], name="Jane", stack="female", labels="{point.category}")
    chart.plot(
        [3, 0, 4, 4, 3],
        name="Janet",
        stack="female",
        labels="{point.y} out of {point.total}",
    )

    regression.check(chart.serialize())
