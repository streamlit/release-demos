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
    df = pd.DataFrame({
        'Sales': np.random.randint(100, 1000, 20),
        'Customer_Rating': np.random.uniform(1, 5, 20),
        'Stock_Level': np.random.randint(0, 50, 20),
        'Season': np.random.choice(["Spring", "Summer", "Fall", "Winter"], 20)
    })
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
    st.info("Basic scatter plot showing the relationship between Sales and Customer Ratings.", icon="💡")
    st.scatter_chart(
        chart_data,
        x="Sales",
        y="Customer_Rating"
    )
    st.code(
        """
        @st.cache_data
        def load_data():
            df = pd.DataFrame({
                'Sales': np.random.randint(100, 1000, 20),
                'Customer_Rating': np.random.uniform(1, 5, 20),
                'Stock_Level': np.random.randint(0, 50, 20),
                'Season': np.random.choice(["Spring", "Summer", "Fall", "Winter"], 20)
            })
            return df

        chart_data = load_data()

        st.scatter_chart(
            chart_data,
            x="Sales",
            y="Customer_Rating"
        )
        """
    )

with tab2:
    st.info("Seasonally-filtered scatter plot of Sales vs Customer Ratings, colored by Stock Levels.", icon="💡")
    
    selected_season = st.selectbox("Choose a season:", ["All", "Spring", "Summer", "Fall", "Winter"], key="season_tab2")
    if selected_season != "All":
        chart_data_filtered = chart_data[chart_data["Season"] == selected_season].reset_index(drop=True)
    else:
        chart_data_filtered = chart_data.reset_index(drop=True)

    x_axis = "Sales"
    y_axis = "Customer_Rating"
    color_dim = "Stock_Level" 

    st.scatter_chart(
        chart_data_filtered,
        x=x_axis,
        y=y_axis,
        color=color_dim 
    )
    st.code(
        """
        @st.cache_data 
        def load_data():
            df = pd.DataFrame({
                'Sales': np.random.randint(100, 1000, 20),
                'Customer_Rating': np.random.uniform(1, 5, 20),
                'Stock_Level': np.random.randint(0, 50, 20),
                'Season': np.random.choice(["Spring", "Summer", "Fall", "Winter"], 20)
            })
            return df

        chart_data = load_data()
        selected_season = st.selectbox("Choose a season:", ["All", "Spring", "Summer", "Fall", "Winter"], key="season_tab2")

        # Filter data based on selected season
        if selected_season != "All": 
            chart_data_filtered = chart_data[chart_data["Season"] == selected_season].reset_index(drop=True)
        else:
            chart_data_filtered = chart_data.reset_index(drop=True)

        x_axis = "Sales"
        y_axis = "Customer_Rating"
        color_dim = "Stock_Level"
        st.scatter_chart(
            chart_data_filtered,
            x=x_axis,
            y=y_axis,
            color=color_dim 
        )
        """
    )

with tab3:
    st.info("Dynamic scatter plot where you can choose the dimensions for X-axis, Y-axis, color, and size.", icon="💡")
    
    col1, col2, col3, col4 = st.columns(4)

    x_axis = col1.selectbox('X-axis:', chart_data.columns, index=0)
    y_axis = col2.selectbox('Y-axis:', chart_data.columns, index=1)
    color_dim = col3.selectbox('Color:', chart_data.columns, index=3)
    size_dim = col4.selectbox('Size:', chart_data.columns, index=2)

    st.scatter_chart(
        chart_data,
        x=x_axis,
        y=y_axis,
        color=color_dim,
        size=size_dim
    )
    st.code(
        """
        @st.cache_data
        def load_data():
            df = pd.DataFrame({
                'Sales': np.random.randint(100, 1000, 20),
                'Customer_Rating': np.random.uniform(1, 5, 20),
                'Stock_Level': np.random.randint(0, 50, 20),
                'Season': np.random.choice(["Spring", "Summer", "Fall", "Winter"], 20)
            })
            return df

        chart_data = load_data()

        # User-controlled selectors for chart dimensions
        col1, col2, col3, col4 = st.columns(4)
        x_axis = col1.selectbox('X-axis:', chart_data.columns, index=0)
        y_axis = col2.selectbox('Y-axis:', chart_data.columns, index=1)
        color_dim = col3.selectbox('Color:', chart_data.columns, index=3)
        size_dim = col4.selectbox('Size:', chart_data.columns, index=2)

        st.scatter_chart(
            chart_data,
            x=x_axis,
            y=y_axis,
            color=color_dim,
            size=size_dim
        )
        """
    )
