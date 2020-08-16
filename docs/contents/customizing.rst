Customizing
=======================
There are several ways with which you can customize styling defaults. In all instances, customization involves creating a :code:`theme` object, which you can pass explicitely to the :code:`render` function during runtime or save to a JSON file, which is then loaded and set during rendering.

Ad-hoc customization
---------------------------
You can explicitely pass a theme object to the :code:`render` function.
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

File-based customization
---------------------------
You can alternatively create a theme object and save it as a JSON file to disk. Unless explicitely set using the :code:`render` function (see above), the render function will search for a custom theme file: 

- if :code:`os.environ["easychart.theme"]` is set, and the file exists, it will use that file
- otherwise, if :code:`os.path.expanduser("~/.easychart/theme.json")` exists, it will use that file
- otherwise, it will default to a package-level file theme