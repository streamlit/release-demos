import streamlit as st
import os
import io

def container():
    st.write(
        """
        # Adding a new concept: containers!

        st.beta_container is a building block that helps you organize your app.
        Just like `st.empty`, `st.beta_container` lets you set aside some space, and
        then later write things to it out of order. But while subsequent calls to
        the same `st.empty` replace the item inside it, subsequent calls to the
        same `st.beta_container` append to it. This works just like the
        `st.sidebar` you've come to know and love.

        -----
        """
    )

    with st.echo("below"):
        container = st.beta_container()
        st.write("I am not in a container 😢")
        container.write("I will show up on top in the container despite being added later")
        container.write("I'm in the container too but I won't replace what's there 🤗")
