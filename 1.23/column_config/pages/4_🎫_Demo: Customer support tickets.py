import pandas as pd
import streamlit as st
from utils import icon

st.set_page_config("Customer Support Tickets", "🎫")
icon("🎫")
"""
# Customer support tickets

This table shows customer support tickets. You can change the status, priority, and 
agent. This demo mostly focuses on using column config for editing behavior in 
`st.data_editor`.

Column config features used:

- Disabling editing for specific columns
- Setting options for categorical/selectbox columns
- Setting default values for new rows and making columns required

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
        "date_created": [
            "2023-04-01 09:00",
            "2023-04-02 14:30",
            "2023-04-04 10:15",
            "2023-04-05 16:45",
            "2023-04-06 11:20",
        ],
        "date_first_reviewed": [
            "2023-04-01 09:00",
            "2023-04-02 14:30",
            "2023-04-04 10:15",
            "2023-04-05 16:45",
            "2023-04-06 11:20",
        ],
        "date_last_reviewed": [
            "2023-04-01 09:00",
            "2023-04-02 14:30",
            "2023-04-04 10:15",
            "2023-04-05 16:45",
            "2023-04-06 11:20",
        ],
        "agent": ["Frank", "Grace", "Heidi", "Ivan", "Judy"],
    }
)

with st.echo("below"):
    edited_data = st.data_editor(
        data,
        use_container_width=True,
        column_config={
            "id": st.column_config.Column("ID", disabled=True),
            "issue": st.column_config.Column("Issue", disabled=True),
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
            "date_created": st.column_config.Column("Date Created", disabled=True),
            "date_first_reviewed": st.column_config.Column(
                "Date First Reviewed", disabled=True
            ),
            "date_last_reviewed": st.column_config.Column(
                "Date Last Reviewed", disabled=True
            ),
            "agent": st.column_config.Column("Agent", required=True),
        },
        num_rows="dynamic",
        column_order=(
            "id",
            "issue",
            "status",
            "priority",
            "agent",
            "date_created",
            "date_first_reviewed",
            "date_last_reviewed",
        ),
    )


with st.expander("Edited Data"):
    "This is the dataframe returned by the data editor:"
    st.dataframe(edited_data, use_container_width=True)
