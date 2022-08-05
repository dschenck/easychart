Plotting with Pandas
=========================================

:code:`easychart` natively supports :code:`pd.Series` and :code:`pd.DataFrame` objects. Each :code:`pd.Series` or :code:`pd.DataFrame` is treated as a single series, and each row will be handled as a data point. Numeric values from a :code:`pd.Index` will be used as the :code:`x` coordinates, although you can override this. 

.. literalinclude:: /_misc/examples/chart-38.py

.. raw:: html 

    <div class="chart-container" style="min-height:400px" data-filename="../_static/charts/chart-38.json?v=1"></div>

Here's an example from a :code:`pd.DataFrame`. 

.. literalinclude:: /_misc/examples/chart-41.py

.. raw:: html 

    <div class="chart-container" style="min-height:400px" data-filename="../_static/charts/chart-41.json?v=1"></div>

.. admonition:: Important
   :class: important

   The number of columns of the :code:`pd.DataFrame` must be appropriate for the series type. 
   
   For example: 
        - a :code:`line` series requires an :code:`(x, y)` value for each point, so 2 columns (or 1 column and the :code:`pd.Index`) are expected 
        - a :code:`columnrange` series requires an :code:`(x, min, max)` value for each point, so 3 columns (or 2 columns and the :code:`pd.Index`) are expected
        - a :code:`bubble` series requires an :code:`(x, y, z)` value for each point, so 3 columns (or 2 columns and the :code:`pd.Index`) are expected

    .. literalinclude:: /_misc/examples/chart-42.py

    .. raw:: html 

        <div class="chart-container" style="min-height:400px" data-filename="../_static/charts/chart-42.json?v=1"></div>

    .. literalinclude:: /_misc/examples/chart-43.py

    .. raw:: html 

        <div class="chart-container" style="min-height:400px" data-filename="../_static/charts/chart-43.json?v=1"></div>


You can override the index of the data by explicitly passing an :code:`index` argument. In the below example, we override the x coordinates to the range 100 to 130. 

.. literalinclude:: /_misc/examples/chart-39.py

.. raw:: html 

    <div class="chart-container" style="min-height:400px" data-filename="../_static/charts/chart-39.json?v=1"></div>


Alternatively, you can drop the index by calling the :code:`values` property of the pandas objects. 

.. admonition:: Important
   :class: important

   This is particularly relevant for scatter plots drawn from two columns of a :code:`pd.DataFrame` objects.

   .. literalinclude:: /_misc/examples/chart-42.py

   .. raw:: html 
   
       <div class="chart-container" style="min-height:400px" data-filename="../_static/charts/chart-42.json?v=1"></div>

In the below example, we drop the index, and the x coordinates default to the range :code:`[0...n]`.

.. literalinclude:: /_misc/examples/chart-40.py

.. raw:: html 

    <div class="chart-container" style="min-height:400px" data-filename="../_static/charts/chart-40.json?v=1"></div>


