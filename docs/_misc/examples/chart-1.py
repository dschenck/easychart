import easychart

chart = easychart.new()
chart.chart.type = "column"
chart.title.text = "France Olympic medals"
chart.subtitle.text = "by year and by medal class"
chart.categories = ["Gold","Silver","Bronze"]
chart.yAxis.title.text = "medals"
chart.append([7, 16, 18], name=2008)
chart.append([11, 11, 13], name=2012)
chart