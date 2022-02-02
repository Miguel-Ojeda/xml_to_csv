from pathlib import Path
import time
from xml_csv_funciones import hlc_data_to_csv, extract_hlc_from_xml
from io_ventanas import elige_carpeta, muestra_mensaje
from subprocess import Popen

'''
# Probamos con un fichero
xml_file = 'D:/Documentos/XML noviembre/Santa Lucia de Tirajana.xml'
csv_file = 'D:/Documentos/XML noviembre/Santa Lucia de Tirajana.csv'


datos_hlc = extract_hlc_from_xml(xml_file)
for item in datos_hlc:
    print(item)
hlc_data_to_csv(datos_hlc, csv_file)
'''

# xml_dir = Path('D:/Documentos/XML noviembre')
xml_dir = Path(elige_carpeta('Elija la carpeta donde están los datos de HLC'))

# Creamos el subdirectorio para los ficheros CSV, basándonos en la fecha y hora actual
str_time = time.strftime('%y%m%d-%H%M%S')
csv_dir = xml_dir / str_time
csv_dir.mkdir(exist_ok=True)

# Vamos a almacenar los datos de cada centro en una lista de diccionarios
# Cada diccionario representa una fila de datos, siendo las keys las columnas
# Una fila podrá ser alguna observación, datos de un docente, ...
# También iremos agregando los datos de todos los centros al total en cada iteración
datos_todos_los_centros = []

for contador, xml_file in enumerate(xml_dir.glob('*.[xX][mM][lL]')):
    # Extraer los datos del centro
    datos_centro = extract_hlc_from_xml(xml_file)
    # Escribir los datos de cada centro en un CSV
    csv_file = csv_dir / f'{xml_file.stem}.csv'
    hlc_data_to_csv(datos_centro, csv_file)
    # Añadimos los datos de cada centro al total con método extend, para añadir todas las filas como nuevos ítems
    datos_todos_los_centros.extend(datos_centro)

# Creamos un CSV con todo_ junto
csv_file = csv_dir / 'todos_los_centros.csv'
hlc_data_to_csv(datos_todos_los_centros, csv_file)

# Salimos
muestra_mensaje('Proceso terminado')
Popen(f'C:/Windows/explorer.exe {csv_dir}')

