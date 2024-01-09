import streamlit as st

def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )
    
st.set_page_config("st.switch_page", "📄", layout="wide")

icon("📄")
st.title("Demo of st.switch_page", anchor=False)

st.divider()

with st.expander("Show code"):
    st.code(
        """
        # List of pages
        pages = {
            "🎡 Scroll container": "./pages/2_🎡_Scroll_container.py",
            "❓ st.query⚊params": "./pages/3_❓_st.query⚊params.py",
            "📄 st.switch⚊pages": "./pages/4_📄_st.switch⚊pages.py",
            "🔗 Link column formatting": "./pages/5_🔗_Link_column_formatting.py"
        }

        st.info('Select page and submit to switch page', icon="👇")
        # Dropdown to select the page
        selected_page = st.selectbox("Select a page:", list(pages.keys()))

        # Button to switch page
        switch_page = st.button("Switch page")
        if switch_page:
            # Switch to the selected page
            page_file = pages[selected_page]
            st.switch_page(page_file)
        """
    )

# List of pages
pages = {
    "🎡 Scroll container": "./pages/2_🎡_Scroll_container.py",
    "❓ st.query⚊params": "./pages/3_❓_st.query⚊params.py",
    "📄 st.switch⚊pages": "./pages/4_📄_st.switch⚊pages.py",
    "🔗 Link column formatting": "./pages/5_🔗_Link_column_formatting.py"
}

st.info('Select page and submit to switch page', icon="👇")
# Dropdown to select the page
selected_page = st.selectbox("Select a page:", list(pages.keys()))

# Button to switch page
switch_page = st.button("Switch page")
if switch_page:
    # Switch to the selected page
    page_file = pages[selected_page]
    st.switch_page(page_file)
