import easychart 

chart = easychart.new()
chart.plot([50, 33, 68, 35, 46, 4, 35, 6, 19, 75, 22, 11])
chart.annotate("Lowest point is here ({point.x}:{point.y})", x=5, y=4, width=100, yOffset=75)
chart.annotate("Highest point is here", x=9, y=75, width=100, xOffset=65)
chart