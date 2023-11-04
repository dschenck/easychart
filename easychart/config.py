import os
import json
import easytree

__all__ = ["config"]


class Config(easytree.dict):
    """
    Package config

    This configuration contains configuration parameters of the easychart package, including
    the list of stylesheets and scripts that are loaded in the jupyter renderer to
    render the Highcharts objects.
    """

    defaults = {
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
        "theme": None,
        "rendering": {
            "container": {"width": "100%", "max-width": "100%"},
            "responsive": False,
        },
        "exporting": {"server": {"url": "http://export.highcharts.com/"}},
    }

    filename = os.environ.get(
        "EASYCHART.CONFIG", os.path.expanduser("~/.easychart/config.json")
    )

    @classmethod
    def load(cls):
        """
        Load the user configuration, if it exists, the default configuration
        otherwise

        Returns
        -------
        Config
        """
        if os.path.exists(Config.filename):
            with open(Config.filename, "r") as file:
                return Config({**Config.defaults, **json.load(file)})
        return Config(Config.defaults)

    def save(self, filename=None):
        """
        Saves the configuration to the user file

        Parameters
        ----------
        filename : str, path
            filename where to save the config file

        Returns
        -------
        None
        """
        if filename is None:
            filename = Config.filename

        if not os.path.exists(os.path.dirname(filename)):
            if os.path.dirname(filename) == os.path.expanduser("~/.easychart"):
                os.mkdir(os.path.dirname(filename))

        with open(filename, "w") as file:
            json.dump(self, file)

    def reload(self):
        """
        Reload user configuration from disk

        Returns
        -------
        None
        """
        self.clear()
        self.update(Config.load())

    def reset(self, *, save=True):
        """
        Resets and overrides the user configuration

        Parameters
        ----------
        save : bool
            True to persist the change to disk

        Returns
        -------
        None
        """
        self.clear()
        self.update(Config.defaults)

        if save:
            self.save()


config = Config.load()
