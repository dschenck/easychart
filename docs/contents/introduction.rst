Getting started
=========================================

About Highcharts and easychart
-----------------------------------------
Highcharts is an interactive charting library, written in Javascript and designed for the web browser. The `Highcharts demo page <https://www.highcharts.com/demo/>`_ is rich with examples that you can use as inspiration. 

easychart is an open-source Python library designed for building Highcharts visualizations in Python and rendering them in a Jupyter notebook or a HTML file.

Installation
-----------------------------------------
Installing :code:`easychart` is simple with pip: 
::

    pip install easychart

Your first chart
-----------------------------------------
Creating and rendering a chart involves constructing a chart *definition* which contains both data and some (optional) configurations, such as the chart's background-color, the format of the axis labels etc. 

Here's a simple example: 
::

    import easychart

    chart = easychart.new()
    chart.plot([1,1,2,3,5,8], name="Fibonacci series")
    chart

.. raw:: html 

    <div class="chart-container" data-filename="../_static/charts/chart-8.json?v=1"></div>

.. note::
    Under the hood, easychart serializes the chart definition to JSON, which is interpreted by the highcharts Javascript library in your browser. 

Serialization
-----------------------------------------
Serialization involves converting a chart object back into a native Python object (a dictionary of only native types). This can be useful for exporting and debugging. 
::

    import easychart 

    chart = easychart.new("column", title="US 2016 Presidential election results")
    chart.yAxis.labels.format = "{value}%"
    chart.categories = ["Electoral vote", "Popular vote"]
    chart.plot([46.1,48.2], name="Hillary Clinton", color="rgb(18,8,55)")
    chart.plot([57.3,42.7], name="Donald Trump", color="rgb(202,0,4)")
    chart.serialize()

    {
        "series": [
            {
                "data": [
                    46.1,
                    48.2
                ],
                "name": "Hillary Clinton",
                "color": "rgb(18,8,55)"
            },
            {
                "data": [
                    57.3,
                    42.7
                ],
                "name": "Donald Trump",
                "color": "rgb(202,0,4)"
            }
        ],
        "chart": {
            "type":"column",
            "zoomType": "x"
        },
        "title": {
            "text": "US 2016 Presidential election results"
        },
        "yAxis": {
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

