import streamlit as st

st.set_page_config(
    page_title='Build your own Connection',
    page_icon='🏗️'
)

st.title('🏗️ Build your own Connection')


st.info("`BaseConnection` makes it easy to build, use and share your own connection implementations.", icon="💡")

"""
You can build your own Connection by extending the [built-in BaseConnection.](https://docs.streamlit.io/library/api-reference/connections/st.connections.baseconnection)
To demonstrate this, this app has a simple [DuckDB](https://duckdb.org/) Connection built in.
You can view the connection source code
[here](https://github.com/streamlit/release-demos/blob/master/1.22/st-connection/duckdb_connection/connection.py).
"""

"""
1. Create a new connection class that extends Streamlit's BaseConnection. It also needs the type
of the underlying connection object to be specified.

```python
from streamlit.connections import BaseConnection
import duckdb

class DuckDBConnection(BaseConnection[duckdb.DuckDBPyConnection])
```

2. Add a `_connect()` method that sets up and returns the underlying connection object. It can pull
secrets specific to the connection from the `self._secrets` property.

```python
def _connect(self, **kwargs) -> duckdb.DuckDBPyConnection:
    if 'database' in kwargs:
        db = kwargs.pop('database')
    else:
        db = self._secrets['database']
    return duckdb.connect(database=db, **kwargs)
```

3. Add a way to get the underlying connection object. BaseConnection has a `_instance` property that does this
by default. Most connections will want some domain-specific property or method that exposes this.

```python
def cursor(self) -> duckdb.DuckDBPyConnection:
    return self._instance.cursor()
```

4. Add any convenience read / getter methods. These should be wrapped with @st.cache_data by default,
and conform to the st.connection best practices.

```python
def query(self, query: str, ttl: int = 3600, **kwargs) -> pd.DataFrame:
    @cache_data(ttl=ttl)
    def _query(query: str, **kwargs) -> pd.DataFrame:
        cursor = self.cursor()
        cursor.execute(query, **kwargs)
        return cursor.df()
    
    return _query(query, **kwargs)
```

**:tada: That's it! You've implemented a minimal Connection class that is ready to be used with st.connection. :balloon:**
"""

with st.expander("To show it's that easy, see the DuckDB code running here :rocket:"):
    """
    You can view the DuckDB connection source code
    [here](https://github.com/streamlit/release-demos/blob/master/1.22/st-connection/duckdb_connection/connection.py).
    """

    with st.echo():
        from duckdb_connection import DuckDBConnection

        conn = st.connection("duckdb", type=DuckDBConnection, database=':memory:')
        conn

    "Let's insert some data with the underlying duckdb cursor"
    with st.echo():
        c = conn.cursor()
        # create a table
        c.execute("CREATE TABLE IF NOT EXISTS items(item VARCHAR, value DECIMAL(10,2), count INTEGER)")
        # drop any existing data from a prior run ;)
        c.execute("DELETE FROM items")
        # insert two items into the table
        c.execute("INSERT INTO items VALUES ('jeans', 20.0, 1), ('hammer', 42.2, 2)")
        # insert a row using prepared statements
        c.execute("INSERT INTO items VALUES (?, ?, ?)", ['laptop', 2000, 1])

    "Now check out the awesome convenience method!"

    with st.echo():
        df = conn.query("select * from items")
        st.dataframe(df)
