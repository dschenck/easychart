Colormaps
=========

Usage 
-----

The :code:`easychart` package comes pre-loaded with the 83 colormaps available in `matplotlib <https://matplotlib.org/stable/users/explain/colors/colormaps.html>`_. Each of these can be assigned by name to the :code:`chart.cAxis` to convert the colormap to the `chart.colorAxis.stops <https://api.highcharts.com/highcharts/colorAxis.stops>`_ of the relevant chart. 

.. note:: 

    Colormap names are case-insensitive

.. literalinclude:: /_misc/examples/chart-61.py

.. raw:: html 

    <div class="chart-container" style="min-height:400px" data-filename="../../_static/charts/chart-61.json?v=1"></div>


Each colormap can be reversed by appending :code:`.reversed` to its name.

.. literalinclude:: /_misc/examples/chart-62.py

.. raw:: html 

    <div class="chart-container" style="min-height:400px" data-filename="../../_static/charts/chart-62.json?v=1"></div>

Each colormap can also be mirrored by appending :code:`.symmetric` to its name.

.. literalinclude:: /_misc/examples/chart-63.py

.. raw:: html 

    <div class="chart-container" style="min-height:400px" data-filename="../../_static/charts/chart-63.json?v=1"></div>

And :code:`.reversed` and :code:`.symmetric` can be used jointly.

.. literalinclude:: /_misc/examples/chart-64.py

.. raw:: html 

    <div class="chart-container" style="min-height:400px" data-filename="../../_static/charts/chart-64.json?v=1"></div>


Colormaps
---------
Selected colormaps. See `here <https://github.com/dschenck/easychart/tree/latest/easychart/colormaps>`_ for full list of available colormaps

Perceptually uniform sequential colormaps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Colormap name
     - Example
   * - plasma
     - .. image:: /static/colormaps/plasma.png
   * - viridis
     - .. image:: /static/colormaps/viridis.png
   * - inferno
     - .. image:: /static/colormaps/inferno.png
   * - magma
     - .. image:: /static/colormaps/magma.png
   * - cividis
     - .. image:: /static/colormaps/cividis.png

Sequential colormaps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Colormap name
     - Example
   * - greens
     - .. image:: /static/colormaps/greens.png
   * - bugn
     - .. image:: /static/colormaps/bugn.png
   * - ylgn
     - .. image:: /static/colormaps/ylgn.png
   * - ylorbr
     - .. image:: /static/colormaps/ylorbr.png
   * - ylorrd
     - .. image:: /static/colormaps/ylorrd.png
   * - reds
     - .. image:: /static/colormaps/reds.png
   * - oranges
     - .. image:: /static/colormaps/oranges.png
   * - orrd
     - .. image:: /static/colormaps/orrd.png
   * - purd
     - .. image:: /static/colormaps/purd.png
   * - rdpu
     - .. image:: /static/colormaps/rdpu.png
   * - bupu
     - .. image:: /static/colormaps/bupu.png
   * - purples
     - .. image:: /static/colormaps/purples.png
   * - pubu
     - .. image:: /static/colormaps/pubu.png
   * - blues
     - .. image:: /static/colormaps/blues.png
   * - ylgnbu
     - .. image:: /static/colormaps/ylgnbu.png
   * - greys
     - .. image:: /static/colormaps/greys.png
   * - pink
     - .. image:: /static/colormaps/pink.png

Diverging colormaps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
   :widths: 25 75
   :header-rows: 1
   
   * - Colormap name
     - Example
   * - rdgy
     - .. image:: /static/colormaps/rdgy.png
   * - brbg
     - .. image:: /static/colormaps/brbg.png
   * - rdbu
     - .. image:: /static/colormaps/rdbu.png
   * - puor
     - .. image:: /static/colormaps/puor.png
   * - piyg
     - .. image:: /static/colormaps/piyg.png
   * - prgn
     - .. image:: /static/colormaps/prgn.png
   * - coolwarm
     - .. image:: /static/colormaps/coolwarm.png
   * - bwr
     - .. image:: /static/colormaps/bwr.png
   * - seismic
     - .. image:: /static/colormaps/seismic.png


Cyclic colormaps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Colormap name
     - Example
   * - twilight
     - .. image:: /static/colormaps/twilight.png
   * - twilight_shifted
     - .. image:: /static/colormaps/twilight_shifted.png
   * - hsv
     - .. image:: /static/colormaps/hsv.png

Other colormaps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Colormap name
     - Example
   * - terrain
     - .. image:: /static/colormaps/terrain.png