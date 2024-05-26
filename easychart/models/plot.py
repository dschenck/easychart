import easychart.encoders
import easychart.internals as internals


class Plot:
    """
    Individual chart container
    """

    def __init__(self, chart, *, width=None, constr=None):
        """
        Parameters
        ------------
        chart : Chart
            chart
        width : str
            width of the plot, expressed as a number of pixels or a percentage
            of the container width
        constr : str
            one of 'chart', 'stock', 'map' or 'gantt'
            defaults to 'chart'
        """
        if isinstance(chart, Plot):
            chart, width, constr = (
                chart.chart,
                width or chart.width,
                chart.constr or constr,
            )

        self.chart = chart

        self.width = internals.Size(
            width
            or self.chart.get(
                ["chart", "width"],
                "100%" if easychart.config.rendering.responsive else "600px",
            )
        )

        self.constr = chart.get("constr", constr) or "chart"

    def serialize(self) -> dict:
        """
        Returns
        -------
        dict
        """
        return {
            "chart": self.chart.serialize(),
            "width": self.width,
            "constr": self.constr,
        }
