# Health_Prediction
# Health Prediction Application

## Project Overview

The Health Prediction Application is a web-based AI/ML healthcare system developed using Python Flask, MySQL, HTML, CSS, JavaScript, and Machine Learning algorithms. The application allows users to manage patient health records and predict possible health conditions based on blood test results.

The system performs CRUD (Create, Read, Update, Delete) operations and uses a trained Machine Learning model to generate health-related remarks automatically from patient blood test values.

---

# Features

## CRUD Operations

* Add new patient records
* View all patient records
* Update patient information
* Delete patient records

## AI/ML Prediction

The application predicts possible health conditions using:

* Glucose
* Haemoglobin
* Cholesterol

The prediction result is automatically displayed in the Remarks section.

## Input Validation

* Email validation
* Future date restriction for DOB
* Numeric validation for blood values

## Responsive User Interface

* User-friendly interface
* Bootstrap-based responsive design
* Simple navigation and data management

---

# Technology Stack

## Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap 5

## Backend

* Python
* Flask Framework

## Database

* MySQL

## Machine Learning

* Scikit-learn
* Decision Tree Classifier

---

# Project Structure

```bash
Health_prediction/
│
├── app.py
├── model.py
├── health_model.pkl
├── requirements.txt
├── health_prediction.sql
│
├── dataset/
│   └── health_data.csv
│
├── templates/
│   ├── index.html
│   ├── add_patient.html
│   └── edit_patient.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

# Database Setup

## Create Database

```sql
CREATE DATABASE health_prediction;
USE health_prediction;
```

## Create Table

```sql
CREATE TABLE patients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100),
    dob DATE,
    email VARCHAR(100),
    glucose FLOAT,
    haemoglobin FLOAT,
    cholesterol FLOAT,
    remarks VARCHAR(255)
);
```

---

# Installation Steps

## 1. Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

## 2. Open Project Folder

```bash
cd Health_prediction
```

## 3. Install Required Packages

```bash
pip install -r requirements.txt
```

---

# Required Python Packages

```txt
flask
mysql-connector-python
pandas
numpy
scikit-learn
joblib
```

---

# Train Machine Learning Model

Run the following command:

```bash
python model.py
```

This will generate:

```bash
health_model.pkl
```

---

# Run Application

```bash
python app.py
```

Open browser:

```bash
http://127.0.0.1:5000
```

---

# Machine Learning Algorithm Used

## Decision Tree Classifier

The application uses the Decision Tree Classification Algorithm from Scikit-learn to predict possible health conditions based on blood test values.

### Input Features

* Glucose
* Haemoglobin
* Cholesterol

### Predicted Results

* Normal
* Diabetes Risk
* High Risk
* Anemia
* Heart Risk

---

# API/ML Integration

The Machine Learning model is integrated into the Flask backend using:

* Joblib
* Scikit-learn

The model automatically predicts health remarks whenever a new patient record is added or updated.

---

# Challenges Faced

* MySQL database connectivity issues
* Flask template routing errors
* ML model integration with Flask
* CRUD operation debugging
* Input validation handling

These challenges were resolved through debugging, proper project structuring, and testing.

---

# Future Improvements

* Add authentication and login system
* Deploy application on cloud
* Add charts and analytics dashboard
* Use larger healthcare datasets
* Improve ML prediction accuracy
* Add REST API support

---


