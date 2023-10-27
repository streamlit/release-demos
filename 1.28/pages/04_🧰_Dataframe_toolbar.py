import pandas as pd
import streamlit as st
import base64

@st.cache_data
def get_file_url(path):
    file_ = open(path, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    return data_url

def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )
    
st.set_page_config("Toolbar for dataframes demo", "🧰", layout="wide")
icon("🧰")

st.title("Toolbar for dataframes demo", anchor=False)
st.write("Check out the new toolbar on top of `st.dataframe` and `st.data_editor` that lets you add and delete rows, download your data as a CSV, and search your data. Check out our [updated Dataframes guide](https://docs.streamlit.io/library/advanced-features/dataframes).")

tab1, tab2, tab3 = st.tabs([
    "🚣‍♀️ Add and delete rows", 
    "📥 Download data as a CSV",
    "🔎 Search your data ",
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
    file_url = get_file_url('/mount/src/release-demos/1.28/pages/add_delete.gif')
    st.markdown(
        f'<img src="data:image/gif;base64,{file_url}" width=1000 alt="demo gif">',
        unsafe_allow_html=True,
    )

with tab2:
    file_url = get_file_url('/mount/src/release-demos/1.28/pages/download.gif')
    st.markdown(
        f'<img src="data:image/gif;base64,{file_url}" width=1000 alt="demo gif">',
        unsafe_allow_html=True,
    )

with tab3:
    file_url = get_file_url('/mount/src/release-demos/1.28/pages/search.gif')
    st.markdown(
        f'<img src="data:image/gif;base64,{file_url}" width=1000 alt="demo gif">',
        unsafe_allow_html=True,
    )

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
