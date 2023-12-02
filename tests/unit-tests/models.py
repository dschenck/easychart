import easychart
import easychart.models


def test_initialization():
    chart = easychart.new()
    assert isinstance(chart, easychart.Chart)


def test_series():
    chart = easychart.new()
    assert isinstance(chart, easychart.Chart)
    assert isinstance(chart.series, easychart.models.Series)


def test_chart_show():
    grid = easychart.new().show(width=100, theme="economist")
    assert isinstance(grid, easychart.Grid)
    assert grid.theme == "economist"
    assert len(grid.plots) == 1
    assert grid.plots[0].width == "100px"


def test_chart_grid():
    chart = easychart.new()
    grid = easychart.Grid()

    grid.add(chart)
    grid.add(chart, width="50%")
    grid.add(easychart.new(width=300))

    assert grid.plots[0].width == "600px"
    assert grid.plots[1].width == "50%"
    assert grid.plots[2].width == "300px"


def test_plot_width_changes_if_responsive():
    easychart.config.rendering.responsive = False

    chart = easychart.Chart()
    plot = easychart.Plot(chart)
    assert plot.width == "600px"

    easychart.config.rendering.responsive = True

    chart = easychart.Chart()
    plot = easychart.Plot(chart)
    assert plot.width == "100%"


def test_chart_type():
    chart = easychart.new("column")
    assert chart.chart.type == "column"


def test_chart_color_axis():
    chart = easychart.new()
    chart.cAxis = True
    assert chart.colorAxis == {}
    assert chart.cAxis == {}

    chart = easychart.new()
    chart.cAxis = {"minColor": 1, "maxColor": 2}
    assert chart.colorAxis == {"minColor": 1, "maxColor": 2}
    assert chart.cAxis == {"minColor": 1, "maxColor": 2}


def test_vline():
    chart = easychart.new()
    chart.vline(10)
    assert chart.xAxis == {"plotLines": [{"value": 10, "color": "black"}]}

    chart = easychart.new()
    chart.vline(10, color="red")
    assert chart.xAxis == {"plotLines": [{"value": 10, "color": "red"}]}

    chart = easychart.new()
    chart.vline(10, c="red")
    assert chart.xAxis == {"plotLines": [{"value": 10, "color": "red"}]}


def test_hline():
    chart = easychart.new()
    chart.hline(10)
    assert chart.yAxis == {"plotLines": [{"value": 10, "color": "black"}]}

    chart = easychart.new()
    chart.hline(10, color="red")
    assert chart.yAxis == {"plotLines": [{"value": 10, "color": "red"}]}

    chart = easychart.new()
    chart.hline(10, c="red")
    assert chart.yAxis == {"plotLines": [{"value": 10, "color": "red"}]}


def test_new_axis_format_percentage():
    chart = easychart.new(yformat="%")
    assert chart.yAxis.labels.format == "{(multiply value 100)}%"

    chart = easychart.new(xformat="%")
    assert chart.xAxis.labels.format == "{(multiply value 100)}%"
