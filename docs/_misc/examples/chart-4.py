import easychart

#data is a pd.DataFrame about 54k diamonds
data = easychart.datasets.load("diamonds").sample(10000)

chart = easychart.new(title="Diamond prices", zoom="xy")
chart.subtitle = "by carat (weight) and by clarity"
chart.xAxis.title.text = "carat"
chart.yAxis.title.text = "price (USD)"
for clarity in ["VS1", "VVS2", "VVS1", "IF"]: 
    #isolate the diamonds with the given level of clarity
    sample = data[data["clarity"] == clarity]
    chart.plot(sample["price"], index=sample["carat"], type="scatter", name=clarity)
chart