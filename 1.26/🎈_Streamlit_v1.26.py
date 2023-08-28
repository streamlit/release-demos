import streamlit as st

VERSION = "1.26"

st.set_page_config(
    page_title=f"New features in Streamlit 1.26",
    page_icon=':memo:',
    initial_sidebar_state="expanded",
    layout="wide",
)

intro = f"""
This release launches the features :red[st.status] and :red[st.toggle], and includes bug fixes and improvements.
"""

release_notes = f"""
---
**Highlights**

- 🤖 Introducing `st.status` to display output from long-running processes and external API calls ([#7140](https://github.com/streamlit/streamlit/pull/7140)). Works great with `st.chat_message`. See our [documentation](https://docs.streamlit.io/library/api-reference/status/st.status) for how to use this feature.
- 🚥 Introducing [st.toggle](https://docs.streamlit.io/library/api-reference/widgets/st.toggle) — an alternative to `st.checkbox` when you need an on/off switch.

**Notable Changes**

- 🎨 Simple [chart elements](https://docs.streamlit.io/library/api-reference/charts) have a `color` parameter to set the color of your data points or series ([#7022](https://github.com/streamlit/streamlit/pull/7022)).
- 🌈 [Markdown](https://docs.streamlit.io/library/api-reference/text/st.markdown) supports rainbow and gray colors ([#7106](https://github.com/streamlit/streamlit/pull/7106), [#7179](https://github.com/streamlit/streamlit/pull/7179)).
- 📏 [st.header](https://docs.streamlit.io/library/api-reference/text/st.header) and [st.subheader](https://docs.streamlit.io/library/api-reference/text/st.subheader) have optional, colored dividers ([#7133](https://github.com/streamlit/streamlit/pull/7133)).
- 🚀 Deploying to Community Cloud is even easier—locally running apps have a [deploy button](https://docs.streamlit.io/library/advanced-features/app-menu#deploy-this-app) in their toolbars ([#7085](https://github.com/streamlit/streamlit/pull/7085), [#6935](https://github.com/streamlit/streamlit/issues/6935)).
- 🖌️ [st.download_button](https://docs.streamlit.io/library/api-reference/widgets/st.download_button) has a new parameter `type` for theming ([#7056](https://github.com/streamlit/streamlit/pull/7056), [#7038](https://github.com/streamlit/streamlit/issues/7038)).
- 🤖 [st.chat_message](https://docs.streamlit.io/library/api-reference/chat/st.chat_message) has ai and human presets for messages ([#7094](https://github.com/streamlit/streamlit/pull/7094)).
- 💅 [st.radio](https://docs.streamlit.io/library/api-reference/widgets/st.radio) options support markdown and have captions ([#7018](https://github.com/streamlit/streamlit/pull/7018), [#7105](https://github.com/streamlit/streamlit/pull/7105), [#6085](https://github.com/streamlit/streamlit/issues/6085)).
- 🧼 Assorted visual tweaks ([#7050](https://github.com/streamlit/streamlit/pull/7050), [#894](https://github.com/streamlit/streamlit/issues/894)).
- 🛏️ Replaced deprecated `imghdr` dependency with `pillow` ([#7081](https://github.com/streamlit/streamlit/pull/7081), [#7027](https://github.com/streamlit/streamlit/issues/7027)).
- 🔢 [st.number_input](http://localhost:3000/library/api-reference/widgets/st.number_input)'s step buttons (+/-) are ignored during tabbing navigation ([#7154](https://github.com/streamlit/streamlit/pull/7154)). Thanks [@denck007](https://github.com/denck007)!

**Other changes**

- 🍞 Bug fix: Toast messages are no longer blocked by `st.chat_input` ([#7204](https://github.com/streamlit/streamlit/pull/7204), [#7115](https://github.com/streamlit/streamlit/issues/7115)).
- 🕸️ Bug fix: Widget IDs are now stable to prevent inconsistent statefulness ([#7003](https://github.com/streamlit/streamlit/pull/7003)).
- 🦟 Bug fix: Browser autofill is correctly recognized within forms now ([#7150](https://github.com/streamlit/streamlit/pull/7150), [#7101](https://github.com/streamlit/streamlit/issues/7101), [#7084](https://github.com/streamlit/streamlit/issues/7084)).
- 🪱 Bug fix: `st.file_uploader` no longer causes session state to reset when a websocket connection is dropped and reconnected ([#7149](https://github.com/streamlit/streamlit/pull/7149), [#7025](https://github.com/streamlit/streamlit/pull/7025)).
- 🏎️ Bug fix: Pydeck JSON data is cached for improved performance ([#7113](https://github.com/streamlit/streamlit/pull/7113), [#5532](https://github.com/streamlit/streamlit/issues/5532)).
- 🦋 Bug fix: `st.chat_input` no longer submits prematurely while typing with an input method editor ([#6993](https://github.com/streamlit/streamlit/pull/6993)).
- 🐞 Bug fix: Label backgrounds for `st.tabs` are now transparent ([#7070](https://github.com/streamlit/streamlit/pull/7070), [#5707](https://github.com/streamlit/streamlit/issues/5707)).
- 🐝 Bug fix: Page width is no longer ignored when using the `help` parameter in `st.button` ([#7033](https://github.com/streamlit/streamlit/pull/7033), [#6161](https://github.com/streamlit/streamlit/issues/6161)).
- 🐜 Bug fix: Tweaked Altair color specification for improved visibility in dark mode ([#7061](https://github.com/streamlit/streamlit/pull/7061), [#3343](https://github.com/streamlit/streamlit/issues/3343)).
- 🪲 Bug fix: `st.chat_message` can correctly use local images as avatars ([#7130](https://github.com/streamlit/streamlit/pull/7130)).
- 🐛 Bug fix: Specified that MD5 is not used for security ([#7122](https://github.com/streamlit/streamlit/pull/7122), [#7120](https://github.com/streamlit/streamlit/issues/7120)).
- 🪄 Bug fix: Async function docstrings are ignored by [Streamlit magic](https://docs.streamlit.io/library/api-reference/write-magic/magic) ([#7143](https://github.com/streamlit/streamlit/pull/7143), [#7137](https://github.com/streamlit/streamlit/issues/7137)).
---
"""
# End release updates

def draw_main_page():

    st.title(f"Welcome to Streamlit {VERSION}! :wave:", anchor=False)

    st.caption(intro)

    st.write(release_notes)

draw_main_page()
