import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

# Load dataset
data = pd.read_csv("dataset/health_data.csv")

X = data[['glucose', 'haemoglobin', 'cholesterol']]
y = data['result']

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, 'health_model.pkl')

print("Model Trained Successfully")