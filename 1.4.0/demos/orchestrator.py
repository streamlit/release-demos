
import streamlit as st
from . import examples



def show_examples():

    st.write(
        """
        # 📸 st.camera_input
        
        We are launching a new widget, which lets the user take an image through their 
        webcam and upload it with the app! Use it with:
        
        ```python
        img_file = st.camera_input("Take a picture")
        ```
        """
    )

    st.write("---")
    examples.show()


if __name__ == "__main__":
    pass
