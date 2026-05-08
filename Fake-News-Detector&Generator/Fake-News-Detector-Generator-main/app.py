import streamlit as st
import pickle
from generator import generate_fake_news

# Load model and vectorizer
model = pickle.load(open("model/model.pkl","rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl","rb"))

# Page settings
st.set_page_config(
    page_title="Fake News Generator & Detector",
    page_icon="📰",
    layout="centered"
)

# Title
st.title("📰 Fake News Generator & Detector")
st.write("AN AI based system to detect and generate fake news articles. Built with Streamlit and scikit-learn.")

# Divider
st.markdown("---")

# Fake News Generator
st.subheader("⚡ Fake News Generator")

if st.button("Generate Fake News"):
    fake_news = generate_fake_news()
    st.info(fake_news)

st.markdown("---")

# Fake News Detector
st.subheader("🔍 Fake News Detector")

user_input = st.text_area("Enter a news article or headline")

if st.button("Check News"):

    if user_input == "":
        st.warning("Please enter some news text")

    else:
        text_vector = vectorizer.transform([user_input])
        prediction = model.predict(text_vector)

        if prediction[0] == 0:
            st.error("🚨 This looks like FAKE news")
        else:
            st.success("✅ This looks like REAL news")

st.markdown("---")

st.caption("Project: Fake News Generator & Detector | IBM PBEL Internship")