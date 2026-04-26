# SmartLog Azucarera

Open-source, educational OT/IT mini-project: a lightweight industrial sensor logger for a sugar factory.
It simulates temperature/humidity readings, stores them locally in SQLite, and writes daily JSON backups for traceability and offline analysis.

## Why this exists

In many plants, data collection starts small (a single PC + a couple of sensors) and later grows into dashboards, alerts, and integrations (MES/ERP).
This repo is intentionally simple but structured so it can be extended into a real monitoring pipeline.

## Features

- Simulated sensor readings (temperature, humidity, machine status)
- Local persistence in SQLite (`data/smartlog.db`)
- Daily JSON backups (`cloud_backup/backup_YYYYMMDD.json`)
- Threshold-based alerts (warning and critical stop with manual reset)

## Project layout

- `main.py`: main loop (sample production-like runtime)
- `sensor_simulator.py`: generates simulated sensor readings
- `database.py`: SQLite initialization + inserts
- `cloud_backup.py`: daily backup writer (JSON)
- `MANUAL.md`: operator-oriented notes

## Requirements

- Python 3.10+ (Windows/macOS/Linux)
- No runtime dependencies for the CLI logger

Optional:
- Web demo dashboard: see `requirements-demo.txt`
- API docs generation: see `requirements-dev.txt`

## Quickstart (Windows PowerShell)

```powershell
cd smartlog-azucarera
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -U pip
py main.py
```

## Quickstart (macOS/Linux)

```bash
cd smartlog-azucarera
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python main.py
```

## Usage example

The logger runs forever and writes a record every 5 seconds.
It prints one of:

- `OK` (temperature ≤ 70°C)
- `WARNING` (temperature > 70°C)
- `FAIL` (temperature > 100°C) and waits for an operator to manually reset

To stop the process:

- `Ctrl+C`

## Configuration

Edit `main.py`:

- `INTERVAL_SECONDS`: sampling interval (default 5 seconds)

## Demo dashboard (Streamlit)

If you want a simple web UI (local-first, runs on your machine):

```powershell
cd smartlog-azucarera
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements-demo.txt
streamlit run streamlit_app.py
```

## API docs (auto-generated)

This repo can generate a static HTML API reference from Python docstrings:

```powershell
cd smartlog-azucarera
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pydoc -w main sensor_simulator database cloud_backup
mkdir -Force docs\\api | Out-Null
Move-Item *.html docs\\api\\ -Force
```

Pre-generated HTML docs are included in `docs/api/`.

## Contributing

See `CONTRIBUTING.md`.

## Wiki

Repo-based wiki pages live in `docs/wiki/`.

## License

MIT, see `LICENSE`.
