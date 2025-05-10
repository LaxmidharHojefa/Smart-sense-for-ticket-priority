# # from flask import Flask, request, jsonify, render_template
# from flask_cors import CORS
# import pickle
# import re

# # Initialize Flask app
# app = Flask(__name__)
# CORS(app)

# # Load pre-trained model and components
# with open("model.pkl", "rb") as f:
#     model = pickle.load(f)

# with open("vectorizer.pkl", "rb") as f:
#     vectorizer = pickle.load(f)

# with open("label_encoder.pkl", "rb") as f:
#     label_encoder = pickle.load(f)

# def clean_text(text):
#     return re.sub(r'\W+', ' ', text.lower().strip())

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/predict", methods=["POST"])
# def predict():
#     data = request.get_json()
#     subject = data.get("subject", "")
#     body = data.get("body", "")
#     combined_text = clean_text(subject + " " + body)
#     transformed = vectorizer.transform([combined_text])
#     prediction = model.predict(transformed)
#     priority = label_encoder.inverse_transform(prediction)[0]
#     return jsonify({"priority": priority})

# if __name__ == "__main__":
#     app.run(debug=True)


# ✅ app.py
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
import re
from textblob import TextBlob

app = Flask(__name__)
CORS(app)

# Load ML components
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

def clean_text(text):
    return re.sub(r'\W+', ' ', text.lower().strip())

def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.2:
        return "Positive"
    elif polarity < -0.2:
        return "Negative"
    else:
        return "Neutral"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    subject = data.get("subject", "")
    body = data.get("body", "")
    combined_text = clean_text(subject + " " + body)
    sentiment = get_sentiment(combined_text)
    transformed = vectorizer.transform([combined_text])
    prediction = model.predict(transformed)
    priority = label_encoder.inverse_transform(prediction)[0]
    return jsonify({"priority": priority, "sentiment": sentiment})

if __name__ == "__main__":
    app.run(debug=True)
