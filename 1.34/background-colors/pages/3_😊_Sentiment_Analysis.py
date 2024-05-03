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

    # Create a list of tuples containing the start index, end index, and color for each phrase
    replacements = []
    for assessment in assessments:
        phrase_list, polarity, _, _ = assessment
        first_token = phrase_list[0]
        last_token = phrase_list[-1]
        start_index = text.lower().find(first_token.lower())
        end_index = text.lower().rfind(last_token.lower()) + len(last_token)
        if start_index != -1 and end_index != -1:
            color = "green" if polarity > 0.1 else "red" if polarity < -0.1 else "gray"
            replacements.append((start_index, end_index, color))

    # Sort replacements by start_index in descending order to avoid disrupting indices
    replacements.sort(key=lambda x: x[0], reverse=True)

    # Apply replacements from the end of the text to the beginning
    for start, end, color in replacements:
        colored_segment = f":{color}-background[{text[start:end]}]"
        output_text = output_text[:start] + colored_segment + output_text[end:]

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
