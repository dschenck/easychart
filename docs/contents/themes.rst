Themes and styling
==================
A theme is a set of pre-defined options that are applied as default options before each chart is rendered. You can read more about themes on the Highcharts documentation page.

Changing the theme on the fly
-------------------------------
By default, charts will render with the *easychart* theme, but the package comes with a collection of 20 themes, courtesy of `Joshua Kunst <http://jkunst.com/highcharts-themes-collection/>`_. To render a chart in a different theme, render the chart and pass the name of the theme: 
::

    #pass the theme explicitely to the render function
    easychart.render(chart, theme="economist")

Alternatively, you can also pass a theme object to the :code:`render` function.
::
    
    import easychart

    #create a theme object
    theme = {"chart":{"backgroundColor":"#eeeeee"}, "yAxis":{"gridLineColor":"white"}}
    
    #pass the theme explicitely to the render function
    easychart.render(chart, theme=theme)

Changing the default theme
--------------------------
You can change the default theme
:: 

    import easychart

    easychart.config.theme = "economist"
    easychart.config.save() # if you want future notebooks to use this theme

.. note::
    
    You can set different values to :code:`easychart.config.theme`: 

    - the name of a built-in theme (`see list here <https://github.com/dschenck/easychart/tree/latest/easychart/themes>`_) like :code:`easychart` or :code:`economist`.
    - the complete path to a theme file (e.g. :code:`C:\\users\\David\\my-custom-theme.json`)
    - the name of a theme file (e.g. `custom-theme.json`) saved in the current working directory  
    - the name of a theme file (e.g. `custom-theme.json`) saved in the :code:`os.path.expanduser("~/.easychart")`

    In each case, with or without the :code:`.json` extension.

You can always reset your config back to factory defaults later
:: 

    easychart.config.reset(save=True) # or False to temporarily reset

You can also define the theme as the :code:`EASYCHART.THEME` environment variable. 

.. note::

    The value of the environment variable, if defined, will take precedence over the value defined in :code:`easychart.config.theme`

Creating a custom theme
------------------------
To create a custom theme: 

1. create a theme file (e.g. :code:`my-custom-theme.json`)
2. save it as :code:`os.path.expanduser("~/.easychart/my-custom-theme.json")`
3. update the config to point to this custom theme file

Here's a snippet to get started:
::

    import json
    import os 
    import easychart

    #create the folder if it doesn't exist
    if not os.path.exists(os.path.expanduser("~/.easychart")): 
        os.mkdir(os.path.expanduser("~/.easychart"))

    #create the theme.json file 
    with open(os.path.expanduser("~/.easychart/my-custom-theme.json"), "w") as file: 
        json.dump({}, file)

    #print the location of the file
    print(os.path.expanduser("~/.easychart/my-custom-theme.json"))

    # update the config
    easychart.config.theme = "my-custom-theme"
    easychart.config.save() # if you want to use this custom theme in all future notebooks

.. note::
    
    It's probably easiest to start from and amend an `existing <https://github.com/dschenck/easychart/blob/latest/easychart/themes/easychart.json>`_ theme file.