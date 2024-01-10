import streamlit as st

VERSION = "1.30"

st.set_page_config(
    page_title=f"New features in Streamlit 1.30",
    page_icon=':memo:',
    initial_sidebar_state="expanded",
    layout="wide",
)

intro = "This release features introduces `st.switch_page` and `st.query_params`. Check out the [demo app](https://release130.streamlit.app) to try out the new features."

release_notes = f"""
---

**Highlights**

- 🔄 Announcing `st.switch_page` to programmatically switch pages in multipage apps! Check out our docs to learn about this highly anticipated feature!
- ❓Introducing `st.query_params` to handle variables passed through your app’s URL. Check out our docs to understand this feature and how it’s been upgraded and improved from our experimental version!

**Notable Changes**

- 📐 `st.container` can be configured with a height to create grids or scrolling containers ([#7697](https://github.com/streamlit/streamlit/pull/7697), [#2169](https://github.com/streamlit/streamlit/issues/2169), [#2447](https://github.com/streamlit/streamlit/issues/2447)).
- 🔗 For dataframes, `LinkColumn` has a simplified UI and can be configured with display text, including programmatically defined text through regular expressions ([#7784](https://github.com/streamlit/streamlit/pull/7784), [#7741](https://github.com/streamlit/streamlit/pull/7741), [#6787](https://github.com/streamlit/streamlit/issues/6787)).
- 🧭 Sidebar navigation for multipage apps can be hidden via configuration ([#7852](https://github.com/streamlit/streamlit/pull/7852)).
- ⏩ Plotly figures can load even faster when used in combination with `orjson` ([#7860](https://github.com/streamlit/streamlit/pull/7860)). Thanks, [eric-skydio](https://github.com/eric-skydio)!
- ♻️ Behavior change: Query parameters are removed when changing pages ([#7817](https://github.com/streamlit/streamlit/pull/7817), [#6725](https://github.com/streamlit/streamlit/issues/6725), [#5505](https://github.com/streamlit/streamlit/issues/5505)).

**Other Changes**

- 🛠️ `showFooter` is no longer an embed option since the footer no longer exists ([#7902](https://github.com/streamlit/streamlit/pull/7902), [#7785](https://github.com/streamlit/streamlit/issues/7785)).
- 🕵️ All security concerns should be reported through [HackerOne](https://hackerone.com/snowflake?type=team) ([#7783](https://github.com/streamlit/streamlit/pull/7783)).
- 🕷️ Bug fix: Tabs are not disabled when stale to prevent flickering ([#7905](https://github.com/streamlit/streamlit/pull/7905), [#7820](https://github.com/streamlit/streamlit/issues/7820)).
- 🛡️ Bug fix: The full file path is used instead of a prefix to prevent custom components from reaching beyond their own folders ([#7901](https://github.com/streamlit/streamlit/pull/7901)).
- 🪱 Bug fix: Widgets raise an exception if its values aren’t Python comparable ([#7840](https://github.com/streamlit/streamlit/pull/7840), [#3714](https://github.com/streamlit/streamlit/issues/3714)).
- 🐞 Bug fix: The down-arrow icons on expanders maintain a consistent size ([#7596](https://github.com/streamlit/streamlit/pull/7596)). Thanks, [matiboux](https://github.com/matiboux)!
- 🐝 Bug fix: Tabs no longer flicker when switching between them ([#7904](https://github.com/streamlit/streamlit/pull/7904)).
- 🐜 Bug fix: Enter-to-submit is automatically disabled when the associated `st.form_submit_button` is disabled ([#7827](https://github.com/streamlit/streamlit/pull/7827), [#7822](https://github.com/streamlit/streamlit/issues/7822)).
- 🪲 Bug fix: Required columns cannot be hidden with column configuration ([#7888](https://github.com/streamlit/streamlit/pull/7888), [#7559](https://github.com/streamlit/streamlit/issues/7559)).
- 🐛 Bug fix: Using `nan` as a value in `SelectboxColumn` will raise an error instead of silently failing ([#7887](https://github.com/streamlit/streamlit/pull/7887), [#7558](https://github.com/streamlit/streamlit/issues/7558)).
- 🌙 Bug fix: Custom component iframes allow dark mode ([#7821](https://github.com/streamlit/streamlit/pull/7821), [#7813](https://github.com/streamlit/streamlit/issues/7813)).
- 🪰 Bug fix: The command to start Streamlit is not sent to the frontend ([#7787](https://github.com/streamlit/streamlit/pull/7787)).
- 💅 Bug fix: The background color of `st.toggle` is enhanced for better visibility ([#7788](https://github.com/streamlit/streamlit/pull/7788)).
- 🪳 Bug fix: Built-in charts can handle ordered categorical columns ([#7771](https://github.com/streamlit/streamlit/pull/7771), [#7776](https://github.com/streamlit/streamlit/issues/7776)).

---
"""
def draw_main_page():

    st.title(f"Welcome to Streamlit {VERSION}! :wave:", anchor=False)

    st.caption(intro)

    st.write(release_notes)

draw_main_page()
