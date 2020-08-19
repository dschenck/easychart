import easytree
import pandas as pd
import numpy as np
import datetime
import json
import re

import easychart.encoders as encoders

class SeriesCollection(easytree.Tree): 
    """
    Series collection
    """
    def append(self, data=None, **kwargs):
        if isinstance(data, (zip, range)):
            data = list(data)
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
        if data is None: 
            return super().append(kwargs)
        raise TypeError(f"Unexpected data type ({data.__class__})")

class Chart(easytree.Tree):
    """
    Highcharts chart configuration.
    """
    def __init__(self):
        self.series = SeriesCollection([])

    def __setattr__(self, name, value):
        if hasattr(self.__class__, f"set_{name}"): 
            getattr(self, f"set_{name}")(value)
            return 
        return super().__setattr__(name, value)

    def set_title(self, value):
        """
        Shortcut for self.title.text = value
        """ 
        if isinstance(value, str):
            self.title.text = value
            return 
        return super().__setattr__("title", value)

    def set_subtitle(self, value):
        """
        Shortcut for self.subtitle.text = value
        """ 
        if isinstance(value, str):
            self.subtitle.text = value
            return 
        return super().__setattr__("subtitle", value)

    def set_categories(self, value):
        """
        Shortcut for self.xAxis.categories = value
        """ 
        self.xAxis.categories = value

    def set_zoom(self, value):
        """
        Shortcut for self.chart.zoomType = value
        """
        if isinstance(value, str) and value.lower() in ["x", "y", "xy"]:
            self.chart.zoomType = value
            return
        if isinstance(value, bool) and value == True: 
            self.chart.zoomType = "xy"
            return
        raise ValueError(f"Unexpected value for zoom ({value})")

    def set_tooltip(self, value):
        """
        Shortcut for tooltipe
        """
        if isinstance(value, bool):
            self.tooltip.enabled = value
            return 
        if value == "shared":
            self.tooltip.shared = True
            return
        if isinstance(value, str):
            match = re.search(r"(^.+){(.+:?.+?)}(.+)", value)
            if match: 
                self.tooltip.valuePrefix = match.groups()[0]
                self.tooltip.valueSuffix = match.groups()[2]

                if ":" in match.groups()[1]:
                    submatch = re.match("\.?(\d)[f%]?", match.groups()[1].split(":")[1])
                    if submatch:
                        self.tooltip.valueDecimals = int(submatch.groups()[0])
            return
        super().__setattr__("tooltip", value)

    def set_decimals(self, value):
        if isinstance(value, int):
            self.tooltip.valueDecimals = value
            return 
        raise ValueError(f"Unexpected value for tooltip decimals ({value})")

    def set_legend(self, value):
        """
        Enable or disable the legend with a boolean
        """
        if isinstance(value, bool):
            self.legend.enabled = value
            return 
        super().__setattr__("legend", value)

    def set_stacking(self, value):
        """
        Set the stacking plot option
        """
        if value not in [None, "normal", "percent"]:
            raise ValueError(f"Unexpected stacking value ({value})")
        self.plotOptions.series.stacking = value
        return

    def append(self, data=None, **kwargs):
        """
        Shortcut for chart.series.append(data, **kwargs)
        """
        return self.series.append(data, **kwargs)

    def vline(self, x, **kwargs):
        """
        Adds a vertical line across the chart
        """
        if self.xAxis.type == "datetime":
            if isinstance(x, (datetime.datetime, datetime.date)):
                x = 1000 * x.timestamp()
            elif isinstance(x, str):
                x = 1000 * pd.Timestamp(x).timestamp()
        self.xAxis.plotLines.append(value=x, **kwargs)

    def hline(self, y, **kwargs):
        """
        Adds a horizontal line across the chart
        """
        self.yAxis.plotLines.append(value=y, **kwargs)

    def vband(self, xmin, xmax, **kwargs):
        """
        Adds a vertical band (mask) from xmin to xmax across the chart
        """
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
        """
        Adds a horizontal band (mask) from ymin to ymax across the chart
        """
        if "color" not in kwargs: 
            kwargs["color"] = "rgba(68, 170, 213, 0.2)"
        self.yAxis.plotBands.append(**{**kwargs, "from":ymin, "to":ymax})
        return self

    def show(self, width="100%", height="400px", theme=None):
        return Plot(self, width, height, theme)
        
    def save(self, filename, indent=0):
        """
        Serializes and saves the chart configuration to a JSON file
        """
        with open(filename, "w") as file: 
            json.dump(self.serialize(), file, cls=encoders.Encoder, indent=indent)
        return

class Plot: 
    """
    Chart container
    """
    def __init__(self, chart, width="100%", height="400px", theme=None):
        """
        Parameters
        ------------
        width : str (optional)
            width of the plot, expressed as a percentage of the page width
        height : str (optional)
            height of the plot, expressed as a number of pixels
        theme : dict (optional)
            dictionary of global options (theme)
        """
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
        """
        Parameters
        ------------------------
        plots : list (optional)
            list of individual plots
        theme : dict (optional)
            dictionary of global options (theme)
        """
        self.plots = plots or []
        self.theme = theme

    def add(self, chart, width="100%", height="400px"):
        """
        Adds a chart (or plot) to the grid

        Parameters
        ------------
        width : str (optional)
            width of the plot, expressed as a percentage of the grid width
        height : str (optional)
            height of the plot, expressed as a number of pixels
        """
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