# Manual de uso - SmartLog Azucarera

Este documento explica como funciona el programa y como operarlo en planta.

## Que hace el programa
- Lee datos de temperatura y humedad simulados.
- Guarda cada lectura en la base de datos local.
- Genera un backup en `cloud_backup/` con los datos.
- Emite avisos cuando la temperatura supera los umbrales definidos.

## Umbrales y acciones
- Temperatura <= 70C: estado OK.
- Temperatura > 70C: aviso en pantalla para notificar al empleado.
- Temperatura > 100C: alerta critica, la maquina se considera detenida y el programa espera rearme manual.

## Como ejecutar
1. Abre una terminal.
2. Entra a la carpeta del proyecto:
   `C:\Users\franf\PycharmProjects\PythonProject\smartlog-azucarera`
3. Ejecuta:
   `py -u main.py`

El programa se mantiene en ejecucion con lecturas cada 5 segundos.

## Rearme manual
Si aparece el mensaje:
`ALERTA CRITICA: temperatura > 100C. Maquina detenida.`
El programa se detiene y muestra:
`Rearmar manualmente y presiona Enter para continuar...`

El operario debe comprobar la maquina, rearmarla de forma segura y luego presionar Enter para continuar con el registro.

## Archivos generados
- Base de datos: `data/smartlog.db`
- Backups diarios: `cloud_backup/backup_YYYYMMDD.json`

## Consideraciones
- La humedad valida debe estar entre 0 y 100. Si sale fuera de rango se descarta.
- Para detener el programa, usa `Ctrl + C`.
