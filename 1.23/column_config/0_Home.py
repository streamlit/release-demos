import streamlit as st

st.set_page_config(
    layout="centered", page_title="Column config demo app", page_icon="⚙️"
)


def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )


icon("⚙️")

"""
# Column config demo

Streamlit just launched column config in 1.23! This feature allows you to customize the
columns of `st.dataframe` and `st.data_editor` to behave and look like you want.

👈  Check out one of the demos in the sidebar or read the [blog post]().
"""
