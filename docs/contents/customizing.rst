Themes and styling
============================
A theme is a set of pre-defined options that are applied as default options before each chart is rendered. You can read more about themes on the Highcharts documentation page.

Changing the theme on the fly
-------------------------------
By default, charts will render with the *easychart* theme, but the package comes with a collection of 20 themes, courtesy of `Joshua Kunst <http://jkunst.com/highcharts-themes-collection/>`_. To render a chart in a different theme, render the chart and pass the name of the theme: 
::

    import easychart

    chart = easychart.new(title="US 2016 Presidential election results", ytitle="", yformat="{value}%")
    chart.categories = ["Electoral vote", "Popular vote"]
    chart.append([46.1,48.2], name="Hillary Clinton (D)", type="column")
    chart.append([57.3,42.7], name="Donald J. Trump (R)", type="column"

    #pass the theme explicitely to the render function
    easychart.render(chart, theme="economist")

Alternatively, you can also pass a theme object to the :code:`render` function.
::
    
    import easychart

    #create a theme object
    theme = {"chart":{"backgroundColor":"#eeeeee"}, "yAxis":{"gridLineColor":"white"}}

    chart = easychart.new(title="US 2016 Presidential election results", 
        ytitle="", yformat="{value}%")
    chart.xAxis.categories = ["Electoral vote", "Popular vote"]
    chart.series.append([46.1,48.2], name="Hillary Clinton (D)", 
        type="column", color="rgb(18,8,55)")
    chart.series.append([57.3,42.7], name="Donald J. Trump (R)", 
        type="column", color="rgb(202,0,4)")

    #pass the theme explicitely to the render function
    easychart.render(chart, theme=theme)

Changing the default theme 
----------------------------
By default, charts will render with the *easychart* theme, but you can configure easychart to use another default theme: simply create a :code:`theme.json` file and save it as :code:`os.path.expanduser("~/.easychart/theme.json")`. Here's a snippet to get started:
::

    import json
    import os 

    #create the folder if it doesn't exist
    if not os.path.exists(os.path.expanduser("~/.easychart")): 
        os.mkdir(os.path.expanduser("~/.easychart"))

    #create the theme.json file 
    with open(os.path.expanduser("~/.easychart/theme.json"), "w") as file: 
        json.dump({}, file)

    #print the location of the file
    print(os.path.expanduser("~/.easychart/theme.json"))

Alternatively, you can also set the :code:`EASYCHART.THEME` environment variable to either a preset theme (e.g. "economist") or the path of a custom theme file. 

Modules and extensions
------------------------------
Some Highchart features - like `exporting <https://www.highcharts.com/docs/export-module/export-module-overview>`_ - require additional modules. To import additional dependencies, extend this `config <https://github.com/dschenck/easychart/blob/master/easychart/config.json>`_ file and save as :code:`os.path.expanduser("~/.easychart/config.json")`.