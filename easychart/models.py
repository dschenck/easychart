import easytree
import pandas as pd
import numpy as np
import datetime
import collections
import simplejson
import re

import easychart.encoders as encoders
import easychart.internals as internals
import easychart.config


class SeriesCollection(easytree.Tree):
    """
    Series collection
    """

    def append(self, data=None, **kwargs):
        if "legend" in kwargs:
            kwargs["showInLegend"] = kwargs.pop("legend")

        if "markers" in kwargs:
            kwargs["marker"] = kwargs.pop("markers")

        if "marker" in kwargs:
            if isinstance(kwargs["marker"], bool):
                kwargs["marker"] = {"enabled": kwargs["marker"]}
            elif kwargs["marker"] is None:
                kwargs["marker"] = {"enabled": False}

        if "width" in kwargs:
            kwargs["lineWidth"] = kwargs.pop("width")

        if "dash" in kwargs:
            kwargs["dashStyle"] = kwargs.pop("dash")

        if "dashstyle" in kwargs:
            kwargs["dashStyle"] = kwargs.pop("dashstyle")

        if "linestyle" in kwargs:
            kwargs["dashStyle"] = kwargs.pop("linestyle")

        if "active" in kwargs:
            kwargs["visible"] = kwargs.pop("active")

        if "enabled" in kwargs:
            kwargs["visible"] = kwargs.pop("enabled")

        if "labels" in kwargs:
            if isinstance(kwargs["labels"], bool):
                kwargs["dataLabels"] = {"enabled": kwargs.pop("labels")}
            elif isinstance(kwargs["labels"], str):
                kwargs["dataLabels"] = {"enabled": True, "format": kwargs.pop("labels")}
            else:
                kwargs["dataLabels"] = kwargs.pop("labels")

        if "datalabels" in kwargs:
            if isinstance(kwargs["datalabels"], bool):
                kwargs["dataLabels"] = {"enabled": kwargs.pop("datalabels")}
            elif isinstance(kwargs["datalabels"], str):
                kwargs["dataLabels"] = {
                    "enabled": True,
                    "format": kwargs.pop("datalabels"),
                }
            else:
                kwargs["dataLabels"] = kwargs.pop("datalabels")

        if isinstance(data, pd.Series):
            if "name" not in kwargs:
                kwargs["name"] = data.name

        if isinstance(data, (pd.Series, pd.DataFrame)):
            if "index" in kwargs:
                if isinstance(kwargs["index"], collections.abc.Iterable):
                    data = data.values.tolist()
                elif isinstance(kwargs["index"], bool):
                    if kwargs["index"] == False:
                        data = data.values.tolist()
                    if kwargs["index"] == True:
                        data = data.reset_index().values.tolist()
            else:
                data = data.reset_index().values.tolist()

        if "index" in kwargs and isinstance(kwargs["index"], collections.abc.Iterable):
            data = [
                internals.flatten(i, v) for (i, v) in zip(kwargs.pop("index"), data)
            ]

        return super().append(data=data, **kwargs)


