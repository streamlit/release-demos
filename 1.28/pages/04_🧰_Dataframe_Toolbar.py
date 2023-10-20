import pandas as pd
import streamlit as st


def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )

    
st.set_page_config("Toolbar for dataframes demo", "🧰", layout="wide")
icon("🧰")

st.title("Toolbar for dataframes demo", anchor=False)
st.write("Check out the new toolbar on top of st.dataframe and st.data_editor that lets you add and delete rows, download your data as a CSV, and search your data.")
st.info("Learn more about dataframes in [<PLACEHOLDER_OUR_DOCS>](https://docs.streamlit.io/).", icon="📖")

tab1, tab2, tab3 = st.tabs([
    "🚣‍♀️ Add/Delete row", 
    "📥 Download table as a CSV",
    "🔎 Search the table ",
])

data = pd.DataFrame(
    {
        "id": ["TCK-1001", "TCK-1002", "TCK-1003", "TCK-1004", "TCK-1005"],
        "issue": [
            "Payment not processed, order not placed",
            "App crashes on login",
            "Unable to reset password",
            "Missing order, tracking code not working",
            "Wrong item received",
        ],
        "status": ["Open", "In Progress", "Resolved", "In Progress", "Closed"],
        "priority": ["High", "Medium", "Low", "Urgent", "High"],
    }
)
with tab1:
    st.info('Now you can add/delete rows in a dataframe.', icon="ℹ️")
    st.image("1.28/pages/add_delete.gif")

with tab2:
    st.info('Downloading the dataframe as a CSV file.', icon="ℹ️")
    st.image("1.28/pages/download.gif")

with tab3:
    st.info('Searching through your dataframe.', icon="ℹ️")
    st.image("1.28/pages/search.gif")

st.info("Give it a spin with this dataframe.", icon="👇")
edited_data = st.data_editor(
    data,
    use_container_width=True,
    column_config={
        "id": st.column_config.Column("ID"),
        "issue": st.column_config.Column("Issue"),
        "status": st.column_config.SelectboxColumn(
            "Status",
            options=["Open", "In Progress", "Resolved", "Closed"],
            default="Open",
            required=True,
        ),
        "priority": st.column_config.SelectboxColumn(
            "Priority",
            options=["Low", "Medium", "High", "Urgent"],
            default="Medium",
            required=True,
        ),
    },
    num_rows="dynamic",
    column_order=(
        "id",
        "issue",
        "status",
        "priority",
    ),
)

# with st.expander("Edited Data"):
#     "This is the dataframe returned by the data editor:"
#     st.dataframe(edited_data, use_container_width=True)

st.code(
    """
    data = pd.DataFrame(
        {
            "id": ["TCK-1001", "TCK-1002", "TCK-1003", "TCK-1004", "TCK-1005"],
            "issue": [
                "Payment not processed, order not placed",
                "App crashes on login",
                "Unable to reset password",
                "Missing order, tracking code not working",
                "Wrong item received",
            ],
            "status": ["Open", "In Progress", "Resolved", "In Progress", "Closed"],
            "priority": ["High", "Medium", "Low", "Urgent", "High"],
        }
    )
    
    edited_data = st.data_editor(
        data,
        use_container_width=True,
        column_config={
            "id": st.column_config.Column("ID"),
            "issue": st.column_config.Column("Issue"),
            "status": st.column_config.SelectboxColumn(
                "Status",
                options=["Open", "In Progress", "Resolved", "Closed"],
                default="Open",
                required=True,
            ),
            "priority": st.column_config.SelectboxColumn(
                "Priority",
                options=["Low", "Medium", "High", "Urgent"],
                default="Medium",
                required=True,
            ),
        },
        num_rows="dynamic",
        column_order=(
            "id",
            "issue",
            "status",
            "priority",
        ),
    )
    """
)
