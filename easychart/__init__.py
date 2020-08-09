from easychart.models import Chart, Plot, Grid
import easychart.ipynb

def new(*, datetime=False, zoom="x", tooltip=None, charttype=None, title=None, subtitle=None, 
        xtitle=None, ytitle=None, xformat=None, yformat=None, ymin=None, ymax=None):
    """
    Convenience method to create a chart
    """

    chart = Chart()

    if datetime: 
        chart.xAxis.type = "datetime"

    if zoom is not None: 
        chart.chart.zoomType = zoom

    if tooltip is not None: 
        if tooltip == "shared":
            chart.tooltip.shared = True

    if charttype is not None: 
        chart.chart.type = charttype

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
    
def render(*charts, width="100%", height="400px", theme=None):
    """
    Render one or several charts or a grid thereof to the jupyter notebook
    """
    if len(charts) == 1 and isinstance(charts[0], Grid):
        return charts[0]
    plots = [Plot(plot, width=width, height=height) if not isinstance(plot, Plot) else plot for plot in charts]
    return Grid(plots, theme=theme)