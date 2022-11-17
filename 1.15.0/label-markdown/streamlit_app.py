import streamlit as st
from PIL import Image

st.set_page_config(initial_sidebar_state="collapsed")

st.title(":gear: Widget Label Markdown Demo")

col1, col2 = st.columns(2, gap="large")
text_contents = '''This is some text'''

plain_table = """ Table:
| Syntax | Description || ----------- | ----------- || Header | Title || Paragraph | Text |
"""

table = """ Table:
| Syntax | Description |
| ----------- | ----------- |
| Header | Title |
| Paragraph | Text |
"""

plain_long_title = """
How would you like to be contacted?
What's your favorite code language?
Pick a Color:
"""

long_title = """
How would you like to be
[contacted](https://dictionary.cambridge.org/us/dictionary/english/contacted)?
What's your favorite `code` language? :computer:
**Pick** a *Color*: :rainbow:
"""

corgi = Image.open("1.15.0/label-markdown/corgi.jpeg")

img_title = "This is an image: ![Corgi](corgi)"


with col1:
    st.header("Regular Labels:")
    st.color_picker('Instructions: Pick a Color:', '#3E55CB')
    st.selectbox("How would you like to be contacted?",
        ("Corgi Stampede", "Home phone", "Mobile phone"))
    st.metric(label="Temperature", value="105 °F", delta=None)
    st.checkbox("Agree to the thing")
    st.text_input('Share a thought:', 'Donations welcome')
    st.download_button('Download random text', text_contents)
    st.radio( "What's your favorite coding language?",
        ('Python', 'Javascript', 'Ruby'))
    st.multiselect(
    'I need to highlight these very important words',
    ['Coffee', 'Puppies', 'Doritos'])
    st.button("Go Button")
    tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
    expand_1 = st.expander("An expander.. with surprises inside")
    expand_1.text_area(plain_long_title, disabled=True)
    expand_1.text_area(plain_table, disabled=True)
    expand_1.text_area(img_title, disabled=True)


with col2:
    st.header("Fancy Labels :nail_care::skin-tone-3::")
    st.color_picker('Instructions: **Pick** a *Color*: :rainbow:', '#3E55CB')
    st.selectbox("How would you like to be [contacted](https://dictionary.cambridge.org/us/dictionary/english/contacted)?",
        ("Carrier Pidgeon", "Email", "Mobile phone"))
    st.metric(label="Temperature = *Spicy* :hot_pepper:", value="105 °F", delta=None)
    st.checkbox("Agree to the thing :thumbsup:")
    st.text_input('Share a thought ~~or your credit card number~~:', 'Donations welcome')
    st.download_button('Download random text :page_facing_up:', text_contents)
    st.radio( "What's your favorite `coding` language? :computer:",
        ('Python', 'Javascript', 'Ruby'))
    st.multiselect(
    'I need to highlight these **very** important words',
    ['Coffee', 'Puppies', 'Golf'])
    st.button("**Stop** Button :traffic_light:")
    tab1, tab2, tab3 = st.tabs(["**Cat** :cat:", "*Dog* :dog:", "~~Owl~~ :owl:"])
    expand_2 = st.expander("An **expander**.. with surprises ~~widgets~~ inside :cyclone:")
    expand_2.text_area(long_title)
    expand_2.text_area(table)
    expand_2.text_area(img_title, key=2)

with st.sidebar:
    st.color_picker('Instructions: **Pick** a *Color*: :rainbow:', '#BB0329')
    st.selectbox("How would you like to be [contacted](https://dictionary.cambridge.org/us/dictionary/english/contacted)?",
        ("Corgi Stampede", "Email", "Mobile phone"))
    st.metric(label="Temperature = **Cold** :snowflake:", value="30 °F", delta=None)
    st.checkbox("Agree to the thing :thumbsup::skin-tone-3:")
    st.text_input('Random thought ~~or your credit card number~~:', 'Donations welcome')
    st.download_button(':arrow_down: Download random text', text_contents)
    st.radio( "What's your favorite `code` language? :computer:",
    ('Python', 'Javascript', 'Ruby'))
    st.multiselect(
    'I need to highlight these **very** important words',
    ['Coffee', 'Puppies', 'Sushi'])
    st.button("**Go** Button :white_check_mark:")
    tab4, tab5, tab6 = st.tabs(["**Cat** :cat:", "*Dog* :dog:", "~~Owl~~ :owl:"])
    expand_3 = st.expander("An **expander**.. with surprises ~~widgets~~ inside :cyclone:")
    expand_3.text_area(long_title, key=7)
    expand_3.text_area(table, key=8)
    expand_3.text_area(img_title, key=9)
