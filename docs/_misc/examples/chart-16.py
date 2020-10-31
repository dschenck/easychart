import easychart
import random

x = [random.random() for _ in range(100)]
y = [-5 + 7.5 * i + random.random() for i in x]

chart = easychart.new()
chart.plot(y, index=x, type="scatter")
chart.regress(y, x)