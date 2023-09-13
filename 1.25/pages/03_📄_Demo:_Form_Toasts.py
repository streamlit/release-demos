import streamlit as st

st.set_page_config(
    page_title='Form Toasts',
    page_icon='📄'
)

st.title("📄 Form Toasts")
st.caption("Different toasts based on form submission (try changing the frequency of the email from Daily to Weekly)")
code = '''
    with st.form("my_form"):
        st.write("**Email Signup:**")
        st.radio("How did you hear about us?", ('Online', 'Friends', 'Other'))
        selected = st.selectbox('How frequently would you like to be emailed? 📧', ('Daily', 'Weekly', 'Monthly'), index=0)
        submitted = st.form_submit_button("Submit", type="primary")
        if submitted and selected == 'Daily':
            st.toast(f'Form submit **SUCCESS** - look forward to hearing from us **{selected}**!', icon='✅')
        if submitted and selected != 'Daily':
            st.toast("**Form Submitted** - don't forget you can always change your preferences later, for example updating your email contact frequency to receive the latest and greatest content", icon='✅')
'''
st.code(code, language='python')

with st.form("my_form"):
    st.write("**Email Signup:**")
    st.radio("How did you hear about us?", ('Online', 'Friends', 'Other'))
    selected = st.selectbox('How frequently would you like to be emailed? 📧', ('Daily', 'Weekly', 'Monthly'), index=0)
    submitted = st.form_submit_button("Submit", type="primary")
    if submitted and selected == 'Daily':
        st.toast(f'Form submit **SUCCESS** - look forward to hearing from us **{selected}**!', icon='✅')
    if submitted and selected != 'Daily':
        st.toast("**Form Submitted** - don't forget you can always change your preferences later, for example updating your email contact frequency to receive the latest and greatest content", icon='✅')
    