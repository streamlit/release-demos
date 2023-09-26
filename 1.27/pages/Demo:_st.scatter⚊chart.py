import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='st.scatter_chart demo',
    page_icon='📊',
    layout="wide"
)

st.title("📊 Scatter Chart Demo", anchor=False)

@st.cache_data
def load_data():
    df = pd.read_csv('1.27/pages/data_simplified.csv')
    df = df.sort_values(by=['Median Income'])
    st.write(df)
    return df

df = load_data()

with st.expander("Dataset"):
    st.dataframe(df)

tab1, tab2, tab3 = st.tabs(
    [
        "Multi-Dimensional Analysis",
        "Custom Dimensions & Colors",
        "Scatter Basics"
    ]
)

with tab1:
    st.subheader("Dynamic Scatter Chart", anchor=False)
    st.caption("Choose the dimensions for the chart's x-axis, y-axis, color, and size to explore the relationship between the geographic region of the US, average house price, average rent, and median income.") 

    col1, col2, col3, col4 = st.columns(4)

    x_axis = col1.selectbox('X-axis:', df.columns, index=3, disabled=True)
    y_axis = col2.selectbox('Y-axis:', df.columns, index=0)
    color_dim = col3.selectbox('Color:', df.columns, index=2)
    size_dim = col4.selectbox('Size:', df.columns, index=1)

    st.scatter_chart(
        df,
        x=x_axis,
        y=y_axis,
        color=color_dim,
        size=size_dim,
        height=600,
        use_container_width=True
    )
    st.divider()
    st.code(
        """
        import streamlit as st
        import pandas as pd

        @st.cache_data
        def load_data():
            df = pd.read_csv('data_simplified.csv')
            return df

        df = load_data()

        col1, col2, col3, col4 = st.columns(4)

        x_axis = col1.selectbox('X-axis:', df.columns, index=5, disabled=True)
        y_axis = col2.selectbox('Y-axis:', df.columns, index=4)
        color_dim = col3.selectbox('Color:', df.columns, index=1)
        size_dim = col4.selectbox('Size:', df.columns, index=3)

        st.scatter_chart(
            df,
            x=x_axis,
            y=y_axis,
            color=color_dim,
            size=size_dim,
            height=600,
            use_container_width=True
        )
        """
    )

# with tab2:
#     st.subheader("Region in the US vs Average House price", anchor=False)
#     st.caption("The chart shows some minimal correlation between Region in the US and Average House Price.")
#     st.scatter_chart(
#         df,
#         x='Region in the US',
#         y='Average House Price',
#         color='Rank',
#         height=800,
#         use_container_width=True
#     )
#     st.caption("💡 Rank is by housing price")
#     st.divider()
#     st.code(
#         """
#         import streamlit as st
#         import pandas as pd

#         @st.cache_data
#         def load_data():
#             df = pd.read_csv('data_simplified.csv')
#             return df

#         df = load_data()

#         st.scatter_chart(
#             df,
#             x='Region in the US',
#             y='Average House Price',
#             color='Rank',
#             height=800,
#             use_container_width=True
#         )
#         """
#     )

# with tab3:
#     st.subheader("Average Rent vs Region in the US", anchor=False)
#     st.caption("This chart shows some positive correlation between Average Rent and Region in the US.")
#     st.scatter_chart(
#         df,
#         x='Average Rent',
#         y='Region in the US',
#         height=600,
#         use_container_width=True
#     )
#     st.divider()
#     st.code(
#         """
#         import streamlit as st
#         import pandas as pd

#         @st.cache_data
#         def load_data():
#             df = pd.read_csv('data_simplified.csv')
#             return df

#         df = load_data()

#         st.scatter_chart(
#             df,
#             x='Average Rent',
#             y='Region in the US',
#             height=600,
#             use_container_width=True
#         )
#         """
#     )
