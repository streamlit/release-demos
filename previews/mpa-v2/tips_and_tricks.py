import streamlit as st

def page1():
    st.markdown("This is a page")

def page2():
    st.markdown("This is another page")
    if st.button("Make a mistake"):
        raise TypeError("Something bad happened")


pg = st.navigation([st.Page(page1), st.Page(page2)])

st.set_page_config(
        # Add a prefix to the browser tab title
        page_title=f"My App: {pg.title}",
        # Update the layout for only certain pages
        layout="wide" if pg.url_path == "page2" else "centered",
    )

# Hide the Streamlit "running man" on all pages
st.sidebar.html(
    """
    <style>
    [data-testid="stStatusWidget"] {
            visibility: hidden;
            height: 0%;
            position: fixed;
        }
    </style>
    """,
)

custom_error_handling = st.sidebar.toggle("Custom error handling")

# Wrap all pages in try / except for "global" exception handling
try:
    pg.run()
except Exception as e:
    if custom_error_handling:
        st.error(f"Oops, something funny happened with a {type(e).__name__}", icon="😿")
        st.image("https://media1.tenor.com/m/t7_iTN0iYekAAAAd/sad-sad-cat.gif")
    else:
        raise e
