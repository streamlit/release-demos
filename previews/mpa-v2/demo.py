import streamlit as st

def page2():
    #st.title("Page 2")
    st.markdown("Here's a second page")

def page3():
    #st.title("Page 3")
    st.markdown("Here's a third page")
    raise TypeError("This page has the wrong type")

def north_star():
    #st.title("North Star")
    st.markdown("Welcome to my awesome app")

st.logo("logo.png", url="https://www.snowflake.com", collapsed_version="logo_small.png")
st.html("""
  <style>
    [data-testid=stSidebarNavLink] {
      color: rgba(49, 51, 63, 0.6);
    }
    [data-testid=stSidebarNavLink]:hover {
      color: rgba(49, 51, 63, 0.6);
    }
  </style>
""")

if "logged_in" not in st.session_state:
    st.write("You'll need to log in to continue.")
    if st.button("Log in"):
        st.session_state.logged_in = True
        st.rerun()
    else:
        st.stop()

with st.sidebar:
  st.subheader("Having fun yet?")
  st.slider("Amount of fun", 0, 1000, 450)
  st.radio("Your thoughts", ["I agree", "I disagree"])
  st.text_input("Thoughts", placeholder="Add your thoughts", label_visibility="collapsed")
  st.button("Submit")
  if st.button("Logout"):
      del st.session_state["logged_in"]
      st.rerun()

st.title('📊 Interactive Data Explorer')

with st.expander('About this app'):
  st.markdown('**What can this app do?**')
  st.info('This app shows the use of Pandas for data wrangling, Altair for chart creation and editable dataframe for data interaction.')
  st.markdown('**How to use the app?**')
  st.warning('To engage with the app, 1. Select genres of your interest in the drop-down selection box and then 2. Select the year duration from the slider widget. As a result, this should generate an updated editable DataFrame and line plot.')


pg = st.navigation({
    "Overview": [
        st.Page(north_star, title="Home", default=True, icon=":material/home:"),
        st.Page(north_star, title="North Star", icon=":material/star_border:"),
        ],
    "Metrics": [
        st.Page(page2, title="Core Metrics", icon=":material/hourglass_top:"),
        st.Page("movies.py", title="Movie Explorer", icon=":material/movie_filter:"),
        st.Page(page3, title="App statuses over time", icon=":material/access_time:"),
        st.Page(page3, title="Cloud apps leaderboard", icon=":material/share:"),
        ],
})


try:
    pg.run()
except Exception as e:
   st.error(f"Something went wrong: {str(e)}", icon=":material/error:")