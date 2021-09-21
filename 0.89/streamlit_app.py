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

from demos import hamburger_menu, experimental_cache


previous_version = "0.88.0"
demo_pages = {
    "Hamburger Menu": hamburger_menu.show,
    "Experiemental Cache Primitives": experimental_cache.show,
}

st.set_page_config(page_title=f"New features in Streamlit {VERSION}")

contributors = []

intro = f"""
This release launches `st.metric` 🎉
"""

release_notes = f"""
---
## Highlights

- 💰 Introducing `st.experimental_memo` and `experimental_singleton`, a new primitive for caching! See our blog post
- 🍔 Streamlit allows developers to configure their hamburger menu to be more user-centric

## Notable Changes

- 💅 We updated our UI to a more polished look with a new font.
- 🎨 We now support `theme.base` in the theme object when it's sent to custom components.
- 🧠 We've modified session state to reset widgets if any of their arguments changed even if they provide a key.
    - Some widget behavior may have changed, but we believe this change makes the most sense. We have added a section to our documentation describing how they behave. [link here]

## Other Changes

- 🐞 Bug fixes: Support svgs from a URL ([#3809](https://github.com/streamlit/streamlit/pull/3809)) and that do not start with <svg> tag ([#3789](https://github.com/streamlit/streamlit/pull/3789))
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
    if "page" in query_params and query_params["page"][0] == "headliner":
        idx = 1
    else:
        idx = 0
    selected_demo = st.sidebar.radio("", pages, idx)
else:
    selected_demo = "Release Notes"

# Draw main page
if selected_demo in demo_pages:
    demo_pages[selected_demo]()
else:
    draw_main_page()