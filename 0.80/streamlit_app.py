import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

try:
    sys.path.remove(str(parent))
except ValueError: # Already removed
    pass

import streamlit as st
from util.release_helper import create_static_notes

VERSION = '.'.join(st.__version__.split('.')[:2])

from demos.anchors import anchors
from demos.layout_demo import layout_demo

previous_version = "0.79.0"
demo_pages = {
    "Anchor tags": anchors,
    "Bug Fixes: Horizontal Layout": layout_demo
}

st.set_page_config(
    page_title=f"New features in Streamlit {VERSION}"
)

contributors = [
    "nrontsis",
    "sachitv",
    "SimonBiggs",
    "F1nnM",
    "erumoico"
]

intro = f"""
This release launches Secrets Management and Anchor Tags features as well as improvements to Horizontal Layouts 
and several bug fixes.
"""

release_notes = f"""
---
**Features**

- 🔐 Streamlit now support Secrets management for apps deployed to Streamlit Sharing! Check out our blog post(add link)
- ⚓️ Titles and headers now come with automatically generated anchor links

**Other Changes**

- Added `allow-downloads` capability to custom components ([#3040](https://github.com/streamlit/streamlit/issues/3040))
- Fixed a bug which resulted in markdown tables not being rendered correctly with dark theme ([#3020](https://github.com/streamlit/streamlit/issues/3020))
- Fixed a bug where the color picker in the Custom Theme picker did not support click and drag (#2970)
- `st.write` now can render objects which have a `_repr_html_` property ([#1117](https://github.com/streamlit/streamlit/issues/1117))

"""
# End release updates

def draw_main_page():
    st.write(f"""
    # Welcome to Streamlit {VERSION}! 👋
    """)


    st.write(intro)

    st.write(release_notes)

    create_static_notes(contributors, previous_version, VERSION)


# Draw sidebar
pages = list(demo_pages.keys())

if len(pages):
    pages.insert(0, "Release Notes")
    st.sidebar.title(f"Streamlit v{VERSION} Demos")
    selected_demo = st.sidebar.radio("", pages)
else:
    selected_demo = "Release Notes"

# Draw main page
if selected_demo in demo_pages:
    demo_pages[selected_demo]()
else:
    draw_main_page()
