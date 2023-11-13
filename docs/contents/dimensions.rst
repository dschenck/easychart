Chart dimensions
----------------

.. note:: 

    New and updated in version 0.0.17

By default, charts are rendered in the Jupyter notebook with a default width of :code:`600px` and height of :code:`400px`.

.. hint::
    
    These default values are consistent with the default dimensions that the Highcharts library implements itself.

The chart :code:`width` and :code:`height` can be provided as arguments to the :code:`easychart.new` function: 
::
    
    >>> import easychart
    >>> chart = easychart.new(width=900, height=600) # pixels or percentages

... or set as properties to the :code:`chart` object:
::

    >>> chart = easychart.new()
    >>> chart.width  = 900 # pixels or percentages
    >>> chart.height = 600 # pixels or percentages

... or directly as properties of the :code:`chart.chart` object: 
::

    >>> chart = easychart.new()
    >>> chart.chart.width  = 900 # pixels ONLY
    >>> chart.chart.height = 600 # pixels or percentages



.. note::

    For the chart **width**, if given a percentage value (e.g. :code:`50%`), the chart width will be computed (by easychart) as a fraction of the default width (e.g. :code:`50%` of :code:`600px` is :code:`300px`).

    Example:
    ::

        >>> chart = easychart.new(width="200%")
        >>> chart.chart.width # the width property is set in chart.chart.width
        1200


    For the chart **height**, if given a percentage value (e.g. :code:`50%`), the chart height will be rendered (by Highcharts) as a fraction of the chart width (e.g. set height equal to :code:`50%` of the chart width). This allows for preserving the aspect ratio across responsive sizes.

Responsive rendering
====================
With responsive rendering, the chart :code:`width` shrinks and grows to fill the available space that it is provided with by its parent container. 

To enable responsive rendering, simply amend the easychart config as follows: 
::

    easychart.config.rendering.responsive = True # False to revert 
    easychart.config.save() # if you want to preserve this in future sessions

.. tip::

    By default, the parent container's :code:`width` and :code:`max-width` are both set to :code:`100%` of the notebook width. You can also customize the container dimensions (in absolute pixels or percentage of available space)

    ::
        
        # percentage of notebook width or pixels as string (e.g. "1200px")
        easychart.config.rendering.container.width = "100%"
        easychart.config.rendering.container["max-width"] = "980px" 
        easychart.config.save() # if you want to preserve this in future sessions



.. topic:: Why is responsive rendering disabled by default ? 

   By definition, a responsive chart's dimensions depends on the user's screen dimensions. This means that exporting a responsive chart as PNG/JPEG will need to fall back on the default dimensions (e.g. 600px for width and 400px for height). To ensure consistency between the chart dimensions rendered in the notebook and the chart dimensions exported as images, responsive rendering was disabled by default. 
