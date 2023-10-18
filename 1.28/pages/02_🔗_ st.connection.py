import streamlit as st

def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )
    
st.set_page_config("st.connection Demo", "🔗", layout="wide")
icon("🔗")

st.title("st.connection Demo", anchor=False)
# st.caption(
#     """
#     With `st.connection()`, you can now connect data sources and APIs to your Streamlit app with a fraction of the code.
#     """
# )
st.info("You can now switch from **st.experimental_connection** to the more stable and officially supported **st.connection**. Learn more about [st.connection](https://docs.streamlit.io/).", icon="💡")
st.write("Learn more about `st.connection` in [<PLACEHOLDER_OUR_DOCS>](https://docs.streamlit.io/).")

tab1, tab2 = st.tabs([
    "🚀 With **st.connection**", 
    "🐢 How it worked before"
])

with tab1:
    st.info('With **st.connection**, fetch data directly without manual setup.', icon="ℹ️")

    st.markdown("#### Your credentials in the `.streamlit/secrets.toml` file:")

    st.code(
        """
        [connections.snowflake]
        user = "<username>"
        password = "<pass>"
        warehouse = "MY_WH"
        role = "MYROLE"
        account = "MY ACCOUNT ID"
        """, language="toml"
    )

    st.markdown("#### Your code in the `streamlit_app.py` file:")

    st.code(
        """
        import streamlit as st
        import pandas as pd

        @st.cache_resource
        def get_snowflake_connection():
            return st.connection("snowflake")

        @st.cache_data
        def fetch_pet_data(conn):
            return conn.query("SELECT species, weight FROM pets_table")

        # Connect and fetch data
        conn = get_snowflake_connection()
        pets_df = fetch_pet_data(conn)

        # Sidebar for species selection
        species_filter = st.sidebar.multiselect("Select species", pets_df['species'].unique())

        # Main app
        st.title("Average Pet Weight by Species")

        if species_filter:
            # Calculate average weights for selected species using pandas
            avg_weights = pets_df[pets_df['species'].isin(species_filter)].groupby('species')['weight'].mean()
            st.bar_chart(avg_weights)
        else:
            st.warning("Select species from the sidebar to see the average weights.", icon="⚠️")
        """, language="python"
    )


with tab2:
    st.info('Manually managing database connections and cursors.', icon="ℹ️")

    st.markdown("#### Your credentials in the `.streamlit/secrets.toml` file:")

    st.code(
        """
        [connections.snowflake]
        user = "<username>"
        password = "<pass>"
        warehouse = "MY_WH"
        role = "MYROLE"
        account = "MY ACCOUNT ID"
        """, language="toml"
    )

    st.markdown("#### Your code in the `streamlit_app.py` file:")

    st.code(
        """
        import streamlit as st
        import snowflake.connector

        @st.cache_resource
        def get_snowflake_connection():
            secrets = st.secrets["connections.snowflake"]
            conn = snowflake.connector.connect(
                user=secrets["user"],
                password=secrets["password"],
                warehouse=secrets["warehouse"],
                role=secrets["role"],
                account=secrets["account"]
            )
            return conn

        @st.cache_data
        def fetch_pet_data(conn):
            cur = conn.cursor()
            cur.execute("SELECT species, weight FROM pets_table")
            rows = cur.fetchall()
            cur.close()
            return pd.DataFrame(rows, columns=["species", "weight"])

        # Connect and fetch data
        conn = get_snowflake_connection()
        pets_df = fetch_pet_data(conn)

        # Sidebar for species selection
        species_filter = st.sidebar.multiselect("Select species", pets_df['species'].unique())

        # Main app
        st.title("Average Pet Weight by Species")

        if species_filter:
            # Calculate average weights for selected species using pandas
            avg_weights = pets_df[pets_df['species'].isin(species_filter)].groupby('species')['weight'].mean()
            st.bar_chart(avg_weights)
        else:
            st.warning("Select species from the sidebar to see the average weights.", icon="⚠️")

        # Close the connection
        conn.close()
        """, language="python"
    )
