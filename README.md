# Health Prediction Application

## Overview

The Health Prediction Application is a Flask-based web application that manages patient health records and predicts health conditions using Machine Learning. The application provides complete CRUD (Create, Read, Update, Delete) operations, data validation, MySQL database integration, and AI/ML-based prediction functionality.

This project was developed as part of a technical assessment to demonstrate web development, database management, API development, validation handling, and machine learning integration.

---

## Features

### Patient Record Management

* Create new patient records
* View all patient records
* Update existing patient records
* Delete patient records

### Data Validation

* Email format validation
* Duplicate record detection
* Invalid date validation
* Future date validation
* Required field validation

### Machine Learning Integration

* Health prediction using patient parameters
* Real-time prediction generation
* Trained ML model integration using Joblib

### Database Management

* MySQL database connectivity
* Secure record storage
* CRUD functionality support

---

## Technology Stack

### Frontend

* HTML5
* CSS3
* Bootstrap

### Backend

* Python
* Flask

### Database

* MySQL

### Machine Learning

* Scikit-Learn
* Pandas
* NumPy
* Joblib

---

## Project Architecture

User Interface (HTML/CSS)
↓
Flask Application
↓
Validation Layer
↓
Machine Learning Model
↓
MySQL Database

---

## Project Structure

Health_Prediction/

│

├── app.py

├── model.pkl

├── scaler.pkl

├── requirements.txt

│

├── static/

│ ├── css/

│ ├── images/

│

├── templates/

│ ├── index.html

│ ├── add_patient.html

│ ├── records.html

│ ├── edit_patient.html

│

├── database/

│ └── health_prediction.sql

│

└── README.md

---

## Installation Guide

### Step 1: Clone Repository


cd health-prediction-app

### Step 2: Create Virtual Environment

python -m venv venv

### Step 3: Activate Environment

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate

### Step 4: Install Required Packages

pip install -r requirements.txt

### Step 5: Configure Database

Create a MySQL database:

CREATE DATABASE health_prediction;

Create patient table:

CREATE TABLE patients (
id INT AUTO_INCREMENT PRIMARY KEY,
full_name VARCHAR(100),
dob DATE,
email VARCHAR(100) UNIQUE,
glucose FLOAT,
haemoglobin FLOAT,
cholesterol FLOAT,
prediction VARCHAR(50)
);

### Step 6: Configure Database Credentials

Update database connection settings inside app.py:

db = mysql.connector.connect(
host="localhost",
user="root",
password="your_password",
database="health_prediction"
)

### Step 7: Run Application

python app.py

Open browser:

http://127.0.0.1:5000

---

## API Endpoints

### Create Patient

POST /add

Purpose:
Creates a new patient record.

---

### Get All Patients

GET /records

Purpose:
Returns all patient records stored in the database.

---

### Update Patient

POST /update/<id>

Purpose:
Updates existing patient information.

---

### Delete Patient

GET /delete/<id>

Purpose:
Deletes a patient record.

---

## Validation Rules

### Email Validation

Valid Examples:

[robyn@gmail.com](mailto:robyn@gmail.com)

[sam@news.com.au](mailto:sam@news.com.au)

Invalid Examples:

hunter@gmail

kris.wu.gmail.com

Reason:
The application requires a valid email format containing '@' and a valid domain extension.

---

### Date Validation

Valid Example:

28.01.1960

Invalid Examples:

31.11.2001

19.10.2030

Reasons:

* Invalid calendar date
* Future date not allowed

---

### Duplicate Record Validation

The application prevents duplicate patient entries to maintain data integrity.

---

## Machine Learning Integration

### Input Features

* Glucose
* Haemoglobin
* Cholesterol

### Workflow

1. User enters patient details.
2. Application validates all fields.
3. Input data is prepared for prediction.
4. Trained ML model generates prediction.
5. Prediction result is displayed and stored.

### Model Loading

model = joblib.load("model.pkl")

prediction = model.predict(features)

### Why This ML Approach Was Selected

The machine learning model was selected because:

* Fast prediction generation
* Easy Flask integration
* Reliable performance
* Suitable for healthcare screening applications
* Lightweight deployment using Joblib

---

## Assessment Test Cases

### Successfully Created Records

1. Robyn Pears
2. Darryl Tim
3. Sam Kerr
4. Madison XI
5. Tenille Singh
6. Prem Kumar

### Rejected Records

John Hunter
Reason: Invalid Email Format

Peter Larry
Reason: Invalid Date (31 November does not exist)

Robyn Pears (Duplicate)
Reason: Duplicate Record

Kris Wu
Reason: Future Date of Birth and Invalid Email Format

---

## CRUD Demonstration

### Create

Patient records can be added using the Add Patient form.

### Read

All patient records are displayed in the Records page.

### Update

Patient details can be edited and saved.

Example:
Email changed to:

[gokul@infocare.com](mailto:gokul@infocare.com)

### Delete

Patient records can be permanently removed from the system.

---

## Future Improvements

* User Authentication
* Admin Dashboard
* Role-Based Access Control
* PDF Report Generation
* Email Notifications
* Cloud Deployment
* REST API Expansion
* Advanced Health Analytics

---

## GitHub Repository

Upload the complete source code to GitHub and include:

* Source Code
* README.md
* requirements.txt
* SQL File
* Model Files
* Screenshots

---


