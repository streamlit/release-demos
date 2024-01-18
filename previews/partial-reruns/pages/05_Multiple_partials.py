import datetime
import random
import time

import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config("Partial reruns preview", page_icon="⚡")

np.random.seed(0)
random.seed(0)

chart_data_1 = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
chart_data_2 = pd.DataFrame(
    np.random.randn(50, 4), columns=["col 1", "col 2", "col 3", "col 4"]
)


if "reruns" not in st.session_state:
    st.session_state.reruns = 0

st.session_state.reruns += 1

st.button("Button in main script")

with st.spinner("Doing some heavy work in the main script..."):
    time.sleep(3)


@st.partial
def interactive_form():
    st.caption(
        "Interacting with any of the elements in this partial will only rerun the code of this partial."
    )
    # Changes to the selectbox only "reruns" the group function and its widgets
    option = st.selectbox("How would you like to be contacted?", ("Email", "Phone"))
    contact_info = st.text_input(f"Enter {option}")

    if st.button("Submit"):
        st.success(f"Contact data ({option}: {contact_info}) submitted successfully!")


@st.partial
def chart_filtering(data: pd.DataFrame):
    time.sleep(1)
    st.caption(
        "Interacting with any of the elements in this partial will only rerun the code of this partial."
    )
    # filter chart_data columns via a multiselect widget:
    columns = st.multiselect("Select columns", data.columns.tolist())
    st.line_chart(data if not columns else data[columns])


@st.partial(run_every=5)
def stream_data():
    rng = np.random.default_rng()
    chart_data = pd.DataFrame(rng.random((20, 3)), columns=["a", "b", "c"])
    columns = st.multiselect("Select columns", chart_data.columns.tolist(), key="foo")
    st.bar_chart(chart_data if not columns else chart_data[columns])
    st.caption(f"Last updated {datetime.datetime.now()}")


# cache_data doesn't seem to work right now resulting in: TypeError: cannot pickle '_thread.RLock' object
@st.cache_resource
def transform_data():
    return chart_data_1.to_csv().encode("utf-8")


@st.partial
def improved_download_button():
    st.download_button(
        label="Download data as CSV",
        data=transform_data(),
        file_name="large_df.csv",
        mime="text/csv",
    )


with st.expander("Chart filtering 1 with partial rerun", expanded=True):
    with st.spinner("Crunching data..."):
        time.sleep(1)
    chart_filtering(chart_data_1)

with st.expander("Chart filtering 2 with partial rerun", expanded=True):
    with st.spinner("Crunching data..."):
        time.sleep(1)
    chart_filtering(chart_data_2)

with st.expander("Interactive form with partial rerun", expanded=True):
    interactive_form()

with st.expander("Streaming chart with partial rerun", expanded=True):
    stream_data()

# with st.expander("Download button that doesn't require full rerun", expanded=True):
#     improved_download_button()

other_input = st.text_input(f"Input in main script")
st.write(f"Reruns of main script: {st.session_state.reruns}")
