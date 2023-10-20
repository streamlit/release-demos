import streamlit as st

VERSION = "1.28"

st.set_page_config(
    page_title=f"New features in Streamlit 1.28",
    page_icon=':memo:',
    initial_sidebar_state="expanded",
    layout="wide",
)

intro = f"""
This release launches [AppTest](https://release128-demo-test.streamlit.app/AppTest), improvements to the [caching spinner](https://release128-demo-test.streamlit.app/Cache_spinner), a handy [data toolbar](https://release128-demo-test.streamlit.app/Dataframe_toolbar), and [`st.connection`](https://release128-demo-test.streamlit.app/st.connection) is no longer experimental – it's fully supported! The release also includes bug fixes. [todo: update links once url changes]
"""

release_notes = f"""
---
**Highlights**

- ✨ Introducing [will be filled in from docs]

**Notable Changes**

- 👻 [will be filled in from docs]

**Other changes**

- 🐛 Bug fix: [will be filled in from docs]
---
"""
# End release updates

def draw_main_page():

    st.title(f"Welcome to Streamlit {VERSION}! :wave:", anchor=False)

    st.write(intro)

    st.write(release_notes)

draw_main_page()
