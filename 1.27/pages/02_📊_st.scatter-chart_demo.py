import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title='st.scatter_chart demo',
    page_icon='📊',
    layout="wide"
)

st.title("📊 Scatter Chart Demo", anchor=False)

@st.cache_data
def load_data():
    df = pd.DataFrame(np.random.randn(20, 3), columns=["col1", "col2", "col3"])
    df["col4"] = np.random.choice(["A", "B", "C"], 20)
    return df


chart_data = load_data()

tab1, tab2, tab3 = st.tabs(
    [
        "Scatter Basics", 
        "Custom Dimensions & Colors", 
        "Multi-Dimensional Analysis"
    ]
)

with tab1:
    st.info("Simple scatter plot showcasing random data points.", icon="💡")
    st.scatter_chart(
        chart_data,
        x="col1",
        y="col2"
    )
    st.code(
        """
        @st.cache_data
        def load_data():
            df = pd.DataFrame(np.random.randn(20, 3), columns=["col1", "col2", "col3"])
            df["col4"] = np.random.choice(["A", "B", "C"], 20)
            return df
        chart_data = load_data()
        st.scatter_chart(
            chart_data,
            x="col1",
            y="col2"
        )
        """
    )


with tab2:
    st.info("Customized scatter plot with color and size variations.", icon="💡")
    st.scatter_chart(
        chart_data,
        x="col1",
        y="col2",
        color="col4",
        size="col3",
    )
    st.code(
        """
        @st.cache_data
        def load_data():
            df = pd.DataFrame(np.random.randn(20, 3), columns=["col1", "col2", "col3"])
            df["col4"] = np.random.choice(["A", "B", "C"], 20)
            return df
        chart_data = load_data()
        st.scatter_chart(
            chart_data,
            x="col1",
            y="col2",
            color="col4",
            size="col3",
        )
        """
    )

with tab3:
    st.info("Two-dimensional scatter plot with distinct color codes.", icon="💡")
    st.scatter_chart(
        chart_data,
        x="col1",
        y=["col2", "col3"],
        size="col4",
        color=["#FF0000", "#0000FF"],  # Optional
    )
    st.code(
        """
        @st.cache_data
        def load_data():
            df = pd.DataFrame(np.random.randn(20, 3), columns=["col1", "col2", "col3"])
            df["col4"] = np.random.choice(["A", "B", "C"], 20)
            return df
        chart_data = load_data()
        st.scatter_chart(
            chart_data,
            x="col1",
            y=["col2", "col3"],
            size="col4",
            color=["#FF0000", "#0000FF"],  # Optional
        )
        """
    )
