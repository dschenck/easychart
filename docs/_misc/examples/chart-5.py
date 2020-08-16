import easychart

#data is a pd.DataFrame about 54k diamonds
data = easychart.datasets.load("diamonds")

#count number of diamonds by cut and color
data = data.groupby(["color", "cut"])["price"].count().unstack()

chart = easychart.new(title="Diamond inventories by cut and color")
chart.xAxis.categories = data.index
chart.xAxis.title.text = "Diamond color"
chart.yAxis.title.text = "Count"
chart.plotOptions.column.stacking = "normal"
chart.series.append(data, type="column")
chart