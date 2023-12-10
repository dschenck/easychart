Rendering
=========
Rendering is the process by which a chart configuration is serialized and displayed as a Highcharts instance in your Jupyter notebook in your browser.

Modules and extensions
----------------------

Some chart types (e.g. Sankey) or features (e.g. `exporting <https://www.highcharts.com/docs/export-module/export-module-overview>`_) require additional javascript modules to render in your Jupyter notebook. 

.. note::
    By default, the following modules are loaded
       - https://code.highcharts.com/highcharts.js (required)
       - https://code.highcharts.com/highcharts-more.js
       - https://code.highcharts.com/modules/heatmap.js
       - https://code.highcharts.com/modules/exporting.js
       - https://code.highcharts.com/modules/offline-exporting.js
       - https://code.highcharts.com/modules/export-data.js
       - https://code.highcharts.com/modules/annotations.js
       - https://code.highcharts.com/modules/accessibility.js

The full list of available modules is available from the `Highcharts CDN <https://code.highcharts.com/>`_ page. 

.. hint::
    Check the `Highcharts API documentation <https://api.highcharts.com/highcharts/>`_ to see which chart types have dependencies. For example, the `venn <https://api.highcharts.com/highcharts/series.venn>`_ chart type requires the venn module.

To load an additional module in your Jupyter notebook, add the required modules script path to the config. Here are a few examples: 
::

    import easychart

    # Sankey module
    # https://api.highcharts.com/highcharts/series.sankey
    easychart.config.scripts.append("https://code.highcharts.com/modules/sankey.js")

    # save changes if you want these imports to persist in your next session
    easychart.config.save()

.. attention::
    Do not mix versioned modules (e.g. https://code.highcharts.com/8/highcharts.js) with unversioned modules (https://code.highcharts.com/modules/heatmap.js) as this may result in conflicts.

To see which modules are already imported in your config, simply print the configuration to your console: 
:: 

    import easychart 

    print(easychart.config)

Once customized and saved the config file is saved at the following location
::

    import os

    os.path.expanduser("~/.easychart/config.json")


You can reset the config file back to factory values by calling the `reset` method: 
::

    import easychart
    
    easychart.config.reset()
    easychart.config.save()


