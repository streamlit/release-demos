import streamlit as st

edited_list = st.data_editor(["red", "green", "blue"], num_rows="dynamic")
st.write("Here are all the colors you entered:")
st.write(edited_list)
