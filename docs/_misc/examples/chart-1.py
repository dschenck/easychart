import easychart

chart = easychart.new("column")
chart.title = "France Olympic medals"
chart.subtitle = "by year and by medal class"
chart.categories = ["Gold","Silver","Bronze"]
chart.yAxis.title.text = "medals"
chart.plot([7, 16, 18], name=2008)
chart.plot([11, 11, 13], name=2012)
chart