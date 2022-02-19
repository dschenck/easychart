import easychart
import pandas as pd

# data is a pd.DataFrame of stock prices
data = easychart.datasets.load("stocks")
data = data[:"20200430"].resample("M").last().pct_change()[1:]

stats = 100 * pd.concat(
    [
        data.quantile(0.10).rename("10%"),
        data.quantile(0.25).rename("25%"),
        data.quantile(0.75).rename("75%"),
        data.quantile(0.90).rename("90%"),
        data.iloc[-1].rename("last"),
    ],
    axis=1,
)

chart = easychart.new()
chart.title = "Normal monthly stock movements"
chart.subtitle = (
    "April 2020 change vs 10% and 25% quantile percentage changes since 2003"
)
chart.categories = stats.index
chart.yAxis.labels.format = "{value}%"
chart.tooltip = ("shared", "{value:.1}%")
chart.plotOptions.columnrange.grouping = False
chart.plotOptions.line.states.hover.enabled = False
chart.plot(
    zip(stats["10%"], stats["90%"]),
    name="10%-90% range",
    type="columnrange",
    color="rgba(20, 20, 20, 0.1)",
)
chart.plot(
    zip(stats["25%"], stats["75%"]),
    name="25%-75% range",
    type="columnrange",
    color="rgba(20, 20, 20, 0.3)",
)
chart.plot(stats["last"], name="April 2020", lineWidth=0, allowPointSelect=False)

chart
