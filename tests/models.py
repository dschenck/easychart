import easychart
import easychart.models


def test_initialization():
    chart = easychart.new()
    assert isinstance(chart, easychart.Chart)


def test_series():
    chart = easychart.new()
    assert isinstance(chart, easychart.Chart)
    assert isinstance(chart.series, easychart.models.SeriesCollection)
