import os
import sqlite3

DB_PATH = "data/smartlog.db"

def init_db():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sensor_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            temperature REAL NOT NULL,
            humidity REAL NOT NULL,
            machine_status TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

def insert_data(data):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO sensor_logs (timestamp, temperature, humidity, machine_status)
        VALUES (?, ?, ?, ?)
    """, (
        data["timestamp"],
        data["temperature"],
        data["humidity"],
        data["machine_status"]
    ))

    conn.commit()
    conn.close()
