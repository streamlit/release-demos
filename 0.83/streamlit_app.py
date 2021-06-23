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

previous_version = "0.82.0"
demo_pages = {
    "Session State": session_state.show,
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
    # TODO: This doesn't work yet. Locally it actually works, but on Streamlit Sharing
    #   it doesn't somehow. The query params are actually read and parsed correctly,
    #   but it doesn't manage to set the index based on it. Seems to be a weird
    #   interaction between the widget value in session state and value given in arg.
    #   See if this is fixed in final session state version.
    st.write(query_params)
    if "page" in query_params:
        st.write(query_params["page"])
    if "page" in query_params and query_params["page"][0] == "headliner":
        index = 1
    else:
        index = 0
    selected_demo = st.sidebar.radio("", pages, index, key="pages")
else:
    selected_demo = "Release Notes"

# Draw main page
if selected_demo in demo_pages:
    demo_pages[selected_demo]()
else:
    draw_main_page()