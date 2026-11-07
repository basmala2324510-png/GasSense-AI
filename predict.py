import joblib

MODEL_FILE = "best_gassense_model.pkl"

try:
    model = joblib.load(MODEL_FILE)
except FileNotFoundError:
    print("AI model not trained yet. Collect real data first.")
    raise SystemExit

print("GasSense AI - Prediction System")

try:
    gas = float(input("Enter gas reading: "))
    temperature = float(input("Enter temperature: "))
    humidity = float(input("Enter humidity: "))

    prediction = model.predict([[gas, temperature, humidity]])

    print("Predicted status:", prediction[0])

except ValueError:
    print("Please enter valid numeric readings.")