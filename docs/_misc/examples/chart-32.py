import easychart

data = [
    ["Chrome", 58.9],
    ["Firefox", 13.29],
    ["Internet Explorer", 13],
    ["Edge", 3.78],
    ["Safari", 3.42],
    ["Safari", 7.61],
]

chart = easychart.new("pie")
chart.plot(data, innerSize="50%")

with chart.plotOptions.pie as options:
    options.startAngle = -90
    options.endAngle = 90
    options.center = ["50%", "75%"]

chart
