# 🎯 Ticket Priority Predictor

**Ticket Priority Predictor** is a machine learning-based web application designed to classify the priority level of customer support tickets based on the subject and description entered by users. This project helps automate ticket triaging, allowing teams to focus on urgent issues first and streamline support operations.

---

## 🚀 Features

- 🔍 Predicts ticket priority as **Low**, **Medium**, or **High**
- 🤖 Utilizes a trained ML model with TF-IDF vectorizer and label encoder
- 🌐 Frontend with a simple and clean user interface using HTML, CSS, and JavaScript
- 🔧 Flask-based backend API for seamless prediction and integration
- 📦 JSON-based communication between frontend and backend

---

## 🧰 Tech Stack

- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Python, Flask  
- **Machine Learning**: scikit-learn  
- **Utilities**: Pickle (for model storage), Flask-CORS

---

## 🗂️ Project Structure

```text
ticket-priority-predictor/
├── app.py               # Flask backend application
├── model.pkl            # Trained machine learning model
├── vectorizer.pkl       # TF-IDF vectorizer used for text transformation
├── label_encoder.pkl    # Label encoder for priority classes
│
├── templates/
│   └── index.html       # Frontend HTML interface
│
├── static/
│   └── style.css        # Optional CSS styling file
│
└── README.md            # Project documentation (you are here)
```

## ⚙️ How It Works

1. User submits a ticket subject and description via the web interface.
2. The backend receives the input, processes the text, and transforms it using a TF-IDF vectorizer.
3. The transformed data is fed into a pre-trained ML model.
4. The model outputs a priority label which is decoded using a label encoder.
5. The predicted priority is returned and displayed to the user.

---

## 🧪 Getting Started

Follow the steps below to run the project locally:

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ticket-priority-predictor.git
cd ticket-priority-predictor
```

### 2. Install Dependencies
Make sure you have Python installed (recommended: Python 3.7 or above). Then install required packages:

```bash
pip install flask flask-cors scikit-learn
```

Optionally, create a virtual environment before installing dependencies.

### 3. Ensure These Files Exist
Make sure the following trained model files are present in the root directory:

- model.pkl
- vectorizer.pkl
- label_encoder.pkl

These files should be created during your model training phase and stored using the pickle module.

### 4. Run the Flask Application
Start the backend server:

```bash
python app.py
```

You should see the app running at:

```bash
http://127.0.0.1:5000/
```

### 5. Use the Web Interface
Open the URL in your browser. Enter a ticket subject and description to get an instant priority prediction.

#### ✅ Example
#### Input:
**Subject**: Website is down
**Body**: Our application server has been unresponsive since this morning.

#### Output:
**Predicted Priority**: High

### 📌 Future Enhancements
Add support for multi-language inputs

- Integrate deep learning models for better accuracy
- Implement user login and dashboard system
- Store incoming tickets and predictions in a database
- Add logging and analytics for ticket trends

### 📝 License
This project is licensed under the MIT License. You are free to use, modify, and distribute it with attribution.
