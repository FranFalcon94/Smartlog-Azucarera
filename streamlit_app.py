from __future__ import annotations

from datetime import datetime

import pandas as pd
import streamlit as st

from cloud_backup import backup_to_cloud
from database import fetch_recent, init_db, insert_data
from sensor_simulator import generate_sensor_data


def _to_dataframe(rows: list[dict]) -> pd.DataFrame:
    df = pd.DataFrame(rows)
    if df.empty:
        return df
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce", utc=True)
    df = df.sort_values("timestamp")
    return df


def main() -> None:
    st.set_page_config(page_title="SmartLog Azucarera Demo", layout="wide")
    st.title("SmartLog Azucarera")
    st.caption("Local-first demo dashboard for the simulated industrial logger.")

    init_db()

    col_a, col_b, col_c = st.columns([1, 1, 2])
    with col_a:
        limit = st.number_input("Rows to display", min_value=10, max_value=5000, value=200, step=50)
    with col_b:
        if st.button("Generate one reading"):
            reading = generate_sensor_data()
            if 0 <= float(reading["humidity"]) <= 100:
                insert_data(reading)
                backup_to_cloud(reading)
                st.success(f"Inserted reading at {reading['timestamp']}")
            else:
                st.error("Invalid humidity (outside 0..100). Reading discarded.")
    with col_c:
        st.info(
            "Tip: run `py main.py` in another terminal to generate data continuously, "
            "then refresh this page to see new records."
        )

    rows = fetch_recent(int(limit))
    df = _to_dataframe(rows)

    if df.empty:
        st.warning("No data yet. Click 'Generate one reading' to insert your first record.")
        return

    latest = df.iloc[-1]
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Temperature (C)", f"{latest['temperature']:.2f}")
    m2.metric("Humidity (%)", f"{latest['humidity']:.2f}")
    m3.metric("Machine status", str(latest["machine_status"]))
    m4.metric("Last timestamp (UTC)", latest["timestamp"].strftime("%Y-%m-%d %H:%M:%S"))

    chart_col, table_col = st.columns([2, 1])
    with chart_col:
        st.subheader("Recent trends")
        st.line_chart(df.set_index("timestamp")[["temperature", "humidity"]])

    with table_col:
        st.subheader("Latest rows")
        st.dataframe(
            df[["timestamp", "temperature", "humidity", "machine_status"]].tail(50),
            use_container_width=True,
            hide_index=True,
        )

    st.subheader("Backup status")
    today_name = datetime.utcnow().strftime("%Y%m%d")
    st.write(f"Expected backup file: `cloud_backup/backup_{today_name}.json`")


if __name__ == "__main__":
    main()

