"""SmartLog Azucarera - minimal industrial logger.

Runs an infinite loop that generates simulated sensor readings, validates them,
persists them to SQLite, and appends them to a daily JSON backup file.
"""

import time
from sensor_simulator import generate_sensor_data
from database import init_db, insert_data
from cloud_backup import backup_to_cloud

INTERVAL_SECONDS = 5

def main():
    print("SmartLog Azucarera started...")
    init_db()

    while True:
        data = generate_sensor_data()

        if 0 <= data["humidity"] <= 100:
            insert_data(data)
            backup_to_cloud(data)

            print(f"Record stored: {data}")

            if data["temperature"] > 100:
                print("CRITICAL ALERT: temperature > 100C. Machine stopped.")
                input("Perform a safe manual reset, then press Enter to continue...")
            elif data["temperature"] > 70:
                print("WARNING: temperature > 70C. Notify the operator.")
        else:
            print("Invalid reading detected (humidity out of range).")

        time.sleep(INTERVAL_SECONDS)

if __name__ == "__main__":
    main()
