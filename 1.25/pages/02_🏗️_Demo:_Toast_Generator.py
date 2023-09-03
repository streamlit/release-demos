import streamlit as st

st.set_page_config(
    page_title='Toast Generator',
    page_icon='🏗️'
)

st.title('🏗️ Toast Generator')
st.caption("Create a toast by selecting the icon & body.")
icon = st.selectbox('What icon would you like to use?', (None, 'ℹ️', '✅', '⚠️', '🚨', '🐶', '🐱', "🐯", '🐰', '🦊',), index=0)
message = st.radio("Default toast messages:", ("Short: This is a toast message!", "Long: Random toast message that is a really really really really really really really really really long message, going way past the 3 line limit", "Valid Markdown: **Bold**, *Italics*, ~Strike~, `Code` [Link](www.example.com) :red[Colored text]"), index=0)
text = st.text_area('Or... enter a custom message below:', placeholder="Toast text here", height=100)

if st.button("Generate Toast :tada:"):
    message = text if text else message
    st.toast(message, icon=icon)