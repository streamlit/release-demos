import pandas as pd
import streamlit as st
from utils import icon

st.set_page_config("Final four", "🤔")
icon("🤔")
"""
# Final four

Fun little demo to guess who will play in the final four. Try it out!

Column config features used:

- Image columns
- Disabling editing for specific columns
"""


df = pd.DataFrame(
    {
        "Date": ["2023/03/26", "2023/03/26", "2023/03/26", "2023/03/26"],
        "Team A": ["FL Altantic", "UConn", "Creighton", "Miami FL"],
        "Team A Logo": [
            f"https://upload.wikimedia.org/wikipedia/en/4/40/Florida_Atlantic_Owls_logo.svg",
            f"https://upload.wikimedia.org/wikipedia/en/b/b0/Connecticut_Huskies_logo.svg",
            f"https://upload.wikimedia.org/wikipedia/en/6/6f/Creighton_Bluejays_logo.svg",
            f"https://upload.wikimedia.org/wikipedia/commons/e/e9/Miami_Hurricanes_logo.svg",
        ],
        "Team A Wins": [False, False, False, False],
        "Team B": ["Kansas State", "Gonzaga", "San Diego St", "Texas"],
        "Team B Logo": [
            f"https://upload.wikimedia.org/wikipedia/en/e/e5/Kansas_State_Wildcats_logo.svg",
            f"https://upload.wikimedia.org/wikipedia/en/b/bd/Gonzaga_Bulldogs_logo.svg",
            f"https://upload.wikimedia.org/wikipedia/commons/7/7c/San_Diego_State_Aztecs_logo.svg",
            f"https://upload.wikimedia.org/wikipedia/commons/8/8d/Texas_Longhorns_logo.svg",
        ],
        "Team B Wins": [False, False, False, False],
    }
)

with st.echo("below"):
    edited_df = st.data_editor(
        df,
        column_config={
            "Date": st.column_config.DateColumn(),
            "Team A Logo": st.column_config.ImageColumn(""),
            "Team B Logo": st.column_config.ImageColumn(""),
        },
        disabled=["Date", "Team A", "Team B", "Team A Logo", "Team B Logo"],
        hide_index=True,
    )

st.subheader("Who gets to play in the final four!")
warning = ""
final_four_df = pd.DataFrame()
if (
    edited_df.iloc[0, :]["Team A Wins"] == True
    and edited_df.iloc[0, :]["Team B Wins"] == False
    and edited_df.iloc[2, :]["Team A Wins"] == True
    and edited_df.iloc[2, :]["Team B Wins"] == False
):
    final_four_df = pd.DataFrame(
        {
            "Team A": ["FL Altantic"],
            "Team A Logo": [
                f"https://upload.wikimedia.org/wikipedia/en/4/40/Florida_Atlantic_Owls_logo.svg"
            ],
            "Team B": ["Creighton"],
            "Team B Logo": [
                f"https://upload.wikimedia.org/wikipedia/en/6/6f/Creighton_Bluejays_logo.svg"
            ],
        }
    )
elif (
    edited_df.iloc[0, :]["Team A Wins"] == True
    and edited_df.iloc[0, :]["Team B Wins"] == False
    and edited_df.iloc[2, :]["Team A Wins"] == False
    and edited_df.iloc[2, :]["Team B Wins"] == True
):
    final_four_df = pd.DataFrame(
        {
            "Team A": ["FL Altantic"],
            "Team A Logo": [
                f"https://upload.wikimedia.org/wikipedia/en/4/40/Florida_Atlantic_Owls_logo.svg"
            ],
            "Team B": ["San Diego St"],
            "Team B Logo": [
                f"https://upload.wikimedia.org/wikipedia/commons/7/7c/San_Diego_State_Aztecs_logo.svg"
            ],
        }
    )
elif (
    edited_df.iloc[0, :]["Team A Wins"] == False
    and edited_df.iloc[0, :]["Team B Wins"] == True
    and edited_df.iloc[2, :]["Team A Wins"] == False
    and edited_df.iloc[2, :]["Team B Wins"] == True
):
    final_four_df = pd.DataFrame(
        {
            "Team A": ["Kansas State"],
            "Team A Logo": [
                f"https://upload.wikimedia.org/wikipedia/en/e/e5/Kansas_State_Wildcats_logo.svg"
            ],
            "Team B": ["San Diego St"],
            "Team B Logo": [
                f"https://upload.wikimedia.org/wikipedia/commons/7/7c/San_Diego_State_Aztecs_logo.svg"
            ],
        }
    )
