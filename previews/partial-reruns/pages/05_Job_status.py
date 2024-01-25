import datetime
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config("Partial reruns preview", page_icon="⚡")

st.header("Job status")
st.caption("Trigger a job and see progress updates until it completes")

from utils import show_source
show_source(__file__)

def get_job_status():
    status_vals = [20, 40, 60, 80, "complete"]
    if "status_idx" not in st.session_state:
        st.session_state.status_idx = 0
    else:
        st.session_state.status_idx += 1
    return status_vals[st.session_state.status_idx]

@st.partial(run_every=2)
def check_job_status():
    status = get_job_status()
    if status == "complete":
        st.session_state.job_status = "complete"
        st.rerun()
    st.progress(status, "Job status")
    st.caption(f"Last updated {datetime.datetime.now()}")

if st.session_state.get("job_status") == "complete":
    st.success("Job succeeded!", icon="🎉")
    st.session_state.job_status = "stopped"
    del st.session_state["status_idx"]

if st.button("Trigger the job") or st.session_state.get("job_status") == "running":
    st.session_state.job_status = "running"
    check_job_status()
