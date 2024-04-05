import streamlit as st

def page2():
    st.title("Page 2")
    st.markdown("Here's a second page")

def page3():
    st.title("Page 3")
    st.markdown("Here's a third page")

def home():
    st.title("Home")
    st.markdown("Welcome to my awesome app")

pg = st.navigation({
    "Main": [st.Page(home, title="Home", default=True)],
    "Pages": [st.Page(page2), st.Page(page3)]
})

pg.run()