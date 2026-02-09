# SmartLog Azucarera

Simulador de sensores industriales para una fabrica azucarera. Registra datos en SQLite local y guarda respaldos diarios en archivos JSON.

## Estructura

- `main.py`: bucle principal
- `sensor_simulator.py`: genera datos simulados
- `database.py`: inicializa y escribe en SQLite
- `cloud_backup.py`: respaldo diario en JSON
- `data/smartlog.db`: base de datos local

## Uso

```bash
python main.py
```
