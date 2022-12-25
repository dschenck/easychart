Column chart 
=====================================================

.. raw:: html 

    <div class="chart-container" style="min-height:400px" data-filename="../../_static/charts/chart-1.json?v=1"></div>

.. literalinclude:: /_misc/examples/chart-1.py

Column spacing
--------------
You can control the space between columns (i.e. between series) and between groups of columns (i.e. values) by setting the :code:`groupPadding` and :code:`pointPadding` values respectively under :code:`chart.plotOptions.column`.

.. note::

    The padding is expressed in units of the x-axis, not pixels

.. raw:: html 

    <div class="chart-container" style="min-height:400px" data-filename="../../_static/charts/chart-58.json"></div>

.. literalinclude:: /_misc/examples/chart-58.py
