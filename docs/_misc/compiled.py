# chart-17.py
import easychart

data = [[-9.9, 10.3],
        [-8.6, 8.5],
        [-10.2, 11.8],
        [-1.7, 12.2],
        [-0.6, 23.1],
        [3.7, 25.4],
        [6.0, 26.2],
        [6.7, 21.4],
        [3.5, 19.5],
        [-1.3, 16.0],
        [-8.7, 9.4],
        [-9.0, 8.6]]

chart = easychart.new("columnrange")
chart.title = 'Temperature variation by month'
chart.subtitle = "Observed in Vik i Sogn, Norway, 2017"
chart.tooltip = "{value}°C"
chart.yAxis.title.text = "Temperature ( °C )"
chart.legend = False
chart.inverted = True
chart.categories = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
chart.plot(data, name="Temperature")
chart.save("../static/charts/chart-17.json", indent=4)


# chart-23.py
import easychart
import pandas as pd

data = pd.DataFrame([[107, 31, 635, 203, 2],[133, 156, 947, 408, 6],
                     [814, 841, 3714, 727, 31],[1216, 1001, 4436, 738, 40]], 
                    index=[1800,1900,2000,2016], 
                    columns=['Africa', 'America', 'Asia', 'Europe', 'Oceania'])

chart = easychart.new("bar")
chart.title = "Historic World Population by Region"
chart.subtitle = "Source: <a href='https://en.wikipedia.org/wiki/World_population'>Wikipedia.org</a>"
chart.categories = data.columns
chart.yAxis.title = {"text":"Population (millions)", "align":"high"}
chart.tooltip = "{value:.0f}m"
for year in data.index: 
    chart.plot(data.loc[year], name=year, datalabels=(year==2016))
chart
chart.save("../static/charts/chart-23.json", indent=4)


# chart-27.py
import easychart

data = [
    ['Brazil', 'Portugal', 5],
    ['Brazil', 'France', 1],
    ['Canada', 'Portugal', 1],
    ['Canada', 'France', 5],
    ['Mexico', 'Portugal', 1],
    ['Mexico', 'France', 1],
    ['USA', 'Portugal', 1],
    ['USA', 'France', 1],
    ['Portugal', 'Angola', 2],
    ['Portugal', 'Senegal', 1],
    ['France', 'Angola', 1],
    ['France', 'Senegal', 3],
    ['Spain', 'Senegal', 1],
    ['Spain', 'Morocco', 3],
    ['England', 'Morocco', 2],
    ['England', 'South Africa', 7],
    ['South Africa', 'China', 5],
    ['Angola', 'Japan', 3],
    ['Senegal', 'India', 1],
    ['Senegal', 'Japan', 3],
    ['Mali', 'India', 1],
    ['Morocco', 'India', 1],
    ['Morocco', 'Japan', 3]
]

chart = easychart.new(type="sankey")
chart.title = "Sankey diagram"
chart.subtitle = "Flow diagram in which the width of the arrows is proportional to the flow rate"
chart.plot(data, keys=["from","to","weight"])
chart
chart.save("../static/charts/chart-27.json", indent=4)


# chart-13.py
import easychart

chart = easychart.new(tooltip="shared")
chart.title = "Average Monthly Temperature and Rainfall in Tokyo"
chart.subtitle = "Source: WorldClimate.com"
chart.categories = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

#add two axes
chart.yAxis.append(title={"text":"Temperature"}, labels={"format":'{value}°C'})
chart.yAxis.append(title={"text":"Rainfall"}, labels={"format":'{value} mm'}, opposite=True)

chart.plot([49.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4], 
             name="Rainfall", type="column", yAxis=1, tooltip={"valueSuffix":"mm"})
chart.plot([7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6],
             name="Temperature", type="spline", yAxis=0, tooltip={"valueSuffix":"°C"})
chart
chart.save("../static/charts/chart-13.json", indent=4)


# chart-26.py
import easychart

