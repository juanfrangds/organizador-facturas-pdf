# Organizador de Facturas PDF con Python

Este proyecto es un script que automatiza la organización de archivos PDF de facturas.

### 🧠 ¿Qué hace?

🔹 Busca todos los archivos PDF dentro de una carpeta.  
🔹 Extrae el nombre del cliente y la fecha desde el nombre del archivo (ej. `Factura_ClienteA_2025-05-01.pdf`).  
🔹 Crea subcarpetas automáticamente (por cliente y por mes).  
🔹 Mueve cada factura a la carpeta correspondiente.

### 📁 Ejemplo de estructura generada

/Organizadas
└── ClienteA
└── 2025-05
└── Factura_ClienteA_2025-05-01.pdf

### ⚙️ Cómo usar

1. Coloca tus archivos PDF en una carpeta.
2. Edita el script para que apunte a esa ruta.
3. Ejecuta el script con Python.
4. ¡Listo! Tus facturas estarán organizadas por cliente y mes.

### 📦 Dependencias

- Python 3
- Módulos estándar: `os`, `shutil`, `re`, `datetime`

### ✍️ Autor

Desarrollado por Juan Francisco Garcia de Sousa - Automatización con Python para pequeños negocios.  

