import pytest
import easychart


def test_racechart_rendering():
    charts = []
    for i in range(100):
        chart = easychart.new()
        chart.plot([j for j in range(10, 30)])
        charts.append(chart)

    assert easychart.ext.racechart.render(charts[0], charts)
    assert easychart.ext.racechart.render(charts[0], charts, options={"animate": True})
    assert easychart.ext.racechart.render(charts[0], charts, options={"animate": False})

    assert easychart.ext.racechart.render(
        charts[0], charts, options={"animate": False, "interval": 50}
    )
