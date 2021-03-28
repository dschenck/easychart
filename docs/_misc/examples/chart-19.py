import easychart 

#some data
data = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

chart = easychart.new("line")
chart.title = 'Logarithmic series'
chart.yAxis.type = "logarithmic"
chart.plot(data)
chart