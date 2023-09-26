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
    df['Average House Price'] = df['Average House Price'].str.replace('$', '').str.replace(',', '').astype(int)
    df['Median Income'] = df['Median Income'].str.replace('$', '').str.replace(',', '').astype(int) 
    
    sorted_regions = df.groupby('Region in the US')['Average House Price'].mean().sort_values().index.tolist()
    df['Region in the US'] = pd.Categorical(df['Region in the US'], categories=sorted_regions, ordered=True)
    df = df.sort_values('Region in the US')

    # Create income buckets
    income_bins = [0, 50000, 100000, 150000, 200000, float('inf')]
    income_labels = ['<50k', '50k-100k', '100k-150k', '150k-200k', '200k+']
    df['Income Bucket'] = pd.cut(df['Median Income'], bins=income_bins, labels=income_labels, right=False)

    df['Income Bucket'] = pd.Categorical(df['Income Bucket'], categories=income_labels, ordered=True)
    df = df.sort_values('Income Bucket')

    return df

df = load_data()

df['Region in the US'] = df['Region in the US'].astype(str)

with st.expander("Dataset"):
    st.dataframe(df)

tab1, tab2 = st.tabs(
    [
        "Multi-Dimensional Analysis",
        "Scatter Basics"
    ]
)

with tab1:
    st.subheader("Dynamic Scatter Chart", anchor=False)
    st.caption("Dynamic scatter plot where you can choose the dimensions for X-axis, Y-axis, color, and size.")

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
            df = pd.read_csv('1.27/pages/data_simplified.csv')
            df['Average House Price'] = df['Average House Price'].str.replace('$', '').str.replace(',', '').astype(int)
            df['Median Income'] = df['Median Income'].str.replace('$', '').str.replace(',', '').astype(int) 
            
            sorted_regions = df.groupby('Region in the US')['Average House Price'].mean().sort_values().index.tolist()
            df['Region in the US'] = pd.Categorical(df['Region in the US'], categories=sorted_regions, ordered=True)
            df = df.sort_values('Region in the US')
        
            # Create income buckets
            income_bins = [0, 50000, 100000, 150000, 200000, float('inf')]
            income_labels = ['<50k', '50k-100k', '100k-150k', '150k-200k', '200k+']
            df['Income Bucket'] = pd.cut(df['Median Income'], bins=income_bins, labels=income_labels, right=False)
        
            df['Income Bucket'] = pd.Categorical(df['Income Bucket'], categories=income_labels, ordered=True)
            df = df.sort_values('Income Bucket')
        
            return df

        df = load_data()

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
        """
    )

with tab2:
    st.subheader("Average Rent vs Region in the US", anchor=False)
    st.caption("This chart shows some positive correlation between Average Rent and Region in the US.")
    st.scatter_chart(
        df,
        x='Average Rent',
        y='Region in the US',
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
            df = pd.read_csv('1.27/pages/data_simplified.csv')
            df['Average House Price'] = df['Average House Price'].str.replace('$', '').str.replace(',', '').astype(int)
            df['Median Income'] = df['Median Income'].str.replace('$', '').str.replace(',', '').astype(int) 
            
            sorted_regions = df.groupby('Region in the US')['Average House Price'].mean().sort_values().index.tolist()
            df['Region in the US'] = pd.Categorical(df['Region in the US'], categories=sorted_regions, ordered=True)
            df = df.sort_values('Region in the US')
        
            # Create income buckets
            income_bins = [0, 50000, 100000, 150000, 200000, float('inf')]
            income_labels = ['<50k', '50k-100k', '100k-150k', '150k-200k', '200k+']
            df['Income Bucket'] = pd.cut(df['Median Income'], bins=income_bins, labels=income_labels, right=False)
        
            df['Income Bucket'] = pd.Categorical(df['Income Bucket'], categories=income_labels, ordered=True)
            df = df.sort_values('Income Bucket')
        
            return df

        df = load_data()

        st.scatter_chart(
            df,
            x='Average Rent',
            y='Region in the US',
            height=600,
            use_container_width=True
        )
        """
    )
