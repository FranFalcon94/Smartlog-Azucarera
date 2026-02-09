import random
from datetime import datetime


def generate_sensor_data():
    temperature = round(random.uniform(40, 110), 2)
    humidity = round(random.uniform(30, 90), 2)

    if temperature > 100:
        status = "FAIL"
    elif temperature > 70:
        status = "WARNING"
    else:
        status = "OK"

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "temperature": temperature,
        "humidity": humidity,
        "machine_status": status,
    }
