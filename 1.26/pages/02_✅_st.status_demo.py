import time
import streamlit as st

st.set_page_config(
    page_title='st.status demo',
    page_icon='✅',
    layout="wide"
)

@st.cache_data
def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )


icon(":white_check_mark:")
st.title("Status Panel Demo", anchor=False)

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(
    [
        "Simple run",
        "With label update",
        "Collapse after run",
        "Switch to error",
        "Without context manager",
        "Empty status",
        "Completed status",
        "Uncaught exception",
    ]
)

with tab1:
    st.write("Brief description of what happens when you click 'Run'")
    if st.button("Run", key="tab1"):
        with st.echo(code_location="below"):
            with st.status("Downloading data...", expanded=False):
                st.write("Searching for data...")
                time.sleep(2)
                st.write("Found URL.")
                time.sleep(1)
                st.write("Downloading data...")
                time.sleep(1)
with tab2:
    if st.button("Run", key="tab2"):
        st.write("Brief description of what happens when you click 'Run'")
        with st.echo(code_location="below"):
            with st.status("Downloading data...", expanded=True) as status:
                st.write("Searching for data...")
                time.sleep(2)
                st.write("Found URL.")
                time.sleep(1)
                st.write("Downloading data...")
                time.sleep(2)
                status.update(label="Download successful.")


with tab3:
    if st.button("Run", key="tab3"):
        st.write("Brief description of what happens when you click 'Run'")
        with st.echo(code_location="below"):
            with st.status("Downloading data...", expanded=True) as status:
                st.write("Searching for data...")
                time.sleep(2)
                st.write("Found URL.")
                time.sleep(1)
                st.write("Downloading data...")
                time.sleep(1)
                status.update(label="Download successful.", expanded=False)

with tab4:
    if st.button("Run", key="tab4"):
        st.write("Brief description of what happens when you click 'Run'")
        with st.echo(code_location="below"):
            with st.status("Downloading data...", expanded=True) as status:
                st.write("Searching for data...")
                time.sleep(2)
                st.write("Found URL.")
                time.sleep(1)
                st.write("Downloading data...")
                time.sleep(1)
                status.update(label="Download failed.", state="error")

with tab5:
    if st.button("Run", key="tab5"):
        st.write("Brief description of what happens when you click 'Run'")
        with st.echo(code_location="below"):
            status = st.status("Downloading data...", expanded=True)
            status.write("Searching for data...")
            time.sleep(2)
            status.write("Found URL.")
            time.sleep(1)
            status.write("Downloading data...")
            time.sleep(1)
            status.update(
                label="Download successful.", state="complete", expanded=False
            )
with tab6:
    if st.button("Run", key="tab6"):
        st.write("Brief description of what happens when you click 'Run'")
        with st.echo(code_location="below"):
            st.status("Empty status...")

with tab7:
    if st.button("Run", key="tab7"):
        st.write("Brief description of what happens when you click 'Run'")
        with st.echo(code_location="below"):
            with st.status("Download sucessful.", state="complete", expanded=True):
                st.write("Searching for data...")
                st.write("Found URL.")
                st.write("Downloading data...")

with tab8:
    if st.button("Run", key="tab8"):
        st.write("Brief description of what happens when you click 'Run'")
        with st.echo(code_location="below"):
            with st.status("Downloading data...") as status:
                st.write("Searching for data...")
                time.sleep(2)
                st.write("Found URL.")
                time.sleep(1)
                st.write("Downloading data...")
                raise Exception("Download failed.")
