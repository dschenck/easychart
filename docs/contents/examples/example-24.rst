Support for time
=====================================================

.. note::
    New in version 0.1.14. Datetime objects are converted to UNIX timestamps. Non-localized datetime objects are converted to UTC.

.. raw:: html 

    <div class="chart-container" style="min-height:400px" data-filename="../../_static/charts/chart-24.json?v=1"></div>


.. literalinclude:: /_misc/examples/chart-24.py

You can control the format of the X-axis labels and the tooltip header by adjusting their respective formats

.. raw:: html 

    <div class="chart-container" style="min-height:400px" data-filename="../../_static/charts/chart-25.json?v=1"></div>


.. literalinclude:: /_misc/examples/chart-25.py

Formatting 
----------
To format labels, the following formats are available. 

    - :code:`%a`: Short weekday, like 'Mon'
    - :code:`%A`: Long weekday, like 'Monday'
    - :code:`%d`: Two digit day of the month, 01 to 31
    - :code:`%e`: Day of the month, 1 through 31
    - :code:`%w`: Day of the week, 0 through 6
    - :code:`%b`: Short month, like 'Jan'
    - :code:`%B`: Long month, like 'January'
    - :code:`%m`: Two digit month number, 01 through 12
    - :code:`%y`: Two digits year, like 09 for 2009
    - :code:`%Y`: Four digits year, like 2009
    - :code:`%H`: Two digits hours in 24h format, 00 through 23
    - :code:`%k`: Hours in 24h format, 0 through 23
    - :code:`%I`: Two digits hours in 12h format, 00 through 11
    - :code:`%l`: Hours in 12h format, 1 through 12
    - :code:`%M`: Two digits minutes, 00 through 59
    - :code:`%p`: Upper case AM or PM
    - :code:`%P`: Lower case AM or PM
    - :code:`%S`: Two digits seconds, 00 through 59
    - :code:`%L`: Milliseconds (naming from Ruby)

.. raw:: html 

    <div class="chart-container" style="min-height:400px" data-filename="../../_static/charts/chart-51.json?v=1"></div>


.. literalinclude:: /_misc/examples/chart-51.py