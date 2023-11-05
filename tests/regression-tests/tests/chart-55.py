import pytest


def regress(regression):
    import easychart

    data = [
        ["A", "D", 9, "#BCD4DE"],  # gray
        ["A", "C", 2, "#FFD675"],  # light yellow
        ["D", "E", 4, "#BCD4DE"],  # gray
        ["D", "F", 4, "#BCD4DE"],  # gray
        ["B", "C", 4, "#FFD675"],  # light yellow
        ["B", "D", 4, "#BCD4DE"],  # gray
        ["C", "E", 3, "#F7BA2D"],  # darker yellow
        ["C", "F", 3, "#BCD4DE"],  # gray
    ]

    nodes = [
        {"id": "A", "color": "#457b9d"},  # blue
        {"id": "B", "color": "#2a9d8f"},  # green
        {"id": "C", "color": "#e9c46a"},  # yellow
        {"id": "D", "color": "#f4a261"},  # orange
        {"id": "E", "color": "#e76f51"},  # red
        {"id": "F", "color": "#1d3557"},  # night
    ]

    chart = easychart.new(type="sankey")
    chart.plot(data, keys=["from", "to", "weight", "color"], nodes=nodes)

    regression.check(chart.serialize())
