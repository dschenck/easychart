API
===============================

Utility functions
-----------------------------------
.. automodule:: easychart
    :members: new, render

Objects
-----------------------------------
.. autoclass:: easychart.Chart
    :members: append, plot, serialize, save, vline, hline, vband, hband

Setter aliases
-----------------------------------------
The :code:`Chart` object comes with a number of setter shortcuts, also known as aliases.

Title
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Setting a string to :code:`chart.title` will assign the value to the :code:`chart.title.text` attribute.
::

    chart = easychart.new()
    #equivalent to chart.title.text = "Chart title"
    chart.title = "Chart title"

Subtitle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Setting a string to :code:`chart.subtitle` will assign the value to the :code:`chart.subtitle.text` attribute.
::

    chart = easychart.new()
    #equivalent to chart.subtitle.text = "Chart subtitle"
    chart.subtitle = "Chart subtitle" 

Datetime
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Setting :code:`chart.datetime` equal to :code:`True` will set the xAxis' type equal to datetime
::

    chart = easychart.new()
    #equivalent to chart.xAxis.type = "datetime"
    chart.datetime = True

Categories
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Setting a value to :code:`chart.categories` will assign the value to the :code:`chart.xAxis.categories` attribute.
::

    chart = easychart.new()
    #equivalent to chart.xAxis.categories = ["Paris","New York","Nairobi"]
    chart.categories = ["Paris","New York","Nairobi"]

Zoom
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Setting None, "x", "y" or "xy" to :code:`chart.zoom` will assign the value to the :code:`chart.chart.zoomType` attribute.
::

    chart = easychart.new()
    #equivalent to chart.chart.zoomType = "xy"
    chart.zoom = "xy"

Tooltip
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Setting a boolean to :code:`chart.tooltip` will set enable or disable the tooltip. 
::

    chart = easychart.new()
    #equivalent to chart.tooltip.enabled = False
    chart.tooltip = False

Setting :code:`"shared"` to :code:`chart.tooltip` will set :code:`chart.tooltip.shared = True`. 
::

    chart = easychart.new()
    #equivalent to chart.tooltip.shared = True
    chart.tooltip = "shared"

Setting a label format string to tooltip will affect the decimals, prefix and suffix. 
::

    chart = easychart.new()
    chart.tooltip = "${value:.2f} per unit"

is equivalent to 
::

    chart = easychart.new()
    chart.tooltip.valuePrefix = "$"
    chart.tooltip.valueSuffix = " per unit"
    chart.tooltip.valueDecimals = 2

Setting a tuple of values to the :code:`chart.tooltip` will set each value to the toolip attribute, as per the above rules. 
::

    chart = easychart.new()
    chart.tooltip = ("shared", "{value}mm")

is equivalent to:
::

    chart = easychart.new()
    chart.tooltip.shared = True
    chart.tooltip.valueSuffix = "mm"

Legend
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Setting a boolean to legend will enable or disable the legend
::

    chart = easychart.new()
    #equivalent to chart.legend.enabled = False
    chart.legend = False

Stacking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Setting one of None, "percent" or "normal" to :code:`chart.stacking` will affect the value to :code:`chart.plotOptions.series.stacking`. 
::

    chart = easychart.new()
    #equivalent to chart.plotOptions.series.stacking = "percent"
    chart.stacking = "percent"


.. autoclass:: easychart.Plot
    :members: __init__

.. autoclass:: easychart.Grid
    :members: __init__, add

