import easychart

# compute the annual high, low and last value of the S&P since 2010
data = easychart.datasets.load("S&P500")["Close"]["20100101":]
data = data.groupby(data.index.year).agg(["min", "max", "last"])

chart = easychart.new(title="S&P 500 annual trading range", tooltip="shared")
chart.plot(
    data[["min", "max"]],
    type="arearange",
    color="#eeeeee",
    name="annual range",
    marker={"enabled": False},
)
chart.plot(data["last"], name="end of year")
