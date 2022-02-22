import easychart

labels = ["O", "A", "B", "AB"]
values = [45, 40, 11, 4]

chart = easychart.new("pie", title="Distribution of blood type in the US")
chart.subtitle = "Source: American Red Cross"
chart.tooltip = "{point.percentage:.0f}%"
chart.plot([{"name": label, "y": value} for label, value in zip(labels, values)])
chart
