import easychart
import pandas as pd

# data retrieved from https://apps.fas.usda.gov/psdonline/app/index.html#/app/advQuery
data = pd.DataFrame(
    [
        [19661, 16595, 21334, 18036, 30321, 28929, 23864, 27000, 15500],
        [11269, 17431, 18107, 17775, 16019, 21016, 16851, 18844, 11000],
    ],
    columns=[
        "MY14/15",
        "MY15/16",
        "MY16/17",
        "MY17/18",
        "MY18/19",
        "MY19/20",
        "MY20/21",
        "MY21/22",
        "MY22/23",
    ],
    index=["corn", "wheat"],
)

chart = easychart.new("column")
chart.title = "Ukraine grain exports, by marketing year (MY)"
chart.subtitle = "thousand metric tons"
chart.stacked = True
chart.categories = data.columns

for row in data.index:
    chart.plot(data.loc[row], name=row)

chart.caption.text = "Source: USDA FAS, accessed 30 November 2022"

# move the legend to the right of the chart
# each item stacked vertically
# the whole of it centered in the middle
# with some margin between each legend entry
with chart.legend as legend:
    legend.align = "right"
    legend.layout = "vertical"
    legend.verticalAlign = "middle"
    legend.itemMarginTop = 15
    legend.title.text = "Legend"

chart
