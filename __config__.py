PAGE_CONFIG = {
    "title": "Streamlit Releasing v0.65!",
    "icon": "🌟",
    "layout": "wide",
    "sidebar":"collapsed"
}

FEATURES = {
    "Page Configurations [beta]": {
        "docs": 'https://docs.streamlit.io/en/stable/api.html#streamlit.beta_set_page_config',
        "execute": False,
        "text":"""
In Streamlit 0.65, you can now configure your page with the current options:
- Page title: Text displayed by your browser tab
- Page icon: Icon displayed by your browser tab
- Layout: Choose between wide or centered layout mode
- Initial Sidebar State: Collapse or expand the sidebar by default

Note: This feature is currently in beta and subject to change.
""",
        "code":'''
st.beta_set_page_config(
    page_title="{0}",
    page_icon="{1}",
    layout="{2}",
    initial_sidebar_state="{3}"
)
'''.format(PAGE_CONFIG["title"], PAGE_CONFIG["icon"], PAGE_CONFIG["layout"], PAGE_CONFIG["sidebar"]),
    },
    "Query Params [experimental]": {
        "execute": True,
        "text":"We have added to our experimental namespace the ability to get and set query parameters. With these query params, you can bookmark or share your app in various states. Thanks [@zhaoooyue](https://github.com/zhaoooyue) for the contribution!",
        "code":'query_params.py',
    },
    "Improved Dataframe Support": {
        "text":"""
With 0.65, there is additional support for pandas dataframes. These components can now take in a panda dataframe as a list of options:
- `st.radio`
- `st.multiselect`
- `st.selectbox`
        """,
        "code":'dataframe.py',
    },
    "New st.stop API": {
        "docs":"https://docs.streamlit.io/en/stable/api.html#streamlit.stop",
        "execute": True,
        "text":"With 0.65, we now offer the ability to stop code execution immediately with `st.stop`. This functionality can be used to handle conditional cases",
        "code":'stop.py',
    },
    "Inline SVG support for st.image": {
        "execute": True,
        "text":"You can now pass in inline svg as a string!",
        "code":'svg.py',
    },
}

def set_page_config():
    import streamlit as st
    st.beta_set_page_config(
        page_title=PAGE_CONFIG["title"],
        page_icon=PAGE_CONFIG["icon"],
        layout=PAGE_CONFIG["layout"],
        initial_sidebar_state=PAGE_CONFIG["sidebar"]
    )
