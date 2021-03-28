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