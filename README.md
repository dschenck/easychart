# easychart
[highcharts](https://www.highcharts.com/) meets python in your [Jupyter](https://jupyter.org/) notebook
 
  

## Getting started
Installing easychart is easy with pip

```
pip install easychart
```

Open a new Jupyter notebook

```python
import easychart

chart = easychart.new("column")
chart.title.text = "France Olympic medals",
chart.subtitle.text ="by year and by medal class"
chart.yAxis.title.text = "medals"
chart.categories = ["Gold","Silver","Bronze"]
chart.plot([7, 16, 18], name=2008)
chart.plot([11, 11, 13], name=2012)
chart
```

<img src="https://raw.githubusercontent.com/dschenck/easychart/latest/docs/static/demo%20(1).svg"/>

## Documentation
Complete documentation is hosted on [read the docs](https://easychart.readthedocs.io/en/latest/). Have a look at one of the [25+ example charts](https://easychart.readthedocs.io/en/latest/contents/examples/index.html). 
