import streamlit as st
import random

st.set_page_config(
    page_title='Sidebar Toasts',
    page_icon='⤵️'
)

# Content for the main page
st.title("⤵️ Sidebar Toasts")
st.caption("See the sidebar for toasts triggered from the sidebar!")

st.sidebar.caption("Toasts triggered from the sidebar")

def sidebar_callback():
    toast_index = [0, 1, 2, 3]
    toast_messages = ["This is a toast triggered from the sidebar", "Short: This is a toast message!", "Long: Random toast message that is a really really really really really really really long message, going way past the 3 line limit"]
    for i in toast_index:
        text = random.choice(toast_messages)
        st.toast(f"{i+1} of 4: {text}", icon='⬅️')

st.sidebar.write("Toast triggered using `st.toast` in a callback from sidebar:")
st.sidebar.button("✔️ Sidebar Toast", type="secondary", on_click=sidebar_callback)

def with_sidebar_callback():
    toast_index = [0, 1, 2, 3]
    toast_messages = ["This is a toast triggered using `with st.sidebar`", "Short: This is a toast message!", "Long: Random toast message that is a really really really really really really really long message, going way past the 3 line limit"]
    for i in toast_index:
        text = random.choice(toast_messages)
        st.toast(f"{i+1} of 4: {text}", icon='⬅️')

with st.sidebar:
    st.write("Toast triggered under `with st.sidebar` notation:")
    st.button("🙃 More sidebar toasts", on_click=with_sidebar_callback)

def on_sidebar_callback():
    toast_message = "This is a toast triggered directly **ON** st.sidebar"
    st.sidebar.toast(toast_message, icon='⬅️')

st.sidebar.write("Using `st.sidebar.toast` throws an :red[Error]:")
st.sidebar.button(":x: Toast called **ON** Sidebar", on_click=on_sidebar_callback)