labels = ["O","A","B","AB"]
values = [45,40,11,4]

chart = easychart.new("pie", title="Distribution of blood type in the US")
chart.subtitle = "Source: American Red Cross"
chart.tooltip = "{point.percentage:.0f}%"
chart.plot(values, index=labels, labels="{point.name} ({point.y}%)")
chart
chart.save("../static/charts/chart-26.json", indent=4)


# chart-12.py
import easychart

data = [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
        [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
 
chart = easychart.new()
chart.title = "Atmosphere Temperature by Altitude"
chart.subtitle = "According to the Standard Atmosphere Model"
chart.chart = {"type":"spline", "inverted":True}

with chart.xAxis as axis:
    axis.reversed = False
    axis.title.text = "Altitude"
    axis.labels.format = "{value} km"
    
with chart.yAxis as axis: 
    axis.labels.format = "{value}°"
    axis.title.text = "Temperature"
    axis.title.rotation = 0
    
chart.tooltip.headerFormat =  '<b>{series.name}</b><br/>'
chart.tooltip.pointFormat =  '{point.x} km: {point.y}°C'
    
chart.legend.enabled = False
chart.append(data, name="temperature")
chart
chart.save("../static/charts/chart-12.json", indent=4)


# chart-16.py
import easychart
import random

x = [random.random() for _ in range(100)]
y = [-5 + 7.5 * i + random.random() for i in x]

chart = easychart.new()
chart.plot(y, index=x, type="scatter")
chart.regress(y, x)
chart.save("../static/charts/chart-16.json", indent=4)


# chart-22.py
import easychart

data = [[0, 0, 10], [0, 1, 19], [0, 2, 8], [0, 3, 24], [0, 4, 67], [1, 0, 92], 
        [1, 1, 58], [1, 2, 78], [1, 3, 117], [1, 4, 48], [2, 0, 35], [2, 1, 15],
        [2, 2, 123], [2, 3, 64], [2, 4, 52], [3, 0, 72], [3, 1, 132], [3, 2, 114], 
        [3, 3, 19], [3, 4, 16], [4, 0, 38], [4, 1, 5], [4, 2, 8], [4, 3, 117], 
        [4, 4, 115], [5, 0, 88], [5, 1, 32], [5, 2, 12], [5, 3, 6], [5, 4, 120], 
        [6, 0, 13], [6, 1, 44], [6, 2, 88], [6, 3, 98], [6, 4, 96], [7, 0, 31],
        [7, 1, 1], [7, 2, 82], [7, 3, 32], [7, 4, 30], [8, 0, 85], [8, 1, 97], 
        [8, 2, 123], [8, 3, 64], [8, 4, 84], [9, 0, 47], [9, 1, 114], [9, 2, 31], 
        [9, 3, 48], [9, 4, 91]]

chart = easychart.new("heatmap")
chart.title = "Sales per employee per weekday"
chart.xAxis.categories = ['Alexander', 'Marie', 'Maximilian', 'Sophia', 'Lukas', 'Maria', 'Leon', 'Anna', 'Tim', 'Laura']
chart.yAxis.categories = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
chart.yAxis.reversed = True
with chart.colorAxis as axis: 
    axis.min = 0
    axis.minColor =  "#FFFFFF"
    axis.maxColor =  "#44ab79"
with chart.legend as legend: 
    legend.align = "right"
    legend.layout = "vertical"
    legend.margin = 0
    legend.verticalAlign = "top"
    legend.y = 20
    legend.symbolHeight = 250
chart.plot(data, name="daily sale", labels=True)
chart
chart.save("../static/charts/chart-22.json", indent=4)


# chart-1.py
import easychart

chart = easychart.new("column")
chart.title = "France Olympic medals"
chart.subtitle = "by year and by medal class"
chart.categories = ["Gold","Silver","Bronze"]
chart.yAxis.title.text = "medals"
chart.plot([7, 16, 18], name=2008)
chart.plot([11, 11, 13], name=2012)
chart
chart.save("../static/charts/chart-1.json", indent=4)


# chart-19.py
import easychart 

#some data
data = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

chart = easychart.new("line")
chart.title = 'Logarithmic series'
chart.yAxis.type = "logarithmic"
chart.plot(data)
chart
chart.save("../static/charts/chart-19.json", indent=4)


# chart-5.py
import easychart

#data is a pd.DataFrame about 54k diamonds
data = easychart.datasets.load("diamonds")

#count number of diamonds by cut and color
data = data.groupby(["color", "cut"])["price"].count().unstack()

chart = easychart.new("column", title="Diamond inventories by cut and color")
chart.categories = data.index
chart.xAxis.title.text = "Diamond color"
chart.yAxis.title.text = "Count"
chart.stacking = "normal"
for cut in data: 
    chart.plot(data[cut], name=cut)
chart
chart.save("../static/charts/chart-5.json", indent=4)


# chart-18.py
import pandas as pd
import easychart 

data = pd.DataFrame([[7.0, 6.9, 9.5, 14.5, 18.4, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6],
                     [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8]], 
                    index=["Tokyo","London"],
                    columns=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])

chart = easychart.new("line")
chart.title = "Monthly Average Temperature"
chart.subtitle = "Source: WorldClimate.com"
chart.categories = data.columns
chart.yAxis.title.text = "Temperature (°C)"
for city in data.index:
    chart.plot(data.loc[city], name=city, labels="{point.y}°C")
chart
chart.save("../static/charts/chart-18.json", indent=4)


# chart-4.py
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
chart.save("../static/charts/chart-4.json", indent=4)


# chart-7.py
import easychart

#compute the annual high, low and last value of the S&P since 2010
data = easychart.datasets.load("S&P500")["Close"]["20100101":]
data = data.groupby(data.index.year).agg(["min","max","last"])

chart = easychart.new(title="S&P 500 annual trading range", tooltip="shared", ytitle="")
chart.categories = data.index
chart.plot(zip(data["min"], data["max"]), type="arearange", 
                color="#eeeeee", name="annual range", 
                marker={"enabled":False})
chart.plot(data["last"], name="end of year")
chart
chart.save("../static/charts/chart-7.json", indent=4)


# chart-3.py
import easychart

labels = ["O","A","B","AB"]
values = [45,40,11,4]

chart = easychart.new("pie", title="Distribution of blood type in the US")
chart.subtitle = "Source: American Red Cross"
chart.tooltip = "{point.percentage:.0f}%"
chart.plot([{"name":label, "y":value} for label, value in zip(labels, values)])
chart
chart.save("../static/charts/chart-3.json", indent=4)


# chart-2.py
import easychart

#data is a pd.Series of the US unemployment rate
data = easychart.datasets.load("unemployment")

chart = easychart.new(datetime=True, title="US unemployment rate", zoom="x")
chart.subtitle = "Source: Federal Reserve (FRED)"
chart.yAxis.labels.format = "{value}%"
chart.plot(data, name="unemployment rate")
chart
chart.save("../static/charts/chart-2.json", indent=4)


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
chart.subtitle = "Detrended (100 = 1975-2020 average)"
chart.categories = pivot.index
chart.marker = False
chart.plot(zip(pivot["5%"], pivot["95%"]), name="10%-90% range", type="arearange", color="#eeeeee")
chart.plot(zip(pivot["25%"], pivot["75%"]), name="25%-75% range", type="arearange", color="#cccccc")
chart.plot(pivot["0%"], name="min", dashstyle="dot", color="black")
chart.plot(pivot["100%"], name="max", dashstyle="dot", color="black")
chart.plot(pivot[2019], name="2019")
chart.plot(pivot[2020], name="2020")
chart
chart.save("../static/charts/chart-6.json", indent=4)


# chart-25.py
import easychart
import datetime

#fancy fibonacci one-liner
fib = lambda x: 1 if x < 2 else fib(x - 1) + fib(x - 2)

x = [datetime.time(x) for x in range(14)]
y = [fib(x + 1) for x in range(14)]

chart = easychart.new(datetime=True)
chart.xAxis.labels.format = "{value:%H:%M}"
chart.tooltip.xDateFormat = '%H:%M'
chart.plot(y, index=x, name="another example")
chart
chart.save("../static/charts/chart-25.json", indent=4)


# chart-11.py
import easychart
import pandas as pd

#data is a pd.DataFrame of stock prices
data = easychart.datasets.load("stocks")
data = data[:"20200430"].resample("M").last().pct_change()[1:]

stats = 100 * pd.concat([data.quantile(0.10).rename("10%"),
                   data.quantile(0.25).rename("25%"),
                   data.quantile(0.75).rename("75%"),
                   data.quantile(0.90).rename("90%"),
                   data.iloc[-1].rename("last")], axis=1)

chart = easychart.new()
chart.title = "Normal monthly stock movements"
chart.subtitle = "April 2020 change vs 10% and 25% quantile percentage changes since 2003"
chart.categories = stats.index
chart.yAxis.labels.format = "{value}%"
chart.tooltip = ("shared", "{value:.1}%")
chart.plotOptions.columnrange.grouping = False
chart.plotOptions.line.states.hover.enabled = False
chart.plot(zip(stats["10%"], stats["90%"]), name="10%-90% range", 
             type="columnrange", color="rgba(20, 20, 20, 0.1)")
chart.plot(zip(stats["25%"], stats["75%"]), name="25%-75% range", 
             type="columnrange", color="rgba(20, 20, 20, 0.3)")
chart.plot(stats["last"], name="April 2020", lineWidth=0, allowPointSelect=False)

chart
chart.save("../static/charts/chart-11.json", indent=4)


# chart-15.py
import easychart

chart = easychart.new()
chart.chart.type = "line"
chart.chart.polar = True
chart.categories = ['Sales', 'Marketing', 'Development', 'Support','Technology', 'Administration']
chart.plot([43000, 19000, 60000, 35000, 17000, 10000], pointPlacement='on', name="budget")
chart.plot([50000, 39000, 42000, 31000, 26000, 14000], pointPlacement='on', name="actual")
chart.save("../static/charts/chart-15.json", indent=4)


# chart-21.py
import easychart

data = [
    { "x": 95,   "y": 95,   "z": 13.8, "name": "BE", "country": "Belgium" },
    { "x": 86.5, "y": 102.9,"z": 14.7, "name": "DE", "country": "Germany" },
    { "x": 80.8, "y": 91.5, "z": 15.8, "name": "FI", "country": "Finland" },
    { "x": 80.4, "y": 102.5,"z": 12,   "name": "NL", "country": "Netherlands" },
    { "x": 80.3, "y": 86.1, "z": 11.8, "name": "SE", "country": "Sweden" },
    { "x": 78.4, "y": 70.1, "z": 16.6, "name": "ES", "country": "Spain" },
    { "x": 74.2, "y": 68.5, "z": 14.5, "name": "FR", "country": "France" },
    { "x": 73.5, "y": 83.1, "z": 10,   "name": "NO", "country": "Norway" },
    { "x": 71,   "y": 93.2, "z": 24.7, "name": "UK", "country": "United Kingdom" },
    { "x": 69.2, "y": 57.6, "z": 10.4, "name": "IT", "country": "Italy" },
    { "x": 68.6, "y": 20,   "z": 16,   "name": "RU", "country": "Russia" },
    { "x": 65.5, "y": 126.4,"z": 35.3, "name": "US", "country": "United States" },
    { "x": 65.4, "y": 50.8, "z": 28.5, "name": "HU", "country": "Hungary" },
    { "x": 63.4, "y": 51.8, "z": 15.4, "name": "PT", "country": "Portugal" },
    { "x": 64,   "y": 82.9, "z": 31.3, "name": "NZ", "country": "New Zealand" }
]
    
chart = easychart.new("bubble")
chart.title = 'Sugar and fat intake per country'
chart.subtitle = 'Source: <a href="http://www.euromonitor.com/">Euromonitor</a> and <a href="https://data.oecd.org/">OECD</a>'
with chart.xAxis as axis: 
    axis.title.text = 'Daily fat intake'
    axis.labels.format = "{value}g/day"
with chart.yAxis as axis:
    axis.title.text = 'Daily sugar intake'
    axis.labels.format = "{value}g/day"
chart.plot(data, datalabels="{point.name}", name="Obesity rate (% total population)")
chart
chart.save("../static/charts/chart-21.json", indent=4)


# chart-9.py
import easychart 

chart = easychart.new(title="US 2016 Presidential election results", 
    ytitle="", yformat="{value}%")
chart.categories = ["Electoral vote", "Popular vote"]
chart.plot([46.1,48.2], name="Hillary Clinton", 
    type="column", color="rgb(18,8,55)")
chart.plot([57.3,42.7], name="Donald Trump", 
    type="column", color="rgb(202,0,4)")
chart
chart.save("../static/charts/chart-9.json", indent=4)


# chart-14.py
import easychart

#min, Q1, median, Q3, max
data = [[760, 801, 848, 895, 965],
        [733, 853, 939, 980, 1080],
        [714, 762, 817, 870, 918],
        [724, 802, 806, 871, 950],
        [834, 836, 864, 882, 910]]

chart = easychart.new(type="boxplot")
chart.categories = ["A","B","C","D","E"]
chart.plot(data, name="distribution of values")
chart.save("../static/charts/chart-14.json", indent=4)


# chart-20.py
import easychart

chart = easychart.new("column")
chart.stacked = True
chart.title = 'Total fruit consumption, grouped by gender'
chart.categories = ['Apples', 'Oranges', 'Pears', 'Grapes', 'Bananas']
with chart.yAxis as axis: 
    axis.allowDecimals = False
    axis.min = 0 
    axis.title.text = "Number of fruits"
chart.tooltip = "{value:.0f}"
chart.plot([5, 3, 4, 7, 2], name="John", stack="male")
chart.plot([3, 4, 4, 2, 5], name="Joe", stack="male")
chart.plot([2, 5, 6, 2, 1], name="Jane", stack="female")
chart.plot([3, 0, 4, 4, 3], name="Janet", stack="female")
chart
chart.save("../static/charts/chart-20.json", indent=4)


# chart-8.py
import easychart

chart = easychart.new()
chart.plot([1,1,2,3,5,8], name="Fibonacci series")
chart
chart.save("../static/charts/chart-8.json", indent=4)


# chart-24.py
import easychart
import datetime

#fancy fibonacci one-liner
fib = lambda x: 1 if x < 2 else fib(x - 1) + fib(x - 2)

x = [datetime.time(x) for x in range(14)]
y = [fib(x + 1) for x in range(14)]

chart = easychart.new(datetime=True)
chart.plot(y, index=x, name=datetime.time(20,0))
chart
chart.save("../static/charts/chart-24.json", indent=4)


# chart-10.py
import easychart

#data is a pd.DataFrame with world population by continent 
#in 1950, 2017, 2030, 2050 and 2100
data = easychart.datasets.load("populations")

chart = easychart.new()
chart.title = "Distribution of world population by continent"
chart.subtitle = "UN World Population Prospect (2017)"
chart.stacking = "percent"
chart.yAxis.labels.format = "{value}%"
chart.tooltip = ("shared", "{value:.1}%")
for column in data.columns[::-1]: 
    chart.plot(data[column], index=data.index, type="area", marker=False)
chart.vband(2020, 2100, color="rgba(200,200,200,0.2)", zIndex=20,
            label={"text":"forecast", "style":{"color":"white"}})
chart
chart.save("../static/charts/chart-10.json", indent=4)

