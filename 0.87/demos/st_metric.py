import streamlit as st


def show():
    st.image(
        "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/285/slot-machine_1f3b0.png",
        width=100,
    )
    st.write(
        """
        # Try out `st.metric`!

        It lets you to display a number in big bold font in your app. Really useful 
        for KPIs or other important metrics.
        """
    )

    st.metric("Streamlit version", 0.87, "0.01")

    st.write("---")
    st.write("`st.metric` looks especially nice in combination with `st.columns`:")
    col1, col2, col3 = st.columns(3)
    col1.metric("Metric 1", "1.2k", "5%")
    col2.metric("Metric 2", 456, "-8%")
    col3.metric("Metric 2", 0.75, "0.12")

    st.write("---")
    st.write("Want to use it? Have a look in our [docs]()!")


if __name__ == "__main__":
    show()
