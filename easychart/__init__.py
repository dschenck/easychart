from easychart.config import config
from easychart.models import Chart, Plot, Grid

import easychart.ipynb
import easychart.datasets
import easychart.themes
import easychart.colormaps
import easychart.extensions as ext

__version__ = "0.1.20"


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
    ctype=None
):
    """
    Creates a new chart with some preset defaults

    Parameters
    ------------------
    type : str
        the default type of series

    datetime : bool
        sets the x-axis as a datetime axis

    zoom : str
        one of None, "x", "y" or "xy"

    tooltip : str
        one of None or "shared"

    title : str
        title text of the chart

    subtitle : str
        subtitle text of the chart

    xAxis : dict
        The xAxis options

    yAxis : dict
        the yAxis options

    cAxis : str, dict
        the colorAxis options

    xtitle : str
        x-axis title

    ytitle : str
        y-axis title

    xformat : str
        format of the x-axis labels

    yformat : str
        format of the y-axis labels

    ymin : float
        minimum of the y-axis

    ymax : float
        maximum of the y-axis

    stacked : bool
        True to stack the series, False otherwise

    width : int
        The chart width, in pixels

    height : int or str
        The chart height, in pixels, or in percentage of the chart width

    exporting : bool
        True to enable exporting menu on chart, False to disable

    xtype : str
        The axis type for the x-axis

    ytype : str
        The axis type for the y-axis

    ctype : str
        The axis type for the color axis

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

    if xformat is not None:
        chart.xAxis.labels.format = xformat

    if ytitle is not None:
        chart.yAxis.title.text = ytitle

    if yformat is not None:
        chart.yAxis.labels.format = yformat

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

    chartkwargs = {
        k: v
        for k, v in kwargs.items()
        if k
        in [
            "type",
            "datetime",
            "zoom",
            "tooltip",
            "title",
            "subtitle",
            "xtitle",
            "ytitle",
            "xformat",
            "yformat",
            "ymin",
            "ymax",
            "xmin",
            "xmax",
            "cmin",
            "cmax",
            "legend",
            "categories",
            "stacked",
            "width",
            "height",
            "exporting",
            "xtype",
            "ytype",
            "ctype",
            "xAxis",
            "yAxis",
            "cAxis",
        ]
    }
    serieskwargs = {k: v for k, v in kwargs.items() if k not in chartkwargs}

    chart = new(**chartkwargs)
    chart.plot(data, **serieskwargs)
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
