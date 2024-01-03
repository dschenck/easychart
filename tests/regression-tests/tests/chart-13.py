import pytest


def regress(regression):
    import easychart

    chart = easychart.new(tooltip="shared")
    chart.title = "Average Monthly Temperature and Rainfall in Tokyo"
    chart.subtitle = "Source: WorldClimate.com"
    chart.categories = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]

    # add two axes
    chart.yAxis.append(
        title={"text": "Temperature"}, labels={"format": "{value}&deg;C"}
    )
    chart.yAxis.append(
        title={"text": "Rainfall"}, labels={"format": "{value} mm"}, opposite=True
    )

    chart.plot(
        [
            49.9,
            71.5,
            106.4,
            129.2,
            144.0,
            176.0,
            135.6,
            148.5,
            216.4,
            194.1,
            95.6,
            54.4,
        ],
        name="Rainfall",
        type="column",
        yAxis=1,
        tooltip={"valueSuffix": "mm"},
    )
    chart.plot(
        [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6],
        name="Temperature",
        type="spline",
        yAxis=0,
        tooltip={"valueSuffix": "&deg;C"},
    )

    regression.check(chart.serialize())
