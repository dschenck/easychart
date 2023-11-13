import easychart
import requests

# load the map
# see collection here https://code.highcharts.com/mapdata/
topo = requests.get(
    "https://code.highcharts.com/mapdata/countries/fr/fr-all.topo.json"
).json()

# data
data = [
    ["fr-cor", 10],
    ["fr-bre", 11],
    ["fr-pdl", 12],
    ["fr-pac", 13],
    ["fr-occ", 14],
    ["fr-naq", 15],
    ["fr-bfc", 16],
    ["fr-cvl", 17],
    ["fr-idf", 18],
    ["fr-hdf", 19],
    ["fr-ara", 20],
    ["fr-ges", 21],
    ["fr-nor", 22],
    ["fr-lre", 23],
    ["fr-may", 24],
    ["fr-gf", 25],
    ["fr-mq", 26],
    ["fr-gua", 27],
]

chart = easychart.new("map")
chart.chart.map = topo
chart.colorAxis = {}  # required
chart.plot(data, joinBy="hc-key")
chart
