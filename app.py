from flask import Flask, render_template, request, jsonify
import pickle
import webbrowser
import os
import re

from backend.feature_extraction import extract_features

app = Flask(
    __name__,
    template_folder="frontend/templates",
    static_folder="frontend/static"
)

# Load trained model
with open("backend/model.pkl", "rb") as f:
    model = pickle.load(f)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    data = request.get_json()
    url = data['url'].strip()

    
    
    features = extract_features(url)

    print("URL:", url)
    print("Raw features:", features)

    import pandas as pd

    feature_names = [
        "url_length",
        "dot_count",
        "hyphen_count",
        "slash_count",
        "digit_count",
        "at_count",
        "question_count",
        "equal_count",
        "percent_count",
        "subdomain_count",
        "has_ip",
        "suspicious_words",
        "special_char_count",
        "hostname_length",
        "path_length",
        "digit_ratio",
        "has_shortener"
    ]

    features = pd.DataFrame(features, columns=feature_names)

    prediction = model.predict(features)[0]

    print("Prediction:", prediction)

    probability = model.predict_proba(features)[0]
    confidence = round(max(probability) * 100, 2)

    if prediction == "Phishing":
        result = "Phishing Website Detected"
    else:
        result = "Legitimate Website"

    return jsonify({
        "prediction": result,
        "confidence": confidence
    })


if __name__ == "__main__":

    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        webbrowser.open("http://127.0.0.1:5000")

    app.run(debug=True)