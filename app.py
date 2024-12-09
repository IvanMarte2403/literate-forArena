import csv
import os

# Ruta del CSV
csv_file = 'datos.csv'

# Carpeta de salida
output_dir = 'firmas'
os.makedirs(output_dir, exist_ok=True)

# Leer la plantilla HTML
with open('Firma.html', 'r', encoding='utf-8') as f:
    template = f.read()

with open(csv_file, 'r', encoding='latin-1', newline='') as f:
    # Definimos los fieldnames manualmente
    fieldnames = ['Nombre', 'correo', 'Puesto']
    reader = csv.DictReader(f, fieldnames=fieldnames, delimiter=';')
    
    # Si la primera línea es un encabezado incorrecto, podemos saltarla
    # next(reader)  # Descomentar si fuera necesario saltar la primera línea
    
    for row in reader:
        nombre = row.get('Nombre', '').strip()
        correo = row.get('correo', '').strip()
        puesto = row.get('Puesto', '').strip()

        if not nombre:
            continue

        html_content = template.replace('{{NOMBRE}}', nombre)
        html_content = html_content.replace('{{CORREO}}', correo)
        html_content = html_content.replace('{{PUESTO}}', puesto)

        nombre_archivo = f"firma_{nombre.replace(' ', '_')}.html"
        output_path = os.path.join(output_dir, nombre_archivo)

        with open(output_path, 'w', encoding='utf-8') as out:
            out.write(html_content)

        print(f"Archivo {output_path} generado correctamente.")
