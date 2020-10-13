import easychart

chart = easychart.new(type="pie", title="Distribution of blood type in the US")
chart.subtitle.text = "Source: American Red Cross"
chart.tooltip.pointFormat = "{point.percentage:.0f}%"
chart.append([{"name":bloodtype, "y":percentage} for bloodtype, percentage 
                in zip(["O","A","B","AB"],[45,40,11,4])])
chart