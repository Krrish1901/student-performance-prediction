import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# Load trained model
model = joblib.load("student_model.pkl")

# Sample student data
sample = pd.DataFrame({
    "gender": ["female"],
    "race/ethnicity": ["group B"],
    "parental level of education": ["bachelor's degree"],
    "lunch": ["standard"],
    "test preparation course": ["completed"]
})

# Recreate encoders
encoders = {}

# Possible values from dataset
categories = {
    "gender": ["female", "male"],

    "race/ethnicity": [
        "group A",
        "group B",
        "group C",
        "group D",
        "group E"
    ],

    "parental level of education": [
        "some high school",
        "high school",
        "some college",
        "associate's degree",
        "bachelor's degree",
        "master's degree"
    ],

    "lunch": [
        "free/reduced",
        "standard"
    ],

    "test preparation course": [
        "none",
        "completed"
    ]
}

# Encode columns
for column in sample.columns:

    le = LabelEncoder()

    le.fit(categories[column])

    sample[column] = le.transform(sample[column])

    encoders[column] = le

# Predict
prediction = model.predict(sample)

# Decode prediction
grade_labels = {
    0: "A",
    1: "B",
    2: "C",
    3: "D"
}

print("\nPredicted Grade:", grade_labels[prediction[0]])
