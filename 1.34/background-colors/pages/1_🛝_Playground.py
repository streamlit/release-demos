import streamlit as st

st.set_page_config(
    page_title="Playground",
    page_icon="🛝",
)

st.title("🛝 Playground")

st.markdown(
    "Select a color and type some text to see it rendered with the selected background color."
)

col1, col2 = st.columns(2)

with col1:
    # Color options
    color_options = {
        "Rainbow": "rainbow-background",
        "Red": "red-background",
        "Blue": "blue-background",
        "Green": "green-background",
        "Orange": "orange-background",
        "Gray": "gray-background",
        "Violet": "violet-background",
    }

    # User input for color selection
    selected_color = st.radio(
        "Choose a background color",
        list(color_options.values()),
        format_func=lambda x: list(color_options.keys())[
            list(color_options.values()).index(x)
        ].capitalize(),
        horizontal=True,
    )

    # User input for text
    user_input = st.text_input("Enter your text here:", value="This is some text")

    # Display the colored text
    st.markdown(f":{selected_color}[{user_input}]")


with col2:
    user_input = st.text_input(
        "Type in your text and add one or more background colors",
        value=":red-background[This is some text] that has :violet-background[multiple background colors].",
    )
    st.markdown(user_input)
