# Developer Notes

## Data model

The SQLite table `sensor_logs` stores:

- `timestamp` (UTC ISO-8601 string)
- `temperature` (C)
- `humidity` (%)
- `machine_status` (`OK`, `WARNING`, `FAIL`)

## Extension points

- Replace `sensor_simulator.generate_sensor_data()` with a real ingestion layer (Modbus/OPC-UA/serial).
- Replace JSON backups with object storage (S3/Azure Blob/etc.) while keeping the same `backup_to_cloud()` interface.
- Add integrity guarantees for backups (e.g., HMAC signatures) to detect tampering.
- Add export commands (CSV/JSON bundles) for BI tooling.

## Operational considerations

- The logger is designed to be local-first. If you network it, define clear access controls and avoid exposing SQLite directly.
- If this is used in regulated contexts, define a retention policy and add audit trails for operator actions.
