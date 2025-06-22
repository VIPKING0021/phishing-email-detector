import streamlit as st
import pickle
import re

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# If you used a vectorizer (e.g., TF-IDF), load it too
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Clean text (basic)
def preprocess_text(text):
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)
    text = re.sub(r"\W", ' ', text)
    return text.lower()

# Streamlit UI
st.set_page_config(page_title="Phishing Email Detector", layout="centered")
st.title("🛡️ Phishing Email Detector")

st.write("Paste the email content below to check if it's a phishing attempt.")

user_input = st.text_area("📧 Email Content", height=250)

if st.button("Detect"):
    if user_input.strip() == "":
        st.warning("Please enter email content.")
    else:
        cleaned = preprocess_text(user_input)
        vect = vectorizer.transform([cleaned])
        result = model.predict(vect)[0]

        if result == 1:
            st.error("🚨 This looks like a phishing email!")
        else:
            st.success("✅ This email seems safe.")
