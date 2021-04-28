import random
import time
import streamlit as st

apps = [
    (
        "Analyzing Your Goodreads Reading Habits",
        "https://share.streamlit.io/tylerjrichards/streamlit_goodreads_app/books.py",
    ),
    (
        "Bayesian Deep Learning for Galaxy Zoo DECaLS",
        "https://share.streamlit.io/mwalmsley/galaxy-poster/gz_decals_mike_walmsley.py",
    ),
    (
        "Gravitational Wave Quickview",
        "https://share.streamlit.io/jkanner/streamlit-dataview/master/app.py/+/",
    ),
    (
        "NYC Uber Ridesharing Data",
        "https://share.streamlit.io/streamlit/demo-uber-nyc-pickups/",
    ),
    (
        "Streamlit Cheat Sheet",
        "https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py",
    ),
    ("Traingenerator", "https://traingenerator.jrieke.com/"),
]


def forms_demo():
    st.image(
        "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/271/crystal-ball_1f52e.png",
        width=100,
    )

    st.write(
        """
        # Try out `st.form`!

        We built a super-secret algorithm to recommend a Streamlit app based on your personality. The problem: It takes a long time to run. That's why we use a form to bundle all the input widgets 👇
        """
    )

    st.write("")

    with st.form(key="recommender"):
        st.write("Click **Submit** to get your recommendation!")
        st.selectbox(
            "Your favorite streamlit call",
            ["st.form", "st.balloons 🎈 ", "st.form_submit_button", "st.write"],
        )
        st.text_input("Your favorite thing to build streamlit apps for")
        st.slider("How excited you are about forms", 0, 11, 10)
        submitted = st.form_submit_button()

    st.write("")

    if submitted:
        with st.spinner("🤓 Crunching numbers..."):
            time.sleep(2)
        app_name, app_url = random.choice(apps)
        st.success(
            f"☘️ The algorithm recommends this app to you: [{app_name}]({app_url}) (find more cool apps in [our gallery](https://streamlit.io/gallery)!)"
        )

        st.info(
            "💡 With `st.form`, this app (and our complex algorithm!) only reruns when you hit the submit button, not at each widget interaction. [Check out the blog post to learn how it works!]()"
        )
