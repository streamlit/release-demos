import streamlit as st
import validators


VERSION = '.'.join(st.__version__.split('.')[:2])


st.beta_set_page_config(
    page_title=f"New features in Streamlit {VERSION}",
    page_icon=":shark:",  # Pick a fun new emoji for every version.
)


def draw_main_page():
    st.write("""
# Release notes

## New features

- Foo
- Bar

## Notable fixes

- Foo
- Bar

## Callouts

Deprecation Warning: The `st.image` parameter `format` has been renamed to `output_format`

# More info

- As usual, the source code for this app can be found in [Github](#).
- If you'd like to know what _exactly_ went into this release, check out the [commit
diff](https://github.com/streamlit/streamlit/compare/0.64.0...0.65.0).
- We can be found at https://streamlit.io and https://twitter.com/streamlit
- Finally, come by
[the forums](https://discuss.streamlit.io/c/official-announcements/6) if you'd like ask questions,
post awesome apps, or just say hi!
    """)



def draw_foo():
    st.write("# Demo of foo")

    import numpy as np
    arr = np.random.randn(10, 5)
    st.line_chart(arr)


def draw_bar():
    st.write("# Demo of bar")

    st.write("# :smiley:")


demos = {
    "Release notes": draw_main_page,
    "Demo of foo": draw_foo,
    "Demo of bar": draw_bar,
}


# Draw sidebar

# Draw main page


f"""
# Welcome to Streamlit {VERSION}! :wave:

This app is a demo of several :fire: **red-hot** :fire: features that made it into this Streamlit
version.

To get started, choose what you'd like to see below.
"""

"---"

selected_demo = st.radio("Select one", list(demos.keys()))

"---"

demos[selected_demo]()
