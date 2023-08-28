import time
import streamlit as st

st.set_page_config(
    page_title='st.status demo',
    page_icon='✅',
    layout="wide"
)

st.title(":white_check_mark: Status Panel Demo", anchor=False)

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
    st.info("This tab demonstrates a basic use case of the `st.status` widget. Click 'Run' to initiate a data download operation, displayed without any status label updates.",
            icon="💡")
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
    st.info("This tab showcases the `st.status` widget with a dynamic label update. Click 'Run' to initiate a data download operation; the status label will update upon successful completion.",
            icon="💡")
    if st.button("Run", key="tab2"):
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
    st.info("This tab demonstrates the functionality of `st.status` to collapse upon task completion. Click 'Run' to initiate a data download; the status widget will collapse after successful download.",
            icon="💡")
    if st.button("Run", key="tab3"):
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
    st.info("This tab illustrates how the `st.status` widget handles errors. Click 'Run' to initiate a data download. The status label will switch to an error state if the download fails.",
            icon="💡")
    if st.button("Run", key="tab4"):
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
    st.info("This tab demonstrates the use of `st.status` without a context manager. Click 'Run' to initiate a data download operation. The widget will function as expected even without a context manager.",
            icon="💡")
    if st.button("Run", key="tab5"):
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
    st.info("This tab displays an `st.status` widget without a label or state. Click 'Run' to view an empty status widget.",  icon="💡")
    if st.button("Run", key="tab6"):
        with st.echo(code_location="below"):
            st.status("Empty status...")

with tab7:
    st.info("This tab shows how the `st.status` widget displays a 'complete' state. Click 'Run' to initiate a data download operation. The status will indicate completion when the task is done.",
            icon="💡")
    if st.button("Run", key="tab7"):
        with st.echo(code_location="below"):
            with st.status("Download sucessful.", state="complete", expanded=True):
                st.write("Searching for data...")
                st.write("Found URL.")
                st.write("Downloading data...")

with tab8:
    st.info("This tab demonstrates how the `st.status` widget reacts to uncaught exceptions. Click 'Run' to initiate a data download operation. An exception will be thrown, affecting the status widget.",
            icon="💡")
    if st.button("Run", key="tab8"):
        with st.echo(code_location="below"):
            with st.status("Downloading data...") as status:
                st.write("Searching for data...")
                time.sleep(2)
                st.write("Found URL.")
                time.sleep(1)
                st.write("Downloading data...")
                raise Exception("Download failed.")
