import streamlit as st
import os
import io

def expander():
    st.write(
        """
        # Clean things up with expanders

        Now that we've maximized horizontal space, try st.beta_expander,
        to maximize your vertical space! Some of you may have been using
        `st.checkbox` for this before, and expander is a prettier, more
        performant replacement 🙂

        -----
        """
    )

    # with st.echo("below"):
    filters = st.beta_expander("Search and Filter", expanded=True)
    filter1, filter2, filter3 = filters.beta_columns((4, 2, 1))

    filter1.text_input("Search")
    filter2.selectbox(
        "By Author",
        ["", "domoritz", "tanmaylaud", "cclauss", "kinghuang", "matthiasgoergens", "1wpro2"]
    )
    filter3.selectbox("Sort by", ["", "Name", "Newest", "Oldest"])
