"""Daily JSON backups for SmartLog Azucarera.

This module writes an append-only JSON array per day. In a real deployment,
this could be replaced with an object storage backend (S3/Azure Blob/etc.).
"""

import json
from datetime import datetime
from pathlib import Path

CLOUD_FOLDER = Path(__file__).resolve().parent / "cloud_backup"

def backup_to_cloud(data):
    """Append one reading to the daily JSON backup file."""
    CLOUD_FOLDER.mkdir(parents=True, exist_ok=True)
    filename = CLOUD_FOLDER / f"backup_{datetime.utcnow().strftime('%Y%m%d')}.json"

    existing = []
    if filename.exists():
        try:
            with filename.open("r", encoding="utf-8") as f:
                content = f.read().strip()
                if content:
                    existing = json.loads(content)
        except json.JSONDecodeError:
            existing = []

    existing.append(data)

    with filename.open("w", encoding="utf-8") as f:
        json.dump(existing, f, indent=4)
