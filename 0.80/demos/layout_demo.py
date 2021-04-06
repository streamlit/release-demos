import streamlit as st
import numpy as np


def layout_demo():
    st.markdown('''
    ---
    [Fix for image galleries not being the same size](https://github.com/streamlit/streamlit/issues/3013)
    ''')
    # Produce 3 images and put them into 3 columns next to each other, scaling them automatically to columns width
    with st.echo():
        [col.image(img, use_column_width=True) for col, img in zip(st.beta_columns(3), np.zeros((3, 250, 250, 3)))]

    st.markdown('---')

    st.markdown('''
    [Fix for column vertical column alignment](https://github.com/streamlit/streamlit/issues/2716)
    ''')

    st.markdown('''
    [Fix gap not working on Safari](https://github.com/streamlit/streamlit/pull/3042)
    ''')

    with st.echo():
        search_term = st.text_input('Search term', value='streamlit')

        col1, col2 = st.beta_columns([2, 1])

        with col1:
            from_date = st.selectbox('1 month ago', options=['A', 'B'])

        with col2:
            limit = st.number_input('Limit', value=10000)

        col3, col4, col5 = st.beta_columns(3)

        with col3:
            min_replies = st.number_input('Minimum replies', value=0)
        with col4:
            min_retweets = st.number_input('Minimum retweets', value=0)
        with col5:
            min_hearts = st.number_input('Minimum hearts', value=0)


