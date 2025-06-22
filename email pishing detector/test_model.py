import pickle

# Load the model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Test email
custom_email = """Congratulations! You've won a free iPhone. Click this link to claim your prize: http://scamlink.com"""

# Convert the email to numbers
email_vector = vectorizer.transform([custom_email])

# Make a prediction
prediction = model.predict(email_vector)

# Show result
if prediction[0] == 1:
    print("⚠️ This is a PHISHING email!")
else:
    print("✅ This email is safe.")
