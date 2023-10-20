import streamlit as st
# import pokebase as pb
import pandas as pd
import numpy as np
from PIL import Image
import time
import random

def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )
    
st.set_page_config("Improved cache spinner demo", "🌀", layout="wide")
icon("🌀")
cache_load = 15

st.title("Improved cache spinner demo", anchor=False)
st.info("""If you've used `st.cache_data` or `st.cache_resource`, you've probably noticed the spinner displayed in your UI in the event of a "cache miss" when your cached function runs. We've made **visual improvements** to this spinner – it is now overlayed on top of existing UI elements, preventing jumpiness and visual glitches.""")

def clear_cache():
    st.cache_data.clear()

corgi = Image.open("1.28/pages/kevin.jpg")
col_a, col_b, col_c = st.columns(3)
with col_b:
    st.button("Show me the spinners", on_click=clear_cache)

col1, col2 = st.columns(2)

@st.cache_data
def render_df():
    df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
    time.sleep(cache_load)
    return df

@st.cache_data
def render_chart():
    df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
    time.sleep(cache_load)
    return df

with col1:
    st.header("Old spinner")
    st.write("This spinner displaces the image.")
    with st.spinner("Pushes the corgi down ⬇️"):
        time.sleep(3)
    st.image(corgi)
with col2:
    st.header("New and improved spinner")
    st.write("This spinner is overlayed on top of the image, rather than pushing it down.")

    @st.cache_data
    def retrieve_corgi_image():
        time.sleep(cache_load)
        return corgi
    st.image(retrieve_corgi_image())
    # st.caption("🚗 Corgi on a Roadtrip")
# tell user what happens when they select the ruler below
# st.info("Use the slider to simulate different cache load times. It'll help you see how the enhanced caching spinner behaves.", icon="ℹ️")
# cache_load = st.slider("Choose cache function load time:", 0, 30, 10)



