import time
import numpy as np
import streamlit as st

st.set_page_config("st.experimental_fragment", page_icon="⚡")

st.header("⚡ Introducing Streamlit fragments!")

"""
⚡ **`@st.experimental_fragment` is a new decorator that turns any function into a "fragment"
that can run independently of the wider page.**

Whenever an input widget inside the fragment changes, only the fragment reruns. This app introduces
the feature and some common use cases.

- 🎮 Try it yourself: `pip install streamlit>=1.33`
- 📖 Check out the [docs article](https://docs.streamlit.io/develop/concepts/architecture/fragments)
  and [API reference](https://docs.streamlit.io/develop/api-reference/execution-flow/st.fragment)
  for more details.
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
