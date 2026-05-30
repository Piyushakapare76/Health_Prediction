from flask import Flask, render_template, request, redirect, flash
import mysql.connector
import joblib
from datetime import date
import re

app = Flask(__name__, template_folder='templates')

app.secret_key = "healthapp"

# MYSQL CONNECTION
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="health_prediction"
)

# LOAD ML MODEL
model = joblib.load('health_model.pkl')


# HOME PAGE
@app.route('/')
def index():

    cur = db.cursor()

    cur.execute("SELECT * FROM patients")

    data = cur.fetchall()

    return render_template('index.html', patients=data)


# ADD PAGE
from datetime import date

@app.route('/add')
def add_patient():
    return render_template(
        'add_patient.html',
        today=date.today().strftime('%Y-%m-%d')
    )

# INSERT
@app.route('/insert', methods=['POST'])
def insert():

    full_name = request.form['full_name']
    dob = request.form['dob']
    email = request.form['email']
    glucose = request.form['glucose']
    haemoglobin = request.form['haemoglobin']
    cholesterol = request.form['cholesterol']

    # Email Validation
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if not re.match(pattern, email):
        flash("Invalid Email Address! Please enter a valid email.")
        return redirect('/add')

    # DOB Validation
    if dob > str(date.today()):
        flash("Future Date of Birth is not allowed!")
        return redirect('/add')

    # ML Prediction
    prediction = model.predict([[
        float(glucose),
        float(haemoglobin),
        float(cholesterol)
    ]])

    remarks = prediction[0]

    cur = db.cursor()

    sql = """
    INSERT INTO patients
    (full_name, dob, email, glucose,
     haemoglobin, cholesterol, remarks)
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        full_name,
        dob,
        email,
        glucose,
        haemoglobin,
        cholesterol,
        remarks
    )

    cur.execute(sql, values)
    db.commit()

    flash("Patient Added Successfully")

    return redirect('/')
# EDIT PAGE
@app.route('/edit/<int:id>')
def edit(id):

    cur = db.cursor()

    cur.execute("SELECT * FROM patients WHERE id=%s", (id,))

    patient = cur.fetchone()

    return render_template(
        'edit_patient.html',
        patient=patient
    )


# UPDATE
@app.route('/update/<int:id>', methods=['POST'])
def update(id):

    full_name = request.form['full_name']
    dob = request.form['dob']
    email = request.form['email']
    glucose = request.form['glucose']
    haemoglobin = request.form['haemoglobin']
    cholesterol = request.form['cholesterol']

    prediction = model.predict([[
        float(glucose),
        float(haemoglobin),
        float(cholesterol)
    ]])

    remarks = prediction[0]

    cur = db.cursor()

    sql = """
    UPDATE patients

    SET
    full_name=%s,
    dob=%s,
    email=%s,
    glucose=%s,
    haemoglobin=%s,
    cholesterol=%s,
    remarks=%s

    WHERE id=%s
    """

    values = (
        full_name,
        dob,
        email,
        glucose,
        haemoglobin,
        cholesterol,
        remarks,
        id
    )

    cur.execute(sql, values)

    db.commit()

    flash("Updated Successfully")

    return redirect('/')


# DELETE
@app.route('/delete/<int:id>')
def delete(id):

    cur = db.cursor()

    cur.execute("DELETE FROM patients WHERE id=%s", (id,))

    db.commit()

    flash("Deleted Successfully")

    return redirect('/')


if __name__ == "__main__":

    app.run(debug=True)