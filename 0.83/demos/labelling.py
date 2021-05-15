import os
import random

import streamlit as st


def labelling():
    st.write(
        """
        # 🐾 Data Labelling
        
        This app allows you to assign labels to images (e.g. for machine learning). It 
        uses `st.session_state` to store the annotation results and the list of 
        remaining images.
        """
    )

    script_path = os.path.dirname(__file__)
    rel_path = "images"
    abs_file_path = script_path + "/" + rel_path
    files = os.listdir(abs_file_path)

    if "annotations" not in st.session_state:
        st.session_state.annotations = {}
        st.session_state.files = files
        st.session_state.current_image = "cat.1.jpg"

    def annotate(label):
        st.session_state.annotations[st.session_state.current_image] = label
        # TODO: Handle when all are done!
        st.session_state.current_image = random.choice(st.session_state.files)
        st.session_state.files.remove(st.session_state.current_image)

    image_path = abs_file_path + "/" + st.session_state.current_image
    # TODO: Fix width here. Maybe just show quadratic crop?
    st.image(image_path, width=300)

    col1, col2 = st.beta_columns(2)
    col1.button("This is a dog! 🐶", on_change=annotate, args=("dog",))
    col2.button("This is a cat! 🐱", on_change=annotate, args=("cat",))
    # annotation_response = st.selectbox(
    #     key="annotation_response", label="", options=["cat", "dog"]
    # )
    # st.button(label="Next", on_change=annotate)

    st.markdown("---")
    st.header("Annotations")
    st.write(st.session_state.annotations)

    if len(st.session_state.files) == 0:
        st.warning("Finished Annotation")
        st.stop()
