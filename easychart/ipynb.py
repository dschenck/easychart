try:
    ip = get_ipython()
except:
    ip = None
        
if ip and (ip.__module__.startswith('IPython') or ip.__module__.startswith('ipykernel')):
    
    import easychart
    import easychart.encoders
    import html
    import json
    import IPython
    import os

    def render(obj):
        """
        Creates an iframe to render a grid of highchart plots
        """
        if isinstance(obj, easychart.Chart):
            grid = easychart.Grid([easychart.Plot(obj)])
        elif isinstance(obj, easychart.Plot):
            grid = easychart.Grid([obj], theme=obj.theme)
        elif isinstance(obj, easychart.Grid):
            grid = obj
        else: 
            raise TypeError(f"Unexpected type ({obj.__class__})")

        if grid.theme is None: 
            if os.environ.get("easychart.theme"): 
                if os.path.exists(os.environ["easychart.theme"]): 
                    with open(os.environ["easychart.theme"], "r") as file: 
                        grid.theme = json.load(file)
            elif os.path.exists(os.path.expanduser("~/.easychart/theme.json")):
                with open(os.path.expanduser("~/.easychart/theme.json"), "r") as file: 
                    grid.theme = json.load(file)
            else:
                with open(os.path.join(os.path.dirname(__file__), "theme.json"), "r") as file: 
                    grid.theme = json.load(file)

        with open(os.path.join(os.path.dirname(__file__), "template.html"), "r") as file: 
            template = file.read()
            template = template.replace("{{ theme }}", json.dumps(grid.theme))
            template = template.replace("{{ plots }}", json.dumps([plot.serialize() for plot in grid.plots], cls=easychart.encoders.Encoder))
            
        return f'<iframe style="border:0;outline:none" srcdoc="{html.escape(template)}" height="{grid.height}" width="100%"></iframe>'

    if IPython.__version__ >= '0.11':
        formatter = ip.display_formatter.formatters['text/html']
            
        for cls in [easychart.Chart, easychart.Plot, easychart.Grid]:
            formatter.for_type(cls, render)
