import os
import simplejson
import html
import IPython
import IPython.display

import easychart
import easychart.encoders
import easychart.themes
import easychart.internals

from jinja2 import Environment, FileSystemLoader


class racechart:
    """
    Parameters
    ----------
    charts : list[easychart.Chart]
        plots

    theme : str
        theme name

    init : easychart.Chart
        the initial chart

    options : dict
        rendering options, including:

        one:one : bool
            defaults to False
            as per Highcharts documentation:

            When true, the series, xAxis, yAxis and annotations collections will be updated one to one, and items will be either added or removed to match the new updated options. For example, if the chart has two series and we call chart.update with a configuration containing three series, one will be added. If we call chart.update with one series, one will be removed. Setting an empty series array will remove all series, but leaving out theseries property will leave all series untouched. If the series have id's, the new series options will be matched by id, and the remaining ones removed.

        animate : bool
            defaults to False

        interval : int
            the number of milliseconds between each update

    """

    def __init__(self, charts: list, *, init: easychart.Chart = None, options=None):
        self.charts = charts
        self.init = easychart.Plot(init or charts[0])
        self.options = options or {}

    def render(self, *, theme=None):
        """
        Returns
        -------
        IPython.display.HTML
        """

        # create the environment
        environment = Environment(
            loader=FileSystemLoader(os.path.join(os.path.dirname(__file__)))
        )

        # get the template and render
        template = environment.get_template("template.jinja").render(
            **{
                "init": simplejson.dumps(
                    self.init.serialize(), default=easychart.encoders.default
                ),
                "charts": simplejson.dumps(
                    self.charts, default=easychart.encoders.default
                ),
                "theme": simplejson.dumps(easychart.themes.get(theme)),
                "scripts": easychart.config.scripts,
                "stylesheets": easychart.config.stylesheets,
                "options": simplejson.dumps(
                    {
                        "one:one": False,
                        "animate": False,
                        "interval": 500,
                        **self.options,
                    }
                ),
                "count": len(self.charts),
            }
        )

        return IPython.display.HTML(
            f"""
                <iframe 
                    style="border:0;outline:none;width:{easychart.internals.Size(easychart.config.rendering.container.width)};max-width:{easychart.internals.Size(easychart.config.rendering.container.get("max-width", "100%"))}" 
                    onload='javascript:(function(o){{o.style.height=o.contentWindow.document.body.scrollHeight+"px";}}(this));' 
                    srcdoc="{html.escape(template)}">
                </iframe>
            """
        )
