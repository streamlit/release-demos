import streamlit as st

st.set_page_config(
    page_title='Snowflake Connections',
    page_icon='❄️'
)

st.title('❄️ Snowflake Connections')


st.info("`SnowflakeConnection` makes it easy to connect to Snowflake", icon="💡")

"""
A SnowflakeConnection example is shown here, but won't work in the Cloud app since it needs local Snowflake credentials.
To use it, you can:
- Clone [this app](https://github.com/streamlit/release-demos/tree/master/1.28/st-connection) locally
- Run `pip install "streamlit>=1.28" "snowflake-snowpark-python[pandas]"` or equivalent
- Set up local credentials for your Snowflake account.
"""

with st.expander("Examples of local Snowflake credentials setup"):
    st.code("""
# .streamlit/secrets.toml
[connections.snowflake]
type = "snowflake"
authenticator = "externalbrowser"
account = "[MYACCOUNT]"
user = "[username]"
role = "[MYROLE]"
warehouse = "[MYWAREHOUSE]"
    """, language = "toml")

    """
    *For questions on the required `account` value, see [here](https://docs.snowflake.com/en/user-guide/python-connector-api.html#label-account-format-info).
    Full list of supported parameters [here](https://docs.snowflake.com/en/user-guide/python-connector-api.html#connect).*
    """

"""
- View the [API Reference for SnowflakeConnection](https://docs.streamlit.io/library/api-reference/connections/st.connections.snowflakeconnection).
- View the [tutorial for connecting Streamlit to Snowflake](https://docs.streamlit.io/knowledge-base/tutorials/databases/snowflake).
"""

run_the_code = st.checkbox("Try running the code (requires local snowflake creds)")

st.subheader("Initialize a connection")
with st.echo():
    if run_the_code:
        conn = st.connection('snowflake')

        conn

st.subheader("query() for convenience")

"`conn.query()` will cache by default and return a pandas dataframe."

with st.expander("⚠️ **NOTE:** On query and native Snowpark dataframes"):
    """
    - `conn.query()` returns a pandas dataframe, meaning that any further calculations or transformations
      will run in the app execution thread directly. This might be fine for initial prototyping or smaller scale
      use cases.
    - However in many cases, it will be faster to run processing natively in a Snowpark Dataframe, particularly for
      large data sets or intensive use cases. In this case, you will need to use the Snowpark Session as described below.
    """

with st.echo():
    if run_the_code:
        query = """
            select 50 as high_fives, 25 as fist_bumps, 'Q1' as quarter
            union
            select 20 as high_fives, 35 as fist_bumps, 'Q2' as quarter
            union
            select 60 as high_fives, 30 as fist_bumps, 'Q3' as quarter
        """
        df = conn.query(query)
        st.dataframe(df)

st.subheader("session() for full operations")

"Use `conn.session()` in a `with` block to access a [Snowpark Session](https://docs.snowflake.com/en/developer-guide/snowpark/reference/python/session.html) for more advanced (and often faster) operations."

"You may want to wrap this in a function with `@st.cache_data` to be even faster!"
with st.echo():
    if run_the_code:
        from snowflake.snowpark.functions import col
        import pandas as pd
        with conn.session() as session:
            local_df = pd.DataFrame({"OWNER": ["jerry", "barbara", "alex"], "PET": ["fish", "cat", "puppy"], "COUNT": [4, 2, 1]})
            snow_df = session.create_dataframe(local_df)
            snow_df = snow_df.filter(col('COUNT') > 1)
            st.dataframe(snow_df)
