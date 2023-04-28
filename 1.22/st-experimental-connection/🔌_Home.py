import streamlit as st

st.set_page_config(
    page_title='st.connection Preview',
    page_icon='🔌'
)

st.title("🔌 Introducing st.connection")

"""
## Quickly and easily connect your app to data and APIs!

### Setting up connections is PAINFUL 🤕

Connecting to data sources and APIs is one of the most annoying parts when building data apps. It typically requires finding and installing
external packages, figuring out how to manage your credentials securely outside of code, and finding the right methods to get data out in
the format you need. Not forgetting the need to add Streamlit caching capabilities! For example you can see the 14 lines of code in our
[MySQL tutorial here](https://docs.streamlit.io/knowledge-base/tutorials/databases/mysql#write-your-streamlit-app) - using a mysql.connector,
st.cache_resource, st.cache_data, managing a cursor, and converting the row result format!

### Meet `st.connection` 🥂

We're very excited to release st.connection, which makes it easy to connect your Streamlit apps to data and APIs, with a fraction of the code.
With st.connection, the MySQL example above becomes just 4 lines of code:
"""

tab1, tab2 = st.tabs([
    "🚀 With st.connection",
    "🐢 Compare to today"
])

with tab1:
    st.code("""
import streamlit as st

conn = st.experimental_connection('pets_db', type='sql')
pet_owners = conn.query('select * from pet_owners')
st.dataframe(pet_owners)
    """, language='python'
    )

with tab2:
    "Sourced from [Streamlit's MySQL tutorial](https://docs.streamlit.io/knowledge-base/tutorials/databases/mysql#write-your-streamlit-app)"

    st.code("""
import streamlit as st
import mysql.connector

@st.experimental_singleton
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()

@st.experimental_memo(ttl=600)
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
- Concrete implementations in Streamlit for a few key data sources
- An extendable `BaseConnection` class to easily build (and share) new connection types!

Here are the included connections it supports today:

- Many SQL dialects (MySQL, Postgres, Snowflake, BigQuery, Microsoft SQL Server, ...)
- Snowflake Snowpark
- Cloud file storage (S3, GCS, Azure Blob Storage, ...)
- And more coming very very soon!

### View the code

Find the WIP feature code in [feature/st.experimental_connection branch](https://github.com/streamlit/streamlit/tree/feature/st.experimental_connection) of streamlit/streamlit
- [Connection classes](https://github.com/streamlit/streamlit/tree/feature/st.experimental_connection/lib/streamlit/connections)
- [Factory function](https://github.com/streamlit/streamlit/blob/feature/st.experimental_connection/lib/streamlit/runtime/connection_factory.py)

👈 Dive in

**This preview is shared for feedback purposes only and is not intended for any production-like use.**
"""
