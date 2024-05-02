import spacy
import streamlit as st
from spacytextblob.spacytextblob import SpacyTextBlob

st.set_page_config(page_title="Sentiment Analysis", page_icon="😊")

# Load the small English model from spaCy
nlp = spacy.load("en_core_web_sm")
# Add the SpacyTextBlob to the pipeline
nlp.add_pipe("spacytextblob")


def analyze_sentiment(text):
    """Analyze sentiment and return text colored based on polarity at the phrase level."""
    doc = nlp(text)
    output_text = text  # Start with the original text
    assessments = doc._.blob.sentiment_assessments.assessments

    # Process each assessment and apply colors
    for assessment in reversed(assessments):
        phrase_list, polarity, _, _ = assessment
        phrase = " ".join(phrase_list)  # Join the list to form the phrase
        start = output_text.rfind(phrase)  # Find the last occurrence of the phrase
        if start != -1:
            end = start + len(phrase)
            color = "green" if polarity > 0.1 else "red" if polarity < -0.1 else "gray"
            # Slice and insert the color
            output_text = (
                output_text[:start]
                + f":{color}-background[{phrase}]"
                + output_text[end:]
            )

    return output_text, assessments


st.header("Sentiment Analysis with Text Highlighting", divider=True)
st.caption(
    "This app analyzes the sentiment of the entered text and highlights it based on the [sentiment polarity](https://spacy.io/universe/project/spacy-textblob)."
)

user_input = st.text_area(
    "Enter text",
    "I love Streamlit! It works great and I use it all the time. Frontend development in HTML and CSS is not fun, so Streamlit is the perfect tool for me to quickly build data web apps.",
)

highlighted_text, assessments = analyze_sentiment(user_input)
st.markdown(highlighted_text)

with st.expander("View sentiment assessments"):
    for assessment in assessments:
        st.text(assessment)
