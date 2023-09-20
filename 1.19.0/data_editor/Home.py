import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(layout="centered", page_title="Data Editor", page_icon="🧮")


@st.cache_data
def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )


icon(":partying_face:")
st.title("You're in!")

st.markdown(
    "Welcome! EduX just unveiled the marvelous 🧮 **st.data_pathway** in its latest 1.19"
    " release. Student pathways... except it's more: it's editable! Students can"
    " now discuss and edit their pathway catered to their needs. Let's get started."
)

st.markdown(
    "Our algorithm is constantly calculating your best schedule seen ("
    " [here](https://www.edux.ai/faq)) to demonstrate our"
    " calculation process!"
)

show = st.button("View your degree path!")
if show:
    switch_page("demo: clipboard")

st.markdown(
    """
Read more in our documentation section :smiley: [EduX Docs](https://www.edux.ai/docs)!
"""
)
