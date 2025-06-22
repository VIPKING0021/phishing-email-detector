import pandas as pd

# csv file load kri idhr
data = pd.read_csv(r"D:\dataset\Phishing_Email.csv")

# useless clumn ko delete kiya
data = data.drop(columns=["Unnamed: 0"])

# rename kra safe emails ko 0 or phishing emails ko 1
data["Email Type"] = data["Email Type"].map({"Safe Email": 0, "Phishing Email": 1})

# print krwaya
print(data.head())



#last wala code run me eeero tha isliye blank columns ko delete kiya or drop kiya



# Load 
data = pd.read_csv(r"D:\dataset\Phishing_Email.csv")

# Drop empty email texts
data = data.dropna(subset=["Email Text"])

# Drop extra index column
data = data.drop(columns=["Unnamed: 0"])

# Convert labels
data["Email Type"] = data["Email Type"].map({"Safe Email": 0, "Phishing Email": 1})





from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import pickle

# Step 1: Turn email text into numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data["Email Text"])  # inputs
y = data["Email Type"]  # answers (0 or 1)

# Step 2: Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train the model
model = MultinomialNB()
model.fit(X_train, y_train)

# Step 4: Test the model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print("✅ Model Accuracy:", accuracy)

# Step 5: Save the model and vectorizer
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)