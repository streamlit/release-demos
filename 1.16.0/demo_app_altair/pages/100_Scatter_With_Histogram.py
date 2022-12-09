import streamlit as st
import altair as alt
import inspect
from vega_datasets import data

@st.experimental_memo
def get_chart_64383(use_container_width: bool):
    import altair as alt
    import pandas as pd
    import numpy as np
    
    x = np.random.normal(size=100)
    y = np.random.normal(size=100)
    
    m = np.random.normal(15, 1, size=100)
    
    source = pd.DataFrame({"x": x, "y":y, "m":m})
    
    # interval selection in the scatter plot
    pts = alt.selection(type="interval", encodings=["x"])
    
    # left panel: scatter plot
    points = alt.Chart().mark_point(filled=True, color="black").encode(
        x='x',
        y='y'
    ).transform_filter(
        pts
    ).properties(
        width=300,
        height=300
    )
    
    # right panel: histogram
    mag = alt.Chart().mark_bar().encode(
        x='mbin:N',
        y="count()",
        color=alt.condition(pts, alt.value("black"), alt.value("lightgray"))
    ).properties(
        width=300,
        height=300
    ).add_selection(pts)
    
    chart = # build the chart:
    alt.hconcat(
        points,
        mag,
        data=source
    ).transform_bin(
        "mbin",
        field="m",
        bin=alt.Bin(maxbins=20)
    )
    
    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])
    
    with tab1:
        st.altair_chart(chart, theme="streamlit", use_container_width=True)
    with tab2:
        st.altair_chart(chart, theme=None, use_container_width=True)

try:
    st.expander("See code").code(inspect.getsource(get_chart_64383))
    get_chart_64383(use_container_width=True)
except Exception as e:
    st.exception(e)

