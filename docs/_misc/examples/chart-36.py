import easychart
import pandas as pd

data = pd.DataFrame(
    [[5, 3, 4, 7, 2], [2, 2, 3, 2, 1], [3, 4, 4, 2, 5]],
    index=["John", "Jane", "Joe"],
    columns=["Apples", "Oranges", "Pears", "Grapes", "Bananas"],
)

chart = easychart.new("bar")
chart.stacked = True
chart.categories = data.columns

for person, row in data.iterrows():
    chart.plot(row, name=person)

chart
