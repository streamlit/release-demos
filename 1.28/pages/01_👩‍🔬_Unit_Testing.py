import streamlit as st

def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )
    
st.set_page_config("Unit Testing Demo", "👩‍🔬", layout="wide")
icon("👩‍🔬")

st.title("Unit Testing Demo", anchor=False)
st.caption("A new API to write unit tests for Streamlit apps.")
st.write("Learn more about unit testing in [<PLACEHOLDER_OUR_DOCS>](https://docs.streamlit.io/).")
st.divider()

st.info("The GIF shows the function code, test code, and running the tests.", icon="ℹ️")
st.write("# [GIF goes here]")

col1, col2 = st.columns(2)

with col1:
    st.info('Main code to be tested.', icon="🧑‍💻")
    st.code(
        """
        import streamlit as st

        def my_function():
            pass
        """, language="python"
    )

with col2:
    st.info('Test code.', icon="🧪")
    st.code(
        """
        import streamlit as st

        def test_my_function():
            pass
        """, language="python"
    )