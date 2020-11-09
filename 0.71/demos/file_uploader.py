import streamlit as st
import pandas as pd

def file_uploader():
    st.write(
        """
        # File Uploader: Automatically reset file buffer

        In the original file uploader, we were creating a new buffer for you each
        time we reran. As part of the new file uploader, we optimized and are
        now returning the same buffer on rerun. Unfortunately, file buffer
        positions do not automatically reset. This was not obvious to users based
        on the error message.

        To make it easy for our users, we are now automatically resetting the
        file buffers returned from `st.file_uploader` on rerun.

        -----

        ### Example
        """
    )

    with st.echo("below"):
        # Changing slider after uploading a file will trigger a re-run.
        value = st.slider('Drag to trigger a rerun', 0, 100)

        file = st.file_uploader('Upload CSV', type="csv")
        if file:
            df = pd.read_csv(file)
            st.write(df.head())
