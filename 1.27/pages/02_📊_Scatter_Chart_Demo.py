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
    df = pd.read_csv('1.27/pages/dataset.csv')
    return df

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
    st.caption("The relationship between Country's math scores and child poverty index appears strongly correlated.")
    st.scatter_chart(
        df,
        x='Child Poverty Index',
        y='Math Score',
        use_container_width=True
    )
    st.divider()
    st.code(
        """
        import streamlit as st
        import pandas as pd

        @st.cache_data
        def load_data():
            df = pd.read_csv('census.csv')
            return df

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
    st.caption("The relationship between country's math scores and child poverty index appears strongly correlated.")
    st.scatter_chart(
        df,
        y='Math Score',
        x='Child Poverty Index',
        color='Human Rights Council Democracy Index',
        use_container_width=True
    )
    st.caption("💡 A high Human Rights Council score means democratic and a low number means not democratic")
    st.divider()
    st.code(
        """
        import streamlit as st
        import pandas as pd

        @st.cache_data
        def load_data():
            df = pd.read_csv('census.csv')
            return df

        df = load_data()

        st.scatter_chart(
            df,
            y='Math Score',
            x='Child Poverty Index',
            color='Human Rights Council Democracy Index',
            use_container_width=True
        )
        """
    )

with tab3:
    st.subheader("Dynamic Scatter Chart", anchor=False)
    st.caption("Dynamic scatter plot where you can choose the dimensions for X-axis, Y-axis, color, and size.")

    col1, col2, col3, col4 = st.columns(4)

    x_axis = col1.selectbox('X-axis:', df.columns, index=3, disabled=True)
    y_axis = col2.selectbox('Y-axis:', df.columns, index=1)
    color_dim = col3.selectbox('Color:', df.columns, index=6)
    size_dim = col4.selectbox('Size:', df.columns, index=4)

    st.scatter_chart(
        df,
        x=x_axis,
        y=y_axis,
        color=color_dim,
        size=size_dim,
        use_container_width=True
    )
    st.divider()
    st.code(
        """
        import streamlit as st
        import pandas as pd

        @st.cache_data
        def load_data():
            df = pd.read_csv('dataset.csv')
            return df

        df = load_data()

        col1, col2, col3, col4 = st.columns(4)

        x_axis = col1.selectbox('X-axis:', df.columns, index=3, disabled=True)
        y_axis = col2.selectbox('Y-axis:', df.columns, index=1)
        color_dim = col3.selectbox('Color:', df.columns, index=6)
        size_dim = col4.selectbox('Size:', df.columns, index=4)

        st.scatter_chart(
            df,
            x=x_axis,
            y=y_axis,
            color=color_dim,
            size=size_dim,
            use_container_width=True
        )
        """
    )
