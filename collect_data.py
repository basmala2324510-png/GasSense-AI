import csv
import os
from datetime import datetime

FILE_NAME = "gas_data.csv"

def save_reading(gas_level, temperature, humidity, status):
    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists or os.path.getsize(FILE_NAME) == 0:
            writer.writerow([
                "timestamp",
                "gas_level",
                "temperature",
                "humidity",
                "status"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            gas_level,
            temperature,
            humidity,
            status
        ])

    print("Reading saved successfully!")


print("GasSense AI - Data Collection System")
print("Ready to receive real sensor readings.")