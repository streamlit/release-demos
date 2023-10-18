import pandas as pd
import streamlit as st


def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )

    
st.set_page_config("Toolbar for DataFrames Demo", "🧰")
icon("🧰")

st.title("Toolbar for DataFrames Demo", anchor=False)
st.caption("A toolbar on top of `st.dataframe` and `st.data_editor` that lets you add/delete rows, download as CSV, and search.")
st.write("Learn more about dataframes in [<PLACEHOLDER_OUR_DOCS>](https://docs.streamlit.io/).")

tab1, tab2, tab3 = st.tabs([
    "🚣‍♀️ Add/Delete row", 
    "📥 Download as CSV",
    "🔎 Search",
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
    st.info('Adding/deleting rows in a dataframe.', icon="ℹ️")
    st.image("1.28/pages/add_delete.gif")

with tab2:
    st.info('Downloading the dataframe as a CSV file.', icon="ℹ️")
    st.image("pages/download.gif")

with tab3:
    st.info('Searching through your dataframe.', icon="ℹ️")
    st.image("pages/search.gif")

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

with st.expander("Edited Data"):
    "This is the dataframe returned by the data editor:"
    st.dataframe(edited_data, use_container_width=True)

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
