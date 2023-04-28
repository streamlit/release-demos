import streamlit as st

from snowflake.snowpark.functions import col
import pandas as pd

st.set_page_config(
    page_title='st.connection for Snowpark',
    page_icon='🏂'
)

st.title('🏂 st.connection for Snowpark')

"""
Snowpark connection API is shown here, but won't work in the Cloud app since it needs local Snowflake credentials.
To use it, you can:
- Clone [this app](https://github.com/sfc-gh-jcarroll/st-connection-prpr) locally
- Install the [whl file](https://core-previews.s3-us-west-2.amazonaws.com/pr-6457/streamlit-1.21.0-py2.py3-none-any.whl)
  and do `pip install snowflake-snowpark-python` (or equivalent)
  - If you have [pipenv](https://pipenv.pypa.io/en/latest/) installed, just do `pipenv sync`
- Set up local credentials for your Snowflake account.
"""

with st.expander("Examples of local Snowpark credentials setup"):
    st.code("""
# .streamlit/secrets.toml
[connections.snowpark]
type = "snowpark"
authenticator = "externalbrowser"
account = "[MYACCOUNT]"
user = "[username]"
role = "[MYROLE]"
warehouse = "[MYWAREHOUSE]"
    """, language = "toml")

    "Alternatively, you can use `~/.snowsql/config` (syntax is the same except the header)"
    st.code("""
# ~/.snowsql/config
[connections]
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

run_the_code = st.checkbox("Try running the code (requires local snowflake creds)")

st.subheader("Initialize a connection")
with st.echo():
    if run_the_code:
        conn = st.experimental_connection('snowpark')

        conn

st.subheader("query() for convenience")

"`conn.query()` will cache by default and return a pandas dataframe."

with st.expander("⚠️ **NOTE:** On query and native Snowpark dataframes"):
    """
    - `conn.query()` returns a pandas dataframe, meaning that any further calculations or transformations
      will run in the app execution thread directly. This might be fine for initial prototyping or smaller scale
      use cases.
    - However in many cases, it will be faster to run processing natively in a Snowpark Dataframe, particularly for
      large data sets or intensive use cases. In this case, you will need to use `conn.Session()` as described below.
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

st.subheader("session for full operations")
"Use `conn.session` to get the underlying Snowpark Session for more advanced (and often faster) operations."

"You may want to wrap this in a function with `@st.cache_data` to be even faster!"
with st.echo():
    if run_the_code:
        sess = conn.session
        local_df = pd.DataFrame({"OWNER": ["jerry", "barbara", "alex"], "PET": ["fish", "cat", "puppy"], "COUNT": [4, 2, 1]})
        snow_df = sess.create_dataframe(local_df)
        snow_df = snow_df.filter(col('COUNT') > 1)
        st.dataframe(snow_df)

st.subheader("safe_session() for thread safety")
"Since Snowpark Session isn't natively thread safe, use `conn.safe_session()` in a `with` block to get a safe version."

"You may want to wrap this in a function with `@st.cache_data` to be even faster!"
with st.echo():
    if run_the_code:
        with conn.safe_session() as session:
            local_df = pd.DataFrame({"OWNER": ["jerry", "barbara", "alex"], "PET": ["fish", "cat", "puppy"], "COUNT": [4, 2, 1]})
            snow_df = session.create_dataframe(local_df)
            snow_df = snow_df.filter(col('COUNT') > 1)
            st.dataframe(snow_df)
