import unittest
import easychart
import easychart.models


class TestTree(unittest.TestCase):
    def test_initialization(self):
        chart = easychart.new()
        assert isinstance(chart, easychart.Chart)

    def test_series(self):
        chart = easychart.new()
        assert isinstance(chart, easychart.Chart)
        assert isinstance(chart.series, easychart.models.SeriesCollection)
