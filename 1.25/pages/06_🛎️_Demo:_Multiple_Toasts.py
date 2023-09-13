import streamlit as st
import random

st.set_page_config(
    page_title='Multiple Toasts',
    page_icon='🛎️'
)

st.title("🛎️ Multiple Toasts")
st.caption("Multiple Toasts can be displayed as part of a process. This demonstrates the stacking behavior with most recent at the bottom right.")
toasts = st.slider("How Many Toasts to Trigger?", 0, 5, 3)
def callback_function():
    toast_icons = ['ℹ️', '✅', '⚠️', '🚨', '🐶', '🐱', "🐯", '🐰', '🦊']
    toast_messages = ["Short: This is a toast message!", "Long: Random toast message that is a really really really really really really really long message, going way past the 3 line limit"]
    for i in range(toasts):
        emoji = random.choice(toast_icons)
        text = random.choice(toast_messages)
        st.toast(f"Toast {i+1} of {toasts}: {text}", icon=emoji)

st.button("Stack Toasts", on_click=callback_function)