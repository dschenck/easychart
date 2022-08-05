import easychart
import pandas as pd

grades = pd.DataFrame(
    [[68, 87], [71, 85]], columns=["min", "max"], index=["male", "female"]
)

chart = easychart.new("columnrange")
chart.categories = grades.index
chart.plot(grades, name="min-max range of grades")
chart
