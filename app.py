import streamlit as st
from textblob import TextBlob
st.set_page_config(page_title="Tweet Sentiment Classifier", layout="centered")
st.title("🧠 Tweet Sentiment Predictor")
st.write("Type in a tweet and I'll tell you if it's Positive, Negative, or Neutral.")
with st.form("sentiment_form"):
    tweet = st.text_area("Enter your tweet here:", height=150)
    submitted = st.form_submit_button("Analyze Sentiment")
if submitted and tweet.strip():
    blob = TextBlob(tweet)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "😊 Positive"
        st.success(f"Sentiment: {sentiment} (Score: {round(polarity, 3)})")
    elif polarity < 0:
        sentiment = "😠 Negative"
        st.error(f"Sentiment: {sentiment} (Score: {round(polarity, 3)})")
    else:
        sentiment = "😐 Neutral"
        st.info(f"Sentiment: {sentiment} (Score: {round(polarity, 3)})")


    st.markdown("**🔍 Sentiment Breakdown**")
    words = tweet.split()
    highlights = []
    for word in words:
        score = TextBlob(word).sentiment.polarity
        if score > 0.2:
            highlights.append(f":green[{word}]")
        elif score < -0.2:
            highlights.append(f":red[{word}]")
        else:
            highlights.append(word)
    st.write(" ".join(highlights))

