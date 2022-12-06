import easychart

chart = easychart.new("area")
chart.plotOptions.area.fillOpacity = 0.5
chart.plot([10, 9, 11, 11, 8, 13, 12, 14], name="Arvid")
chart.plot([13, 9, 10, 10, 8, None, 8, 6], name="Yasin", color="#5A5A5A")
chart
