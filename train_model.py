import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

texts = [
    "Server down issue urgent",
    "Forgot password help",
    "Laptop not turning on critical",
    "Need access to database",
    "VPN not working high",
    "How to reset email password",
    "System crash critical",
    "Login problem medium"
]
labels = ["High", "Low", "High", "Medium", "High", "Low", "High", "Medium"]

le = LabelEncoder()
y = le.fit_transform(labels)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

with open("label_encoder.pkl", "wb") as f:
    pickle.dump(le, f)

print("Model, vectorizer, and label encoder saved successfully.")
