import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

FILE_NAME = "gas_data.csv"

try:
    data = pd.read_csv(FILE_NAME)
except pd.errors.EmptyDataError:
    print("Dataset is empty. Waiting for real sensor readings.")
    raise SystemExit

features = ["gas_level", "temperature", "humidity"]
target = "status"

if not all(col in data.columns for col in features + [target]):
    print("Dataset is not ready yet.")
    raise SystemExit

if len(data) < 20 or data[target].nunique() < 2:
    print("We need at least 20 real, labeled readings.")
    raise SystemExit

X = data[features]
y = data[target]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

models = {
    "Random Forest": RandomForestClassifier(
        n_estimators=100, random_state=42
    ),
    "Extra Trees": ExtraTreesClassifier(
        n_estimators=100, random_state=42
    ),
    "Decision Tree": DecisionTreeClassifier(
        random_state=42
    )
}

results = []

for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    results.append((name, accuracy, model))

    print(f"\n{name}")
    print(f"Accuracy: {accuracy * 100:.2f}%")
    print(classification_report(y_test, predictions))

best_model = max(results, key=lambda item: item[1])

joblib.dump(best_model[2], "best_gassense_model.pkl")

print("\nBest model:", best_model[0])
print("Test accuracy:", round(best_model[1] * 100, 2), "%")