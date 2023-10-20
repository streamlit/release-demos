import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time
import random
import base64

def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )

@st.cache_data
def get_file_url(path):
    file_ = open(path, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    return data_url

@st.cache_data
def retrieve_corgi_image():
    time.sleep(cache_load)
    return corgi
    
st.set_page_config("Improved cache spinner demo", "🌀", layout="wide")
icon("🌀")
cache_load = 20
def clear_cache():
    st.cache_data.clear()
    
st.title("Improved cache spinner demo", anchor=False)
# col_a, col_b = st.columns([1, 2])
# with col_b:
st.info("""If you've used `st.cache_data` or `st.cache_resource`, you've probably noticed the spinner displayed in your UI in the event of a "cache miss" when your cached function runs. We've made **visual improvements** to this spinner – it is now overlayed on top of existing UI elements, preventing jumpiness and visual glitches.""")
# with col_a:
#     file_url = get_file_url('1.28/pages/spinner.gif')
#     st.markdown(
#         f'<img src="data:image/gif;base64,{file_url}" width=200 alt="demo gif">',
#         unsafe_allow_html=True,
#     )
#     st.button("Show me the spinners!", on_click=clear_cache)

corgi = Image.open("1.28/pages/kevin.jpg")
# col_a, col_b, col_c = st.columns(3)
# with col_b:
# st.button("Show me the spinners!", on_click=clear_cache)

col1, col2 = st.columns(2)
with col1:
    st.header("Old spinner")
    st.button("Show me the spinners!", on_click=clear_cache)
    st.write("This spinner displaces the image.")
    with st.spinner("Pushes the corgi down ⬇️"):
        time.sleep(3)
    st.image(corgi)
with col2:
    st.header("New and improved spinner")
    st.text("")
    st.write("This spinner is overlayed on top of the image or any visual element. The improved spinner is smaller and does not push widgets down, creating a smoother UI.")
    st.image(retrieve_corgi_image())
