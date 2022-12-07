import easychart

chart = easychart.new("scatter")
chart.xAxis.min = 0
chart.xAxis.max = 6
chart.plot([(1, 5), (3, 5), (5, 5)])

chart.annotate("Callout is the default shape", x=1, y=5)

chart.annotate("Connector is akin to floating text", x=3, y=5, shape="connector")

chart.annotate(
    "You may want to set a width to a long-text annotation to avoid it growing too large",
    x=5,
    y=5,
    width=100,
)

chart
