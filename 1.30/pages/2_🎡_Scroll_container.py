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

@st.cache_data
def load_image(url):
    """Load an image from a URL and cache it."""
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

# URLs of the images
cat_images_urls = [
    "https://raw.githubusercontent.com/streamlit/release-demos/master/1.30/images/cats/alex-nicolopoulos-hxn2HjZHyQE-unsplash.jpg",
    "https://raw.githubusercontent.com/streamlit/release-demos/master/1.30/images/cats/amber-kipp-75715CVEJhI-unsplash.jpg",
    "https://raw.githubusercontent.com/streamlit/release-demos/master/1.30/images/cats/daria-shatova-46TvM-BVrRI-unsplash.jpg",
    "https://raw.githubusercontent.com/streamlit/release-demos/master/1.30/images/cats/jae-park-7GX5aICb5i4-unsplash.jpg",
    "https://raw.githubusercontent.com/streamlit/release-demos/master/1.30/images/cats/modcatshop-pdALzg0yN-8-unsplash.jpg",
    "https://raw.githubusercontent.com/streamlit/release-demos/master/1.30/images/cats/the-lucky-neko-2JcixB1Ky3I-unsplash.jpg"
]

pups_images_urls = [
    "https://raw.githubusercontent.com/streamlit/release-demos/master/1.30/images/pups/andrew-wagner-4RmkomQYkXk-unsplash.jpg",
    "https://raw.githubusercontent.com/streamlit/release-demos/master/1.30/images/pups/arjan-stalpers-8-sgismcDAQ-unsplash.jpg",
    "https://raw.githubusercontent.com/streamlit/release-demos/master/1.30/images/pups/fatty-corgi-1QsQRkxnU6I-unsplash.jpg",
    "https://raw.githubusercontent.com/streamlit/release-demos/master/1.30/images/pups/hendo-wang-DsGeUBaJPwc-unsplash.jpg",
    "https://raw.githubusercontent.com/streamlit/release-demos/master/1.30/images/pups/stephanie-cook-0yHhzZi2wPI-unsplash.jpg",
    "https://raw.githubusercontent.com/streamlit/release-demos/master/1.30/images/pups/xuan-nguyen-zr0beNrnvgQ-unsplash.jpg"
]

def get_images(image_urls):
    return [load_image(url) for url in image_urls]

st.set_page_config("Demo of scroll container", "", layout="wide")

icon("🎡")
st.title("Scroll container", anchor=False)

st.divider()

# General attribution for all images
st.info(
    """
    All images are sourced from [Unsplash](https://unsplash.com/). 
    Unsplash images are freely usable under their [licensing terms](https://unsplash.com/license).
    """, icon="📸")



col1, col2 = st.columns(2)

with col1:
    st.subheader("Scroll container", anchor=False)
    with st.expander("Show code"):
        st.code(
            """
            cat_images = get_images(cat_images_urls)
            with st.container(height=600): # set the height of the container
                for img in cat_images:
                    st.image(img, use_column_width=True)
            """
        )
    cat_images = get_images(cat_images_urls)
    with st.container(height=600):
        for img in cat_images:
            st.image(img, use_column_width=True)

with col2:
    st.subheader("Non-scroll container", anchor=False)
    with st.expander("Show code"):
        st.code(
                """
                pup_images = get_images(pups_images_urls)
                with st.container():
                    for img in pup_images:
                        st.image(img, use_column_width=True)
                """
            )
    pup_images = get_images(pups_images_urls)
    with st.container():
        for img in pup_images:
            st.image(img, use_column_width=True)

