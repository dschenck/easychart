import easychart

data = [
    ["A", "D", 9, "#BCD4DE"],  # gray
    ["A", "C", 2, "#FFD675"],  # light yellow
    ["D", "E", 4, "#BCD4DE"],  # gray
    ["D", "F", 4, "#BCD4DE"],  # gray
    ["B", "C", 4, "#FFD675"],  # light yellow
    ["B", "D", 4, "#BCD4DE"],  # gray
    ["C", "E", 3, "#F7BA2D"],  # darker yellow
    ["C", "F", 3, "#BCD4DE"],  # gray
]

chart = easychart.new(type="sankey")
chart.plot(data, keys=["from", "to", "weight", "color"])
chart
