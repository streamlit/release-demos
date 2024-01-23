import time
import numpy as np
import streamlit as st

st.set_page_config("Partial reruns preview", page_icon="⚡")

st.header("⚡ Introducing partial reruns!")

"""
⚡ **`@st.partial` is a new decorator that turns any function into a Streamlit container that can run independently
of the wider page.** _(Note: We will probably change the name in the final version)_

Whenever an input widget inside the partial function changes, only the function is rerun.
"""

st.info("**[Install the latest whl](https://github.com/streamlit/release-demos/raw/master/previews/partial-reruns/streamlit-1.30.0-py2.py3-none-any.whl)** to give it a try! 👈", icon="🎮")


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
