from easychart.models import Chart, Plot, Grid
import easychart.ipynb
import easychart.datasets as datasets

def new(*, type=None, datetime=False, zoom="x", tooltip=None, title=None, subtitle=None, 
        xtitle=None, ytitle=None, xformat=None, yformat=None, ymin=None, ymax=None):
    """
    Creates a new chart with some preset defaults

    Parameters
    ------------------
    type : str
        the default type of series
    datetime : boolean
        sets the x-axis as a datetime axis
    zoom : str
        one of None, "x", "y" or "xy"
    tooltip : str
        one of None or "shared"
    title : str
        title of the chart
    subtitle : str
        subtitle of the chart
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
    """

    chart = Chart()

    if type is not None: 
        chart.chart.type = type

    if datetime: 
        chart.xAxis.type = "datetime"

    if zoom is not None: 
        chart.chart.zoomType = zoom

    if tooltip is not None: 
        if tooltip == "shared":
            chart.tooltip.shared = True

    if title is not None: 
        chart.title.text = title

    if subtitle is not None: 
        chart.subtitle.text = subtitle

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

    return chart

def plot(data, **kwargs):
    """
    Convenience method to create a chart and append a series
    """
    chartkwargs = {k:v for k,v in kwargs.items() if k in 
        ["datetime", "zoom", "title", "subtitle","tooltip","xtitle","ytitle"]}
    serieskwargs = {k:v for k, v in kwargs.items() if k not in chartkwargs}
    chart = new(**chartkwargs)
    chart.series.append(data, **serieskwargs)
    return chart

def render(*charts, width="100%", height="400px", theme=None):
    """
    Render one or several charts or a grid thereof to the jupyter notebook
    """
    if len(charts) == 1 and isinstance(charts[0], Grid):
        return charts[0]
    plots = [Plot(plot, width=width, height=height) if not isinstance(plot, Plot) else plot for plot in charts]
    return Grid(plots, theme=theme)