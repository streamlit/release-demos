import streamlit as st

st.set_page_config(
    page_title='st.link_button demo',
    page_icon='🔗',
    layout="wide"
)

st.title("🔗 Link Button Demo", anchor=False)
st.write("Learn more about `st.link_button` in [our docs](https://docs.streamlit.io/library/api-reference/widgets/st.link_button).")

st.info("Click the button below to explore the Streamlit gallery in a new tab.", icon="💡")

st.link_button("Go to gallery", "https://streamlit.io/gallery")

st.code(
    """
    # Code to create the link button
    st.link_button("Go to gallery", "https://streamlit.io/gallery")
    """
)
