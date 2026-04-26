# Operator Manual - SmartLog Azucarera

This document explains how the logger behaves and how to operate it in a plant-like environment.

## What the program does

- Reads simulated temperature and humidity values.
- Stores each valid reading in the local SQLite database.
- Writes a daily backup into `cloud_backup/` in JSON format.
- Prints alerts when temperature crosses predefined thresholds.

## Thresholds and actions

- Temperature <= 70C: `OK`.
- Temperature > 70C: warning message for the operator.
- Temperature > 100C: critical alert; the machine is considered stopped and the program waits for a manual reset.

## How to run (Windows PowerShell)

1. Open a terminal.
2. Go to the project folder:
   `C:\Users\franf\PycharmProjects\PythonProject\smartlog-azucarera`
3. Run:
   `py -u main.py`

The program keeps running, writing one record every 5 seconds.

## Manual reset procedure

If you see:
`CRITICAL ALERT: temperature > 100C. Machine stopped.`
The program will pause and prompt:
`Perform a safe manual reset, then press Enter to continue...`

Before resuming, the operator should verify the machine condition, reset it safely, and only then press Enter.

## Generated artifacts

- Database: `data/smartlog.db`
- Daily backups: `cloud_backup/backup_YYYYMMDD.json`

## Notes

- Valid humidity must be between 0 and 100. Values outside that range are discarded.
- To stop the program, use `Ctrl+C`.

