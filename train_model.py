import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

FILE_NAME = "gas_data.csv"

if not os.path.exists(FILE_NAME):
    print("Dataset not found!")
    exit()

try:
    data = pd.read_csv(FILE_NAME)
except pd.errors.EmptyDataError:
    print("Dataset is empty. Waiting for real sensor readings.")
    exit()
required_columns = [
    "gas_level",
    "temperature",
    "humidity",
    "status"
]

if not all(column in data.columns for column in required_columns):
    print("Dataset is incomplete or not ready.")
    exit()

if len(data) < 20 or data["status"].nunique() < 2:
    print("Not enough real labeled data to train the AI yet.")
    exit()

X = data[["gas_level", "temperature", "humidity"]]
y = data["status"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

joblib.dump(model, "gassense_model.pkl")

print("GasSense AI training completed!")
print("Accuracy:", round(accuracy * 100, 2), "%")
print("Model saved successfully!")