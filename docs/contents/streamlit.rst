Integration with Streamlit
==========================

Charts made with easychart can be rendered on Streamlit. This [demo](https://github.com/dschenck/streamlit-demo/tree/main) application shows you how. 
::

    import streamlit as st
    import easychart

    # this is to ensure the chart takes 100% of the available width
    # otherwise it will default to 600px (not responsive)
    easychart.config.rendering.responsive = True

    chart = easychart.new("column")
    chart.title = "France Olympic medals"
    chart.subtitle = "by year and by medal class"
    chart.categories = ["Gold", "Silver", "Bronze"]
    chart.yAxis.title.text = "medals"
    chart.plot([7, 16, 18], name=2008)
    chart.plot([11, 11, 13], name=2012)

    st.components.v1.html(easychart.rendering.render(chart), height=400)


.. note:: 

    To ensure the charts are rendered *responsively*, set the :code:`easychart.config.rendering.responsive = True`

