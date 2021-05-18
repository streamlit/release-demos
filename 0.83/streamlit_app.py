import sys
from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

try:
    sys.path.remove(str(parent))
except ValueError:  # Already removed
    pass

import streamlit as st
from util.release_helper import create_static_notes

VERSION = ".".join(st.__version__.split(".")[:2])

from demos import session_state
from demos import fake

previous_version = "0.82.0"
demo_pages = {
    # "Session State": session_state.show,
    "Fake": fake.show
}

st.set_page_config(page_title=f"New features in Streamlit {VERSION}")

contributors = []

intro = f"""
This release launches ...
"""

release_notes = f"""
---
**Highlights**

- foo

**Other changes**

- bar

"""
# End release updates


def draw_main_page():
    st.write(
        f"""
        # Welcome to Streamlit {VERSION}! 👋
        """
    )

    st.write(intro)

    st.write(release_notes)

    create_static_notes(contributors, previous_version, VERSION)


# Draw sidebar
pages = list(demo_pages.keys())

if len(pages):
    pages.insert(0, "Release Notes")
    st.sidebar.title(f"Streamlit v{VERSION} Demos")
    query_params = st.experimental_get_query_params()
    st.write(query_params)
    if "page" in query_params and query_params["page"][0] == "forms_demo":
        st.write("shortcut")
        page_index = 1
    else:
        page_index = 0
    st.write(page_index)

    st.sidebar.radio(
        "", ["option 1", "option 2", "option 3"], index=page_index, key="radio123"
    )
    selected_demo = st.sidebar.radio("", pages, page_index)
else:
    selected_demo = "Release Notes"

# Draw main page
if selected_demo in demo_pages:
    demo_pages[selected_demo]()
else:
    draw_main_page()