import datetime
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config("Fragments preview", page_icon="⚡")

st.header("Streaming chart")
st.caption("Every few seconds, the chart is updated with the latest (random) data using `run_every=`. The app only runs during the updates.")

from utils import show_source
show_source(__file__)

np.random.seed(0)
rng = np.random.default_rng()
if st.button("Reset streaming") or "chart_data" not in st.session_state:
    st.session_state.chart_data = pd.DataFrame(rng.random((20, 3)), columns=["a", "b", "c"])

@st.experimental_fragment(run_every=2)
def generate_chart():
    rng = np.random.default_rng()
    new_data = pd.DataFrame(rng.random((2, 3)), columns=["a", "b", "c"])
    st.session_state.chart_data = pd.concat([st.session_state.chart_data, new_data], ignore_index=True)
    chart_data = st.session_state.chart_data
    columns = st.multiselect("Select columns", chart_data.columns.tolist())
    st.bar_chart(chart_data if not columns else chart_data[columns])
    st.caption(f"Last updated {datetime.datetime.now()}")

with st.container():
    generate_chart()
