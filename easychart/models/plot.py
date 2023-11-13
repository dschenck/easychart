import easychart.encoders
import easychart.internals as internals


class Plot:
    """
    Individual chart container
    """

    def __init__(self, chart, *, width=None):
        """
        Parameters
        ------------
        chart : Chart
            chart
        width : str
            width of the plot, expressed as a number of pixels or a percentage
            of the container width
        """
        if isinstance(chart, Plot):
            chart, width = chart.chart, width or chart.width

        self.chart = chart
        self.width = internals.Size(
            width
            or self.chart.get(
                ["chart", "width"],
                "100%" if easychart.config.rendering.responsive else "600px",
            )
        )

    def serialize(self) -> dict:
        """
        Returns
        -------
        dict
        """
        return {
            "chart": self.chart.serialize(),
            "width": self.width,
        }
