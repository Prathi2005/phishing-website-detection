# ML-Based Phishing Website Detection System

A machine learning-based web application that analyzes website URLs and classifies them as **Phishing** or **Legitimate** using URL-based features and a Random Forest classifier.

## 📌 Overview

Phishing websites are designed to deceive users into providing sensitive information. This project detects potentially phishing URLs by extracting characteristics from the URL and applying a trained machine learning model.

The system uses a **Flask web application** that provides a simple interface where users can enter a URL and receive a prediction.

## ✨ Features

* URL-based phishing detection
* Automated URL feature extraction
* Comparison of multiple machine learning algorithms
* Random Forest-based classification
* Flask web application
* External URL testing

## 🛠️ Technologies Used

* **Python**
* **Scikit-learn**
* **Pandas**
* **NumPy**
* **Flask**
* **HTML, CSS, JavaScript**

## 🧠 Machine Learning

The system extracts URL-based features including:

* URL length
* Dot count
* Hyphen count
* HTTPS presence
* Slash count
* Digit count
* Special characters
* Subdomain count
* IP address presence
* Suspicious words

Five machine learning algorithms were compared:

| Algorithm           |   Accuracy |
| ------------------- | ---------: |
| Logistic Regression |     71.57% |
| Decision Tree       |     85.04% |
| KNN                 |     82.62% |
| Naive Bayes         |     69.08% |
| **Random Forest**   | **87.74%** |

Based on the comparison, **Random Forest** was selected as the final classification model and saved as `model.pkl`.

## 📊 Results

The final Random Forest model was additionally evaluated on an **external balanced test set containing 136 URLs**.

| Metric    |      Score |
| --------- | ---------: |
| Accuracy  | **97.06%** |
| Precision |   **100%** |
| Recall    | **94.12%** |
| F1-Score  | **96.97%** |

These results represent the model's performance on the external test set and are separate from the algorithm comparison results shown above.

## 📁 Project Structure

```text
phishing-website-detection/
├── backend/
│   ├── __init__.py
│   ├── feature_extraction.py
│   └── model.pkl
├── frontend/
│   ├── static/
│   └── templates/
├── dataset/
├── notebooks/
├── testing/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Prathi2005/phishing-website-detection.git
cd phishing-website-detection
```

### 2. Install dependencies

It is recommended to use a virtual environment.

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python app.py
```

The Flask application will start on the local server. Open the URL displayed in the terminal in your web browser.

## 🔮 Future Scope

* Incorporating webpage and HTML-based features
* Adding domain and certificate analysis
* Expanding the dataset with newer phishing URLs
* Improving detection of obfuscated and shortened URLs

## 👩‍💻 Author

**Prathiksha Acharya**

MCA Student
