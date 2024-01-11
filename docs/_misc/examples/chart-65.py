import easychart

data = easychart.datasets.load("stocks")
matrix = data.resample("M").last().pct_change().corr()

chart = easychart.heatmap(
    matrix, colormap="reds", labels="{(multiply point.value 100):.0f}%"
)
chart.title = "Monthly return correlation"
chart.subtitle = f"Data from {data.index[0]:%d %b %y} to {data.index[-1]:%d %b %y}"
chart
