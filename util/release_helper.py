import streamlit as st

def create_release_notes(release_notes, previous_version, current_version):
    st.write(f"""
# Welcome to Streamlit {current_version}! 👋

This app is a demo of several :fire: **red-hot** :fire: features that made it into this Streamlit
version.
""")

    st.info("""
        :point_left: **To get started, choose a demo on the left sidebar.**
    """)

    st.write(release_notes)
    st.write("""
### Release Details

- If you'd like to know what _exactly_ went into this release, check out the [commit
diff](https://github.com/streamlit/streamlit/compare/{previous_version}...{st.__version__}).
- To play with this demo app, please see the source code in [Github](https://github.com/streamlit/release-demos/tree/master/{current_version}).

---

### Special Thanks
As always, thank you to all our [contributors](https://github.com/streamlit/streamlit/graphs/contributors) who help make Streamlit great!
[TODO: insert contributor log avatar image thing]

### Connect With Us

- We can be found at https://streamlit.io and https://twitter.com/streamlit
- Come by
[the forums](https://discuss.streamlit.io/c/official-announcements/6) if you'd like ask questions,
post awesome apps, or just say hi!
    """)
