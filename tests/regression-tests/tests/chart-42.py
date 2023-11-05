import pytest


def regress(regression):
    import math
    import pandas as pd
    import easychart

    numbers = pd.DataFrame([[x, math.cos(x)] for x in range(-100, 100)])

    chart = easychart.new("scatter")
    chart.plot(numbers.values)  # 2 columns only (no index)

    regression.check(chart.serialize())
