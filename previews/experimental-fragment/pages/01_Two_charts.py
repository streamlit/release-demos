import streamlit as st
import pandas as pd
import time

st.set_page_config("st.experimental_fragment", page_icon="⚡", layout="wide")

st.header("Two independent charts with their own inputs")
st.caption("Each graph filter update loads independently. This makes interactions much faster compared to re-running everything.")

from utils import show_source
show_source(__file__)

color_vals = {"Purple": "#800080", "Green": "#219e21", "Blue": "#0000FF"}
color = color_vals[st.selectbox("Line color", color_vals.keys())]

app_df = pd.DataFrame([[1, 1, 1], [2, 2, 2], [3, 3, 2], [4, 4, 2], [5, 5, 3]], columns=["day", "apps", "external_apps"])
meetup_df = pd.DataFrame([[1, 4], [2, 3], [3, 5], [4, 2], [5, 4], [6, 3], [7, 4]], columns=["month", "meetups"])
col1, col2 = st.columns(2)

@st.experimental_fragment
def app_chart():
    st.subheader("App count")
    st.caption("This chart always takes 3 seconds to load")
    time.sleep(3)
    exclude = st.checkbox("Exclude internal apps")
    y = "apps" if not exclude else "external_apps"
    st.line_chart(app_df, x="day", y=y, color=color)

with col1:
    app_chart()

@st.experimental_fragment
def meetup_chart():
    st.subheader("Developer meetups")
    st.caption("This chart always takes 1 seconds to load")
    time.sleep(1)
    first, last = st.slider("Month filter", 1, 7, (1, 7), label_visibility="collapsed")
    filtered_df = meetup_df[(meetup_df["month"] >= first) & (meetup_df["month"] <= last)]
    st.bar_chart(filtered_df, x="month", y="meetups", color=color)

with col2:
    meetup_chart()
