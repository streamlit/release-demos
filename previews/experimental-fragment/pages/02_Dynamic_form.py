import streamlit as st
import time

st.set_page_config("st.fragment", page_icon="⚡")

st.header("Dynamic form - full app only runs on submit")

from utils import show_source
show_source(__file__)

states = {
    "USA": ["", "California", "Washington", "New Jersey"],
    "Canada": ["", "Quebec", "Ontario", "British Columbia"],
    "Germany": ["", "Brandenberg", "Hesse", "Bavaria"]
    }

with st.spinner():
    time.sleep(1.5)

@st.fragment
def get_location():
    with st.container(border=True):
        st.subheader("Enter your location")
        st.info("""Fill out the form below. **Unlike** a regular Streamlit form, this form updates dynamically!
            But **like** a regular form, the outer page and spinner only runs after a successful submit.
            """)

        state = None
        country = st.selectbox("Country", ["", "USA", "Canada", "Germany"])
        if country:
            state = st.selectbox("State", states[country])
        city = st.text_input("City")

        submit_enabled = city and state and country
        if st.button("Submit", type="primary", disabled=not submit_enabled):
            if len(city) < 8:
                st.warning(f"City name {city} must be at least 8 characters")
            else:
                st.session_state.new_location = dict(country=country, state=state, city=city)
                st.rerun()

get_location()

if "new_location" in st.session_state:
    result = st.session_state.pop("new_location")
    st.success("We have recorded your location, thank you!")
    "Response:"
    st.json(result)
