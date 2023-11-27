import streamlit as st
from PIL import Image
import base64

@st.cache_data
def get_file_url(path):
    file_ = open(path, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    return data_url

def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )
    
st.set_page_config("Demos", "🚀", layout="wide")

icon("🚀")
st.title("v1.29 Feature Demos", anchor=False)

# Border Demo
st.header("🔲 Customizable border")
st.caption("You can now add or remove border around `st.container` and `st.form`!")

before, after = st.columns(2)
with before:
    st.subheader("Old non-customizable borders")
    st.caption("⬇️ `st.container` does not have the border parameter ")
    with st.container():
        st.markdown("This is inside a container without border")
        st.dataframe(data={"col1": [1, 2], "col2": [3, 4]}, use_container_width=True)
        st.button("Do something", use_container_width=True)
    st.code(
        """
        with st.container():
            st.info("This is inside a container without border")
            st.dataframe(data={"col1": [1, 2], "col2": [3, 4]}, use_container_width=True)
            st.button("Do something", use_container_width=True)
        """
    )

    st.caption("⬇️ `st.form` does not have the border parameter ")
    with st.form(key="my_form"):
        st.markdown("This is inside a form with border")
        st.dataframe(data={"col1": [1, 2], "col2": [3, 4]}, use_container_width=True)
        st.form_submit_button(label="Submit", help="Help text")
    st.code(
        """
        with st.form(key="my_form"):
            st.info("This is inside a form with border")
            st.dataframe(data={"col1": [1, 2], "col2": [3, 4]}, use_container_width=True)
            st.form_submit_button(label="Submit", help="Help text")
        """
    )

with after:
    st.subheader("New customizable borders")
    st.caption("⬇️ New `st.container` has border parameter ")
    st.warning("[CODE BELOW WILL BE EXECUTED DURING THE NEXT NIGHTLY RELEASE ON 27TH NOV.]")
    st.markdown("[CONTAINER WITH BORDER WILL GO HERE]")
    st.code("""
    with st.container(border=True):
        st.info("This is inside a container with border")
        st.dataframe(data={"col1": [1, 2], "col2": [3, 4]}, use_container_width=True)
        st.button("Do something", use_container_width=True)
    """)
    st.markdown("[FORM WITHOUT BORDER WILL GO HERE]")
    st.caption("⬇️ New `st.form` has border parameter ")
    st.code("""
    with st.form(key="my_form", border=False):
        st.info("This is inside a form without border")
        st.dataframe(data={"col1": [1, 2], "col2": [3, 4]}, use_container_width=True)
        st.form_submit_button(label="Submit", help="Help text")
    """)

st.divider()

# App skeleton Demo
st.header("🦴 App skeleton")
st.caption("When loading a Streamlit app URL, the ':blue[Please wait...]' message is now replaced by a gray pulsating app skeleton!")

skeleton_url = get_file_url("/mount/src/release-demos/1.29/pages/skeleton.gif")

gif1, gif2 = st.columns(2)
with gif1:
    st.subheader("Old loading message")
    st.caption("Upon reload, the page shows :blue[Please wait...]")
    st.markdown(
        f'<img src="data:image/gif;base64,{skeleton_url}" width=450 alt="demo gif">',
        unsafe_allow_html=True,
    )

with gif2:
    st.subheader("New loading behavior")
    st.caption("The new update shows the app skeleton ")
    st.warning("[A SIMILAR GIF TO THE ONE ON THE RIGHT WILL GO HERE WITH THE UPDATED BEHAVIOR]")
    st.markdown("[GIF HERE]")
    st.info('Refresh your browser to see the new update in action', icon="💡")

st.divider()

# Anchor Demo
st.header("🔗 Improved anchor button")
st.caption("Streamlit headers have anchors on the left side which overlaps other elements. This new change moves it to the right side of the header.")

anchor = Image.open("/mount/src/release-demos/1.29/pages/anchor_img.png")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Anchor on the left")
    st.caption("Behavior before the update")
    st.image(anchor)
with col2:
    st.subheader("New and updated anchor on the right")
    st.caption("Hover over the header to interact with the new changes")
    from datetime import datetime

    with st.container():
        st.header('Chart Timeframe Selection')
        timeframe = st.radio(
            "Select timeframe:",
            ('All', 'Last 28 days', 'Quarter to date (QTD)', 'Year to date (YTD)')
        )
        start_date, end_date = st.date_input(
            "Enter a date range",
            value=(datetime(2019, 12, 1), datetime(2023, 7, 27)),
            min_value=datetime(2000, 1, 1),
            max_value=datetime.today()
        )
        st.warning("[HEADER ABOVE WILL UPDATE ON MONDAY TO HAVE ANCHOR ON THE RIGHT SIDE]")
