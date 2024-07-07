import easytree
import pandas as pd
import collections

import easychart.internals as internals


class Series(easytree.list):
    """
    Series collection
    """

    @internals.alias("showInLegend", "legend")
    @internals.alias("marker", "markers")
    @internals.alias("lineWidth", "linewidth", "width", "lw")
    @internals.alias("dashStyle", "dashstyle", "dash", "linestyle", "ls")
    @internals.alias("visible", "active", "enabled")
    @internals.alias("dataLabels", "datalabels", "labels")
    @internals.alias("opacity", "alpha", "transparency")
    @internals.alias("name", "label")
    @internals.alias("color", "c")
    @internals.alias("data", "y")
    @internals.alias("index", "x")
    @internals.alias("showInNavigator", "navigator")
    @internals.alias("markersize", "ms", "size", "radius")
    @internals.alias("markercolor", "mc", "markerfacecolor", "markerfillcolor", "mfc")
    @internals.alias("markerlinewidth", "mlw")
    @internals.alias("markerlinecolor", "mlc")
    def append(self, data=None, **kwargs):
        if "markersize" in kwargs:
            kwargs["marker"] = {
                **kwargs.get("marker", {}),
                "radius": kwargs.pop("markersize"),
            }

        if "markercolor" in kwargs:
            kwargs["marker"] = {
                **kwargs.get("marker", {}),
                "fillColor": kwargs.pop("markercolor"),
            }

        if "markerlinewidth" in kwargs:
            kwargs["marker"] = {
                **kwargs.get("marker", {}),
                "lineWidth": kwargs.pop("markerlinewidth"),
            }

        if "markerlinecolor" in kwargs:
            kwargs["marker"] = {
                **kwargs.get("marker", {}),
                "lineColor": kwargs.pop("markerlinecolor"),
            }

        if "marker" in kwargs:
            if isinstance(kwargs["marker"], bool):
                kwargs["marker"] = {"enabled": kwargs["marker"]}
            elif isinstance(kwargs["marker"], (int, float)):
                kwargs["marker"] = {"radius": kwargs["marker"]}
            elif kwargs["marker"] in [
                "circle",
                "square",
                "diamond",
                "triangle",
                "triangle-down",
            ]:
                kwargs["marker"] = {"symbol": kwargs["marker"]}
            elif kwargs["marker"] is None:
                kwargs["marker"] = {"enabled": False}

        if "dataLabels" in kwargs:
            if isinstance(kwargs["dataLabels"], bool):
                kwargs["dataLabels"] = {"enabled": kwargs.pop("dataLabels")}
            elif isinstance(kwargs["dataLabels"], str):
                kwargs["dataLabels"] = {
                    "enabled": True,
                    "format": kwargs.pop("dataLabels"),
                }
            else:
                kwargs["dataLabels"] = kwargs.pop("dataLabels")

        if "color" in kwargs:
            if isinstance(kwargs["color"], int):
                kwargs["colorIndex"] = kwargs.pop("color")

        if isinstance(data, pd.Series):
            if "name" not in kwargs:
                kwargs["name"] = data.name

        if isinstance(data, (pd.Series, pd.DataFrame)):
            if "index" in kwargs:
                if isinstance(kwargs["index"], collections.abc.Iterable):
                    data = data.values.tolist()
                elif isinstance(kwargs["index"], bool):
                    if kwargs["index"] == False:
                        data = data.values.tolist()
                    if kwargs["index"] == True:
                        data = data.reset_index().values.tolist()
            else:
                data = data.reset_index().values.tolist()

        if "index" in kwargs and isinstance(kwargs["index"], collections.abc.Iterable):
            data = [
                internals.flatten(i, v) for (i, v) in zip(kwargs.pop("index"), data)
            ]

        return super().append(data=data, **kwargs)
