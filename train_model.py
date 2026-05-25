import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load dataset
df = pd.read_csv("StudentsPerformance.csv")

# Create average score
df["average_score"] = (
    df["math score"] +
    df["reading score"] +
    df["writing score"]
) / 3

# Create grade categories
def grade_category(score):
    if score >= 85:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "D"

df["Grade"] = df["average_score"].apply(grade_category)

# Features
X = df.drop(
    [
        "math score",
        "reading score",
        "writing score",
        "average_score",
        "Grade"
    ],
    axis=1
)

# Target
y = df["Grade"]

# Encode ALL categorical columns
label_encoders = {}

for column in X.columns:

    # Convert column to string first
    X[column] = X[column].astype(str)

    le = LabelEncoder()

    X[column] = le.fit_transform(X[column])

    label_encoders[column] = le

# Encode target variable
target_encoder = LabelEncoder()
y = target_encoder.fit_transform(y)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print(f"\nModel Accuracy: {accuracy:.2f}")

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "student_model.pkl")

print("\nModel saved successfully as student_model.pkl")