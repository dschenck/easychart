import easychart

labels = {
    "format": "{point.from} -> {point.to} {point.weight}km",
    "nodeFormat": "Node {point.name}",
}

data = [
    ["A", "D", 9],
    ["A", "C", 2],
    ["D", "E", 4],
    ["D", "F", 4],
    ["B", "C", 4],
    ["B", "D", 2],
    ["C", "E", 3],
    ["C", "F", 3],
]

chart = easychart.new(type="sankey")
chart.plot(data, keys=["from", "to", "weight", "dataLabels"], labels=labels)
chart
