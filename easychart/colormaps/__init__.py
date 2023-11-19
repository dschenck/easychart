import json
import os


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

    if name.endswith(".reversed"):
        name, reversed = name.lower()[:-9], True
    else:
        name, reversed = name.lower(), False

    with open(os.path.join(os.path.dirname(__file__), f"{name}.json"), "r") as file:
        colormap = json.load(file)

    if reversed:
        colormap = {**colormap, "colors": colormap["colors"][::-1]}

    return {**colormap, "name": name}
