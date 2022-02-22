Plotting with Pandas
=========================================

By default values from the index of :code:`pd.Series` and :code:`pd.DataFrame` objects are used as the x coordinates. In the below example, the x coordinates range from 10 to 30.

.. raw:: html 

    <div class="chart-container" style="min-height:400px" data-filename="../../_static/charts/chart-38.json?v=1"></div>


.. literalinclude:: /_misc/examples/chart-38.py


You can override the index of the data by explicitly passing an :code:`index` argument. In the below example, we override the x coordinates to the range 100 to 130. 

.. raw:: html 

    <div class="chart-container" style="min-height:400px" data-filename="../../_static/charts/chart-39.json?v=1"></div>


.. literalinclude:: /_misc/examples/chart-39.py

Alternatively, you can drop the index by calling the :code:`values` property of the pandas objects. 

.. admonition:: Important
   :class: important

   This is particularly relevant for scatter plots.

In the below example, we drop the index, and the x coordinates default to the range :code:`[0...n]`.

.. raw:: html 

    <div class="chart-container" style="min-height:400px" data-filename="../../_static/charts/chart-40.json?v=1"></div>


.. literalinclude:: /_misc/examples/chart-40.py