try:
    ip = get_ipython()  # noqa: F821
except:
    ip = None

if ip and (
    ip.__module__.startswith("IPython") or ip.__module__.startswith("ipykernel")
):
    import IPython
    import easychart
    import easychart.rendering

    if IPython.__version__ >= "0.11":
        formatter = ip.display_formatter.formatters["text/html"]

        for cls in [easychart.Chart, easychart.Plot, easychart.Grid]:
            formatter.for_type(cls, easychart.rendering.render)
