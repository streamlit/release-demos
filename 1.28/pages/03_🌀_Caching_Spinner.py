import streamlit as st
import pokebase as pb
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
    
st.set_page_config("Cache Spinner Update Demo", "🌀", layout="wide")
icon("🌀")

st.title("Cache Spinner Update Demo", anchor=False)
st.caption("Enhanced caching spinner prevents UI jumpiness by overlaying, not pushing down, elements.")
st.write("Learn more about caching in [<PLACEHOLDER_OUR_DOCS>](https://docs.streamlit.io/).")
st.divider()

corgi = Image.open("pages/kevin.jpg")
otter = Image.open("pages/sea_otter.png")
duck = Image.open("pages/duck.jpeg")
penguin = Image.open("pages/penguin.jpeg")

def clear_cache():
    st.cache_data.clear()

# tell user what happens when they select the ruler below
st.info("Use the slider to simulate different cache load times. It'll help you see how the enhanced caching spinner behaves.", icon="ℹ️")
cache_load = st.slider("Choose cache function load time:", 0, 30, 10)
st.button("Clear :red[**ALL**] Caches", on_click=clear_cache)
st.divider()

with st.sidebar:
    @st.cache_data
    def fetch_pokemon():
        time.sleep(cache_load)
        random_id = random.randint(1, 251)
        pokemon = pb.pokemon(random_id)
        pokemon_name = pokemon.name
        sprite = pb.SpriteResource('pokemon', random_id, official_artwork=True)
        return pokemon_name.capitalize(), sprite.url
    st.subheader("⚠️ Vital Sidebar Content")
    st.info("The spinner overlays below to prevent UI jumpiness.", icon="🌀")
    st.divider()
    st.write("**Cached Pokemon** :fire:")
    pokemon_name, sprite = fetch_pokemon()
    st.image(sprite, width=150)
    st.caption(f"**{pokemon_name}**")

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


st.subheader("Cache spinners:")
st.info("Notice how the spinner overlays other elements, keeping UI sleek and avoiding jumps.", icon="🔄")
st.write("Rendering a dataframe...")
st.dataframe(render_df())
st.divider()
st.info("A bar chart, also cached. Again, watch for the non-intrusive spinner.", icon="📊")
st.write("Rendering a chart...")
st.bar_chart(render_chart())
st.divider()

st.info("Choose your aquatic pet and see the cached image load smoothly.", icon="🖼️")
st.write("Rendering some images...")
animal = st.radio("Select your aquatic pet:", ["Otter", "Duck", "Penguin"], horizontal=True)

col1, col2 = st.columns(2)

with col1:
    @st.cache_data
    def render_kevin():
        time.sleep(cache_load)
        return corgi

    st.write("**Cached Corgi Cuteness...**")
    st.image(render_kevin())
    st.caption("🚗 Corgi on a Roadtrip")

with col2:
    st.write("**`st.spinner` Cuteness** 🌊")
    if animal == "Duck":
        picture = duck
        caption = "🦆 Baby Duckling"
    elif animal == "Penguin":
        picture = penguin
        caption = "🐧 Little Penguin"
    else:    
        picture = otter
        caption = "🦦 Fluffy Otter"

    with st.spinner("Loading Spinner..."):
        time.sleep(3)
        st.image(picture, use_column_width=True)
        st.caption(caption)
st.divider()

st.info("We're using a regular **st.spinner** for contrast. Notice how it doesn't overlay but instead pushes down other elements? ", icon="⏳")
st.subheader("Using non-cache spinner:")
with st.spinner("`st.spinner` Spinner..."):
    time.sleep(3)

st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")