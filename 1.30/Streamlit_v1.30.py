import streamlit as st

VERSION = "1.30"

st.set_page_config(
    page_title=f"New features in Streamlit 1.30",
    page_icon=':memo:',
    initial_sidebar_state="expanded",
    layout="wide",
)


def draw_main_page():

    st.title(f"Welcome to Streamlit {VERSION}! :wave:", anchor=False)

draw_main_page()
