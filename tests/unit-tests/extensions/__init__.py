import pytest
import easychart


def test_racechart_rendering():
    charts = []
    for i in range(100):
        chart = easychart.new()
        chart.plot([j for j in range(10, 30)])
        charts.append(chart)

    assert easychart.ext.racechart(charts).render()
    assert easychart.ext.racechart(charts, options={"animate": True}).render()
    assert easychart.ext.racechart(charts, options={"animate": False}).render()

    assert easychart.ext.racechart(
        charts, options={"animate": False, "interval": 50}
    ).render()
