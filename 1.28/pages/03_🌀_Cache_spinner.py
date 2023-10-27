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
def retrieve_corgi_image():
    time.sleep(cache_load)
    return corgi
    
st.set_page_config("Improved cache spinner demo", "🌀", layout="wide")
icon("🌀")
cache_load = 20
def clear_cache():
    st.cache_data.clear()
    
st.title("Improved cache spinner demo", anchor=False)
st.write("""When using st.cache_data or st.cache_resource, the cache spinner is now overlayed on top of existing UI elements. This prevents jumpiness and visual glitches!""")

corgi = Image.open("/mount/src/release-demos/1.28/pages/kevin.jpg")
st.button("Show me the spinners!", on_click=clear_cache)

col1, col2 = st.columns(2)
with col1:
    st.header("Old spinner")
    st.write("This spinner displaces the image, pushing the corgi downward ⬇️")
    with st.spinner("Old spinner"):
        time.sleep(3)
    st.image(corgi)
with col2:
    st.header("New and improved spinner")
    st.write("The improved spinner is smaller and overlayed on top of the image.") 
    st.image(retrieve_corgi_image())
