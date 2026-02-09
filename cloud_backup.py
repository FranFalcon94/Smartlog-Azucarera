import json
import os
from datetime import datetime

CLOUD_FOLDER = "cloud_backup"

def backup_to_cloud(data):
    os.makedirs(CLOUD_FOLDER, exist_ok=True)
    filename = f"{CLOUD_FOLDER}/backup_{datetime.utcnow().strftime('%Y%m%d')}.json"

    existing = []
    if os.path.exists(filename):
        try:
            with open(filename, "r") as f:
                content = f.read().strip()
                if content:
                    existing = json.loads(content)
        except json.JSONDecodeError:
            existing = []

    existing.append(data)

    with open(filename, "w") as f:
        json.dump(existing, f, indent=4)
