PAGE_CONFIG = {
    "title": "Streamlit Releasing v0.65!",
    "icon": "🌟",
    "layout": "wide",
    "sidebar":"collapsed"
}

FEATURES = {
    "Page Configurations [beta]": {
        "docs": 'url',
        "text":"""
Now you can configure your page. Current options include:
- Page title: Text displayed by your browser tab
- Page icon: Icon displayed by your browser tab
- Layout: Choose between wide or centered layout mode
- Initial Sidebar State: Collapse or expand the sidebar by default
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
        "text":"We have added to our experimental namespace the ability to get and set query parameters. With these query params, you can bookmark or share your app in various states. Thanks [@zhaoooyue](https://github.com/zhaoooyue) for the contribution!",
        "code":'''
radio_list = ['Eat', 'Sleep', 'Both']
query_params = st.experimental_get_query_params()
# Query parameters are returned as a list to support multiselect.
# Get the first item in the list if the query parameter exists.
default = int(query_params["activity"][0]) if "activity" in query_params else 0
activity = st.radio(
    "What are you doing at home during quarantine?",
    radio_list,
    index = default
)
if activity:
    st.experimental_set_query_params(activity=radio_list.index(activity))
        ''',
    },
    "Improved Dataframe Support": {
        "text":"""
With 0.65, there is additional support for pandas dataframes. These components can now take in a panda dataframe as a list of options:
- `st.radio`
- `st.multiselect`
- `st.selectbox`
        """,
        "code":'''
options = pd.DataFrame({'Options': ['radio', 'multiselect', 'selectbox']})
st.write("Input", options)

st.radio("Dataframe as input for radio buttons", options)
st.multiselect("Dataframe as input for multiselect", options)
st.selectbox("Dataframe as input for selectbox", options)
        ''',
    },
    "New st.stop API": {
        "docs":"TODO",
        "text":"With 0.65, we now offer the ability to stop code execution immediately with `st.stop`. This functionality can be used to handle conditional cases",
        "code":'''
name = st.text_input('Name')
if not name:
    st.warning('Please input a name to see sample code.')
    st.stop()
st.success('Thank you for inputting a name.')
        ''',
    },
    "Inline SVG support for st.image": {
        "text":"You can now pass in inline svg as a string!",
        "code":'''
svg = """<svg width="40" height="40" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg">
  <circle id="svg_1" r="15" cy="20" cx="20" fill="yellow"/>
</svg>"""
st.image(svg)
        ''',
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
