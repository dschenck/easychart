import pytest


def regress(regression):
    import pandas as pd
    import easychart

    data = pd.Series([(x - 20) ** 2 + 3 for x in range(10, 30)], index=range(10, 30))

    chart = easychart.new()
    chart.plot(data, index=range(100, 130))

    regression.check(chart.serialize())
