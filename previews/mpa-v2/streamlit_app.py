import streamlit as st
import pathlib

CURRENT_DIR = pathlib.Path(__file__).parent.resolve()

st.logo(str(CURRENT_DIR / "logo.png"), link="https://www.snowflake.com", icon_image=str(CURRENT_DIR / "logo_small.png"))

### Only define login once, no pages available until login ###

if st.query_params.get("test_more_pages", False):
    st.session_state.logged_in = True

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

### Common elements which are on every page after login ###

st.header("📖 Multi-Page Apps V2: Demo")

"""
**Streamlit Multi-page apps V2 provides a new way to define multi-page Streamlit apps and some new features for the side navigation.**
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


### Add pages as functions (can also point to separate files) ###

def page2():
    st.markdown("You can add core metrics here.")

def page3():
    st.markdown("Here's a third page. This one throws an error which is caught in the main script.")
    raise TypeError("This page has the wrong type")

def north_star():
    st.info("**Install Streamlit 1.36** to give it a try! 👈", icon="🎮")

    st.markdown("""
    Using the new API, when you do `streamlit run streamlit_app.py`, the contents of streamlit_app.py will automatically run before every page instead of defining the home page. Any common code can go here.

    - **Dynamic navigation API:** A new API called `st.navigation()` with `st.Page()` to programmatically define the available pages of your app. This means the available and displayed pages can change in a given session / rerun!
    - **Write common code once:** Besides defining your pages / nav, you can also add any common session setup code, authorization check, page_config, styles, etc only once in this file.
    - **Native logos and icons:** use `st.logo()` to add an app logo at the top left, add text headings between page groups in the native navigation, and (limited) support for Material icons in addition to emojis.

    Let us know what you think! Share bugs, public apps examples and what use-cases you build in the
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


def page4():
    @st.experimental_dialog("Input")
    def get_input():
        st.session_state.input = st.text_input("Some input")
        if st.button("Submit"):
            st.rerun()

    if st.button("Add input"):
        get_input()

    if input := st.session_state.get("input"):
        st.write(f"Welcome, {input}")

# Define the main navigation

pg = st.navigation({
    "Overview": [
        # Load pages from functions
        st.Page(north_star, title="Home", default=True, icon=":material/home:", url_path=""),
        st.Page(north_star, title="North Star", icon=":material/star_border:", url_path="north_star2"),
        ],
    "Metrics": [
        st.Page(page2, title="Core Metrics", icon=":material/hourglass_top:"),
        # You can also load pages from files, as usual
        st.Page("movies.py", title="Movie Explorer", icon=":material/movie_filter:"),
        st.Page(page3, title="App statuses over time", icon=":material/access_time:"),
        st.Page(page3, title="Cloud apps leaderboard", icon=":material/share:", url_path="cloud_apps_leaderboard"),
        st.Page(page4, title="Dialogs", icon=":material/feedback:"),
        ],
})


try:
    pg.run()
except Exception as e:
   st.error(f"Something went wrong: {str(e)}", icon=":material/error:")
