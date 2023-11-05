import pytest


def regress(regression):
    import easychart

    chart = easychart.new(
        title="US 2016 Presidential election results", ytitle="", yformat="{value}%"
    )
    chart.categories = ["Electoral vote", "Popular vote"]
    chart.plot(
        [46.1, 48.2], name="Hillary Clinton", type="column", color="rgb(18,8,55)"
    )
    chart.plot([57.3, 42.7], name="Donald Trump", type="column", color="rgb(202,0,4)")

    regression.check(chart.serialize())
