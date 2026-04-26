"""SQLite storage layer for SmartLog Azucarera."""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "data" / "smartlog.db"


def init_db() -> None:
    """Create the SQLite database and schema if missing."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS sensor_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                temperature REAL NOT NULL,
                humidity REAL NOT NULL,
                machine_status TEXT NOT NULL
            )
            """
        )
        conn.commit()
    finally:
        conn.close()


def insert_data(data: dict) -> None:
    """Insert one sensor reading into the database."""
    conn = sqlite3.connect(DB_PATH)
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO sensor_logs (timestamp, temperature, humidity, machine_status)
            VALUES (?, ?, ?, ?)
            """,
            (
                data["timestamp"],
                data["temperature"],
                data["humidity"],
                data["machine_status"],
            ),
        )
        conn.commit()
    finally:
        conn.close()


def fetch_recent(limit: int = 200) -> list[dict]:
    """Fetch the most recent logs (newest first)."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT id, timestamp, temperature, humidity, machine_status
            FROM sensor_logs
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,),
        )
        rows = cursor.fetchall()
        return [dict(row) for row in rows]
    finally:
        conn.close()
