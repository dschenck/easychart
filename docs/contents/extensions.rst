Modules and extensions
============================

Some chart types (e.g. Sankey) or features (e.g. `exporting <https://www.highcharts.com/docs/export-module/export-module-overview>`_) require additional javascript modules to render in your Jupyter notebook. 

.. note::
    Check the Highcharts API documentation to see which chart types have dependencies. For example, the `venn <https://api.highcharts.com/highcharts/series.venn>`_ chart type requires the venn module.

To import these module dependencies, add the required modules scripts to the config. Here are a few examples: 
::

    import easychart

    #Sankey module
    #https://api.highcharts.com/highcharts/series.sankey
    easychart.config.scripts.append("https://code.highcharts.com/8/modules/sankey.js")

    #exporting module
    #https://api.highcharts.com/highcharts/exporting
    easychart.config.scripts.append("https://code.highcharts.com/8/modules/exporting.js")

    #annotations module
    #https://api.highcharts.com/highcharts/annotations
    easychart.config.scripts.append("https://code.highcharts.com/8/modules/annotations.js")

    #heatmap module
    #https://api.highcharts.com/highcharts/series.heatmap
    easychart.config.scripts.append("https://code.highcharts.com/8/modules/heatmap.js")

    #streamgraph module
    #https://api.highcharts.com/highcharts/series.streamgraph
    easychart.config.scripts.append("https://code.highcharts.com/modules/streamgraph.js")

    #bellcurve module
    #https://api.highcharts.com/highcharts/series.bellcurve
    easychart.config.scripts.append("https://code.highcharts.com/modules/bellcurve.js")

    #save changes if you want these imports to persist in your next session
    easychart.config.save()

To see which modules are already imported in your config, simply print the configuration to your console: 
:: 

    import easychart 

    print(easychart.config)

The config file is saved at the following location
::

    import os

    os.path.expanduser("~/.easychart/config.json")


You can reset the config file back to factory values by calling the `reset` method: 
::

    import easychart
    
    easychart.config.reset()
    easychart.config.save()


