import pandas as pd
import inspect
import re

from easychart.config import config
from easychart.models import Chart, Plot, Grid

import easychart.ipynb
import easychart.datasets
import easychart.themes
import easychart.colormaps
import easychart.extensions as ext
import easychart.rendering

__version__ = "0.1.30"


def new(
    type=None,
    *,
    datetime=False,
    zoom="x",
    tooltip=None,
    title=None,
    subtitle=None,
    xAxis=None,
    yAxis=None,
    cAxis=None,
    xtitle=None,
    ytitle=None,
    xformat=None,
    yformat=None,
    ymin=None,
    ymax=None,
    xmin=None,
    xmax=None,
    cmin=None,
    cmax=None,
    legend=None,
    categories=None,
    stacked=None,
    width=None,
    height=None,
    exporting=None,
    xtype=None,
    ytype=None,
    ctype=None,
    xreversed=None,
    yreversed=None,
    creversed=None,
    ycategories=None,
    xcategories=None,
    xopposite=None,
    yopposite=None,
    labels=None,
    twinx=None,
    twiny=None,
    colormap=None,
    constr=None,
):
    """
    Creates a new chart with some preset defaults

    Parameters
    ------------------
    type : str
        The default series type (e.g. "line", "scatter", "column", "arearange", etc...)

    datetime : bool
        Sets the type of the xAxis to 'datetime'

    zoom : str
        Sets the interactive zoom options;
        Value must be one of None (no zoom), "x" (horizontal), "y" (vertical) or "xy" (both)

    tooltip : str
        Sets the tooltip options;
        A dict of options, "shared", True or None

    title : str
        The chart title options
        Value can be a dict of options or a string (the title text)

    subtitle : str
        The chart subtitle options
        Value can be a dict of options or a string (the subtitle text)

    xAxis : dict
        The xAxis options

    yAxis : dict
        The yAxis options

    cAxis : str, dict
        The colorAxis options
        Can be a dict of options or a colormap name

    xtitle : str
        The xAxis title

    ytitle : str
        The yAxis title

    xformat : str
        The format of the xAxis labels

    yformat : str
        The format of the yAxis labels

    ymin : float
        The minimum of the yAxis

    ymax : float
        The maximum of the yAxis

    stacked : bool
        True to stack the series, False otherwise

    width : int
        The chart width, in pixels or in percentages
        If given a percentage value (e.g. "50%"), then value is computed as a fraction of '600px'.
        See chart dimensions for more details.

    height : int or str
        The chart height, in pixels, or in percentages.
        If given a percentage value (e.g. "60%"), then value is computed as a fraction of
        the chart width.

    exporting : bool
        True to enable exporting menu on chart,
        False to disable

    xtype : str
        The axis type for the xAxis (e.g. "log", "datetime")

    ytype : str
        The axis type for the yAxis (e.g. "log", "datetime")

    ctype : str
        The axis type for the color axis (e.g. "log")

    xreversed : bool
        Whether to reverse the xAxis (from high to low)

    yreversed : bool
        Whether to reverse the yAxis (from high to low)

    creversed : bool
        Whether to reversed the colorAxis (from high to low)

    ycategories : list
        the yAxis category labels

    xcategories : list
        the xAxis category labels

    xopposite : bool
        Whether to draw the xAxis on the opposite side (generally right of chart)

    yopposite : bool
        Whether to draw the yAxis on the opposite side (generally top of chart)

    labels : bool, list, dict
        Series labels

    twinx : bool
        True to twin the xAxis on the opposite side

    twiny : bool
        True to twin the yAxis on the opposite side

    colormap: str
        A colormap name to create the colorAxis

    Returns
    -------
    easychart.Chart
    """

    chart = Chart()

    if type is not None:
        chart.chart.type = type

    if datetime:
        chart.xAxis.type = "datetime"

    if zoom is not None:
        chart.chart.zoomType = zoom

    if tooltip is not None:
        chart.tooltip = tooltip

    if title is not None:
        chart.title = title

    if subtitle is not None:
        chart.subtitle = subtitle

    if xAxis is not None:
        chart.xAxis = xAxis

    if yAxis is not None:
        chart.yAxis = yAxis

    if cAxis is not None:
        chart.cAxis = cAxis

    if xtitle is not None:
        chart.xAxis.title.text = xtitle

    if ytitle is not None:
        chart.yAxis.title.text = ytitle

    if yformat is not None:
        if yformat in ["percent", "percentage", "pct", "%"]:
            chart.yAxis.labels.format = "{(multiply value 100)}%"
        elif re.match(r":\.\d%", yformat):
            chart.yAxis.labels.format = f"{{(multiply value 100){yformat[:-1]}f}}%"
        else:
            chart.yAxis.labels.format = yformat

    if xformat is not None:
        if xformat in ["percent", "percentage", "pct", "%"]:
            chart.xAxis.labels.format = "{(multiply value 100)}%"
        elif re.match(r":\.\d%", xformat):
            chart.xAxis.labels.format = f"{{(multiply value 100){xformat[:-1]}f}}%"
        else:
            chart.xAxis.labels.format = xformat

    if ymin is not None:
        chart.yAxis.min = ymin

    if ymax is not None:
        chart.yAxis.max = ymax

    if xmin is not None:
        chart.xAxis.min = xmin

    if xmax is not None:
        chart.xAxis.max = xmax

    if cmin is not None:
        chart.colorAxis.min = cmin

    if cmax is not None:
        chart.colorAxis.max = cmax

    if legend is not None:
        chart.legend = legend

    if categories is not None:
        chart.categories = categories

    if xcategories is not None:
        chart.xAxis.categories = xcategories

    if ycategories is not None:
        chart.yAxis.categories = ycategories

    if stacked is not None:
        chart.stacked = stacked

    if width is not None:
        chart.width = width

    if height is not None:
        chart.height = height

    if exporting is not None:
        chart.exporting = exporting

    if xtype is not None:
        chart.xAxis.type = xtype

    if ytype is not None:
        chart.yAxis.type = ytype

    if ctype is not None:
        chart.colorAxis.type = type

    if xreversed is not None:
        chart.xAxis.reversed = xreversed

    if yreversed is not None:
        chart.yAxis.reversed = yreversed

    if creversed is not None:
        chart.colorAxis.reversed = creversed

    if xopposite is not None:
        chart.xAxis.opposite = xopposite

    if yopposite is not None:
        chart.yAxis.opposite = yopposite

    if labels is not None:
        chart.labels = labels

    if twinx is True:
        chart.twinx()

    if twiny is True:
        chart.twiny()

    if colormap is not None:
        chart.cAxis = colormap

    if constr is not None:
        chart.constr = constr

    return chart


