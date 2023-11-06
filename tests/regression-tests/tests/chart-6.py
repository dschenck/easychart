import pytest


def regress(regression):
    import easychart

    # data is pd.Series of electric and gas utility industrial production
    data = easychart.datasets.load("electricity")

    # detrend the data naively
    growth = (
        (data / data.shift(12) - 1).fillna(0).apply(lambda x: (1 + x) ** (1 / 12) - 1)
    )
    data = data.divide((1 + growth.ewm(alpha=0.25).mean()).cumprod())
    # slice the data since 1975
    data = data["1975-01-01":]
    # rebase the data to average 100
    data = 100 * data / data.mean()

    # create a pivot (month, year)
    pivot = data.groupby([data.index.month, data.index.year]).last().unstack()
    pivot.index = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "July",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]

    # compute different levels of historical norms
    for decile in [0, 0.05, 0.25, 0.5, 0.75, 0.95, 1]:
        pivot[f"{decile:.0%}"] = pivot.iloc[:, :-1].quantile(decile, axis=1).round(4)

    # create the chart
    chart = easychart.new(tooltip="shared", title="US gas and electricity production")
    chart.subtitle = "Detrended (100 = 1975-2020 average)"
    chart.categories = pivot.index
    chart.marker = False
    chart.plot(
        zip(pivot["5%"], pivot["95%"]),
        name="10%-90% range",
        type="arearange",
        color="#eeeeee",
    )
    chart.plot(
        zip(pivot["25%"], pivot["75%"]),
        name="25%-75% range",
        type="arearange",
        color="#cccccc",
    )
    chart.plot(pivot["0%"], name="min", dashstyle="dot", color="black")
    chart.plot(pivot["100%"], name="max", dashstyle="dot", color="black")
    chart.plot(pivot[2019], name="2019")
    chart.plot(pivot[2020], name="2020")

    regression.check(chart.serialize())
