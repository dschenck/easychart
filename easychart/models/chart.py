import easytree
import pandas as pd
import numpy as np
import simplejson
import re
import requests
import warnings

import easychart
import easychart.encoders
import easychart.internals as internals

from .series import Series


class Chart(easytree.dict):
    """
    A Highchart chart configuration
    """

    def __init__(self):
        self.series = Series([])

    def __setattr__(self, name, value):
        if hasattr(self.__class__, name) and getattr(self.__class__, name).fset:
            return getattr(Chart, name).fset(self, value)
        return super().__setattr__(name, value)

    @property
    def categories(self):
        """
        Get or set the xAxis categories.

        Categories are names used instead of number for categorical charts. Each category
        name is mapped to a number, with the first element assigned the value of 0.

        .. note::

            Alias for :code:`chart.xAxis.categories`. See `Highcharts API <https://api.highcharts.com/highcharts/xAxis.categories>`_
            for additional details on the xAxis categories

        :Example:
        ::

            >>> import easychart

            >>> chart = easychart.new("column")
            >>> chart.categories = ["France","UK"]
            >>> chart.plot([10, 20])

        :getter: Return the xAxis categories (if any)

            :returns: list

        :setter: Set the xAxis categories

            :accepts: iterable
        """
        return self.xAxis.categories

    @categories.setter
    def categories(self, value):
        """
        See :code:`Chart.categories`
        """
        self.xAxis.categories = value

    @property
    def cAxis(self):
        """
        Get or set color axis configuration

        .. note::

            Alias for :code:`chart.colorAxis`. See `Highcharts API <https://api.highcharts.com/highcharts/colorAxis>`_
            for additional details on the color axis

        :getter: Return the colorAxis options (if any)

            :returns: dict

        :setter: Set the colorAxis options

            :accepts: True, dict

            .. note::

                - If given True, assigns an empty dictionary to :code:`chart.colorAxis`
                - If given a str, loads and assigns the colormap to :code:`chart.colorAxis.stops`
                - If given a dict, assigns the value as is to :code:`chart.colorAxis`
        """
        return self.colorAxis

    @cAxis.setter
    def cAxis(self, value):
        """
        See above
        """
        if isinstance(value, bool) and value is True:
            self.colorAxis = {}
        elif isinstance(value, str):
            colormap = easychart.colormaps.get(value)

            self.colorAxis.stops = [
                (i / (len(colormap["colors"]) - 1), color)
                for i, color in enumerate(colormap["colors"])
            ]
        else:
            self.colorAxis = value

    @property
    def datalabels(self):
        """
        Get or set data labels options

        .. note::

            Alias for :code:`chart.plotOptions.series.dataLabels`. See  `Highcharts API
            <https://api.highcharts.com/highcharts/plotOptions.series.dataLabels>`_
            for additional details on data labels

        :getter: Return the datalabel options (if any)

            :returns: dict

        :setter: Set the datalabel options

            :accepts: bool, str, tuple, dict

            .. note::

                - If given a bool, value is assigned to :code:`chart.plotOptions.series.dataLabels.enabled`
                - If given a str, value is assigned to :code:`chart.plotOptions.series.dataLabels.format`
                - If given a dict, value is assigned as is
                - If given a tuple, values are iteratively assigned as described above

        """
        return self.plotOptions.series.dataLabels

    @datalabels.setter
    def datalabels(self, value):
        """
        See above
        """
        if isinstance(value, tuple):
            for element in value:
                self.datalabels = element
            return

        if isinstance(value, bool):
            self.plotOptions.series.dataLabels.enabled = value

        elif isinstance(value, str):
            self.plotOptions.series.dataLabels.enabled = True
            self.plotOptions.series.dataLabels.format = value

        else:
            self.plotOptions.series.dataLabels = value

    @property
    def datetime(self):
        """
        Get or set whether the xAxis is a datetime axis

        :getter: Returns whether the xAxis is a datetime axis

            :returns: bool

        :setter: Sets whether the xAxis is a datetime axis

            :accepts: bool
        """
        return self.xAxis.type == "datetime"

    @datetime.setter
    def datetime(self, value):
        """
        See :code:`Chart.datetime`
        """
        if isinstance(value, bool):
            if value is True:
                self.xAxis.type = "datetime"
            else:
                self.xAxis.type = None
        raise ValueError("Expected datetime to be True or False, received {value}")

    @property
    def decimals(self):
        """
        Returns the number of tooltip decimals

        :getter: Return the number of tooltip decimals

            :returns: int

        :setter: Set the number of tooltip decimals

            :accepts: int
        """
        return self.tooltip.get("valueDecimals")

    @decimals.setter
    def decimals(self, value):
        """
        See :code:`Chart.decimals`
        """
        if isinstance(value, int):
            self.tooltip.valueDecimals = value
        else:
            raise ValueError("Expected decimals to be an integer, received '{value}")

    @property
    def exporting(self):
        """
        Get or set the exporting options

        :getter: Return the exporting options

            :returns: int

        :setter: Set the exporting options

            :accepts: bool, dict

            .. note::

                - If given a bool, value is assigned to :code:`chart.exporting.enabled`
                - If given a dict, value is assigned as is
        """
        return super().__getattr__("exporting")

    @exporting.setter
    def exporting(self, value):
        """
        See :code:`exporting`
        """
        if isinstance(value, bool):
            self.exporting.enabled = value
        else:
            self.exporting = value

    @property
    def height(self):
        """
        Get or set the chart height

        .. note::

            alias for :code:`chart.chart.height`

        :getter: Return the chart height

            :returns: int, str

        :setter: Set the chart height

            :accepts: int, str

            .. note::

                The chart height can be provided as a number of pixels,
                a string representing a number of pixels (e.g. :code:`"400px"`)
                or a percentage (e.g. :code:`50%`) of the chart width
        """
        return self.chart.get("height")

    @height.setter
    def height(self, value):
        """
        See :code:`chart.height`
        """
        self.chart.height = value

    @property
    def inverted(self):
        """
        Get or set whether the chart is inverted

        .. note::

            alias for :code:`chart.chart.inverted`

        :getter: Return whether the chart is inverted

            :returns: bool

        :setter: Set whether the chart is inverted

            :accepts: bool
        """
        return self.chart.inverted

    @inverted.setter
    def inverted(self, value):
        """
        See :code:`Chart.inverted`
        """
        self.chart.inverted = value

    @property
    def labels(self):
        """
        Alias for :code:`Chart.datalabels`
        """
        return self.datalabels

    @labels.setter
    def labels(self, value):
        """
        Alias for :code:`Chart.datalabels`
        """
        self.datalabels = value

    @property
    def legend(self):
        """
        Get or set the legend

        :getter: Return the legend configuration

            :returns: dict

        :setter: Set the legend configuration

            :accepts: bool, dict

            .. note::

                - If given a bool, value is assigned to :code:`chart.legend.enabled`
                - If given a dict, value is assigned to :code:`chart.legend`
        """
        return super().__getattr__("legend")

    @legend.setter
    def legend(self, value):
        """
        See :code:`Chart.legend`
        """
        if isinstance(value, bool):
            self.legend.enabled = value
        else:
            super().__setattr__("legend", value)

    @property
    def marker(self):
        """
        Return marker options

        :getter: Returns marker options

            :returns: dict

        :setter: Sets marker options

            :accepts: bool, dict

            .. note::

                - If given a bool, value is assigned to :code:`chart.plotOptions.series.marker.enabled`
                - If given None, assigns False to :code:`chart.plotOptions.series.marker.enabled`
                - If given a dict, value is assigned to :code:`chart.plotOptions.series.marker`
        """
        return self.plotOptions.series.marker

    @marker.setter
    def marker(self, value):
        """
        See :code:`Chart.marker`
        """
        if isinstance(value, bool):
            self.plotOptions.series.marker.enabled = value
        elif value is None:
            self.plotOptions.series.marker.enabled = False
        else:
            self.plotOptions.series.marker = value

    @property
    def stacked(self):
        """
        Alias for :code:`Chart.plotOptions.series.stacking`
        """
        return self.stacking

    @stacked.setter
    def stacked(self, value):
        """
        See :code:`Chart.plotOptions.series.stacking`
        """
        self.stacking = value

    @property
    def stacking(self):
        """
        Get or set the stacking option
        """
        return self.plotOptions.series.get("stacking")

    @stacking.setter
    def stacking(self, value):
        """
        See :code:`Chart.stacking`
        """
        if isinstance(value, bool):
            if value is True:
                self.plotOptions.series.stacking = "normal"
            else:
                self.plotOptions.series.stacking = None
        elif value in [None, "normal", "percent"]:
            self.plotOptions.series.stacking = value
        else:
            raise ValueError(
                f"Expected stacking to be one of 'percent', 'normal', True, False or None, received '{value}"
            )

    @property
    def subtitle(self):
        """
        Get or set the chart subtitle

        .. note::

            See `Highcharts API <https://api.highcharts.com/highcharts/subtitle>`_ for
            full list of available options

        :getter: Return the chart subtitle configuration (if any)

            :returns: dict

        :setter: Set the chart subtitle

            :accepts: str, dict

            .. note::

                - If given a str, assigns the value to :code:`chart.subtitle.text`
                - If given a dict, assigns the value to :code:`chart.subtitle`

            :example:
            ::

                >>> chart = easychart.new()
                >>> chart.subtitle = "Source: USDA"
                >>> chart.serialize()
                {"subtitle":{"text":"Source: USDA"}}
        """
        return super().__getattr__("subtitle")

    @subtitle.setter
    def subtitle(self, value):
        """
        See :code:`Chart.subtitle`
        """
        if isinstance(value, str):
            self.subtitle.text = value
        else:
            super().__setattr__("subtitle", value)

    @property
    def title(self):
        """
        Get or set the chart title

        .. note::

            See `Highcharts API <https://api.highcharts.com/highcharts/title>`_ for
            full list of available options

        :getter: Return the chart title configuration (if defined)

            :returns: dict

        :setter: Set the chart title

            :accepts: str, dict

            .. note::

                - If given a str, assigns the value to :code:`chart.title.text`
                - If given a dict, assigns the value to :code:`chart.title`

            :example:
            ::

                >>> chart = easychart.new()
                >>> chart.title = "US Corn Acreage"
                >>> chart.serialize()
                {"title":{"text":"US Corn Acreage"}}
        """
        return super().__getattr__("title")

    @title.setter
    def title(self, value):
        """
        See :code:`Chart.title`
        """
        if isinstance(value, str):
            self.title.text = value
        else:
            super().__setattr__("title", value)

    @property
    def tooltip(self):
        """
        Get or set tooltip configurations

        :getter: Return the tooltip configuration

            :returns: dict

        :setter: Set the tooltip configuration

            :accepts: str, bool, tuple, dict

            .. note::

                - If given a bool, assigns the value to :code:`chart.tooltip.enabled`
                - If given :code:`"shared"`, sets :code:`tooltip.shared = True`
                - If given a str of the form :code:`<prefix>{value:.4f}<suffix>`, parses it and sets each of the :code:`tooltip.valuePrefix`, :code:`tooltip.valueDecimals` and :code:`tooltipvalueSuffix`
        """
        return super().__getattr__("tooltip")

    @tooltip.setter
    def tooltip(self, value):
        """
        See :code:`Chart.tooltip`
        """
        if isinstance(value, tuple):
            for element in value:
                self.tooltip = element
            return

        if isinstance(value, bool):
            self.tooltip.enabled = value

        elif value == "shared":
            self.tooltip.shared = True

        elif isinstance(value, str):
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
        else:
            super().__setattr__("tooltip", value)

    @property
    def type(self):
        """
        Get or set the default series type

        .. note::

            alias for :code:`chart.chart.type`

        :getter: Return the default series type

            :returns: str

        :setter: Set the default series type

            :accepts: str
        """
        return self.chart.get("type")

    @type.setter
    def type(self, value: str):
        """
        See :code:`chart.type`
        """
        self.chart.type = value

    @property
    def width(self):
        """
        Get or set the chart width

        .. note::

            alias for :code:`chart.chart.width`

        :getter: Return the chart width

            :returns: int, str

        :setter: Set the chart width

            :accepts: int, str

            .. note::

                The chart width can be provided as a number of pixels,
                a string representing a number of pixels (e.g. :code:`"400px"`)
                or a percentage (e.g. :code:`50%`) of the default chart width
                which is defined as :code:`600px`
        """
        return self.chart.width

    @width.setter
    def width(self, value):
        """
        See :code:`chart.width`
        """
        if isinstance(internals.Size(value), internals.Size.Percentage):
            warnings.warn(
                "Setting chart.chart.width in percentages (e.g. 50%) is deprecated and may be disallowed in future versions. Use pixels (e.g. 400px) instead",
                DeprecationWarning,
                stacklevel=2,
            )

        self.chart.width = int(internals.Size(value).resolve("600px"))

    @property
    def zoom(self):
        """
        Get or set the zoom type for the chart

        .. note::

            Alias for :code:`chart.zoomType`; see `Highcharts API <https://api.highcharts.com/highcharts/chart.zooming.type>`_
            for additional details on available options

        :getter: Return the zoom type (if defined)

            :returns: str

        :setter: Set the zoom options

            :accepts: str, bool

            .. note::

                - If given a str, the value is set under :code:`chart.zoomType`
                - If given True, the value 'xy' is set under :code:`chart.zoomType`
                - If given False, the zoomType is set to :code:`None`

        """
        return self.chart.get("zoomType")

    @zoom.setter
    def zoom(self, value):
        """
        See :code:`Chart.zoom`
        """
        if isinstance(value, str) and value.lower() in ["x", "y", "xy"]:
            self.chart.zoomType = value.lower()

        elif isinstance(value, bool):
            if value is True:
                self.chart.zoomType = "xy"
            else:
                self.chart.zoomType = None

        else:
            raise ValueError(
                f"Expected value for zoom to be one of 'x', 'y' or 'xy', received '{value}'"
            )

    def append(self, data=None, **kwargs):
        """
        Shortcut for :code:`chart.series.append(data, **kwargs)`
        """
        return self.series.append(data, **kwargs)

    def plot(self, data=None, **kwargs):
        """
        Plot data

        Returns
        --------
        self : Chart
            the chart instance
        """
        self.series.append(data, **kwargs)
        return self

    @internals.alias("dashStyle", "linestyle", "ls")
    @internals.alias("color", "c")
    @internals.alias("width", "linewidth", "lw", "w")
    @internals.alias("zIndex", "zindex", "zorder", "z")
    def vline(self, x, *, color="black", **kwargs):
        """
        Adds a vertical line across the chart

        Shortcut for:
        ::

            self.xAxis.plotLines.append(value=x, **kwargs)
        """
        if self.xAxis.type == "datetime":
            if isinstance(x, str):
                x = pd.Timestamp(x)
        if "label" in kwargs and isinstance(kwargs["label"], str):
            kwargs["label"] = {"text": kwargs["label"]}
        self.xAxis.plotLines.append(value=x, color=color, **kwargs)

    @internals.alias("dashStyle", "linestyle", "ls")
    @internals.alias("color", "c")
    @internals.alias("width", "linewidth", "lw", "w")
    @internals.alias("zIndex", "zindex", "zorder", "z")
    def hline(self, y, *, color="black", **kwargs):
        """
        Adds a horizontal line across the chart

        Shortcut for:
        ::

            self.yAxis.plotLines.append(value=x, **kwargs)
        """
        if "label" in kwargs and isinstance(kwargs["label"], str):
            kwargs["label"] = {"text": kwargs["label"]}
        self.yAxis.plotLines.append(value=y, color=color, **kwargs)

    def vband(self, xmin, xmax, *, color="rgba(68, 170, 213, 0.2)", **kwargs):
        """
        Adds a vertical band (mask) from xmin to xmax across the chart
        """
        if self.xAxis.type == "datetime":
            if isinstance(xmin, str):
                xmin = pd.Timestamp(xmin)
            if isinstance(xmax, str):
                xmax = pd.Timestamp(xmax)

        self.xAxis.plotBands.append(
            **{**kwargs, "from": xmin, "to": xmax, "color": color}
        )
        return self

    def hband(self, ymin, ymax, *, color="rgba(68, 170, 213, 0.2)", **kwargs):
        """
        Adds a horizontal band (mask) from ymin to ymax across the chart
        """
        self.yAxis.plotBands.append(
            **{**kwargs, "from": ymin, "to": ymax, "color": color}
        )
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

    def show(self, *, width=None, theme=None):
        """
        Render chart to an easychart.Grid

        Parameters
        ----------
        width : int, str
            plot width
        theme : str, dict
            theme

        Returns
        -------
        Grid

        Note
        ----
        The width given in parameter sets the plot width, not the chart width. See notes on chart and plot sizing
        for more details
        """
        return easychart.Grid([easychart.Plot(self, width=width)], theme=theme)

    def save(self, filename, indent=4):
        """
        Serializes and dumps the chart configuration to file
        """
        with open(filename, "w") as file:
            simplejson.dump(
                self, file, default=easychart.encoders.default, indent=indent
            )
        return

    def export(self, to, theme=None, scale=2, **kwargs):
        """
        Export chart to a static format using an export server
        """
        if to[-3:] not in ["png", "jpg", "svg", "pdf"]:
            raise ValueError(
                f"Expected 'to' argument to end in one of 'png', 'jpg', 'svg', or 'pdf', received '{to}'"
            )

        res = requests.post(
            easychart.config.get(
                ["exporting", "server", "url"], "http://export.highcharts.com/"
            ),
            json={
                "options": self.serialize(),
                "type": f"image/{to[-3:]}",
                "scale": scale,
                "globalOptions": easychart.themes.get(theme),
            },
        )

        if res.status_code != 200:
            raise Exception(f"Export server responded with code {res.status_code}")

        if to in ["png", "jpg", "svg", "pdf"]:
            return res.content

        with open(to, "wb") as file:
            file.write(res.content)

    def serialize(self) -> dict:
        """
        Serializes the chart to a native python structure

        Returns
        -------
        dict
        """
        return simplejson.loads(
            simplejson.dumps(self, default=easychart.encoders.default, ignore_nan=True)
        )