@easychart.internals.alias("colormap", "cmap")
@easychart.internals.alias("colsize", "colwidth")
@easychart.internals.alias("rowsize", "rowheight")
@easychart.internals.alias("cmin", "min")
@easychart.internals.alias("cmax", "max")
@easychart.internals.alias("interpolation", "interpolate", "fuzzy")
def heatmap(
    data,
    *,
    colormap="viridis",
    colsize=1,
    rowsize=1,
    yreversed=True,
    xopposite=True,
    interpolation=False,
    **kwargs,
):
    """
    Convenience function to plot heat maps

    Parameters
    ----------
    data : pd.DataFrame, np.array
        the data to plot

    colormap : str
        the name of the colormap

    colsize : int
        the width of each column
        defaults to 1 (or 1 second, if the xAxis.type is set to datetime)

    rowsize : int
        the height of each row
        defaults to 1 (or 1 second if the yAxis.type is set to datetime)

    yreversed : bool
        whether to plot the yAxis in reverse order
        defaults to True

    xopposite : bool
        whether to draw the xAxis above rather then below the plot area
        defaults to True

    interpolation : bool
        whether to render the heatmap by interpolating each point
        defaults to False

    **kwargs
        any additional argument to pass to :code:`easychart.new`

    Returns
    -------
    easychart.Chart
    """
    if isinstance(data, pd.DataFrame):
        if not (
            isinstance(data.index, pd.DatetimeIndex)
            or pd.api.types.is_numeric_dtype(data.index)
        ):
            kwargs["ycategories"] = kwargs.get("ycategories", data.index)
            data = data.reset_index(drop=True)
        elif kwargs.get("ycategories"):
            data = data.reset_index(drop=True)

        if not (
            isinstance(data.columns, pd.DatetimeIndex)
            or pd.api.types.is_numeric_dtype(data.columns)
        ):
            kwargs["xcategories"] = kwargs.get("xcategories", data.columns)
            data = data.T.reset_index(drop=True).T
        elif kwargs.get("xcategories"):
            data = data.T.reset_index(drop=True).T

    else:
        data = pd.DataFrame(data)

    chart = easychart.new(
        "heatmap",
        yreversed=yreversed,
        xopposite=xopposite,
        colormap=colormap,
        **{
            "ymin": min(data.index),
            "ymax": max(data.index),
            "xmin": min(data.columns),
            "xmax": max(data.columns),
            **{
                k: kwargs.pop(k)
                for k in list(kwargs)
                if k in inspect.signature(new).parameters
            },
        },
    )

    chart.plot(
        data.rename_axis(index="index", columns="columns").T.stack(),
        colsize=colsize,
        rowsize=rowsize,
        interpolation=interpolation,
        **kwargs,
    )

    return chart


def plot(data, **kwargs):
    """
    Convenience method to create a chart and append a series

    Parameters
    ----------
    data : list, pd.Series, pd.DataFrame
        See Chart.plot

    kwargs
        additional keyword arguments passed to :code:`easychart.new` (if a
        key-word argument exists) or to :code:`Chart.plot` otherwise

    Returns
    -------
    easychart.Chart
    """
    if isinstance(data, Chart):
        return render(data, width=kwargs.get("width"), theme=kwargs.get("theme"))

    chart = new(
        **{
            k: kwargs.pop(k)
            for k in list(kwargs)
            if k in inspect.signature(new).parameters
        }
    )

    chart.plot(data, **kwargs)

    return chart


def render(*charts, width=None, theme=None):
    """
    Render one or several charts or a grid thereof to the jupyter notebook

    Parameters
    ---------
    charts : list of Chart
        list of charts

    width : int, str
        each plots's width

    theme : str, dict
        the theme name

    Returns
    -------
    easychart.Grid
    """
    if len(charts) == 1 and isinstance(charts[0], Grid):
        return charts[0]

    return Grid([Plot(chart, width=width) for chart in charts], theme=theme)
