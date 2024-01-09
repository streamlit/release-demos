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
To see the UTM source printed on this page from query params:
1. Append `?utm_source=LinkedIn` (or your desired UTM source like X, Instagram, Discord,..) to the URL.
2. For example, use `https://release130.streamlit.app?utm_source=LinkedIn`.
3. Hit **Enter** to see the UTM source printed below.
"""

st.divider()

# Get the current query parameters
params = st.query_params

utm_source = params.get('utm_source', None) 

if utm_source:
    st.markdown(f"**UTM Source**: {utm_source}")
else:
    st.warning("UTM Source not found in URL.", icon="⚠️")
