import os
import simplejson
import html

import easychart
import easychart.encoders
import easychart.themes
import easychart.internals

from jinja2 import Environment, FileSystemLoader

# create the environment
environment = Environment(
    loader=FileSystemLoader(os.path.join(os.path.dirname(__file__)))
)


def render(plot: easychart.Plot, updates: list, *, theme: str = None, options=None):
    """
    Render a simple race chart

    .. warning::
        Experimental

    Parameters
    ----------
    plot : easychart.Chart, easychart.Plot
        the initial chart

    update : list[dict]
        incremental updates

    theme : str
        theme name

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
    # import IPython only if function is called
    # IPython is a soft dependency
    import IPython
    import IPython.display

    if not isinstance(plot, easychart.Plot):
        plot = easychart.Plot(plot)

    # get the template and render
    template = environment.get_template("template.jinja").render(
        **{
            "plot": simplejson.dumps(
                plot.serialize(), default=easychart.encoders.default
            ),
            "updates": simplejson.dumps(updates, default=easychart.encoders.default),
            "theme": simplejson.dumps(easychart.themes.get(theme)),
            "scripts": easychart.config.scripts,
            "stylesheets": easychart.config.stylesheets,
            "options": simplejson.dumps(
                {
                    "one:one": False,
                    "animate": False,
                    "interval": 500,
                    **(options or {}),
                }
            ),
            "count": len(updates),
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
