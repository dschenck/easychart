import pytest


def regress(regression):
    import math
    import pandas as pd
    import easychart

    numbers = pd.DataFrame(
        [[round(math.cos(x), 4), round(math.sin(x), 4)] for x in range(-10, 10)],
        index=range(-10, 10),
    )

    chart = easychart.new("bubble")
    chart.plot(numbers)  # index + 2 columns

    regression.check(chart.serialize())
