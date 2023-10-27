import streamlit as st

def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )
    
st.set_page_config("st.connection demo", "🔗", layout="wide")
icon("🔗")

st.title("st.connection demo", anchor=False)
st.write("`st.connection` is now fully supported in Streamlit. Upgrade your apps that use the legacy `st.experimental_connection` feature today to enjoy the benefits of this newly released version. Get started building with `st.connection` by checking out [our docs](https://docs.streamlit.io/library/api-reference/connections/st.connection).")

tab1, tab2 = st.tabs([
    "🚀 With **`st.connection`**", 
    "🐢 How it worked before"
])

with tab1:
    st.write('With **`st.connection`**, connect to data sources and fetch data in just a few lines of code.')

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

    st.markdown("#### Your app code:")

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
    st.write('In this example, the database connections and cursors have been managed manually.')

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