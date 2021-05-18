import streamlit as st

def pagination():
    st.write(
        """
        ## 📑 Pagination
        
        Too much data to display? Using `st.session_state`, you can now have multiple 
        pages in your Streamlit app!
        """
    )
    if "page" not in st.session_state:
        st.session_state.page = 0
        
    st.write("Page", st.session_state.page)
    
    if st.session_state.page > 0:
        st.button("Previous page")
    if st.session_state.page < 4:
        st.button("Next page")