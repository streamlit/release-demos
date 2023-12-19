import streamlit as st

st.set_page_config(
    page_title='st.connection',
    page_icon='🔌'
)

st.title("🔌 st.connection")

"""
We're very excited to release `st.connection()`, which makes it easy to connect your Streamlit apps to data and APIs with a fraction of the code.

With st.connection, connecting to a SQL database becomes just 4 lines of code:
"""

tab1, tab2 = st.tabs([
    "🚀 With st.connection",
    "🐢 How it worked before"
])

with tab1:
    st.code("""
import streamlit as st

conn = st.connection('pets_db', type='sql')
pet_owners = conn.query('select * from pet_owners')
st.dataframe(pet_owners)
    """, language='python'
    )

with tab2:
    "Compared to [Streamlit's original MySQL tutorial](https://web.archive.org/web/20230330050343/https://docs.streamlit.io/knowledge-base/tutorials/databases/mysql#write-your-streamlit-app)"

    st.code("""
import streamlit as st
import mysql.connector

@st.cache_resource
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()

@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from pet_owners;")
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")
""", language='python'
    )

"""

### What's included

st.connection includes:

- `st.connection()` factory method to initialize ready-to-use data connection objects
- Concrete implementations built into Streamlit for SQL and Snowpark
- Easy to install connections for [cloud file storage](https://github.com/streamlit/files-connection) and [Google Sheets](https://github.com/streamlit/gsheets-connection)
- An extendable `BaseConnection` class to easily build (and share) new connection types!

👈 Pick a data source to see how easy it is!

[Learn more in the API docs.](https://docs.streamlit.io/library/api-reference/connections)
"""
