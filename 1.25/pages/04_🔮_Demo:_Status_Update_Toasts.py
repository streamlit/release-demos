import streamlit as st
import time

st.set_page_config(
    page_title='Status Update Toasts',
    page_icon='🔮'
)

st.title("🔮 Status Update Toasts")
st.caption("Toasts indicating progress")

slider_wait_time = st.slider("How Long Should Task Take (Seconds)?", 0, 3, 2)

code_1 = '''
    def stacked_callback_function():
        st.toast("Task Started... Long: Random toast message that is a really really really really really really really long message, going way past the 3 line limit", icon='🚀')
        time.sleep(slider_wait_time)
        st.toast("Task Complete!", icon='🎉')
'''
st.code(code_1, language='python')

def stacked_callback_function():
    st.toast("Task Started... Long: Random toast message that is a really really really really really really really long message, going way past the 3 line limit", icon='🚀')
    time.sleep(slider_wait_time)
    st.toast("Task Complete!", icon='🎉')

st.caption("This button will create a toast on start and another toast on completion")
st.button("Start Task - Stack Toasts", on_click=stacked_callback_function)


code = '''
    def callback_function():
        notification = st.toast("Task Started... Long: Random toast message that is a really really really really really really really long message, going way past the 3 line limit", icon='🚀')
        time.sleep(slider_wait_time)
        notification.toast("Task Complete!", icon='🎉')
'''
st.code(code, language='python')

def callback_function():
    notification = st.toast("Task Started... Long: Random toast message that is a really really really really really really really long message, going way past the 3 line limit", icon='🚀')
    time.sleep(slider_wait_time)
    notification.toast("Task Complete!", icon='🎉')

st.caption("This button will create a toast then update that toast's contents on completion. Note that an update can **only occur on an active toast**. If the toast has been dismissed by the user, or has disappeared automatically (after 4 seconds), no update will occur.")
st.button("Start Task - Update Toast", on_click=callback_function)