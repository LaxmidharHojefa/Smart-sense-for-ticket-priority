from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
import re

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Allow cross-origin requests (important for frontend)

# Load pre-trained model and necessary components
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

# Helper function to clean and prepare input text
def clean_text(text):
    return re.sub(r'\W+', ' ', text.lower().strip())

# Flask route for HTML frontend (optional if using templates/index.html)
@app.route("/")
def index():
    return render_template("index.html")

# API route for prediction
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    subject = data.get("subject", "")
    body = data.get("body", "")

    # Combine and clean text
    combined_text = clean_text(subject + " " + body)

    # Transform using vectorizer
    transformed = vectorizer.transform([combined_text])

    # Predict using model
    prediction = model.predict(transformed)

    # Decode label
    priority = label_encoder.inverse_transform(prediction)[0]

    # Return JSON result
    return jsonify({"priority": priority})

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
