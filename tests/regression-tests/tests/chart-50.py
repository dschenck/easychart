import pytest


def regress(regression):
    import easychart

    data = [
        {"y": 120000, "color": "#059669"},
        {"y": 569000, "color": "#059669"},
        {"y": 231000, "color": "#059669"},
        {"isIntermediateSum": True},
        {"y": -342000, "color": "#ef4444"},
        {"y": -233000, "color": "#ef4444"},
        {"isSum": True},
    ]

    chart = easychart.new("waterfall")
    chart.categories = [
        "Services revenues",
        "Product revenues",
        "Licensing revenues",
        "Total revenues",
        "Fixed costs",
        "Variable costs",
        "Profit (loss)",
    ]

    chart.plot(data, labels="{point.y:,:0f}", legend=False)

    regression.check(chart.serialize())
