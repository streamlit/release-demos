import streamlit as st

st.set_page_config(
    page_title='st.toast',
    page_icon=':bread:'
)

@st.cache_data
def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )

icon(":bread:")
st.title("st.toast is here! 🎉")


st.caption(
    "We're very excited to release **:red[st.toast]**, which displays a short notification message at the bottom-right corner of your app!"
)
st.caption(
    "Note that toasts will **automatically disappear after four seconds** - unless the user hovers over or interacts with them."
)
# st.divider()

st.subheader("st.toast API")
code = '''
Display a short message, known as a notification "toast".
The toast appears in the app's bottom-right corner and disappears
after four seconds.
    
Parameters
----------
body : str
    The string to display as Github-flavored Markdown. Syntax
    information can be found at: https://github.github.com/gfm.

    This also supports:

    * Emoji shortcodes, such as ``:+1:``  and ``:sunglasses:``.
        For a list of all supported codes,
        see https://share.streamlit.io/streamlit/emoji-shortcodes.

    * LaTeX expressions, by wrapping them in "$" or "$$" (the "$$"
        must be on their own lines). Supported LaTeX functions are listed
        at https://katex.org/docs/supported.html.

    * Colored text, using the syntax ``:color[text to be colored]``,
        where ``color`` needs to be replaced with any of the following
        supported colors: blue, green, orange, red, violet.
icon : str or None
    An optional, keyword-only argument that specifies an emoji to use as
    the icon for the toast. Shortcodes are not allowed, please use a
    single character instead. E.g. "🚨", "🔥", "✅", etc.
    Defaults to None, which means no icon is displayed.

Example
-------
>>> import streamlit as st
>>>
>>> st.toast('Your edited image was saved!', icon='😍')
'''
st.code(code, language='python')