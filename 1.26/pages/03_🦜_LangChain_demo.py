import streamlit as st
from langchain.agents import AgentExecutor, ConversationalChatAgent
from langchain.callbacks import StreamlitCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.memory.chat_message_histories import StreamlitChatMessageHistory
from langchain.tools import DuckDuckGoSearchRun

st.write("Add a brief description of the functionality demonstrated on this page here")

@st.cache_data
def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )


def initialize_page():
    st.set_page_config(
        page_title="LangChain: Chat with search", 
        page_icon="🦜",
        layout="wide"
    )
    icon(":parrot:")
    st.title("LangChain: Chat with search", anchor=False)

def handle_messages(messages, steps):
    avatars = {"human": "user", "ai": "assistant"}
    for idx, msg in enumerate(messages):
        with st.chat_message(avatars[msg.type]):
            # Render intermediate steps if any were saved
            for step in steps.get(str(idx), []):
                if step[0].tool == "_Exception":
                    continue
                with st.status(f"**{step[0].tool}**: {step[0].tool_input}", state="complete"):
                    st.write(step[0].log)
                    st.write(f"{step[1]}")
            st.write(msg.content)

def get_prompt():
    return st.chat_input(placeholder="Who won the Women's U.S. Open in 2018?")

def handle_chat(prompt, openai_api_key, msgs, memory):
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo", 
        openai_api_key=openai_api_key, 
        streaming=True)
    tools = [DuckDuckGoSearchRun(name="Search")]
    chat_agent = ConversationalChatAgent.from_llm_and_tools(llm=llm, tools=tools)
    executor = AgentExecutor.from_agent_and_tools(
        agent=chat_agent,
        tools=tools,
        memory=memory,
        return_intermediate_steps=True,
        handle_parsing_errors=True,
    )
    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(
            st.container(), 
            expand_new_thoughts=False, 
            collapse_completed_thoughts=False)
        response = executor(prompt, callbacks=[st_cb])
        st.write(response["output"])
        return response["intermediate_steps"]

# Initializing the app
initialize_page()
openai_api_key = st.secrets['OPENAI_API_KEY']
msgs = StreamlitChatMessageHistory()
memory = ConversationBufferMemory(
    chat_memory=msgs, 
    return_messages=True, 
    memory_key="chat_history", 
    output_key="output")

if len(msgs.messages) == 0 or st.sidebar.button("Reset chat history"):
    msgs.clear()
    msgs.add_ai_message("How can I help you?")
    st.session_state.steps = {}

handle_messages(msgs.messages, st.session_state.steps)
prompt = get_prompt()

if prompt:
    st.chat_message("user").write(prompt)
    st.session_state.steps[str(len(msgs.messages) - 1)] = handle_chat(prompt, openai_api_key, msgs, memory)
