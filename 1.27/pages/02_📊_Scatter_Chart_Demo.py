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
    df_candy = pd.read_csv('1.27/pages/census.csv')
    return df_candy

df = load_data()

with st.expander("Dataset"):
    st.dataframe(df)

tab1, tab2, tab3 = st.tabs(
    [
        "Scatter Basics", 
        "Custom Dimensions & Colors", 
        "Multi-Dimensional Analysis"
    ]
)

with tab1:
    st.subheader("Child Poverty Index vs Math Score", anchor=False)
    st.caption("There seems to be a correlation between a high math score and a low child poverty index and vice versa.")
    st.scatter_chart(
        df,
        x='Child Poverty Index',
        y='Math Score',
        use_container_width=True
    )
    st.code(
        """
        import streamlit as st
        import pandas as pd

        @st.cache_data
        def load_data():
            df_candy = pd.read_csv('./census.csv')
            return df_candy

        df = load_data()
        st.scatter_chart(
            df,
            x='Child Poverty Index',
            y='Math Score',
            use_container_width=True
        )
        """
    )

with tab2:
    st.subheader("Child Poverty Index vs Math Score", anchor=False)
    st.caption("There seems to be a correlation between high math score, low child poverty index and high human rights council democracy index.")
    st.scatter_chart(
        df,
        y='Math Score',
        x='Child Poverty Index',
        color='Human Rights Council Democracy Index',
        size='Country GDP per capita',
        use_container_width=True
    )
    st.code(
        """
        import streamlit as st
        import pandas as pd

        @st.cache_data
        def load_data():
            df_candy = pd.read_csv('./census.csv')
            return df_candy

        df = load_data()
        st.scatter_chart(
            df,
            y='Math Score',
            x='Child Poverty Index',
            color='Human Rights Council Democracy Index',
            size='Country GDP per capita',
            use_container_width=True
        )
        """
    )

with tab3:
    st.subheader("Dynamic Scatter Chart", anchor=False)
    st.caption("Dynamic scatter plot where you can choose the dimensions for X-axis, Y-axis, color, and size.")

    col1, col2, col3, col4 = st.columns(4)

    x_axis = col1.selectbox('X-axis:', df.columns, index=0)
    y_axis = col2.selectbox('Y-axis:', df.columns, index=1)
    color_dim = col3.selectbox('Color:', df.columns, index=3)
    size_dim = col4.selectbox('Size:', df.columns, index=2)

    st.scatter_chart(
        df,
        x=y_axis,
        y=x_axis,
        size=color_dim,
        use_container_width=True
    )
    st.code(
        """
        import streamlit as st
        import pandas as pd

        @st.cache_data
        def load_data():
            df_candy = pd.read_csv('./census.csv')
            return df_candy

        df = load_data()

        col1, col2, col3, col4 = st.columns(4)

        x_axis = col1.selectbox('X-axis:', df.columns, index=0)
        y_axis = col2.selectbox('Y-axis:', df.columns, index=1)
        color_dim = col3.selectbox('Color:', df.columns, index=3)
        size_dim = col4.selectbox('Size:', df.columns, index=2)

        st.scatter_chart(
            df,
            x=y_axis,
            y=x_axis,
            size=color_dim,
            use_container_width=True
        )
        """
    )
