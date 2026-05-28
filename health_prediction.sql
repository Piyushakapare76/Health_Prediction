CREATE DATABASE health_prediction;
USE health_prediction;

CREATE TABLE patients (
    id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(100),
    dob DATE,
    email VARCHAR(100),
    glucose FLOAT,
    haemoglobin FLOAT,
    cholesterol FLOAT,
    remarks VARCHAR(255)
);