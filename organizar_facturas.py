import os
import shutil
import re
from datetime import datetime

# 📂 Ruta donde están las facturas
# Cambia esta ruta por la tuya
carpeta_origen = 'D:/Python/proyectos_serios/facturas'
carpeta_destino = os.path.join(carpeta_origen, "Organizadas")

# 🛠 Asegúrate de que la carpeta destino exista
os.makedirs(carpeta_destino, exist_ok=True)

# 🧠 Patrón de nombre de archivo: Factura_ClienteX_YYYY-MM-DD.pdf
patron = r"Factura_(.*?)_(\d{4}-\d{2}-\d{2})\.pdf"

# 📄 Recorrer todos los archivos PDF en la carpeta
for archivo in os.listdir(carpeta_origen):
    if archivo.endswith(".pdf"):
        match = re.match(patron, archivo)
        if match:
            cliente = match.group(1)
            fecha_str = match.group(2)
            try:
                fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
                carpeta_mes = fecha.strftime("%Y-%m")  # Ej: 2024-05

                # Crear carpeta por cliente y mes
                carpeta_cliente = os.path.join(carpeta_destino, cliente)
                carpeta_final = os.path.join(carpeta_cliente, carpeta_mes)
                os.makedirs(carpeta_final, exist_ok=True)

                # Mover el archivo
                ruta_origen = os.path.join(carpeta_origen, archivo)
                ruta_destino = os.path.join(carpeta_final, archivo)
                shutil.move(ruta_origen, ruta_destino)

                print(f"✅ {archivo} movido a {ruta_destino}")
            except ValueError:
                print(f"⚠️ Fecha inválida en: {archivo}")
        else:
            print(f"⚠️ Nombre de archivo no válido: {archivo}")
