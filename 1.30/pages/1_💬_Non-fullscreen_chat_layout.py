import streamlit as st

def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )
    
st.set_page_config("Non-fullscreen chat layout", "💬", layout="wide")

icon("💬")
st.title("Non-fullscreen chat layout", anchor=False)


def create_chat(state_key: str, chat_container, position="inline"):
    if state_key not in st.session_state:
        st.session_state[state_key] = []

    for message in st.session_state[state_key]:
        with chat_container.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input(
        "Chat with me", key=f"{state_key}_input", position=position
    ):
        # Display user message in chat message container
        chat_container.chat_message("user").markdown(prompt)
        st.session_state[state_key].append({"role": "user", "content": prompt})

        chat_container.chat_message("assistant").markdown(f"Echo: {prompt}")
        st.session_state[state_key].append(
            {"role": "assistant", "content": f"Echo: {prompt}"}
        )


st.write("**Chat in scrolling container**")
chat_container_1 = st.container(height=250)
create_chat("chat_1", chat_container_1)

st.divider()

st.write("**Chat in expander**")
with st.expander("Chat"):
    chat_container_2 = st.container(height=350)
    create_chat("chat_2", chat_container_2)

with st.sidebar:
    st.write("**Chat in sidebar**")
    chat_container_3 = st.container(height=350)
    create_chat("chat_3", chat_container_3)
