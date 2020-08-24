10 minutes introduction
=========================================

What is Highcharts
-----------------------------------------
Highcharts is an interactive charting library, written in Javascript and designed for the web browser. The `Highcharts demo page <https://www.highcharts.com/demo/>`_ is rich with examples. 

What is easychart
-----------------------------------------
easychart is a Python library designed to making charts and rendering them in a Jupyter notebook or a HTML file.

Your first chart
-----------------------------------------
Creating and rendering a chart involves writing a chart *definition* which contains both data and some (optional) configurations, such as the chart's background-color, the format of the axis labels etc. At a minimum, a chart must contain data arranged in the form of a list of :code:`series`. Here's a simple example: 
::

    import easychart

    data = {"series":[{"data":[1,1,2,3,5,8], "name":"Fibonacci series"}]}
    easychart.render(data)

.. raw:: html 

    <div class="chart-container" data-filename="../_static/charts/chart-8.json?v=1">loading...</div>

.. note::
    In the above example, the chart definition is a simple python dictionary - no black magic involved here. It has only one key and its value is a list of individual series. There is only one series in the list.

The problem easychart solves
-----------------------------------------
As you can see from the above example, a chart definition can be a simple dictionary - and in this example, easychart was used only to render the chart. There are however some practical limitations with using native python dictionaries: 

- building deeply-nested dictionaries can be burdensome, let alone hard to read
- some data types, such as dates, :code:`pd.Series` and :code:`pd.DataFrame` need to be cast to primitive objects (timestamps, lists or dictionaries)
- rendering must be explicitely called to display the chart

To solve these issues, the easychart library provides a :code:`Chart` object and a few utility functions to faciliate the process of building charts: 
::

    import easychart

    chart = easychart.new()
    chart.series.append([1,1,2,3,5,8], name="Fibonacci series")
    chart

.. note::
    The :code:`Chart` object is itself built on top of the `easytree <https://easytree.readthedocs.io/en/latest/>`_ library. This lightweight library allows to build and work on deeply-nested trees with little overhead. 

Compare: 
:: 

    import easychart

    chart = {"title":{"text":"US 2016 Presidential election results"}, 
            "yAxis":{"labels":{"format":"{value}%}, "title":{"text":""}},
            "xAxis":{"categories":["Electoral vote", "Popular vote"]},
            "series":[{"data":[46.1,48.2], "name":"Hillary Clinton", 
                       "type":"column", "color":"rgb(18,8,55)"},
                      {"data":[57.3,42.7], "name":"Donald Trump",
                       "type":"column", "color":"rgb(18,8,55)"}]}
    easytree.render(chart)

with:
::

    import easychart 

    chart = easychart.new(title="US 2016 Presidential election results")
    chart.yAxis.title.text = ""
    chart.yAxis.labels.format = "{value}%"
    chart.xAxis.categories = ["Electoral vote", "Popular vote"]
    chart.append([46.1,48.2], name="Hillary Clinton", type="column", color="rgb(18,8,55)")
    chart.append([57.3,42.7], name="Donald Trump", type="column", color="rgb(202,0,4)")
    chart

.. raw:: html 

    <div class="chart-container" data-filename="../_static/charts/chart-9.json?v=1">loading...</div>

Serialization
-----------------------------------------
Serialization involves converting a chart object back into a native Python object (a dictionary of only native types). This can be useful for exporting and debugging. 
::

    import easychart 

    chart = easychart.new(title="US 2016 Presidential election results")
    chart.yAxis.title.text = ""
    chart.yAxis.labels.format = "{value}%"
    chart.xAxis.categories = ["Electoral vote", "Popular vote"]
    chart.append([46.1,48.2], name="Hillary Clinton", type="column", color="rgb(18,8,55)")
    chart.append([57.3,42.7], name="Donald Trump", type="column", color="rgb(202,0,4)")
    chart.serialize()

    {
        "series": [
            {
                "data": [
                    46.1,
                    48.2
                ],
                "name": "Hillary Clinton",
                "type": "column",
                "color": "rgb(18,8,55)"
            },
            {
                "data": [
                    57.3,
                    42.7
                ],
                "name": "Donald Trump",
                "type": "column",
                "color": "rgb(202,0,4)"
            }
        ],
        "chart": {
            "zoomType": "x"
        },
        "title": {
            "text": "US 2016 Presidential election results"
        },
        "yAxis": {
            "title": {
                "text": ""
            },
            "labels": {
                "format": "{value}%"
            }
        },
        "xAxis": {
            "categories": [
                "Electoral vote",
                "Popular vote"
            ]
        }
    }

Shortcuts
-----------------------------------------
The :code:`Chart` object comes with a number of setter shortcuts.

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