class Chart(easytree.Tree):
    """
    A Highchart chart configuration

    The :code:`Chart` object comes with convenience setters to make it easier and faster to create charts:

    \- setting a string to :code:`chart.type` will assign the value to the :code:`chart.chart.type` attribute.
    ::

        #equivalent to chart.chart.type = "column"
        chart.type = "column"

    \- setting a value to :code:`chart.height` will assign the value to the :code:`chart.chart.height` attribute.
    ::

        #equivalent to chart.chart.height = "400px"
        chart.height = "400px"

    \- setting a value to :code:`chart.width` will assign the value to the :code:`chart.chart.width` attribute.
    ::

        #equivalent to chart.chart.width = "400px"
        chart.width = "400px"

    \- setting a string to :code:`chart.title` will assign the value to the :code:`chart.title.text` attribute.
    ::

        #equivalent to chart.title.text = "Chart title"
        chart.title = "Chart title"

    \- setting a string to :code:`chart.subtitle` will assign the value to the :code:`chart.subtitle.text` attribute.
    ::

        #equivalent to chart.subtitle.text = "Chart subtitle"
        chart.subtitle = "Chart subtitle"  

    \- setting :code:`chart.datetime` equal to :code:`True` will set the xAxis' type equal to :code:`"datetime"`
    ::

        #equivalent to chart.xAxis.type = "datetime"
        chart.datetime = True

    \- setting an iterable (list, tuple...) to :code:`chart.categories` will assign the value to :code:`chart.xAxis.categories`.
    ::

        #equivalent to chart.xAxis.categories = ["Paris","New York","Nairobi"]
        chart.categories = ["Paris","New York","Nairobi"]

    \- setting :code:`None`, :code:`"x"`, :code:`"y"` or :code:`"xy"` to :code:`chart.zoom` will assign the value to the :code:`chart.chart.zoomType` attribute.
    ::

        #equivalent to chart.chart.zoomType = "xy"
        chart.zoom = "xy"

    \- setting a boolean to :code:`chart.tooltip` will enable or disable the tooltip. 
    ::

        #equivalent to chart.tooltip.enabled = False
        chart.tooltip = False

    \- setting :code:`"shared"` to :code:`chart.tooltip` will set :code:`chart.tooltip.shared = True`. 
    ::

        #equivalent to chart.tooltip.shared = True
        chart.tooltip = "shared"

    \- setting a label format string to :code:`chart.tooltip` will format the decimals, prefix and suffix. 
    ::

        chart.tooltip = "${value:.2f} per unit"

        #is equivalent to...
        chart.tooltip.valuePrefix = "$"
        chart.tooltip.valueSuffix = " per unit"
        chart.tooltip.valueDecimals = 2

    \- setting a tuple of values to the :code:`chart.tooltip` will set each value to the toolip attribute, as per the above rules. 
    ::

        chart.tooltip = ("shared", "{value}mm")

        #is equivalent to...
        chart.tooltip.shared = True
        chart.tooltip.valueSuffix = "mm"

    \- setting a boolean to :code:`chart.legend` will enable or disable the legend
    ::

        #equivalent to chart.legend.enabled = False
        chart.legend = False

    \- setting one of :code:`None`, :code:`"percent"` or :code:`"normal"` to :code:`chart.stacking` will affect the value to :code:`chart.plotOptions.series.stacking`. 
    ::

        #equivalent to chart.plotOptions.series.stacking = "percent"
        chart.stacking = "percent"

    \- setting :code:`True` to :code:`chart.inverted` will invert the chart
    ::

        #equivalent to self.chart.inverted = True
        chart.inverted = True

    \- setting :code:`True` or :code:`False` to :code:`chart.marker` will enable or disable series markers
    ::

        #equivalent to chart.plotOptions.series.marker.enabled = True
        chart.marker = True

    \- setting a non-boolean value to :code:`chart.marker` will assign that value to the series' marker property
    ::

        #equivalent to chart.plotOptions.series.marker = value
        chart.marker = value

    \- setting a boolean value to :code:`chart.datalabels`  or :code:`chart.labels` will enable or disable the chart data labels
    ::

        #equivalent to chart.plotOptions.series.dataLabels.enabled = True
        chart.datalabels = True

    \- setting a string to :code:`chart.datalabels` or :code:`chart.labels` will assign the value as the format of the data labels
    ::

        #equivalent to chart.plotOptions.series.dataLabels.format = value
        chart.labels = "{value}%
    """

    def __init__(self):
        self.series = SeriesCollection([])

    def __setattr__(self, name, value):
        if hasattr(self.__class__, f"set_{name}"):
            getattr(self, f"set_{name}")(value)
            return
        return super().__setattr__(name, value)

    def set_type(self, value):
        """
        Shortcut for self.chart.type = value
        """
        self.chart.type = value

    def set_height(self, value):
        """
        Shortcut for self.chart.height = value
        """
        self.chart.height = value

    def set_width(self, value):
        """
        Shortcut for self.chart.width = value
        """
        self.chart.width = value

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
            self.chart.zoomType = value.lower()
            return
        if isinstance(value, bool) and value == True:
            self.chart.zoomType = "xy"
            return
        raise ValueError(f"Unexpected value for zoom ({value})")

    def set_tooltip(self, value):
        """
        Shortcut for tooltip
        """
        if isinstance(value, tuple):
            for element in value:
                self.tooltip = element
            return
        if isinstance(value, bool):
            self.tooltip.enabled = value
            return
        if value == "shared":
            self.tooltip.shared = True
            return
        if isinstance(value, str):
            match = re.search(r"(^.+)?{(.+:?.+?)}(.+)?", value)
            if match:
                if match.groups()[0] is not None:
                    self.tooltip.valuePrefix = match.groups()[0]
                if ":" in match.groups()[1]:
                    submatch = re.match("\.?(\d)[f%]?", match.groups()[1].split(":")[1])
                    if submatch:
                        self.tooltip.valueDecimals = int(submatch.groups()[0])
                if match.groups()[2] is not None:
                    self.tooltip.valueSuffix = match.groups()[2]
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
        if value not in [None, "normal", "percent", True, False]:
            raise ValueError(f"Unexpected stacking value ({value})")
        if value is True:
            self.plotOptions.series.stacking = "normal"
            return
        self.plotOptions.series.stacking = value
        return

    def set_stacked(self, value):
        """
        Alias for stacking
        """
        self.stacking = value
        return

    def set_datetime(self, value):
        """
        Set the xAxis as a datetime axis
        """
        if isinstance(value, bool) and value == True:
            self.xAxis.type = "datetime"
            return
        raise ValueError("Unexpected value for xAxis.type")

    def set_marker(self, value):
        """
        Set the default marker
        """
        if isinstance(value, bool):
            self.plotOptions.series.marker.enabled = value
            return
        if value is None:
            self.plotOptions.series.marker.enabled = False
            return
        self.plotOptions.series.marker = value

    def set_inverted(self, value):
        """
        Alias for chart.chart.inverted
        """
        self.chart.inverted = value
        return

    def set_datalabels(self, value):
        """
        Alias for chart.plotOptions.series.dataLabels
        """
        if isinstance(value, tuple):
            for element in value:
                self.datalabels = element
            return
        if isinstance(value, bool):
            self.plotOptions.series.dataLabels.enabled = value
            return
        if isinstance(value, str):
            self.plotOptions.series.dataLabels.enabled = True
            self.plotOptions.series.dataLabels.format = value
            return
        self.plotOptions.series.dataLabels = value
        return

    def set_labels(self, value):
        """
        Alias for chart.plotOptions.series.dataLabels
        """
        self.datalabels = value
        return

    def append(self, data=None, **kwargs):
        """
        Shortcut for :code:`chart.series.append(data, **kwargs)`
        """
        return self.series.append(data, **kwargs)

    def plot(self, data=None, **kwargs):
        """
        Shortcut for :code:`chart.series.append(data, **kwargs)`
        
        Returns
        --------
        self : Chart
            the chart instance
        """
        self.series.append(data, **kwargs)
        return self

    def vline(self, x, **kwargs):
        """
        Adds a vertical line across the chart

        Shortcut for: 
        :: 

            self.xAxis.plotLines.append(value=x, **kwargs)
        """
        if "color" not in kwargs:
            kwargs["color"] = "black"
        if self.xAxis.type == "datetime":
            if isinstance(x, str):
                x = pd.Timestamp(x)
        self.xAxis.plotLines.append(value=x, **kwargs)

    def hline(self, y, **kwargs):
        """
        Adds a horizontal line across the chart

        Shortcut for: 
        :: 

            self.yAxis.plotLines.append(value=x, **kwargs)
        """
        if "color" not in kwargs:
            kwargs["color"] = "black"
        self.yAxis.plotLines.append(value=y, **kwargs)

    def vband(self, xmin, xmax, **kwargs):
        """
        Adds a vertical band (mask) from xmin to xmax across the chart
        """
        if "color" not in kwargs:
            kwargs["color"] = "rgba(68, 170, 213, 0.2)"
        if self.xAxis.type == "datetime":
            if isinstance(xmin, str):
                xmin = pd.Timestamp(xmin)
            if isinstance(xmax, str):
                xmax = pd.Timestamp(xmax)
        self.xAxis.plotBands.append(**{**kwargs, "from": xmin, "to": xmax})
        return self

    def hband(self, ymin, ymax, **kwargs):
        """
        Adds a horizontal band (mask) from ymin to ymax across the chart
        """
        if "color" not in kwargs:
            kwargs["color"] = "rgba(68, 170, 213, 0.2)"
        self.yAxis.plotBands.append(**{**kwargs, "from": ymin, "to": ymax})
        return self

    def regress(self, y, x, intercept=True, **kwargs):
        """
        Plots a simple linear regression (y = ax + b) using the scikit-learn 
        regression module (soft dependency). 
        
        .. note: 
            If scikit-learn is not already installed in your 
            environment, simply run :code:`pip install scikit-learn`
        """

        def label(param, intercept, rsquared):
            """
            Generates the regression label
            """

            def f(number):
                """
                Format the string
                """
                if 100 < abs(number) <= 9999:
                    return f"{number:.0f}"
                if 10 < abs(number) <= 100:
                    return f"{number:.1f}"
                if 0.1 < abs(number) <= 10:
                    return f"{number:.2f}"
                return f"{number:.2e}"

            if intercept not in [None, False]:
                return f"y = {f(intercept)} + {f(param)}x (r-squared={rsquared:.2f})"
            return f"y = {f(param)}x (r-squared={rsquared:.2f})"

        try:
            from sklearn.linear_model import LinearRegression
        except ImportError:
            raise ImportError("scikit-learn is a soft-dependency of easychart")

        X = np.reshape(x, (-1, 1))

        reg = LinearRegression(fit_intercept=intercept).fit(X, y)

        if "name" not in kwargs:
            kwargs["name"] = label(
                reg.coef_[0], intercept and reg.intercept_, reg.score(X, y)
            )

        return self.plot(reg.predict(X), index=x, **kwargs)

    def annotate(
        self,
        text,
        *,
        x=0,
        y=0,
        xOffset=None,
        yOffset=None,
        point=None,
        align=None,
        verticalAlign=None,
        shape=None,
        padding=None,
        distance=None,
        backgroundColor=None,
        borderColor=None,
        borderRadius=None,
        borderWidth=None,
        useHTML=None,
        size=None,
        color=None,
        xAxis=0,
        yAxis=0,
        width=None,
        allowOverlap=True,
        draggable="xy",
        zIndex=None,
        visible=None,
    ):
        """
        Add an annotation to a chart

        Parameters
        ----------
        text : str
            The annotation label text
        x : float
            The x position of the point to which the annotation refers to 
        y : float
            The y position of the point to which the annotation refers to
        xAxis : int
            The x-Axis in which the x coordinate is defined
        yAxis : int
            The y-Axis in which the y coordinate is defined
        xOffset : float
            The horizontal offset of the annotation relative to the point (in pixels)
        yOffset : float
            The vertical offset of the annotation relative to the point (in pixels)
        width : int
            The width (in pixels) of the annotation
        point : str
            The id of the point to which the annotation refers to (if x and y not specified)
        align : str (one of "center", "left", "right")
            The horizontal alignment of the annotation relative to the point
        verticalAlign: str (one of "bottom", "middle", "top")
            The vertical alignment of the annotation relative to the point
        shape : str (one of "callout", "connector", "rect", "circle", "diamond", "triangle")
            The shape of the annotation
        padding : int
            The padding within the box (assuming border or background is set)
        distance : float
            The offset of the annotation relative to the point (in lieu of xOffset and yOffset)
        size : int
            The font size
        color : str
            The font color
        
        Note
        ----
        For more details on annotations, check out the `Highcharts API documentation <https://api.highcharts.com/highcharts/annotations.labelOptions>`_
        """
        if point is None:
            point = {"x": x, "y": y, "xAxis": xAxis, "yAxis": yAxis}
        elif isinstance(point, tuple):
            point = dict(zip(["x", "y", "xAxis", "yAxis"], [*point, 0, 0, 0, 0]))
        elif isinstance(point, dict):
            point = {"xAxis": xAxis, "yAxis": yAxis, **point}

        with self.annotations.append({}) as annotation:
            annotation.labels.append(
                internals.dictfilter(
                    {
                        "text": text,
                        "point": point,
                        "x": xOffset,
                        "y": -yOffset if yOffset is not None else yOffset,
                        "align": align,
                        "verticalAlign": verticalAlign,
                        "shape": shape,
                        "padding": padding,
                        "backgroundColor": backgroundColor,
                        "borderColor": borderColor,
                        "borderRadius": borderRadius,
                        "borderWidth": borderWidth,
                        "useHTML": useHTML,
                        "distance": distance,
                        "allowOverlap": allowOverlap,
                        "style": internals.dictfilter(
                            {"fontSize": size, "color": color, "width": width},
                            lambda k, v: v is not None,
                        ),
                    },
                    lambda k, v: v is not None,
                )
            )

            annotation.labelOptions = internals.dictfilter(
                {"visible": visible, "draggable": draggable, "zIndex": zIndex},
                lambda k, v: v is not None,
            )

    def draw(
        self,
        shape,
        *,
        x=None,
        y=None,
        xAxis=0,
        yAxis=0,
        r=None,
        width=None,
        height=None,
        xOffset=None,
        yOffset=None,
        point=None,
        points=None,
        draggable="xy",
        visible=None,
        zIndex=None,
        **kwargs,
    ):
        # easychart feature: drawing line segments
        if shape == "line":
            shape = "path"

            if "fill" not in kwargs:
                kwargs["fill"] = False

            if "color" in kwargs:
                kwargs["stroke"] = kwargs.pop("color")

            if "width":
                kwargs["strokeWidth"], width = width, None

            if "linestyle" in kwargs:
                kwargs["dashStyle"] = kwargs.pop("linestyle")

            if "style" in kwargs:
                kwargs["dashStyle"] = kwargs.pop("style")

        # easychart feature: drawing boxes (rectangles defined in the x/y space)
        if shape == "box":
            shape = "path"
            points = [
                (x, y),
                (x + width, y),
                (x + width, y + height),
                (x, y + height),
                (x, y),
            ]

        if shape == "square" or shape == "rectangle":
            shape = "rect"

        if "color" in kwargs:
            kwargs["fill"] = kwargs.pop("color")

        # inject default axes by default
        if points is not None:
            for i, p in enumerate(points):
                if isinstance(p, (tuple)):
                    points[i] = dict(
                        zip(["x", "y", "xAxis", "yAxis"], [*p, 0, 0, 0, 0])
                    )

                elif isinstance(p, dict):
                    points[i] = {"yAxis": yAxis, "xAxis": xAxis, **p}

        with self.annotations.append({}) as annotation:
            annotation.shapes.append(
                internals.dictfilter(
                    {
                        "type": shape,
                        "point": point
                        or (
                            None
                            if (x == y == None)
                            else {"x": x, "y": y, "xAxis": xAxis, "yAxis": yAxis}
                        ),
                        "x": xOffset,
                        "y": -yOffset if yOffset is not None else yOffset,
                        "points": points,
                        "r": r,
                        "height": height,
                        "width": width,
                        **kwargs,
                    },
                    lambda k, v: v is not None,
                )
            )
            annotation.shapeOptions = internals.dictfilter(
                {"draggable": draggable, "zIndex": zIndex, "visible": visible},
                lambda k, v: v is not None,
            )
        pass

    def show(self, width=None, height=None, theme=None):
        return Plot(self, width, height, theme)

    def save(self, filename, indent=4):
        """
        Serializes and dumps the chart configuration to file
        """
        with open(filename, "w") as file:
            simplejson.dump(
                self.serialize(), file, default=encoders.default, indent=indent
            )
        return

    def serialize(self):
        """
        Serializes the chart to a native python structure
        """
        return simplejson.loads(
            simplejson.dumps(
                super().serialize(), default=encoders.default, ignore_nan=True
            )
        )


