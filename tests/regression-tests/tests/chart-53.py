import pytest


def regress(regression):
    import easychart

    datalabels = {
        "enabled": True,
        "format": "{point.name}",
        "filter": {"property": "y", "operator": ">", "value": 0},
    }

    def pluralize(quantity, label):
        """
        Pluralize a category if quantity > 2
        """
        if quantity < 2:
            return label
        return label + "s"

    def label(quantity, category):
        """
        Create a data label for a given point (y) and category (category)
        """
        return str(quantity) + " " + pluralize(quantity, category)

    chart = easychart.new("column")
    chart.stacked = True
    chart.title = "Adoptions per month, by animal"
    chart.categories = ["June", "July", "August"]
    chart.plot(
        [{"y": y, "name": label(y, "cat")} for y in [1, 3, 5]],
        name="cats",
        datalabels=datalabels,
    )
    chart.plot(
        [{"y": y, "name": label(y, "dog")} for y in [2, 1, 5]],
        name="dogs",
        datalabels=datalabels,
    )

    regression.check(chart.serialize())
