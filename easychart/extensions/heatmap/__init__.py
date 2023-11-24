import pandas as pd
import easychart
import easychart.internals


@easychart.internals.alias("colormap", "cmap")
def heatmap(
    data, *, index=None, categories=None, colormap="viridis", reversed=True, **kwargs
):
    """
    Convenience function to plot heat maps

    Returns
    -------
    easychart.Chart
    """
    if index is None:
        if isinstance(data, pd.DataFrame):
            index = data.index
        else:
            index = range(len(data))

    if categories is None:
        if isinstance(data, pd.DataFrame):
            categories = data.columns
        else:
            categories = range(len(data[0]))

    if isinstance(data, pd.DataFrame):
        data = data.values

    # stack data
    data = pd.DataFrame(
        data, index=range(len(index)), columns=range(len(categories))
    ).pipe(lambda df: df.T.stack().reset_index().values)

    chart = easychart.new("heatmap", **kwargs)
    chart.xAxis.categories = categories
    chart.yAxis.categories = index
    chart.yAxis.reversed = reversed
    chart.cAxis = colormap
    chart.plot(data)

    return chart
