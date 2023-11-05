import pytest


def regress(regression):
    import easychart

    data = [
        ["Brazil", "Portugal", 5],
        ["Brazil", "France", 1],
        ["Canada", "Portugal", 1],
        ["Canada", "France", 5],
        ["Mexico", "Portugal", 1],
        ["Mexico", "France", 1],
        ["USA", "Portugal", 1],
        ["USA", "France", 1],
        ["Portugal", "Angola", 2],
        ["Portugal", "Senegal", 1],
        ["France", "Angola", 1],
        ["France", "Senegal", 3],
        ["Spain", "Senegal", 1],
        ["Spain", "Morocco", 3],
        ["England", "Morocco", 2],
        ["England", "South Africa", 7],
        ["South Africa", "China", 5],
        ["Angola", "Japan", 3],
        ["Senegal", "India", 1],
        ["Senegal", "Japan", 3],
        ["Mali", "India", 1],
        ["Morocco", "India", 1],
        ["Morocco", "Japan", 3],
    ]

    chart = easychart.new(type="sankey")
    chart.title = "Sankey diagram"
    chart.subtitle = (
        "Flow diagram in which the width of the arrows is proportional to the flow rate"
    )
    chart.plot(data, keys=["from", "to", "weight"])

    regression.check(chart.serialize())
