import os
import json
import easychart


def locate(name):
    """
    Locate a theme's file by name

    Parameters
    ----------
    name : str, path
        name or filename of theme

    Returns
    -------
    filename : path
    """
    if not name.endswith(".json"):
        name = f"{name}.json"

    if os.path.exists(name):
        return name

    if os.path.exists(os.path.join(os.getcwd(), name)):
        return os.path.join(os.getcwd(), name)

    if os.path.exists(os.path.join(os.path.expanduser("~/.easychart"), name)):
        return os.path.join(os.path.expanduser("~/.easychart"), name)

    if os.path.exists(os.path.join(os.path.dirname(__file__), name)):
        return os.path.join(os.path.dirname(__file__), name)

    raise OSError(f"Unable to locate theme '{name}'")


def get(theme=None):
    """
    Load theme by name or filename

    Note
    ----
    If theme is None, then a waterfall search is executed:
    - if 'EASYCHART.THEME' environment variable is set, load it
    - if 'theme' argument is set in easychart.config, load it
    - if 'theme.json' exists in os.path.expanduser("~/.easychart"), load it
    - otherwise, load 'easychart' default from within the package

    If theme is not a filename, a waterfall search is executed for its location
    - check the current working directory for a '{theme}.json' file
    - check os.path.expanduser("~/.easychart") for a '{theme}.json' file
    - check the package 'themes' directory

    Parameters
    ----------
    theme : str, path, dict
        theme name, theme filename, or theme

    Returns
    -------
    theme : dict
    """
    if isinstance(theme, dict):
        return theme

    if theme is None:
        if os.environ.get("EASYCHART.THEME"):
            theme = os.environ.get("EASYCHART.THEME")

    if theme is None:
        if easychart.config.get("theme") is not None:
            theme = easychart.config.theme

    if theme is None:
        if os.path.exists(os.path.expanduser("~/.easychart/theme.json")):
            theme = os.path.expanduser("~/.easychart/theme.json")

    if theme is None:
        theme = os.path.join(os.path.dirname(__file__), "easychart.json")

    with open(locate(theme), "r") as file:
        theme = json.load(file)

    return theme
