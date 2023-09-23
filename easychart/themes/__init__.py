import os
import json


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
    Load theme by name, filename

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
        if os.path.exists(os.path.expanduser("~/.easychart/theme.json")):
            theme = os.path.expanduser("~/.easychart/theme.json")

    if theme is None:
        theme = os.path.join(os.path.dirname(__file__), "easychart.json")

    with open(locate(theme), "r") as file:
        theme = json.load(file)

    return theme
