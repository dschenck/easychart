import easychart
import easychart.models


def test_initialization():
    chart = easychart.new()
    assert isinstance(chart, easychart.Chart)


def test_series():
    chart = easychart.new()
    assert isinstance(chart, easychart.Chart)
    assert isinstance(chart.series, easychart.models.SeriesCollection)


def test_chart_show():
    grid = easychart.new().show(width=100, theme="economist")
    assert isinstance(grid, easychart.Grid)
    assert grid.theme == "economist"
    assert len(grid.plots) == 1
    assert grid.plots[0].width == "100px"
