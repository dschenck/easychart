import easychart
import datetime

#fancy fibonacci one-liner
fib = lambda x: 1 if x < 2 else fib(x - 1) + fib(x - 2)

x = [datetime.time(x) for x in range(14)]
y = [fib(x + 1) for x in range(14)]

chart = easychart.new(datetime=True)
chart.plot(y, index=x, name=datetime.time(20,0))
chart