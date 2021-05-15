import streamlit as st
import numpy as np
import functools


# From: https://stackoverflow.com/questions/39922967/python-determine-tic-tac-toe-winner
def checkRows(board):
    for row in board:
        if len(set(row)) == 1:
            return row[0]
    return None


def checkDiagonals(board):
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0]
    if len(set([board[i][len(board) - i - 1] for i in range(len(board))])) == 1:
        return board[0][len(board) - 1]
    return None


def checkWin(board):
    # transposition to check rows, then columns
    for newBoard in [board, np.transpose(board)]:
        result = checkRows(newBoard)
        if result:
            return result
    return checkDiagonals(board)


def tic_tac_toe():
    st.write(
        """
        # 👾 Tic Tac Toe
        
        This app uses `st.session_state` to store the entire game state (= 
        board values, next player, done flag). Any click on the buttons below is handled 
        through the new `on_change` callbacks, passing the "board position" as arguments 
        to the callback.
        """
    )
    st.write("")

    # TODO: One issue here is that we cannot do `if not st.session_state` because the
    #   tic tac toe page here is only accessed after the frontpage has been loaded.
    #   Currently, st.session_state evaluates to True after the 1st run, even if there
    #   was nothing stored in it. Is this how it should be? This is contrary to `dict`!
    # if not st.session_state:
    #     print("hello")

    # Initialize state.
    if "board" not in st.session_state:
        st.session_state.board = np.full((3, 3), ".", dtype=str)
        st.session_state.next_player = "X"
        st.session_state.done = False

    # Define callbacks to handle button clicks.
    def handle_click(i, j):
        if not st.session_state.done:
            st.session_state.board[i, j] = st.session_state.next_player
            st.session_state.next_player = (
                "O" if st.session_state.next_player == "X" else "X"
            )
            winner = checkWin(st.session_state.board)
            if winner != ".":
                st.session_state.done = True
                st.write(f"{winner} won the game!")
                st.balloons()

    # Show one button for each field.
    cols = st.beta_columns(3)
    for i, row in enumerate(st.session_state.board):
        for j, field in enumerate(row):
            cols[j].button(
                field,
                key=f"{i}-{j}",
                on_change=handle_click,
                args=(i, j),
            )