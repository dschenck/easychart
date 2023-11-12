import easychart
import easychart.internals as internals


class Grid:
    """
    Grid of chart plots
    """

    def __init__(self, plots=None, *, width=None, theme=None):
        """
        Parameters
        ------------------------
        plots : list
            list of individual plots

        width : str
            total width of grid, as pixels (e.g. "1280px")

        theme : str, dict
            theme name or dict of theme options
        """
        self.plots = [easychart.Plot(p) for p in (plots or [])]
        self.theme = theme
        self.width = internals.Size(width) if width is not None else width

    def add(self, chart, *, width=None) -> None:
        """
        Adds a chart (or plot) to the grid

        Parameters
        ------------
        width : str
            width of the plot, expressed as a percentage of the grid width
        """
        if not isinstance(chart, easychart.Plot):
            chart = easychart.Plot(chart, width=width)
        self.plots.append(chart)

    def serialize(self) -> dict:
        """
        Returns
        -------
        dict
        """
        return {
            "plots": [plot.serialize() for plot in self.plots],
            "theme": self.theme,
            "width": self.width,
        }
