import pytest


def regress(regression):
    import easychart

    # min, Q1, median, Q3, max
    data = [
        [760, 801, 848, 895, 965],
        [733, 853, 939, 980, 1080],
        [714, 762, 817, 870, 918],
        [724, 802, 806, 871, 950],
        [834, 836, 864, 882, 910],
    ]

    chart = easychart.new(type="boxplot")
    chart.categories = ["A", "B", "C", "D", "E"]
    chart.plot(data, name="distribution of values")

    regression.check(chart.serialize())
