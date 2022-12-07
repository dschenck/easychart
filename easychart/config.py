import os
import json
import easytree

__all__ = ["config"]


class Config:
    def __init__(self):
        self.config = self.load()

    @property
    def filename(self):
        """
        Returns the filename of the user config file
        """
        if os.environ.get("EASYCHART.CONFIG"):
            return os.environ.get("EASYCHART.CONFIG")
        return os.path.expanduser("~/.easychart/config.json")

    def __repr__(self):
        return repr({"filename": self.filename, "config": self.config.serialize()})

    @property
    def defaults(self):
        return {
            "stylesheets": [],
            "scripts": [
                "https://code.highcharts.com/highcharts.js",
                "https://code.highcharts.com/highcharts-more.js",
                "https://code.highcharts.com/modules/heatmap.js",
                "https://code.highcharts.com/modules/exporting.js",
                "https://code.highcharts.com/modules/offline-exporting.js",
                "https://code.highcharts.com/modules/export-data.js",
                "https://code.highcharts.com/modules/annotations.js",
                "https://code.highcharts.com/modules/accessibility.js",
            ],
            "theme": "easychart",
            "rendering": {"container": {"width": 985}, "responsive": False,},
        }

    def load(self):
        """
        Load the configuration
        """
        # load the default values
        config = {**self.defaults}

        # load the user configuration
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                config.update(json.load(file))

        return easytree.Tree(config)

    def save(self, filename=None):
        """
        Saves the configuration to the user file
        """
        if filename is None:
            filename = self.filename

        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.mkdir(os.path.dirname(filename))
            except Exception as e:
                raise Exception(f"Failed to create easychart directory")

        with open(filename, "w") as file:
            easytree.dump(self.config, file, indent=4)
        return

    def reset(self, save=True):
        """
        Resets and overrides the user configuration
        """
        self.config = easytree.Tree(self.defaults)

        if save:
            self.save()
        return

    @property
    def theme(self):
        return self.config.theme

    @theme.setter
    def theme(self, value):
        if not isinstance(value, str):
            raise TypeError("Theme should be a theme name or a path to a theme file")
        self.config.theme = value

    @property
    def stylesheets(self):
        return self.config.stylesheets

    @stylesheets.setter
    def stylesheets(self, values):
        if not isinstance(values, (list, tuple, set)):
            raise TypeError(
                f"Stylesheets must be an iterable, received {type(values).__name__} object"
            )
        if not all([isinstance(value, str) for value in values]):
            raise TypeError(f"Stylesheets must be an iterable of stylesheets URLs")
        self.config.stylesheets = values

    @property
    def scripts(self):
        return self.config.scripts

    @scripts.setter
    def scripts(self, values):
        if not isinstance(values, (list, tuple, set)):
            raise TypeError(
                f"Scripts must be an iterable, received {type(values).__name__} object"
            )
        if not all([isinstance(value, str) for value in values]):
            raise TypeError(f"Scripts must be an iterable of stylesheets URLs")
        self.config.scripts = values


config = Config()
