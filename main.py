import subprocess
import sys

print("================================")
print("       GasSense AI System")
print("================================")

print("1. Open Dashboard")
print("2. Train AI Model")
print("3. Compare AI Models")
print("4. Exit")

choice = input("\nChoose an option: ")

if choice == "1":
    subprocess.run([
        sys.executable, "-m", "streamlit",
        "run", "dashboard.py"
    ])

elif choice == "2":
    subprocess.run([sys.executable, "train_model.py"])

elif choice == "3":
    subprocess.run([sys.executable, "compare_models.py"])

elif choice == "4":
    print("Goodbye!")

else:
    print("Invalid choice.")