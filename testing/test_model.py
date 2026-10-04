import pickle
import pandas as pd
import numpy as np
import sys
import os
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from backend.feature_extraction import extract_features

from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    classification_report,
    precision_score,
    recall_score,
    f1_score
)

# Load Trained Model

model_path = os.path.join(BASE_DIR, "backend", "model.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

# Load Testing CSV

csv_path = os.path.join(os.path.dirname(__file__), "real_world_test.csv")

df = pd.read_csv(csv_path)

predictions = []
confidences = []

# Predict Every URL

for url in df["URL"]:

    features = extract_features(url)

    feature_names = [
        'url_length',
        'dot_count',
        'hyphen_count',
        'slash_count',
        'digit_count',
        'at_count',
        'question_count',
        'equal_count',
        'percent_count',
        'subdomain_count',
        'has_ip',
        'suspicious_words',
        'special_char_count',
        'hostname_length',
        'path_length',
        'digit_ratio',
        'has_shortener'
    ]

    features = pd.DataFrame(features, columns=feature_names)

    prediction = model.predict(features)[0]

    probability = model.predict_proba(features)[0]

    confidence = round(max(probability) * 100, 2)

    predictions.append(prediction)

    confidences.append(confidence)

# Add Predictions

df["Predicted"] = predictions

df["Confidence (%)"] = confidences


# Find TP TN FP FN


results = []

for actual, predicted in zip(df["Actual"], df["Predicted"]):

    if actual == "Phishing" and predicted == "Phishing":
        results.append("TP")

    elif actual == "Benign" and predicted == "Benign":
        results.append("TN")

    elif actual == "Benign" and predicted == "Phishing":
        results.append("FP")

    else:
        results.append("FN")

df["Result"] = results


# Save Results

output_path = os.path.join(os.path.dirname(__file__), "testing_result.csv")

df.to_csv(output_path, index=False)


# Performance Metrics

accuracy = accuracy_score(df["Actual"], df["Predicted"])

precision = precision_score(
    df["Actual"],
    df["Predicted"],
    pos_label="Phishing"
)

recall = recall_score(
    df["Actual"],
    df["Predicted"],
    pos_label="Phishing"
)

f1 = f1_score(
    df["Actual"],
    df["Predicted"],
    pos_label="Phishing"
)

cm = confusion_matrix(
    df["Actual"],
    df["Predicted"],
    labels=["Phishing", "Benign"]
)

TP = cm[0][0]
FN = cm[0][1]
FP = cm[1][0]
TN = cm[1][1]


# Display Results

print("\n========== TEST RESULTS ==========\n")

print(df)

print("\n==================================")

print("Accuracy :", round(accuracy * 100,2), "%")

print("Precision:", round(precision * 100,2), "%")

print("Recall   :", round(recall * 100,2), "%")

print("F1 Score :", round(f1 * 100,2), "%")

print("\nConfusion Matrix\n")

print(cm)

print("\nTP :", TP)

print("TN :", TN)

print("FP :", FP)

print("FN :", FN)

print("\nClassification Report\n")

print(classification_report(df["Actual"], df["Predicted"]))

print("\nResults saved as testing_result.csv")