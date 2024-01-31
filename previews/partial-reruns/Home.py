import time
import numpy as np
import streamlit as st

st.set_page_config("Partial reruns preview", page_icon="⚡")

st.header("⚡ Partial reruns - Feature preview!")

"""
⚡ **`@st.partial` is a new decorator that turns any function into a Streamlit container that can run independently
of the wider page.** _(Note: We will probably change the name in the final version)_
"""

st.info("**[Install the latest whl](https://github.com/streamlit/release-demos/raw/master/previews/partial-reruns/streamlit-1.30.0-py2.py3-none-any.whl)** to give it a try! 👈", icon="🎮")

"""
Whenever an input widget inside the partial function changes, only the function is rerun. This is the preview app as we
finalize development of the feature. We plan to release it in early spring.

Let us know what you think! Share bugs, public apps examples and what use-cases you hope to build in the
[Streamlit forum post](https://discuss.streamlit.io/t/feature-preview-partial-reruns-share-your-feedback-and-cool-apps/60851).
"""

st.subheader("Simple example")

with st.echo():
    with st.spinner("Doing a slow thing"):
        time.sleep(2)

    st.button("Button in main app triggers a spinner", help="Warning! Slow spinner!")

    @st.partial
    def simple_chart():
        st.write("When you move the slider, only the chart updates, and not the spinner above 👆")
        val = st.slider("Number of bars", 1, 20, 4)
        st.bar_chart(np.random.default_rng().random(val))
    
    simple_chart()

st.subheader("Key scenarios")
"""
This app provides a few key scenarios we think will be interesting with partial reruns:
- Two slow-loading charts with their own controls that run independently
- A dynamic form input that only runs the outer page on submission
- An observability-style chart that streams the latest updates every few seconds
- "Cell" of LLM-generated code in between two st.chat_messages
- Tracking and reporting status of a running job

👈 Take a look at the examples to try it.
"""

st.subheader("Key features")

"""
- When the return value of a partial function changes, the full app is re-run with the new return value. This is
  useful for forms or other scenarios where you might trigger a full re-run based on some event.
    - Note that using `st.rerun()` inside a partial function also triggers a full re-run.
- Periodic rerun / streaming: Use the `run_every` kwarg to automatically rerun the partial function at a specified interval.
  This is great for streaming or polling chart updates, or updating progress on a long-running background task.
"""

with st.expander("👀 More details about `@st.partial` behavior"):
    """
    Very roughly, you can think of partial rerun as an inverse or complement to caching functions.

    :warning: **Note:** Some behavior described here may change in the final released version.
    - When you interact with a widget initialized in a partial function, only the partial function code reruns with the user's new value.
    - A partial can access function arguments as well as any local or global variables on the page, and session state.
    - Arguments and immutable variables will be set to the value at the last function execution during a full rerun.
    - Any updates in global variables or session state persist across partial reruns.
    - Updates to mutable local variables like lists or Streamlit containers (!) are persisted across partial reruns.
    - Each partial function has its own container that is reset for each partial rerun, similar to how pages reset on rerun.
    - Streamlit containers and elements initialized outside the partial function are not reset across partial reruns, even
      if they are modified by the function. If a partial function writes to a container initialized outside itself,
      that container will show the cumulative updates from all partial reruns since the last full rerun.
    """

st.subheader("Known limitations of the preview")

"""
This is a happy-path preview shared for community feedback with some known issues. We will address those
issues before a full release! In particular, interacting with widgets in a partial while the app is already
running can cause execution to stop early, and widgets can behave oddly outside the "main" interaction path. 
"""

with st.expander("Details of limitations"):
    """
    - Interacting with a widget in a partial during the initial page run will cause it to not completely
      load the page
    - Interacting with a widget in partial A while partial B is running will cause B to halt without completing
      (This is especially frequent for pages with `run_every=` set, such as "Streaming chart" and "Multiple partials")
    - In the dynamic form example, some interactions with the selectbox will cause multiple submit buttons to draw
    - In general, interacting with global state or containers created outside the partial function can lead to
      non-intuitive or otherwise unexpected results.
    - Partial functions running can stop some functionality of set_page_config
    - Interactions between caching and st.partial are not well tested

    Let us know what you find as you experiment with the preview!
    """
