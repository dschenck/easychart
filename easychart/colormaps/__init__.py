import json
import os


def all() -> list:
    """
    Iterates through all colormaps, yielding one at a time

    Returns
    -------
    generator
    """
    for filename in os.listdir(os.path.dirname(__file__)):
        try:
            yield get(filename.replace(".json", ""))
        except Exception:
            pass


def get(name) -> dict:
    """
    Load and return a color map

    Parameters
    ----------
    name : str

    Returns
    -------
    dict
    """
    if not isinstance(name, str):
        raise ValueError(
            f"Expected colormap name to be a string, received '{type(name).__name__}'"
        )

    if ".reversed" in name:
        name, reversed = name.replace(".reversed", ""), True
    else:
        reversed = False

    if ".symmetric" in name:
        name, symmetric = name.replace(".symmetric", ""), True
    else:
        symmetric = False

    try:
        with open(
            os.path.join(os.path.dirname(__file__), f"{name.lower()}.json"), "r"
        ) as file:
            colormap = json.load(file)
    except FileNotFoundError:
        raise ValueError(f"Colormap '{name}' does not exist.") from None

    if reversed:
        colormap = {**colormap, "colors": colormap["colors"][::-1]}

    if symmetric:
        colormap = {**colormap, "colors": colormap["colors"] + colormap["colors"][::-1]}

    return {**colormap, "name": name}
