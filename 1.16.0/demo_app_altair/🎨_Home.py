import numpy as np
import streamlit as st
from streamlit.components.v1 import html
from streamlit_extras.markdownlit import mdlit
from streamlit_extras.switch_page_button import switch_page

TITLE = "Streamlit theme for Altair charts!"
ICON = "🎨"

# button_element = """
# <div class="stActionButton">
#     <a href="https://github.com/streamlit/release-demos/tree/master/1.16.0" style="text-decoration:none; color:inherit; background:inherit;" target="_blank" rel="noopener noreferrer"><button class="css-9s5bis edgvbvh3"><div class="css-1wbqy5l e10z71041"><img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" style="width: 1em; height: 1em; vertical-align: -0.15em; border-radius: 3px; margin-right: 0em;">
# <span>Open code</span></div></button></a></div>
# """

st.set_page_config(page_title=TITLE, page_icon=ICON)
html(
    """
<script>

var newButtonHtmlString = `
<div class="stActionButton">
    <button class="css-9s5bis edgvbvh3"><div class="css-1wbqy5l e10z71041"><img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" style="width: 1em; height: 1em; vertical-align: -0.15em; border-radius: 3px; margin-right: 0em;">
<span>🐙 Open code</span></div></button></a></div>
`;

var newButton = new DOMParser().parseFromString(newButtonHtmlString, "text/html");

//var toolBar = document.querySelector('div[data-testid="stToolbar"]');
//document.querySelector('div[data-testid="stToolbar"]').insertBefore(newButton.body.firstChild);
//document.querySelector('div[class="stActionButton"]').prepend(newButton.body.firstChild);
var toolBar = document.querySelector('div[data-testid="stToolbar"]');
toolBar.insertBefore(newButton.body.firstChild, toolBar.firstChild);
</script>
"""
)
st.title(ICON + " " + TITLE)
ALTAIR_ICON_URL = "https://avatars.githubusercontent.com/u/22396732?s=200&v=4"

mdlit(
    f"""Welcome! 👋

This is a demo app for the 1.16 release of Streamlit, focusing on showcasing the new Streamlit theme for Altair charts! We collected a bunch of example charts from @(Altair's docs)(https://altair-viz.github.io/gallery/index.html) to show you how the charts look with/without Streamlit theme. \n

👈 Check them out by browsing the pages in the sidebar!
"""
)

show = st.button("I'm lazy!")
if show:
    new_page = np.random.choice(
        [
            "Horizontal Stacked Bar Chart",
            "Bar Chart With Mean Line",
            "Layered Bar Chart",
            "Iowa Electricity",
            "Scatter Marginal Hist",
            "Simple Stacked Area Chart",
        ]
    )
    switch_page(new_page)

mdlit(
    """
Read more in the dedicated @(streamlit)(Streamlit blog post)(https://blog.streamlit.io/)!

Oh and if you liked this demo, you might as well like our @(👯)(twin demo for Plotly)(https://plotly.streamlit.app)!\n
"""
)
