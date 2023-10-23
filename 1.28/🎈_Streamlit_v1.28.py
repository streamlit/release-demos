import streamlit as st

VERSION = "1.28"

st.set_page_config(
    page_title=f"New features in Streamlit 1.28",
    page_icon=':memo:',
    initial_sidebar_state="expanded",
    layout="wide",
)

intro = f"""
This release launches a new `Unit testing for Apps` feature, and includes bug fixes and improvements.
"""

release_notes = f"""
---
**Highlights**

- ✨ Introducing 

**Notable Changes**

- 👻 

**Other changes**

- 🐛 Bug fix:
---
"""
# End release updates

def draw_main_page():

    st.title(f"Welcome to Streamlit {VERSION}! :wave:", anchor=False)

    st.caption(intro)

    st.write(release_notes)

draw_main_page()