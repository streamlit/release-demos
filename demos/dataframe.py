import streamlit as st
import pandas as pd

options = pd.DataFrame({'Options': ['radio', 'multiselect', 'selectbox']})
st.write("Input", options)

st.radio("Dataframe as input for radio buttons", options)
st.multiselect("Dataframe as input for multiselect", options)
st.selectbox("Dataframe as input for selectbox", options)
