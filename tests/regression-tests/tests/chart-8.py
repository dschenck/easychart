import pytest


def regress(regression):
    import easychart

    chart = easychart.new()
    chart.plot([1, 1, 2, 3, 5, 8], name="Fibonacci series")

    regression.check(chart.serialize())
