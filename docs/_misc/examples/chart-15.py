import easychart

chart = easychart.new()
chart.chart.type = "line"
chart.chart.polar = True
chart.categories = ['Sales', 'Marketing', 'Development', 'Support','Technology', 'Administration']
chart.plot([43000, 19000, 60000, 35000, 17000, 10000], pointPlacement='on', name="budget")
chart.plot([50000, 39000, 42000, 31000, 26000, 14000], pointPlacement='on', name="actual")