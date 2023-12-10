import pytest
import easychart


def test_plot_arguments():
    """
    Test to ensure that arguments are dispatched to easychart.new
    and chart.plot appropriately
    """
    chart = easychart.plot([1, 3, 2, 4], xtype="datetime", color="red")
    assert chart.series[0].color == "red"
    assert chart.xAxis.type == "datetime"
