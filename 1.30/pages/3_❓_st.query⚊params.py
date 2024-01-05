import streamlit as st

def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )
    
st.set_page_config("st.query_params", "❓", layout="wide")

icon("❓")
st.title("Demo of st.query_params", anchor=False)

st.divider()

query_params = st.query_params
if "is_checked" not in st.session_state:
    st.session_state["is_checked"] = (
        query_params.get("is_checked", "False").lower() == "true"
    )
my_checkbox = st.checkbox("Example Checkbox", key="is_checked")
query_params.is_checked = my_checkbox
st.write(st.session_state)


# # Function to update the query parameters based on the user input
# def update_query_params(name):
#     st.query_params(name=name)

# # Get the user's name from the query parameters or default to an empty string
# user_name = st.query_params.get("name", [""])[0]

# # Input for the user's name
# name_input = st.text_input("Enter your name:", value=user_name)

# # Button to update the greeting and URL query parameters
# if st.button("Update Greeting"):
#     update_query_params(name_input)

# # Greeting message
# if name_input:
#     st.write(f"Hello, {name_input}! 👋")
# else:
#     st.write("Enter your name and press 'Update Greeting' to see a personalized message.")


