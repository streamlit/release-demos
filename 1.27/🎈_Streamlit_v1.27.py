import streamlit as st

VERSION = "1.27"

st.set_page_config(
    page_title=f"New features in Streamlit 1.27",
    page_icon=':memo:',
    initial_sidebar_state="expanded",
    layout="wide",
)

intro = f"""
This release launches the features `st.scatter_chart` and `st.link_button`, and includes bug fixes and improvements.
"""

release_notes = f"""
---
**Highlights**

- ✨ Introducing `st.scatter_chart` — a new, simple chart element to build scatter charts Streamlit-y fast and easy! See our documentation.
- 🔗 Introducing `st.link_button`! Want to open an external link in a new tab with a bit more pizazz than a plain text link? Check out our documentation to see how.
- 🏃 Announcing the general availability of `st.rerun`, a command to interrupt your script and trigger an immediate rerun.

**Notable Changes**

- 👻 You can initialize widgets with an empty state by setting `None` as an initial value for `st.number_input`, `st.selectbox`, `st.date_input`, `st.time_input`, `st.radio`, `st.text_input`, and `st.text_area`!
- 📤 `st.download_button` now uses `target="_self"` instead of opening a new tab ([#7151](https://github.com/streamlit/streamlit/pull/7151), [#7132](https://github.com/streamlit/streamlit/issues/7132)).
- 🧟 Removed unmaintained `pympler` dependency ([#7193](https://github.com/streamlit/streamlit/pull/7193), [#7131](https://github.com/streamlit/streamlit/issues/7131)). Thanks, [rudyardrichter](https://github.com/rudyardrichter)!

**Other changes**

- 🐛 Bug fix: `st.multiselect` now shows a correct message when no result matches a user’s search ([#7205](https://github.com/streamlit/streamlit/pull/7205), [#7116](https://github.com/streamlit/streamlit/issues/7116)).
- 🪲 Bug fix: `st.experimental_user` now defaults to `test@example.com` ([#7219](https://github.com/streamlit/streamlit/pull/7219), [#7215](https://github.com/streamlit/streamlit/issues/7215)).
- 🐜 Bug fix: `st.slider` labels don’t overlap when small ranges are selected ([#7221](https://github.com/streamlit/streamlit/pull/7221), [#3385](https://github.com/streamlit/streamlit/issues/3385)).
- 🐝 Bug fix: Type-checking correctly identifies all string types to avoid hashing errors ([#7255](https://github.com/streamlit/streamlit/pull/7255), [#6455](https://github.com/streamlit/streamlit/issues/6455)).
- 🐞 Bug fix: JSON is parsed with JSON5 to avoid errors from null values when using `st.pydeck_chart` ([#7256](https://github.com/streamlit/streamlit/pull/7256), [#5799](https://github.com/streamlit/streamlit/issues/5799)).
- 🕷️ Bug fix: Identical widgets on different pages are correctly interpreted by Streamlit as distinct ([#7264](https://github.com/streamlit/streamlit/pull/7264), [#6146](https://github.com/streamlit/streamlit/issues/6146)).
- 🦋 Bug fix: Visual tweaks to widgets for responsive behavior ([#7145](https://github.com/streamlit/streamlit/pull/7145)).
- 🪳 Bug fix: SVGs are accurately displayed ([#7183](https://github.com/streamlit/streamlit/pull/7183), [#3882](https://github.com/streamlit/streamlit/issues/3882)).
- 🪰 Bug fix: `st.video` correctly updates with changes to `start_time` ([#7257](https://github.com/streamlit/streamlit/pull/7257), [#7126](https://github.com/streamlit/streamlit/issues/7126)).
- 🦠 Bug fix: Additional error handling was added to `st.session_state` ([#7280](https://github.com/streamlit/streamlit/pull/7280), [#7206](https://github.com/streamlit/streamlit/issues/7206)).
- 🦟 Bug fix: `st.map` correctly refreshes with new data ([#7307](https://github.com/streamlit/streamlit/pull/7307), [#7294](https://github.com/streamlit/streamlit/issues/7294)).
- 🦂 Bug fix: The decorative app header line is no longer covered by the sidebar ([#7297](https://github.com/streamlit/streamlit/pull/7297), [#6264](https://github.com/streamlit/streamlit/issues/6264)).
- 🦗 Bug fix: `st.code` no longer triggers a `CachedStFunctionWarning` ([#7306](https://github.com/streamlit/streamlit/pull/7306), [#7055](https://github.com/streamlit/streamlit/issues/7055)).
- 🕸️ Bug fix: `st.download_button` no longer resets with different `data` ([#7316](https://github.com/streamlit/streamlit/pull/7316), [#7308](https://github.com/streamlit/streamlit/issues/7308)).
- 🐌 Bug fix: Widgets consistently recognize user interaction while a page is still running, with or without `fastRerun` enabled ([#7283](https://github.com/streamlit/streamlit/pull/7283), [#6643](https://github.com/streamlit/streamlit/issues/6643)).
- 🦎 Bug fix: `st.tabs` was improved to better handle and render conditionally appearing tabs ([#7287](https://github.com/streamlit/streamlit/pull/7287), [#7310](https://github.com/streamlit/streamlit/pull/7310), [#5454](https://github.com/streamlit/streamlit/issues/5454), [#7040](https://github.com/streamlit/streamlit/issues/7040)).
---
"""
# End release updates

def draw_main_page():

    st.title(f"Welcome to Streamlit {VERSION}! :wave:", anchor=False)

    st.caption(intro)

    st.write(release_notes)

draw_main_page()