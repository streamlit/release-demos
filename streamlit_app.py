import streamlit as st
import validators

from __config__ import FEATURES, set_page_config

__VERSION__ = "0.65.0"

st.sidebar.header("New features in {0}".format(__VERSION__))
feature = st.sidebar.radio(
    "",
    [*FEATURES]
)

# st.sidebar.header("Notable Bug fixes")
# st.sidebar.markdown("")

st.sidebar.header("Callouts")
st.sidebar.markdown("""
Deprecation Warning: The `st.image` parameter `format` has been renamed to `output_format`
""")

st.sidebar.markdown("----")
st.sidebar.markdown("""
Check out our
[github](https://github.com/streamlit/streamlit/compare/0.64.0...0.65.0)
to see the full list of changes or join us on our
[forum](https://discuss.streamlit.io/c/official-announcements/6) for any discussions!
""")

st.header("Introducing {0}".format(feature))
st.write(FEATURES[feature]["text"])
if ("docs" in FEATURES[feature]):
    st.write("See our [docs]({0}) for more information!".format(FEATURES[feature]["docs"]))

code = FEATURES[feature]["code"]
if (code.endswith('.py')):
    with open("demos/{1}".format(__VERSION__.replace('.', '_'), code), 'r') as f:
        code = f.read()

if ("execute" in FEATURES[feature] and FEATURES[feature]["execute"]):
    exec(code)
st.subheader("Example:")
st.code(code, language="python")
