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
    chart.append(data[column], index=data.index, type="area", marker={"enabled":False})
chart.vband(2020, 2100, color="rgba(200,200,200,0.2)", zIndex=20,
            label={"text":"forecast", "style":{"color":"white"}})
chart