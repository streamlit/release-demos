import streamlit as st

VERSION = "1.29"

st.set_page_config(
    page_title=f"New features in Streamlit 1.29",
    page_icon=':memo:',
    initial_sidebar_state="expanded",
    layout="wide",
)

intro = "This release introduces [:red[PENDING ->]`st.get_query` and `st.set_query`], improvements to `st.container` and `st.form`! The release also includes bug fixes."

release_notes = f"""
---
**Highlights**
* (PENDING)❓ Introducing `st.get_query` and `st.set_query` to handle query parameters in your app’s URL. Check out our docs to learn about this feature.

**Notable changes**
* 🔲 `st.container` and `st.form` now have a `border` parameter to show or hide a border ([#7455](https://github.com/streamlit/streamlit/pull/7455), [#6416](https://github.com/streamlit/streamlit/issues/6416), [#4175](https://github.com/streamlit/streamlit/issues/4175)).
* 🐍 Streamlit supports Python 3.12 ([#7663](https://github.com/streamlit/streamlit/pull/7663))!
* ⌛ `st.dataframe`, `st.data_editor`, and `st.table` support  `datetime.timedelta` values ([#7689](https://github.com/streamlit/streamlit/pull/7689), [#4489](https://github.com/streamlit/streamlit/issues/4489)).
* 🏃 Reduced the overhead of running `AppTest`-simulated apps, especially for fast-running apps ([#7691](https://github.com/streamlit/streamlit/pull/7691)).
* 🛁 String representations of `AppTest` data are improved for a better testing and debugging experience ([#7658](https://github.com/streamlit/streamlit/pull/7658)).
* 🔢 Apps can be configured to identify `Enum` classes as the same if they have matching member names ([#7408](https://github.com/streamlit/streamlit/pull/7408), [#4909](https://github.com/streamlit/streamlit/issues/4909)). Thanks, [Asaurus1](https://github.com/Asaurus1)!
* ❌ ”Made with Streamlit” no longer appears at the bottom of apps ([#7583](https://github.com/streamlit/streamlit/pull/7583)).
* 🧹 Unused config options have been deprecated ([#7584](https://github.com/streamlit/streamlit/pull/7584)).
* 🕳️ Query parameters can be empty ([#7601](https://github.com/streamlit/streamlit/pull/7601), [#7416](https://github.com/streamlit/streamlit/issues/7416)).
* 💅 Visual tweaks ([#7592](https://github.com/streamlit/streamlit/pull/7592), [#7630](https://github.com/streamlit/streamlit/pull/7630)).

**Other changes**
* 🛡️ Bug fix: Added security patch for `pyarrow` vulnerability. Custom components using `pyarrow` table deserialization should require `pyarrow>=14.0.1` ([#7695](https://github.com/streamlit/streamlit/pull/7695), [#7700](https://github.com/streamlit/streamlit/issues/7700)).
* 🦟 Bug fix: Improved typing for `st.connection` ([#7671](https://github.com/streamlit/streamlit/pull/7671)). Thanks, [thezanke](https://github.com/thezanke)!
* 🪰 Bug fix: Retries of `SnowflakeConnection` methods are narrowed to only occur with transient errors to avoid unnecessary repeated errors ([#7645](https://github.com/streamlit/streamlit/pull/7645), [#7637](https://github.com/streamlit/streamlit/issues/7637)).
* 🏗️ Removed the v0 testing framework which was undocumented ([#7657](https://github.com/streamlit/streamlit/pull/7657)).
* 🪳 Bug fix: The navigation expander arrow no longer disappears ([#7634](https://github.com/streamlit/streamlit/pull/7634), [#7547](https://github.com/streamlit/streamlit/issues/7547)).
* ❄️ Improved the error message for `SnowflakeConnection` when a configuration is not found ([#7652](https://github.com/streamlit/streamlit/pull/7652)).
* 🕷️ Bug fix: `st.rerun` no longer causes a `RecursionError` when used with `st.chat_input` ([#7643](https://github.com/streamlit/streamlit/pull/7643), [#7629](https://github.com/streamlit/streamlit/issues/7629)).
* 🐞 Bug fix: `st.file_uploader` no longer causes an extra rerun and therefore doesn’t conflict with `st.chat_input` ([#7641](https://github.com/streamlit/streamlit/pull/7641), [#7556](https://github.com/streamlit/streamlit/issues/7556)).
* 🐝 Bug fix: `AppTest` no longer raises an error when encountering `st.container` ([#7644](https://github.com/streamlit/streamlit/pull/7644), [#7636](https://github.com/streamlit/streamlit/issues/7636)).
* 🪲 Bug fix: Graphviz charts scale correctly when exiting fullscreen view ([#7398](https://github.com/streamlit/streamlit/pull/7398), [#7527](https://github.com/streamlit/streamlit/issues/6527)).
* 🎥 Bug fix: Record a screencast” is hidden when known to be unsupported in a browser ([#7604](https://github.com/streamlit/streamlit/pull/7604)).
* 🐛 Bug fix: Increased the top padding of embedded apps to better display the dataframe toolbar ([#7681](https://github.com/streamlit/streamlit/pull/7681), [#7609](https://github.com/streamlit/streamlit/pull/7609), [#7607](https://github.com/streamlit/streamlit/issues/7607)).
* 🐜 Bug fix: `st.rerun` uses `NoReturn` for improved type checking ([#7422](https://github.com/streamlit/streamlit/pull/7422)) Thanks, [kongzii](https://github.com/kongzii).

---
"""



def draw_main_page():

    st.title(f"Welcome to Streamlit {VERSION}! :wave:", anchor=False)

    st.caption(intro)

    st.write(release_notes)

draw_main_page()