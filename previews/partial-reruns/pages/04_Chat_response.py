import re
import time
import streamlit as st

st.set_page_config("Partial reruns preview", page_icon="⚡")

st.header("Chat response cell")

from utils import show_source
show_source(__file__)

def get_response(messages):
        return """Sure, you can run the code below
```python
import streamlit as st
import pandas as pd

app_df = pd.DataFrame([[1, 1, 1], [2, 2, 2], [3, 3, 2], [4, 4, 2], [5, 5, 3]], columns=["day", "apps", "external_apps"])
exclude = st.checkbox("Exclude internal apps")
y = "apps" if not exclude else "external_apps"
st.line_chart(app_df, x="day", y=y)
```
"""

@st.partial
def parse_and_exec(response):
    code_match = re.search(r"```python\n(.*)\n```", response, re.DOTALL)
    if code_match:
        code = code_match.group(1)
        exec(code)

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
    parse_and_exec(msg["content"])

if prompt := st.chat_input(placeholder="Draw a simple line chart"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = get_response(messages=st.session_state.messages)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
         st.write("Thinking...")
         time.sleep(0.5)
         st.write(response)
    parse_and_exec(response)
