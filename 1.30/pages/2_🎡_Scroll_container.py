import streamlit as st
import requests
from PIL import Image
from io import BytesIO

def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )

def get_image(index):
    """Fetches an image from Unsplash (or another free service)"""
    url = f"https://source.unsplash.com/random/400x300?sig={index}"
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

st.set_page_config("Demo of scroll container", "", layout="wide")

icon("🎡")
st.title("Scroll container", anchor=False)

st.divider()

if "num_elements" not in st.session_state:
    st.session_state.num_elements = 0

st.info("Click on **`Add image`** to add more images within the container and scroll to view the images", icon="👇")
with st.expander("Show code"):
    st.code(
        """
        if "num_elements" not in st.session_state:
            st.session_state.num_elements = 0

        with st.container(height=500):
            for i in range(st.session_state.num_elements):
                col1, col2, col3 = st.columns([1.3, 2, 1])
                # Displaying the image in the middle column
                with col2:
                    col2.image(get_image(i), caption=f"Image {i}", width=600)

        if st.button("Add image", use_container_width=True):
            st.session_state.num_elements += 1
        """
    )
with st.container(height=500):
    for i in range(st.session_state.num_elements):
        # Creating three columns
        col1, col2, col3 = st.columns([1.3,2,1])

        # Displaying the image in the middle column
        with col2:
            col2.image(get_image(i), caption=f"Image {i}", width=600)

if st.button("Add image", use_container_width=True):
    st.session_state.num_elements += 1
