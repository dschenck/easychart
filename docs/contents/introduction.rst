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