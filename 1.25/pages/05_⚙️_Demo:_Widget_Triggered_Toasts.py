import streamlit as st

st.set_page_config(
    page_title='Widget Triggered Toasts',
    page_icon='⚙️'
)

st.title(":gear: Widget Triggered Toasts")
st.caption("Try triggering toasts using the widgets below")

st.write("**Buttons:**")

code = '''
if st.button("🙃 Welcome Toast", type="primary"):
    st.toast("Welcome to the Toast Demo App", icon="🍞")
'''
st.code(code, language='python')

if st.button("🙃 Welcome Toast", type="primary"):
    st.toast("Welcome to the Toast Demo App", icon="🍞")

code_1 = '''
if st.button(":rainbow: Toasts with Markdown"):
    st.toast('Random **Success** toast with `code` and [link](www.example.com)!', icon='✅')
    st.toast('Random *Warning* toast with `code` and [link](www.example.com)!', icon='⚠️')
    st.toast('Random ~Error~ toast with `code` and [link](www.example.com)!', icon='🚨')
'''
st.code(code_1, language='python')

if st.button(":rainbow: Toasts with Markdown"):
    st.toast('Random **Success** toast with `code` and [link](www.example.com)!', icon='✅')
    st.toast('Random *Warning* toast with `code` and [link](www.example.com)!', icon='⚠️')
    st.toast('Random ~Error~ toast with `code` and [link](www.example.com)!', icon='🚨')


# st.write("**Checkbox:**")
# checked = st.checkbox("Agree to terms and conditions :thumbsup:")
# if checked:
#     st.toast("Thanks for agreeing to our terms and conditions!", icon='✅')

st.write("**File Uploader:**")

code_2 = '''
uploaded_file = st.file_uploader("Choose a file", type="py")
if uploaded_file:
    st.toast("File Uploaded", icon='📄')
'''
st.code(code_2, language='python')

uploaded_file = st.file_uploader("Choose a file", type="py")
if uploaded_file:
    st.toast("File Uploaded", icon='📄')