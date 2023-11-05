import pytest


def regress(regression):
    import easychart

    datalabels = {
        "enabled": True,
        "format": "{point.y} {point.series.name} in {point.category} ({point.color})",
        "filter": {"property": "y", "operator": ">", "value": 0},
    }

    chart = easychart.new("column")
    chart.stacked = True
    chart.title = "Adoptions per month, by animal"
    chart.categories = ["June", "July", "August"]
    chart.plot([1, 3, 5], name="cats", datalabels=datalabels)
    chart.plot([1, 0, 4], name="dogs", datalabels=datalabels)

    regression.check(chart.serialize())
