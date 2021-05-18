import streamlit as st

from . import tic_tac_toe
from . import todo_list
from . import labelling
from . import pagination


def show():
    # https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/279/bowling_1f3b3.png
    # https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/279/joystick_1f579-fe0f.png
    st.image(
        "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/279/joystick_1f579-fe0f.png",
        width=100,
    )
    st.write(
        """
        # Try out Session State!

        One of the longest & most highly requested features is finally here! Session 
        state allows you to preserve information throughout a browser session. 
        Below are some ideas for how to use it. 
        """
    )

    st.write("---")

    st.write(
        """
        ## 💯 Counter
        
        The most basic example: Store a count in `st.session_state` and increment when clicked.
        """
    )
    if "counter" not in st.session_state:
        st.session_state.counter = 0

    def increment():
        st.session_state.counter += 1

    st.write("Counter:", st.session_state.counter)
    st.button("Plus one!", on_change=increment)

    if st.session_state.counter >= 50:
        st.success("King of counting there! Your trophy for reaching 50: 🏆")
    elif st.session_state.counter >= 10:
        st.warning("You made it to 10! Keep going to win a prize 🎈")

    st.write("---")
    tic_tac_toe.show()
    st.write("---")
    todo_list.show()
    st.write("---")
    labelling.show()
    st.write("---")
    pagination.show()


if __name__ == "__main__":
    show()
