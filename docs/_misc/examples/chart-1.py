import easychart

chart = easychart.new()
chart.chart.type = "column"
chart.title.text = "France Olympic medals"
chart.subtitle.text = "by year and by medal class"
chart.xAxis.categories = ["Gold","Silver","Bronze"]
chart.yAxis.title.text = "medals"
chart.series.append([7, 16, 18], name=2008)
chart.series.append([11, 11, 13], name=2012)