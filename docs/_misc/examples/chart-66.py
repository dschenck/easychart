import easychart

# ensure the module is available
script = "https://code.highcharts.com/modules/dumbbell.js"

if script not in easychart.config.scripts:
    easychart.config.scripts.append(script)


chart = easychart.new("dumbbell", categories=["A", "B"], legend=False)
chart.plot(
    [[-2, 8], [4, 6]],
    labels="{#if (le point.y 0)}{point.y:,.0f}USD{else}+{point.y}USD{/if}",
)
chart
