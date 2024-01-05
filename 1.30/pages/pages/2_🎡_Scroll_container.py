import streamlit as st

def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )
    
st.set_page_config("Demo of scroll container", "", layout="wide")

icon("🎡")
st.title("Scroll container", anchor=False)

st.divider()

if "num_elements" not in st.session_state:
    st.session_state.num_elements = 0

col1, col2 = st.columns(2)

col1.write("👇 **This container has normal scrolling**")
with col1.container(height=250):
    for i in range(st.session_state.num_elements):
        st.write(f"Element {i}")

col2.write("👇 **Container with pinned to bottom scrolling**")
with col2.container(height=250):
    st.chat_message("assistant")
    for i in range(st.session_state.num_elements):
        st.chat_message("user").write(f"Message {i}")

if st.button("Add element", use_container_width=True):
    st.session_state.num_elements += 1
