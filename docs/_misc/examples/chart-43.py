import math
import pandas as pd
import easychart

numbers = pd.DataFrame(
    [[math.cos(x), math.sin(x)] for x in range(-10, 10)], index=range(-10, 10)
)

chart = easychart.new("bubble")
chart.plot(numbers)  # index + 2 columns
chart
