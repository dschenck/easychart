try:
    ip = get_ipython()
except:
    ip = None
        
if ip and (ip.__module__.startswith('IPython') or ip.__module__.startswith('ipykernel')):
    
    import easychart
    import easychart.templating
    import html
    import IPython

    def render(obj):
        if isinstance(obj, easychart.Chart):
            grid = easychart.Grid([easychart.Plot(obj)])
        elif isinstance(obj, easychart.Plot):
            grid = easychart.Grid([obj], theme=obj.theme)
        elif isinstance(obj, easychart.Grid):
            grid = obj
        else: 
            raise TypeError(f"Unexpected type ({obj.__class__})")

        template = easychart.templating.render(grid)
        return f'<iframe style="border:0;outline:none" srcdoc="{html.escape(template)}" height="{grid.height}" width="100%"></iframe>'

    if IPython.__version__ >= '0.11':
        formatter = ip.display_formatter.formatters['text/html']
            
        for cls in [easychart.Chart, easychart.Plot, easychart.Grid]:
            formatter.for_type(cls, render)
