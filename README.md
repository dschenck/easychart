# easychart

[highcharts](https://www.highcharts.com/) meets python in your [Jupyter](https://jupyter.org/) notebook

[![PyPI version](https://badge.fury.io/py/easychart.svg)](https://badge.fury.io/py/easychart)
[![pythons](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue)](https://pypi.org/project/easytree)
[![build](https://github.com/dschenck/easychart/workflows/testing/badge.svg)](https://github.com/dschenck/easychart/actions)
[![Documentation Status](https://readthedocs.org/projects/easychart/badge/?version=latest)](https://easychart.readthedocs.io/en/latest/?badge=latest)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Downloads](https://static.pepy.tech/badge/easychart/week)](https://pepy.tech/project/easychart)

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

## Plotting with DataFrames

easychart works with pandas, Polars, PyArrow, and other dataframe libraries. Pandas is a dependency while other dataframe libraries are supported via [narwhals](https://github.com/narwhals-dev/narwhals).

```python
import pandas as pd
import easychart

# pandas Series uses index as x-axis
data = pd.Series([10, 20, 30], index=["a", "b", "c"], name="values")
chart = easychart.new()
chart.plot(data)
chart
```

```python
import polars as pl
import easychart

# Polars DataFrame
data = pl.DataFrame({"x": [1, 2, 3], "y": [10, 20, 30]})
chart = easychart.new()
chart.plot(data)
chart
```

## Documentation

Complete documentation is hosted on [read the docs](https://easychart.readthedocs.io/en/latest/). Have a look at one of the [25+ example charts](https://easychart.readthedocs.io/en/latest/contents/examples/index.html).
