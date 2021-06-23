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
    
    if "page" in query_params:
        st.write(query_params["page"])
    if "page" in query_params and query_params["page"][0] == "headliner":
        idx = 1
    else:
        idx = 0
    # TODO: This works right now, but it doesn't work if I set key="pages" here.
    #   The idx above is correct, so doesn't seem like it has to do with query_params,
    #   but rather with session state + the default value for the widget. Is this 
    #   intended behavior or a bug? Could be confusing for users, especially if they 
    #   don't use session state at all (i.e. especially new users). Try this out in a 
    #   smaller example. 
    selected_demo = st.sidebar.radio("", pages, idx)
else:
    selected_demo = "Release Notes"

# Draw main page
if selected_demo in demo_pages:
    demo_pages[selected_demo]()
else:
    draw_main_page()