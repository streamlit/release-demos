import streamlit as st

def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )
    
st.set_page_config("st.query_params", "❓", layout="wide")

icon("❓")
st.title("Demo of st.query_params", anchor=False)

st.divider()

"""
#### Instructions:
To see the Urchin Tracking Module (UTM) source printed on this page:
1. Append `?utm_source=YourSource` to the URL, where `YourSource` is the desired UTM source, like `LinkedIn`, `Facebook`, `Instagram`, `Discord`, etc.
2. For example, use `https://release130.streamlit.app?utm_source=LinkedIn`.
3. Press Enter to reload the page with the UTM parameter.

**What is a UTM Source?**

- UTM parameters are used in URLs to track the effectiveness of online marketing campaigns across traffic sources and publishing media. 

- The UTM source parameter (`utm_source`) identifies which site sent the traffic, and is a common tool in digital marketing analytics.
"""

st.divider()

with st.expander("Show code"):
    st.code(
        """
        # Get the current query parameters
        params = st.query_params
        utm_source = params.get('utm_source', None) 

        if utm_source:
            st.markdown(f"**UTM Source**: {utm_source}")
        else:
            st.warning("UTM Source not found in URL.", icon="⚠️")
        """
    )
# Get the current query parameters
params = st.query_params

utm_source = params.get('utm_source', None) 

if utm_source:
    st.markdown(f"**UTM Source**: {utm_source}")
else:
    st.warning("UTM Source not found in URL.", icon="⚠️")
