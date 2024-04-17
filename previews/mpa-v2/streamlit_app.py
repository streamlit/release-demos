import streamlit as st
import pathlib

CURRENT_DIR = pathlib.Path(__file__).parent.resolve()

def page2():
    st.markdown("You can add core metrics here.")

def page3():
    st.markdown("Here's a third page. This one throws an error which is caught in the main script.")
    raise TypeError("This page has the wrong type")

def north_star():
    st.info("**[Install the latest whl](https://github.com/streamlit/release-demos/raw/master/previews/mpa-v2/streamlit-1.33.0-py2.py3-none-any.whl)** to give it a try! 👈", icon="🎮")

    st.markdown("""
    Using the new API, when you do `streamlit run streamlit_app.py`, the contents of streamlit_app.py will automatically run before every page instead of defining the home page. Any common code can go here.

    - **Dynamic navigation API:** A new API called `st.navigation()` with `st.Page()` to programmatically define the available pages of your app. This means the available and displayed pages can change in a given session / rerun!
    - **Write common code once:** Besides defining your pages / nav, you can also add any common session setup code, authorization check, page_config, styles, etc only once in this file.
    - **Native logos and icons:** use `st.logo()` to add an app logo at the top left, add text headings between page groups in the native navigation, and (limited) support for Material icons in addition to emojis.

    Let us know what you think! Share bugs, public apps examples and what use-cases you hope to build in the
    [Streamlit forum post](https://discuss.streamlit.io/t/coming-soon-multi-page-apps-improved-api-and-new-navigation-ui-features/65679).
                
    The navigation for this app is copied below. **View the [full source code here](https://github.com/streamlit/release-demos/blob/master/previews/mpa-v2/streamlit_app.py).**
    """)

    st.code("""
            pg = st.navigation({
                "Overview": [
                    # Load pages from functions
                    st.Page(north_star, title="Home", default=True, icon=":material/home:"),
                    st.Page(north_star, title="North Star", icon=":material/star_border:"),
                    ],
                "Metrics": [
                    st.Page(page2, title="Core Metrics", icon=":material/hourglass_top:"),
                    # You can also load pages from files, as usual
                    st.Page("movies.py", title="Movie Explorer", icon=":material/movie_filter:"),
                    st.Page(page3, title="App statuses over time", icon=":material/access_time:"),
                    st.Page(page3, title="Cloud apps leaderboard", icon=":material/share:"),
                    ],
            })
            pg.run()
            """)

st.logo(str(CURRENT_DIR / "logo.png"), url="https://www.snowflake.com", collapsed_version=str(CURRENT_DIR / "logo_small.png"))

if "logged_in" not in st.session_state:
    st.write("Welcome to the new Multi-Page Apps demo. You'll need to log in to continue.")
    if st.button("Log in"):
        st.session_state.logged_in = True
        st.rerun()
    else:
        def empty_page():
            pass
        pg = st.navigation([st.Page(empty_page, title="Streamlit Multi-Page V2")], position="hidden")
        pg.run()
        st.stop()

st.header("📖 Multi-Page Apps V2: Preview Demo")

"""
**Streamlit Multi-page apps V2 provides a new way to define multi-page Streamlit apps and some new features coming for the side navigation.**
"""

with st.sidebar:
  st.subheader("Having fun yet?")
  st.slider("Amount of fun", 0, 1000, 450, key="slide")
  st.radio("Your thoughts", ["I agree", "I disagree"], key="radio")
  st.text_input("Thoughts", placeholder="Add your thoughts", label_visibility="collapsed")
  st.button("Submit")
  if st.button("Logout"):
      del st.session_state["logged_in"]
      st.rerun()

pg = st.navigation({
    "Overview": [
        # Load pages from functions
        st.Page(north_star, title="Home", default=True, icon=":material/home:"),
        st.Page(north_star, title="North Star", icon=":material/star_border:"),
        ],
    "Metrics": [
        st.Page(page2, title="Core Metrics", icon=":material/hourglass_top:"),
        # You can also load pages from files, as usual
        st.Page("movies.py", title="Movie Explorer", icon=":material/movie_filter:"),
        st.Page(page3, title="App statuses over time", icon=":material/access_time:"),
        st.Page(page3, title="Cloud apps leaderboard", icon=":material/share:"),
        ],
})


try:
    pg.run()
except Exception as e:
   st.error(f"Something went wrong: {str(e)}", icon=":material/error:")