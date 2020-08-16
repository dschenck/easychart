easychart
======================================
Highcharts meets python

Quickstart
-------------------------------------
Installing :code:`easychart` is simple with pip: 
::

    pip install easychart

Open up a new Jupyter notebook and start creating your charts:
::

    >>> import easychart

    >>> chart = easychart.new(title="France Olympic medals", 
    ...     subtitle="by year and by medal class",
    ...     type="column", ytitle="medals")
    >>> chart.xAxis.categories = ["Gold","Silver","Bronze"]
    >>> chart.series.append([7, 16, 18], name=2008)
    >>> chart.series.append([11, 11, 13], name=2012)
    >>> chart
    
.. raw:: html

    <div class="chart-container" data-filename="_static/charts/chart-1.json?v=1">loading...</div>

.. toctree::
   :maxdepth: 2
   :caption: Table of contents

   contents/introduction
   contents/examples/index
   contents/customizing
   contents/API
   contents/changelog