elif (
    edited_df.iloc[0, :]["Team A Wins"] == False
    and edited_df.iloc[0, :]["Team B Wins"] == True
    and edited_df.iloc[2, :]["Team A Wins"] == True
    and edited_df.iloc[2, :]["Team B Wins"] == False
):
    final_four_df = pd.DataFrame(
        {
            "Team A": ["Kansas State"],
            "Team A Logo": [
                f"https://upload.wikimedia.org/wikipedia/en/e/e5/Kansas_State_Wildcats_logo.svg"
            ],
            "Team B": ["Creighton"],
            "Team B Logo": [
                f"https://upload.wikimedia.org/wikipedia/en/6/6f/Creighton_Bluejays_logo.svg"
            ],
        }
    )
else:
    warning = st.warning(
        "You have not select the all team or you selected multiple teams!"
    )
final_four_df_2 = pd.DataFrame()
if (
    edited_df.iloc[1, :]["Team A Wins"] == True
    and edited_df.iloc[1, :]["Team B Wins"] == False
    and edited_df.iloc[3, :]["Team A Wins"] == True
    and edited_df.iloc[3, :]["Team B Wins"] == False
):
    final_four_df_2 = pd.DataFrame(
        {
            "Team A": ["UConn"],
            "Team A Logo": [
                f"https://upload.wikimedia.org/wikipedia/en/b/b0/Connecticut_Huskies_logo.svg"
            ],
            "Team B": ["Miami FL"],
            "Team B Logo": [
                f"https://upload.wikimedia.org/wikipedia/commons/e/e9/Miami_Hurricanes_logo.svg"
            ],
        }
    )
elif (
    edited_df.iloc[1, :]["Team A Wins"] == True
    and edited_df.iloc[1, :]["Team B Wins"] == False
    and edited_df.iloc[3, :]["Team A Wins"] == False
    and edited_df.iloc[3, :]["Team B Wins"] == True
):
    final_four_df_2 = pd.DataFrame(
        {
            "Team A": ["UConn"],
            "Team A Logo": [
                f"https://upload.wikimedia.org/wikipedia/en/b/b0/Connecticut_Huskies_logo.svg"
            ],
            "Team B": ["Texas"],
            "Team B Logo": [
                f"https://upload.wikimedia.org/wikipedia/commons/8/8d/Texas_Longhorns_logo.svg"
            ],
        }
    )
elif (
    edited_df.iloc[1, :]["Team A Wins"] == False
    and edited_df.iloc[1, :]["Team B Wins"] == True
    and edited_df.iloc[3, :]["Team A Wins"] == False
    and edited_df.iloc[3, :]["Team B Wins"] == True
):
    final_four_df_2 = pd.DataFrame(
        {
            "Team A": ["Gonzaga"],
            "Team A Logo": [
                f"https://upload.wikimedia.org/wikipedia/en/b/bd/Gonzaga_Bulldogs_logo.svg"
            ],
            "Team B": ["Texas"],
            "Team B Logo": [
                f"https://upload.wikimedia.org/wikipedia/commons/8/8d/Texas_Longhorns_logo.svg"
            ],
        }
    )
elif (
    edited_df.iloc[1, :]["Team A Wins"] == False
    and edited_df.iloc[1, :]["Team B Wins"] == True
    and edited_df.iloc[3, :]["Team A Wins"] == True
    and edited_df.iloc[3, :]["Team B Wins"] == False
):
    final_four_df_2 = pd.DataFrame(
        {
            "Team A": ["Gonzaga"],
            "Team A Logo": [
                f"https://upload.wikimedia.org/wikipedia/en/b/bd/Gonzaga_Bulldogs_logo.svg"
            ],
            "Team B": ["Miami FL"],
            "Team B Logo": [
                f"https://upload.wikimedia.org/wikipedia/commons/e/e9/Miami_Hurricanes_logo.svg"
            ],
        }
    )
else:
    if not warning:
        st.warning("You have not select the all team or you selected multiple teams!")

final_four = pd.concat([final_four_df, final_four_df_2], axis=0).reset_index()

if len(final_four) == 2:
    with st.echo("below"):
        final_four_editable = st.dataframe(
            final_four,
            column_config={
                "Date": st.column_config.DateColumn(),
                "Team A Logo": st.column_config.ImageColumn(""),
                "Team B Logo": st.column_config.ImageColumn(""),
            },
            hide_index=True,
        )
