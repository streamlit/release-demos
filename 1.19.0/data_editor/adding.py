import pandas as pd
import streamlit as st

data = {
    "Animal": ["Lion", "Crocodile", "Elephant", "Giraffe", "Penguin"],
    "Weight (kg)": [190, 430, 5000, 800, 4],
    "Is Endangered": [True, True, True, False, False],
    "Classification": ["Mammal", "Reptile", "Mammal", "Mammal", "Bird"],
    "Average Lifespan (years)": [12, 70, 70, 25, 20],
    "Habitat": ["Grassland", "Water", "Savannah", "Savannah", "Antarctica"],
}

df = pd.DataFrame(data)

df["Classification"] = df["Classification"].astype("category")
df["Habitat"] = df["Habitat"].astype("category")

st.experimental_data_editor(df, num_rows="dynamic")