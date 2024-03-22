import time
import numpy as np
import streamlit as st

st.set_page_config("Fragments preview", page_icon="⚡")

st.header("⚡ Fragments - Feature preview!")

"""
⚡ **`@st.experimental_fragment` is a new decorator that turns any function into a "Fragment"
that can run independently of the wider page.**
"""

st.info("**[Install the latest whl](https://github.com/streamlit/release-demos/raw/master/previews/experimental-fragment/streamlit-1.32.2-py2.py3-none-any.whl)** to give it a try! 👈", icon="🎮")

"""
Whenever an input widget inside the fragment changes, only the fragment reruns. This is the preview app as we
finalize development of the feature. We plan to release it in early spring.

Let us know what you think! Share bugs, public apps examples and what use-cases you hope to build in the
[Streamlit forum post](https://discuss.streamlit.io/t/feature-preview-partial-reruns-share-your-feedback-and-cool-apps/60851).
"""

st.subheader("Simple example")

with st.echo():
    with st.spinner("Doing a slow thing"):
        time.sleep(2)

    st.button("Button in main app triggers a spinner", help="Warning! Slow spinner!")

    @st.experimental_fragment
    def simple_chart():
        st.write("When you move the slider, only the chart updates, and not the spinner above 👆")
        val = st.slider("Number of bars", 1, 20, 4)
        st.bar_chart(np.random.default_rng().random(val))
    
    simple_chart()

st.subheader("Key scenarios")
"""
This app provides a few key scenarios we think will be interesting with fragments:
- Two slow-loading charts with their own controls that run independently
- A dynamic form input that only runs the outer page on submission
- An observability-style chart that streams the latest updates every few seconds
- "Cell" of LLM-generated code in between two st.chat_messages
- Tracking and reporting status of a running job

👈 Take a look at the examples to try it.
"""

st.subheader("Key features")

"""
- Periodic rerun / streaming: Use the `run_every` kwarg to automatically rerun the fragment at a specified interval.
  This is great for streaming or polling chart updates, or updating progress on a long-running background task.
- Use `st.rerun()` inside a fragment to trigger a full app re-run. Store values in `st.session_state` to use them
  outside the fragment.
"""

with st.expander("👀 More details about `@st.experimental_fragment` behavior"):
    """
    Very roughly, you can think of fragments as an inverse or complement to caching functions.

    :warning: **Note:** Some behavior described here may change in the final released version.
    - When you interact with a widget initialized in a fragment, only the fragment code reruns with the user's new value.
    - A fragment can access function arguments as well as any local or global variables on the page, and session state.
    - Arguments and immutable variables will be set to the value at the last function execution during a full rerun.
    - Any updates in global variables or session state persist across fragment reruns.
    - Updates to mutable local variables like lists or Streamlit containers (!) are persisted across fragment reruns.
    - Each fragment runs in its own container that IS reset for each fragment rerun, similar to how pages reset on rerun.
    - Streamlit containers and elements initialized outside the fragment are not reset across fragment reruns, even
      if they are modified by the function. If a fragment function writes to a container initialized outside itself,
      that container will show the cumulative updates from all fragment reruns since the last full rerun.
    """

st.subheader("Known limitations of the preview")

"""
Critical and commonly encountered issues have been fixed, however we are aware of some remaining edge cases.
If you find other unexpected behavior while playing with the whl file, please let us know!
"""

with st.expander("Details of limitations"):
    """
    - If you use a callback that draws elements to the main container from inside a fragment, it will unexpectedly
      overwrite elements outside the fragment.
    - In general, interacting with global state or containers created outside the fragment function can lead to
      non-intuitive or otherwise unexpected results.
    - Interactions between caching and st.experimental_fragment are not well tested

    Let us know what you find as you experiment with the preview!
    """
