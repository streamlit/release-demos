import streamlit as st
from streamlit_extras.stylable_container import stylable_container

st.set_page_config(page_icon=":material/local_pizza:")

st.success("We did it!", icon=":material/person_pin:")
if st.button("toast"):
    st.toast("A face", icon=":material/tag_faces:")

def user_message():
    with stylable_container(
        key="user_message",
        css_styles="""
            [data-testid=chatAvatarIcon-custom] {
              background-color: #94d3e6;
              color: #bbbbbb;
              border-color: #000000;
            }
            """,
    ):
        cm = st.chat_message("user", avatar=":material/person_pin:")
    return cm

def assistant_message():
    with stylable_container(
        key="assistant_message",
        css_styles="""
            [data-testid=chatAvatarIcon-custom] {
              background-color: #cccccc;
              color: #ffffff;
              border-color: #000000;
            }
            """,
    ):
        cm = st.chat_message("assistant", avatar=":material/computer:")
    return cm


user_message().markdown("Do you know any jokes?")

with assistant_message():
    st.markdown("Why do scientists darn their socks? \n\nBecause they're socksellent!")

user_message().markdown("LOLOLOL")

st.chat_message("gerald", avatar="user").write("this is gerald")