import pytest


def regress(regression):
    import easychart

    data = [
        ["Austria", 69, 82],
        ["Belgium", 70, 81],
        ["Bulgaria", 69, 75],
        ["Croatia", 65, 78],
        ["Cyprus", 70, 81],
        ["Czech Republic", 70, 79],
        ["Denmark", 72, 81],
        ["Estonia", 68, 78],
        ["Finland", 69, 81],
        ["France", 70, 83],
        ["Greece", 68, 81],
        ["Spain", 69, 83],
        ["Netherlands", 73, 82],
        ["Ireland", 70, 82],
        ["Lithuania", 70, 75],
        ["Luxembourg", 68, 83],
        ["Latvia", 70, 75],
        ["Malta", 69, 82],
        ["Germany", 69, 81],
        ["Poland", 68, 78],
        ["Portugal", 63, 81],
        ["Romania", 66, 75],
        ["Slovakia", 70, 77],
        ["Slovenia", 69, 81],
        ["Sweden", 73, 82],
        ["Hungary", 68, 76],
        ["Italy", 69, 83],
        ["UK", 71, 81],
    ]

    chart = easychart.new(type="dumbbell")
    chart.title = "Change in Life Expectancy"
    chart.subtitle = "1960 vs 2018"
    chart.chart.inverted = True
    chart.xAxis.type = "category"
    chart.yAxis.title.text = "Life expectancy (years)"
    chart.plot(data, keys=["name", "low", "high"], legend=False)

    regression.check(chart.serialize())
