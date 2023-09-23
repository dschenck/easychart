import os
import simplejson
import easychart
import easychart.encoders
import easychart.themes

from jinja2 import Environment, FileSystemLoader

# create the environment
environment = Environment(
    loader=FileSystemLoader(os.path.join(os.path.dirname(__file__)))
)


def render(grid):
    # get the template and render
    template = environment.get_template("template.html")

    return template.render(
        scripts=easychart.config.scripts,
        stylesheets=easychart.config.stylesheets,
        theme=simplejson.dumps(easychart.themes.get(grid.theme)),
        plots=simplejson.dumps(
            grid.serialize(),
            default=easychart.encoders.default,
            ignore_nan=True,
        ),
    )
