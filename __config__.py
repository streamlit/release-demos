FEATURES = {
    "Feature Name [beta/experimental]": {
        "docs": "", # String, Optional, Link to docs
        "execute": False, # Boolean, Optional, Whether or not to run the code
        "text":"""
        # insert description here
        """,
        "code":"" # String of code or file name. If file name, must end in .py
    },
    "Example: Inline SVG support for st.image": {
        "execute": True,
        "text":"You can now pass in inline svg as a string!",
        "code":'svg.py',
    },
}

# Any special executions required
def set_page_config():
    import streamlit as st
    st.beta_set_page_config(
        page_title=PAGE_CONFIG["title"],
        page_icon=PAGE_CONFIG["icon"],
        layout=PAGE_CONFIG["layout"],
        initial_sidebar_state=PAGE_CONFIG["sidebar"]
    )
