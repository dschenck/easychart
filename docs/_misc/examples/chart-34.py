import easychart
import pandas as pd

data = pd.Series([45, 40, 11, 4], index=["O", "A", "B", "AB"])

chart = easychart.new("pie", title="Distribution of blood type in the US")
chart.subtitle = "Source: American Red Cross"
chart.tooltip = "{point.percentage:.0f}%"
chart.plot(data)
chart
