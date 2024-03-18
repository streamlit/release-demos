import streamlit as st

def show_source(filepath):
    with st.expander("Source Code", expanded=False):
        with open(
            filepath,
            encoding="UTF-8",
        ) as f:
            st.code(f.read(), language="python")
