import streamlit as st

def page1():
    st.markdown("This is a page")

def page2():
    st.markdown("This is another page")
    if st.button("Make a mistake"):
        raise TypeError("Something bad happened")
