import easytree
import pandas as pd
import numpy as np
import datetime

class SeriesCollection(easytree.Tree): 
    """
    Series collection
    """
    def append(self, data, **kwargs):
        if isinstance(data, (list, tuple)):
            if "index" in kwargs:
                index = kwargs.pop("index")
                if all([isinstance(d, datetime.date) for d in index]):
                    data = [(1000 * d.timestamp(), v) for (d, v) in zip(index, data)]
                else:
                    data = [(i, v) for (i, v) in zip(index, data)]
            return super().append(data=data, **kwargs)
        if isinstance(data, (pd.Series)):
            if "name" not in kwargs:
                kwargs["name"] = data.name
            if "index" not in kwargs:
                if all([isinstance(d, datetime.date) for d in data.index]):
                    data = [(1000 * d.timestamp(), v) for (d, v) in zip(data.index, data)]
                else:
                    data = data.values
            else:
                index = kwargs.pop("index")
                if all([isinstance(d, datetime.date) for d in index]):
                    data = [(1000 * d.timestamp(), v) for (d, v) in zip(index, data)]
                else:
                    data = [(i, v) for (i, v) in zip(index, data)]
            return super().append(data=data, **kwargs)
        if isinstance(data, pd.DataFrame):
            if "name" in kwargs: 
                if callable(kwargs["name"]):
                    name = [kwargs["name"](c) for c in data.columns]
            else:
                name = data.columns
            for i, column in enumerate(data): 
                self.append(data[column], **{**kwargs, "name":name[i]})
            return
        if isinstance(data, np.ndarray) and data.ndim == 1:
            return self.append(data.tolist(), **kwargs)
        if isinstance(data, np.ndarray) and data.ndim == 2: 
            for column in data.T: 
                self.append(column, **kwargs)
            return
        raise TypeError(f"Unexpected data type ({data.__class__})")

class Chart(easytree.Tree):
    """
    Highcharts chart configuration
    """
    def __init__(self):
        self.series = SeriesCollection([])

    def show(self, width="100%", height="400px", theme=None):
        return Plot(self, width, height, theme)

    def vline(self, x, **kwargs):
        if self.xAxis.type == "datetime":
            if isinstance(x, (datetime.datetime, datetime.date)):
                x = 1000 * x.timestamp()
            elif isinstance(x, str):
                x = 1000 * pd.Timestamp(x).timestamp()
        self.xAxis.plotLines.append(value=x, **kwargs)

    def hline(self, y, **kwargs):
        self.yAxis.plotLines.append(value=y, **kwargs)

    def vband(self, xmin, xmax, **kwargs):
        if "color" not in kwargs: 
            kwargs["color"] = "rgba(68, 170, 213, 0.2)"
        if self.xAxis.type == "datetime":
            if isinstance(xmin, (datetime.datetime, datetime.date)):
                xmin = 1000 * xmin.timestamp()
            elif isinstance(xmin, str):
                xmin = 1000 * pd.Timestamp(xmin).timestamp()
            if isinstance(xmax, (datetime.datetime, datetime.date)):
                xmax = 1000 * xmax.timestamp()
            elif isinstance(xmax, str):
                xmax = 1000 * pd.Timestamp(xmax).timestamp()
        self.xAxis.plotBands.append(**{**kwargs, "from":xmin, "to":xmax})
        return self

    def hband(self, ymin, ymax, **kwargs):
        if "color" not in kwargs: 
            kwargs["color"] = "rgba(68, 170, 213, 0.2)"
        self.yAxis.plotBands.append(**{**kwargs, "from":ymin, "to":ymax})
        return self

class Plot: 
    """
    Chart container
    """
    def __init__(self, chart, width="100%", height="400px", theme=None):
        self.chart  = chart
        if not isinstance(width, str) and not width.endswith("%"):
            width = f"{width}%"
        self.width  = width
        if not isinstance(height, str) and not height.endswith("px"):
            height = f"{height}px"
        self.height = height
        self.theme  = theme

    def __repr__(self):
        return f"<Plot height={self.height} width={self.width}>"

    def serialize(self):
        if isinstance(self.chart, dict): 
            return {"chart":self.chart,"width":self.width,"height":self.height}
        if isinstance(self.chart, (Chart, easytree.Tree)):
            return {"chart":self.chart.serialize(),"width":self.width, "height":self.height}
        raise NotImplementedError

class Grid: 
    """
    Grid of chart plots
    """
    def __init__(self, plots=None, theme=None):
        self.plots = plots or []
        self.theme = theme

    def add(self, chart, width="100%", height="400px"):
        if not isinstance(chart, Plot):
            chart = Plot(chart, width=width, height=height)
        self.plots.append(chart)

    @property
    def height(self):
        #extract the height and width of each plot
        heights = [int(plot.height[:-2]) for plot in self.plots]
        widths  = [int(plot.width[:-1]) for plot in self.plots]
        #group the plots by row
        cumwidth, rows = 0, []
        for i, (height, width) in enumerate(zip(heights, widths)):
            if i == 0: 
                rows.append([height])
            else:
                if (cumwidth + width) <= 100: 
                    rows[-1].append(height)
                else:
                    rows.append([height])
                    cumwidth = 0
            cumwidth += width
        return f"{sum([max(row) for row in rows])}px"