import streamlit as st

def show():
    st.markdown("# Hamburger Menu Configuration")
    st.write("-------------------------------------------------------------------------------")

    st.write("""
    The latest version of the hamburger menu allows developers to configure their menu items for the user.
    """)

    col1, col2 = st.columns(2)
    col1.image("0.89/demos/original.png", caption="The grey section offers developer-specific features")
    col2.image("0.89/demos/original_viewer.png", caption="Visitors of the app will see a simplified menu")

    st.write("-------------------------------------------------------------------------------")

    st.write("""
    ## Configuring the Menu
    
    In addition to developer-specific menu items, we allow developers to override the menu items for
    "Report a bug" and "Get help" with their own custom links or completely remove them.""")

    st.code("""
    get_help_link = https://support.google.com/googlenest/troubleshooter/7211062?hl=en
    menu_items = {'Get help': get_help_link}
    st.set_page_config(menu_items=menu_items)
    """)

    st.caption("Perhaps you should check out our Get help & Report a bug links 😉!")
    
    st.write("""You can also update the content inside the About dialog with Markdown!""")

    st.code("""
    about_info = ''' ## My Custom App 
    This app uses our ML model to demostrate churn prediction '''
    menu_items = {'About': about_info}
    st.set_page_config(menu_items=menu_items)
    """)

    st.image("0.89/demos/about.jpeg", caption="Example about dialog. Tip: Check out the About dialog for this app!")

    