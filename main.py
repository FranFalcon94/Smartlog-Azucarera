import time
from sensor_simulator import generate_sensor_data
from database import init_db, insert_data
from cloud_backup import backup_to_cloud

INTERVAL_SECONDS = 5

def main():
    print("SmartLog Azucarera iniciado...")
    init_db()

    while True:
        data = generate_sensor_data()

        if 0 <= data["humidity"] <= 100:
            insert_data(data)
            backup_to_cloud(data)

            print(f"Datos registrados: {data}")

            if data["temperature"] > 100:
                print("ALERTA CRITICA: temperatura > 100C. Maquina detenida.")
                input("Rearmar manualmente y presiona Enter para continuar...")
            elif data["temperature"] > 70:
                print("AVISO: temperatura > 70C. Notificar al empleado.")
        else:
            print("Dato invalido detectado")

        time.sleep(INTERVAL_SECONDS)

if __name__ == "__main__":
    main()
