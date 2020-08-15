# chart-1.py
import easychart

chart = easychart.new()
chart.chart.type = "column"
chart.title.text = "France Olympic medals"
chart.subtitle.text = "by year and by medal class"
chart.xAxis.categories = ["Gold","Silver","Bronze"]
chart.yAxis.title.text = "medals"
chart.series.append([7, 16, 18], name=2008)
chart.series.append([11, 11, 13], name=2012)
chart.save("../static/charts/chart-1.json", indent=4)


# chart-2.py
import easychart

#data is a pd.Series of the US unemployment rate
data = easychart.datasets.load("unemployment")

chart = easychart.new(datetime=True, title="US unemployment rate", zoom="x")
chart.subtitle.text = "Source: Federal Reserve (FRED)"
chart.yAxis.labels.format = "{value}%"
chart.series.append(data, name="unemployment rate")
chart
chart.save("../static/charts/chart-2.json", indent=4)


# chart-3.py
import easychart

chart = easychart.new(type="pie", title="Distribution of blood type in the US")
chart.subtitle.text = "Source: American Red Cross"
chart.tooltip.pointFormat = "{point.percentage:.0f}%"
chart.series.append([{"name":bloodtype, "y":percentage} for bloodtype, percentage 
                      in zip(["O","A","B","AB"],[45,40,11,4])])
chart.save("../static/charts/chart-3.json", indent=4)


# chart-4.py
import easychart

#data is a pd.DataFrame about 54k diamonds
data = easychart.datasets.load("diamonds").sample(10000)

chart = easychart.new(title="Diamond prices", zoom="xy")
chart.subtitle.text = "by carat (weight) and by clarity"
chart.xAxis.title.text = "carat"
chart.yAxis.title.text = "price (USD)"
for clarity in ["VS1", "VVS2", "VVS1", "IF"]: 
    #isolate the diamonds with the given level of clarity
    sample = data[data["clarity"] == clarity]
    chart.series.append(sample["price"], index=sample["carat"], 
                        type="scatter", name=clarity)
chart
chart.save("../static/charts/chart-4.json", indent=4)