class Plot:
    """
    Chart container
    """

    def __init__(self, chart, width=None, height=None, theme=None):
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
        self.chart = chart

        if height is None:
            if "chart" in chart and "height" in chart["chart"]:
                self.height = internals.Size(chart["chart"]["height"])
            else:
                self.height = internals.Size("400px")
        else:
            self.height = internals.Size(height)

        if width is None:
            if "chart" in chart and "width" in chart["chart"]:
                self.width = internals.Size(chart["chart"].pop("width"))
            else:
                self.width = internals.Size("100%")
        else:
            if "chart" in chart and "width" in chart["chart"]:
                chart["chart"].pop("width")

            self.width = internals.Size(width)

        self.theme = theme

    def __repr__(self):
        return f"<Plot height={self.height} width={self.width}>"

    def serialize(self):
        return {
            "chart": self.chart,
            "width": self.width,
            "height": self.height,
        }


class Grid:
    """
    Grid of chart plots
    """

    def __init__(self, plots=None, theme=None, width="100%", responsive=None):
        """
        Parameters
        ------------------------
        plots : list (optional)
            list of individual plots
        theme : dict (optional)
            dictionary of global options (theme)
        """
        self.plots = (
            [p if isinstance(p, Plot) else Plot(p) for p in plots]
            if plots is not None
            else []
        )
        self.theme = theme

        self.width = internals.Size(width).resolve(
            easychart.config.config.rendering.container.width
        )

        self.responsive = responsive

    def add(self, chart, width=None, height=None):
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
        # extract the height and width of each plot
        dimensions = [
            (
                internals.Size(plot.height).resolve(self.width),
                internals.Size(plot.width).resolve(self.width),
            )
            for plot in self.plots
        ]

        cumwidth, rows = 0, [[]]
        for (height, width) in dimensions:
            # if there are less than 0 pixels left, put on a new row
            if (self.width - (cumwidth + width)) < 0:
                rows.append([height])
                cumwidth = width
            else:
                rows[-1].append(height)
                cumwidth += width

        return f"{sum([max(row) if len(row) > 0 else 0 for row in rows])}px"

    def serialize(self):
        responsive = (
            easychart.config.config.rendering.responsive
            if self.responsive is None
            else self.responsive
        )

        plots = [plot.serialize() for plot in self.plots]

        for plot in plots:
            if not responsive:
                for dimension in ("width", "height"):
                    plot[dimension] = f"{plot[dimension].resolve(self.width)}px"

        return plots

