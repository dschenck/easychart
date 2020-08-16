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


# chart-5.py
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
chart.save("../static/charts/chart-5.json", indent=4)


# chart-6.py
import easychart

#data is pd.Series of electric and gas utility industrial production
data = easychart.datasets.load("electricity")

#detrend the data naively
growth = (data/data.shift(12) - 1).fillna(0).apply(lambda x: (1 + x)**(1/12) - 1)
data = data.divide((1 + growth.ewm(alpha=0.25).mean()).cumprod())
#slice the data since 1975
data = data["1975-01-01":]
#rebase the data to average 100
data = 100 * data / data.mean()

#create a pivot (month, year)
pivot = data.groupby([data.index.month, data.index.year]).last().unstack().fillna("")
pivot.index = ["Jan","Feb","Mar","Apr","May","Jun","July","Aug","Sep","Oct","Nov","Dec"]

#compute different levels of historical norms
for decile in [0, 0.05, 0.25, 0.5, 0.75, 0.95, 1]: 
    pivot[f"{decile:.0%}"] = pivot.iloc[:,:-1].quantile(decile, axis=1)

#create the chart
chart = easychart.new(tooltip="shared", title="US gas and electricity production")
chart.subtitle.text = "Detrended (100 = 1975-2020 average)"
chart.xAxis.categories = pivot.index
chart.plotOptions.arearange.marker.enabled = False
chart.plotOptions.line.marker.enabled = False
chart.series.append(zip(pivot["5%"], pivot["95%"]), name="10%-90% range", type="arearange", color="#eeeeee")
chart.series.append(zip(pivot["25%"], pivot["75%"]), name="25%-75% range", type="arearange", color="#cccccc")
chart.series.append(pivot["0%"], name="min", dashStyle="dot", color="black")
chart.series.append(pivot["100%"], name="max", dashStyle="dot", color="black")
chart.series.append(pivot[2019], name="2019")
chart.series.append(pivot[2020], name="2020")
chart
chart.save("../static/charts/chart-6.json", indent=4)


# chart-7.py
import easychart

#compute the annual high, low and last value of the S&P since 2010
data = easychart.datasets.load("S&P500")["Close"]["20100101":]
data = data.groupby(data.index.year).agg(["min","max","last"])

chart = easychart.new(title="S&P 500 annual trading range", tooltip="shared", ytitle="")
chart.xAxis.categories = data.index
chart.series.append(zip(data["min"], data["max"]), type="arearange", 
                    color="#eeeeee", name="annual range", 
                    marker={"enabled":False})
chart.series.append(data["last"], name="end of year")
chart.save("../static/charts/chart-7.json", indent=4)


# chart-8.py
import easychart

chart = easychart.new()
chart.series.append([1,1,2,3,5,8], name="Fibonacci series")
chart.save("../static/charts/chart-8.json", indent=4)


# chart-9.py
import easychart 

chart = easychart.new(title="US 2016 Presidential election results", 
    ytitle="", yformat="{value}%")
chart.xAxis.categories = ["Electoral vote", "Popular vote"]
chart.append([46.1,48.2], name="Hillary Clinton", 
    type="column", color="rgb(18,8,55)")
chart.append([57.3,42.7], name="Donald Trump", 
    type="column", color="rgb(202,0,4)")
chart.save("../static/charts/chart-9.json", indent=4)

