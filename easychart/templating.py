import os
import json
import simplejson
import easychart
import easychart.encoders

from jinja2 import Environment, FileSystemLoader

# create the environment
environment = Environment(
    loader=FileSystemLoader(os.path.join(os.path.dirname(__file__)))
)


def render(grid):
    # load configuration
    easychart.config

    # determine the theme
    if grid.theme is None:
        if os.environ.get("EASYCHART.THEME"):
            grid.theme = os.environ.get("EASYCHART.THEME")
    if grid.theme is None:
        if easychart.config.theme is not None:
            grid.theme = easychart.config.theme
    if grid.theme is None:
        if os.path.exists(os.path.expanduser("~/.easychart/theme.json")):
            grid.theme = os.path.expanduser("~/.easychart/theme.json")
    if grid.theme is None:
        grid.theme = os.path.join(os.path.dirname(__file__), "themes", "easychart.json")

    # resolve for the actual theme
    if isinstance(grid.theme, str):
        if os.path.exists(
            os.path.join(os.path.expanduser("~/.easychart"), grid.theme + ".json")
        ):
            with open(
                os.path.join(os.path.expanduser("~/.easychart"), grid.theme + ".json"),
                "r",
            ) as file:
                grid.theme = json.load(file)
        elif os.path.exists(
            os.path.join(os.path.dirname(__file__), "themes", grid.theme + ".json")
        ):
            with open(
                os.path.join(os.path.dirname(__file__), "themes", grid.theme + ".json"),
                "r",
            ) as file:
                grid.theme = json.load(file)
        elif os.path.exists(grid.theme):
            with open(grid.theme, "r") as file:
                grid.theme = json.load(file)
        else:
            raise ValueError(
                f"Unable to load theme '{grid.theme}'. Please check your spelling."
            )

    # get the template and render
    template = environment.get_template("template.html")

    return template.render(
        scripts=easychart.config.scripts,
        stylesheets=easychart.config.stylesheets,
        theme=simplejson.dumps(grid.theme),
        plots=simplejson.dumps(
            grid.serialize(), default=easychart.encoders.default, ignore_nan=True,
        ),
    )
