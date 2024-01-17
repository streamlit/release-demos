import streamlit as st
import time

st.set_page_config("Partial reruns preview", page_icon="⚡")

st.header("Dynamic form - full app only runs on submit")

from utils import show_source
show_source(__file__)

states = {
    "USA": ["", "California", "Washington", "New Jersey"],
    "Canada": ["", "Quebec", "Ontario", "British Columbia"],
    "Germany": ["", "Brandenberg", "Hesse", "Bavaria"]
    }

with st.spinner():
    time.sleep(1)
    st.subheader("Enter your location")

@st.partial
def get_location():
    state = None
    if country := st.selectbox("Country", ["", "USA", "Canada", "Germany"]):
        state = st.selectbox("State", states[country])
    city = st.text_input("City")

    submit_enabled = city and state and country
    if st.button("Submit", type="primary", disabled=not submit_enabled):
        if len(city) < 8:
            st.warning(f"City name {city} must be at least 8 characters")
        else:
            return dict(country=country, state=state, city=city)

if result := get_location():
    st.success("We have recorded your location, thank you!")
    "Response:"
    st.json(result)
