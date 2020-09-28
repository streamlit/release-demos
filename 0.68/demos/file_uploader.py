import streamlit as st
import os
import io

def file_uploader():
    st.write(
        """
        # File Uploader

        Since the release of our initial file uploader, we've gotten great feedback
        culminating in this redesigned file uploader.

        1. Multiple file uploads
        2. File metadata
        -----
        """
    )

    with st.echo("below"):
        single_file = st.file_uploader("Single File Uploader")

        if single_file:
            file_container = st.expander(single_file.name)
            file_container.write(single_file.getvalue())

        multiple_files = st.file_uploader("Multiple File Uploader")
        if multiple_files:
            for file in multiple_files:
                file_container = st.expander(file.name)
                file_container.write(file.getvalue())
