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

from demos.forms_demo import forms_demo

previous_version = "0.80.0"
demo_pages = {"st.form": forms_demo}

st.set_page_config(page_title=f"New features in Streamlit {VERSION}")

contributors = ["RedFrez", "brendalf", "SimonBiggs", "bensodenkamp", "mgilbir"]

intro = f"""
This release launches the form containers and caption features as well as bug fixes and improvements.
"""

release_notes = f"""
---
**Highlights**

- 📝 Introducing `st.form` and `st.form_submit_button` which allow for the creation of forms and submit button to batch submit input widgets.
- 🔤 Introducing `st.caption` : A convenience API for for adding small text.
- 🎨 Updates to Theming which allow for editing themes from a base theme configuration
- 🚀 Improvements to deployment experience to Streamlit Sharing from the app menu

**Other changes**

- Support for binary files in Custom Components ([#3144](https://github.com/streamlit/streamlit/pull/3144))

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
    if "page" in query_params and query_params["page"][0] == "forms_demo":
        index = 1
    else:
        index = 0
    selected_demo = st.sidebar.radio("", pages, index)
else:
    selected_demo = "Release Notes"

# Draw main page
if selected_demo in demo_pages:
    demo_pages[selected_demo]()
else:
    draw_main_page()
