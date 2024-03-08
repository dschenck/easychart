import pytest

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


def test_vline_with_two_axes():
    chart = easychart.new()
    chart.xAxis.append({})
    chart.xAxis.append({"opposite": True})

    chart.vline(10, c="red")

    assert chart.xAxis == [
        {"plotLines": [{"value": 10, "color": "red"}]},
        {"opposite": True},
    ]


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


def test_hline_with_two_axes():
    chart = easychart.new()
    chart.yAxis.append({})
    chart.yAxis.append({"opposite": True})

    chart.hline(10, c="red")

    assert chart.yAxis == [
        {"plotLines": [{"value": 10, "color": "red"}]},
        {"opposite": True},
    ]

    chart.hline(5, yAxis=1)

    assert chart.yAxis == [
        {"plotLines": [{"value": 10, "color": "red"}]},
        {"opposite": True, "plotLines": [{"value": 5, "color": "black"}]},
    ]


def test_vband():
    chart = easychart.new()
    chart.vband(3, 5)

    assert chart.xAxis.plotBands == [
        {"from": 3, "to": 5, "color": "rgba(68, 170, 213, 0.2)"}
    ]

    chart.vband(8, 9, color="red")

    assert chart.xAxis == {
        "plotBands": [
            {"from": 3, "to": 5, "color": "rgba(68, 170, 213, 0.2)"},
            {"from": 8, "to": 9, "color": "red"},
        ]
    }

    chart.vband(11, 12, label="test", color="blue")

    assert chart.xAxis == {
        "plotBands": [
            {"from": 3, "to": 5, "color": "rgba(68, 170, 213, 0.2)"},
            {"from": 8, "to": 9, "color": "red"},
            {"from": 11, "to": 12, "color": "blue", "label": {"text": "test"}},
        ]
    }


def test_vband_multiple_axes():
    chart = easychart.new()
    chart.xAxis.append({})
    chart.xAxis.append({})

    chart.vband(3, 5)

    assert chart.xAxis == [
        {"plotBands": [{"from": 3, "to": 5, "color": "rgba(68, 170, 213, 0.2)"}]},
        {},
    ]

    chart.vband(8, 9)

    assert chart.xAxis == [
        {
            "plotBands": [
                {"from": 3, "to": 5, "color": "rgba(68, 170, 213, 0.2)"},
                {"from": 8, "to": 9, "color": "rgba(68, 170, 213, 0.2)"},
            ]
        },
        {},
    ]

    chart.vband(3, 5, xAxis=1)
    chart.vband(7, 8, color="red", xAxis=1)

    assert chart.xAxis == [
        {
            "plotBands": [
                {"from": 3, "to": 5, "color": "rgba(68, 170, 213, 0.2)"},
                {"from": 8, "to": 9, "color": "rgba(68, 170, 213, 0.2)"},
            ]
        },
        {
            "plotBands": [
                {"from": 3, "to": 5, "color": "rgba(68, 170, 213, 0.2)"},
                {"from": 7, "to": 8, "color": "red"},
            ]
        },
    ]


def test_hband():
    chart = easychart.new()
    chart.hband(3, 5)

    assert chart.yAxis.plotBands == [
        {"from": 3, "to": 5, "color": "rgba(68, 170, 213, 0.2)"}
    ]


def test_hband_multiple_axes():
    chart = easychart.new()
    chart.yAxis.append({})
    chart.yAxis.append({})

    chart.hband(3, 5)

    assert chart.yAxis == [
        {"plotBands": [{"from": 3, "to": 5, "color": "rgba(68, 170, 213, 0.2)"}]},
        {},
    ]

    chart.hband(8, 9)

    assert chart.yAxis == [
        {
            "plotBands": [
                {"from": 3, "to": 5, "color": "rgba(68, 170, 213, 0.2)"},
                {"from": 8, "to": 9, "color": "rgba(68, 170, 213, 0.2)"},
            ]
        },
        {},
    ]

    chart.hband(3, 5, yAxis=1)
    chart.hband(7, 8, color="red", yAxis=1)

    assert chart.yAxis == [
        {
            "plotBands": [
                {"from": 3, "to": 5, "color": "rgba(68, 170, 213, 0.2)"},
                {"from": 8, "to": 9, "color": "rgba(68, 170, 213, 0.2)"},
            ]
        },
        {
            "plotBands": [
                {"from": 3, "to": 5, "color": "rgba(68, 170, 213, 0.2)"},
                {"from": 7, "to": 8, "color": "red"},
            ]
        },
    ]


def test_new_axis_format_percentage():
    chart = easychart.new(yformat="%")
    assert chart.yAxis.labels.format == "{(multiply value 100)}%"

    chart = easychart.new(xformat="%")
    assert chart.xAxis.labels.format == "{(multiply value 100)}%"


def test_chart_twinx():
    chart = easychart.new()
    chart.twinx()

    assert len(chart.xAxis) == 2
    assert chart.xAxis[0] == {}
    assert chart.xAxis[1] == {"opposite": True, "linkedTo": 0}

    chart = easychart.new()
    chart.twinx(title={"text": "opposite title"})
    assert chart.xAxis[0] == {}
    assert chart.xAxis[1] == {
        "opposite": True,
        "linkedTo": 0,
        "title": {"text": "opposite title"},
    }

    chart = easychart.new()
    chart.twinx(linked=False)
    assert len(chart.xAxis) == 2
    assert chart.xAxis[1] == {"opposite": True}


def test_chart_twiny():
    chart = easychart.new()
    chart.yAxis.title.text = "yAxis"
    chart.twiny()

    assert len(chart.yAxis) == 2
    assert chart.yAxis[0] == {"title": {"text": "yAxis"}}
    assert chart.yAxis[1] == {
        "opposite": True,
        "linkedTo": 0,
        "title": {"text": "yAxis"},
    }


def test_chart_idempotency():
    chart = easychart.new("column")
    chart.title = "France Olympic medals"
    chart.subtitle = "by year and by medal class"
    chart.categories = ["Gold", "Silver", "Bronze"]
    chart.yAxis.title.text = "medals"
    chart.plot([7, 16, 18], name=2008)
    chart.plot([11, 11, 13], name=2012)

    assert easychart.Chart(chart.serialize()) == chart
