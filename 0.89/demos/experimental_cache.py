import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .db import RNA

def show():
    st.markdown("# Experimental Cache Primitives")
    st.markdown("### @st.experimental_memo")

    st.write("**Caches expensive computation.** It is *much faster* than `@st.cache`. (Like: an order of magnitude faster in many cases).")

    st.write("It has the same basic API as `@st.cache`:")

    with st.echo():
        @st.experimental_memo
        def read_csv(path) -> pd.DataFrame:
            return pd.read_csv(path)

        df = read_csv("0.89/demos/browser_data.csv")

    st.write("It does *not* support `hash_funcs`. Instead, unhashable function parameters must be prefixed with '_' to prevent hashing:")

    with st.echo():
        @st.experimental_memo
        def get_database_results(_sessionmaker, page_size, page):
            # The _sessionmaker parameter will not be hashed
            pass

    with st.expander("What makes a parameter hashable?"):
        st.markdown("""In general, **hashable parameters are composed of pure data**.
        Basic Python datatypes (primitives, lists, dicts, etc), files, numpy
        and pandas types - these are all hashable. Custom objects are generally
        *not* hashable.""")

    st.write(
        "Under the hood, it uses `pickle` to store cached data. "
        "You can mutate the results of a memoized function without changing the cache:")

    with st.echo():
        @st.experimental_memo
        def expensive_computation():
            return [1, 2, 3]

        # Retrieve a memoized result and mutate it
        result = expensive_computation()
        result.append([4, 5, 6])

        # Subsequent calls return the original result
        assert(expensive_computation() == [1, 2, 3])

    st.markdown("### @st.experimental_singleton")

    st.write("A **global key-value store** for non-data objects: database connections, TensorFlow sessions, etc. Use it for *non-serializable* data.")

    st.write("It also has a similar API to `@st.cache`:")

    with st.echo():
        @st.experimental_singleton
        def get_db_sessionmaker(url: str) -> sessionmaker:
            """Create a singleton SQLAlchemy sessionmaker to connect to a database"""
            engine = create_engine(url)
            return sessionmaker(engine)

    st.markdown("## 🥒 memo + singleton demo")

    st.markdown(f"""
    Browse RNA sequences from the public [RNAcentral Postgres database](https://rnacentral.org/help/public-database).
    - `@st.experimental_singleton` stores a singleton SQLAlchemy database connection
    - The pickle-based `@st.experimental_memo` decorator caches query results.
    """)

    st.markdown("""
    ### Connecting to the database
    We use `@st.experimental_singleton` to create a single SQLAlchemy engine that will be shared 
    across all sessions and runs.
    """)

    with st.expander("Toggle code"):
        with st.echo():
            @st.experimental_singleton
            def get_db_sessionmaker() -> sessionmaker:
                # This is a publicly-accessible read-only database. We wouldn't
                # normally stick db creds in our code :)
                DB_URL = "postgresql://reader:NWDMCE5xdipIjRrp@hh-pgsql-public.ebi.ac.uk:5432/pfmegrnargs"
                engine = create_engine(DB_URL)
                return sessionmaker(engine)

    st.markdown("""
    ### Querying the database
    The `get_page` function queries the database and caches its results. Because
    `@st.experimental_memo` cannot hash SQLAlchemy `sessionmaker` objects, we prefix the
    `_sessionmaker` argument name with "_". 
    """)

    with st.expander("Toggle code"):
        with st.echo():
            @st.experimental_memo
            def get_page(_sessionmaker, page_size: int, page: int) -> pd.DataFrame:
                """Retrieve rows from the RNA database, and cache them.

                Parameters
                ----------
                _sessionmaker : a SQLAlchemy session factory. Because this arg name is
                    prefixed with "_", it won't be hashed.
                page_size : the number of rows in a page of result
                page : the page number to retrieve

                Returns
                -------
                pandas.DataFrame
                    A DataFrame containing the retrieved rows. Mutating it won't affect
                    the cache.
                """
                with _sessionmaker() as session:
                    query = (
                        session
                            .query(RNA.id, RNA.seq_short, RNA.seq_long, RNA.len, RNA.upi)
                            .order_by(RNA.id)
                            .offset(page_size * page)
                            .limit(page_size)
                    )
                    return pd.read_sql(query.statement, query.session.bind)

    st.markdown("""
    ### Results
    We retrieve and display a single 1000-row "page" at a time. Pages that are
    already cached will return more quickly, because they don't require a database
    query.
    """)

    PAGE_SIZE = 1000

    # Prompt for the results page
    page = int(st.number_input(
        f"Select page ({PAGE_SIZE} results/page):", min_value=0)
    )

    # Run the query and show the results
    results = get_page(get_db_sessionmaker(), page_size=PAGE_SIZE, page=page)
    st.write(results)

    # (It's safe to mutate results - it won't affect the cache.)
