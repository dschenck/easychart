import IPython
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


def render(charts) -> str:
    """
    Render a chart, plot or grid of charts to
    """
    if isinstance(charts, easychart.Chart):
        grid = easychart.Grid([easychart.Plot(charts)])
    elif isinstance(charts, easychart.Plot):
        grid = easychart.Grid([charts])
    elif isinstance(charts, easychart.Grid):
        grid = charts
    else:
        raise TypeError(f"Unexpected type ({charts.__class__})")

    # get the template and render
    template = environment.get_template("template.jinja").render(
        **{
            "plots": simplejson.dumps([plot.serialize() for plot in grid.plots]),
            "theme": simplejson.dumps(easychart.themes.get(grid.theme)),
            "scripts": easychart.config.scripts,
            "stylesheets": easychart.config.stylesheets,
        }
    )

    return f"""
        <iframe 
            style="border:0;outline:none;width:{easychart.internals.Size(grid.width or easychart.config.rendering.container.width)};max-width:{easychart.internals.Size(easychart.config.rendering.container.get("max-width", "100%"))}" 
            onload='javascript:(function(o){{o.style.height=Math.max(400, o.contentWindow.document.body.scrollHeight)+"px"; o.contentWindow.focus()}}(this));' 
            allow="clipboard-read; clipboard-write"
            srcdoc="{html.escape(template)}">
        </iframe>
    """
