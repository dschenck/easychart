import os
import json
import html
import simplejson
import easychart
import easychart.encoders
import warnings

from jinja2 import Environment, FileSystemLoader, select_autoescape

#create the environment 
environment = Environment(
    loader=FileSystemLoader(
        os.path.join(os.path.dirname(__file__))
    ))

def render(grid):
    #load configuration
    with open(os.path.join(os.path.dirname(__file__), "config.json"), "r") as file: 
        config = json.load(file)
    if os.environ.get("EASYCHART.CONFIG"): 
        if os.path.exists(os.environ["EASYCHART.CONFIG"]): 
            with open(os.environ["EASYCHART.CONFIG"], "r") as file: 
                config.update(json.load(file))
        else:
            warnings.warn("Found 'EASYCHART.CONFIG' environment variable, but path does not exist")
    elif os.path.exists(os.path.expanduser("~/.easychart/config.json")):
        with open(os.path.expanduser("~/.easychart/config.json"), "r") as file: 
            config.update(json.load(file))     

    #determine the theme
    if grid.theme is None: 
        if os.environ.get("EASYCHART.THEME"): 
            grid.theme = os.environ.get("EASYCHART.THEME")
    if grid.theme is None:
        if config.get("theme") is not None: 
            grid.theme = config.get("theme")
    if grid.theme is None:
        if os.path.exists(os.path.expanduser("~/.easychart/theme.json")):
            grid.theme = os.path.expanduser("~/.easychart/theme.json")
    if grid.theme is None:
        grid.theme = os.path.join(os.path.dirname(__file__), "themes", "easychart.json")

    #resolve for the actual theme
    if isinstance(grid.theme, str):
        if os.path.exists(os.path.join(os.path.expanduser("~/.easychart"), grid.theme + ".json")):
            with open(os.path.join(os.path.expanduser("~/.easychart"), grid.theme + ".json"), "r") as file:
                grid.theme = json.load(file)
        elif os.path.exists(os.path.join(os.path.dirname(__file__), "themes", grid.theme + ".json")):
            with open(os.path.join(os.path.dirname(__file__), "themes", grid.theme + ".json"), "r") as file:
                grid.theme = json.load(file)
        elif os.path.exists(grid.theme):
            with open(grid.theme, "r") as file:
                grid.theme = json.load(file)
        else:
            raise ValueError(f"Unable to load theme '{grid.theme}'. Please check your spelling.")

    #get the template and render
    template = environment.get_template("template.html")

    return template.render(
            scripts=config["scripts"], 
            stylesheets=config["stylesheets"],
            theme=simplejson.dumps(grid.theme), 
            plots=simplejson.dumps([plot.serialize() for plot in grid.plots], 
                              default=easychart.encoders.default, ignore_nan=True))

