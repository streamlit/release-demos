import streamlit as st

st.set_page_config(
    page_title="About background colors",
    page_icon="🎨",
)

st.title("🎨 Background colors for text")

st.markdown(
    """This feature adds support for background colors for text in markdown commands. It supports the following colors:"""
)
st.markdown(
    """
- :blue-background[blue]
- :green-background[green]
- :red-background[red]
- :violet-background[violet]
- :orange-background[orange]
- :gray-background[gray], :grey-background[or grey]
- :rainbow-background[rainbow]
"""
)
st.markdown(
    """To add a background color to some text, type `:color-background[text to be colored]`, where `color` needs to be replaced with the name of one of the supported background colors above."""
)

with st.expander("How to use this app"):
    st.markdown(
        """
    If you're in a hurry, you can jump straight into the [examples](#examples-with-st-markdown) below to see how background colors work across different Streamlit commands.

    In case you want to play around with the background colors yourself, check out:
    """
    )

    st.page_link(
        "pages/1_🛝_Playground.py",
        label="**Playground** to experiment with different background colors and text.",
        icon="🛝",
    )
    st.page_link(
        "pages/2_🏷️_Named_Entity_Recognition.py",
        label="**Named Entity Recognition** to see named entities highlighted with different colors.",
        icon="🏷️",
    )
    st.page_link(
        "pages/3_😊_Sentiment_Analysis.py",
        label="**Sentiment Analysis** to see text highlighted based on sentiment polarity.",
        icon="😊",
    )

"## Examples with `st.markdown`"
st.markdown(
    """This is :green-background[important].

This is :green-background[important]. :blue-background[This is blue]

:blue-background[This is blue]. This is :red-background[important]

This is :red-background[important]. This is :violet-background[important].

This is :rainbow-background[important many many words].

This is :red-background[important]. :blue-background[This is blue] We should not have match here which is great! This is :red-background[important]. :blue-background[This is blue]
"""
)

"## Other commands"
with st.echo():
    st.title("This is :red-background[red].")
    st.header("This is :red-background[red].")
    st.subheader("This is :red-background[red].")
with st.echo():
    st.write("## This is :red-background[red].")
    st.write("#### This is :red-background[red].")
with st.echo():
    st.slider("This is :red-background[red].")
    st.expander("This is :red-background[red].").write("Hello")
    st.button("This is :red-background[red].")

"## Edge cases"
with st.echo():
    st.markdown(
        "This opens a background color tag :red-background[but doesn't close it."
    )
with st.echo():
    st.markdown(
        "This opens a background color tag :red-background[and then opens a different :blue-background[one."
    )
with st.echo():
    st.markdown("This is **:blue-background[colored] inside bold**.")
with st.echo():
    st.markdown(":blue-background[This is **bold**].")

"## Background color is also supported on labels"
with st.echo():
    st.button("Background color is :red-background[supported on buttons]!")
with st.echo():
    st.download_button(
        "Background color is :rainbow-background[supported on download buttons]!",
        data=bytes(1234),
    )
with st.form("Background color form"):
    st.text_input(":blue-background[Background color is supported on labels]")
    submitted = st.form_submit_button(
        "Background color is :blue-background[supported on form submit buttons]!"
    )
with st.echo():
    st.checkbox(":violet-background[Also supported on checkboxes!]")
with st.expander(":orange-background[Background color is supported on expanders]"):
    st.write(""":blue-background[It is supported on write!]""")
with st.echo():
    tabA, tabB = st.tabs(
        [
            "Background color is :orange-background[supported on tab A]",
            ":red-background[And is supported on tab B]",
        ]
    )
with tabA:
    st.markdown("""It also :blue-background[works perfectly inside of them!]""")

with tabB:
    st.write("""It also :blue-background[works perfectly inside of them!]""")
