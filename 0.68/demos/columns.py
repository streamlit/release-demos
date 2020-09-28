import streamlit as st
from PIL import Image
from io import BytesIO
import requests
import random

def columns():
    st.write("""
    # Go horizontal with columns

    `st.beta_columns` acts similarly to `st.sidebar`, except now you can put the
    columns anywhere in your app. Just declare each column as a new variable, and
    then you can add in ANY element or component available from the Streamlit library.

    ---
    ##  Create a grid layout!
    """)

    with st.echo("below"):
        svg="""
        <svg xmlns="http://www.w3.org/2000/svg">
            <rect width="100%" height="100%" fill="{0}"/>
            <rect width="20px" height="100%" fill="white"/>
        </svg>
        """

        colors = ['red', 'pink', 'orange','green','blue', 'purple']
        for i in range(1, 3):
            cols = st.beta_columns((2, 1, 3))
            for col in cols:
                col.image(svg.format(random.choice(colors)))

    st.write("""
    ---
    ## Or compare things side-by-side!
    """)

    with st.echo("below"):
        col1, col2 = st.beta_columns(2)

        response = requests.get("https://images.unsplash.com/photo-1592514778340-ec938b4945dd?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop")
        original = Image.open(BytesIO(response.content))
        col1.write("### Original")
        col1.image(original, use_column_width=True)

        grayscale = original.convert('LA')
        col2.write("### Grayscale")
        col2.image(grayscale, use_column_width=True)
