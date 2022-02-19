import easychart

data = [
    {"name": "Spain", "y": 505370, "z": 92.9},
    {"name": "France", "y": 551500, "z": 118.7},
    {"name": "Poland", "y": 312685, "z": 124.6},
    {"name": "Czech Republic", "y": 78867, "z": 137.5},
    {"name": "Italy", "y": 301340, "z": 201.8},
    {"name": "Switzerland", "y": 41277, "z": 214.5},
    {"name": "Germany", "y": 357022, "z": 235.6},
]

chart = easychart.new("variablepie")
chart.title = "Countries compared by population density and total area"
chart.plot(data, zMin=0, name="countries")
chart
