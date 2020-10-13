import easychart

#data is a pd.Series of the US unemployment rate
data = easychart.datasets.load("unemployment")

chart = easychart.new(datetime=True, title="US unemployment rate", zoom="x")
chart.subtitle.text = "Source: Federal Reserve (FRED)"
chart.yAxis.labels.format = "{value}%"
chart.append(data, name="unemployment rate")
chart