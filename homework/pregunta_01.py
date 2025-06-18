"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import pandas as pd
import re
# pylint: disable=import-outside-toplevel

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """

    with open('files/input/clusters_report.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    lines = lines[4:]

    registros = []
    fila = ''

    for line in lines:
        if re.match(r"^\s+\d+\s+", line):
            if fila:
                registros.append(fila)
            fila = line.strip()
        else:
            fila += " " + line.strip()
    if fila:
        registros.append(fila)

    data = []
    for reg in registros:
        partes = re.split(r'\s{2,}', reg)
        if len(partes) >= 4:
            cluster = int(partes[0])
            cantidad = int(partes[1])
            porcentaje = float(partes[2].replace(',', '.').replace('%', '').strip())
            palabras_clave = partes[3]
            if len(partes) > 4:
                palabras_clave += " " + " ".join(partes[4:])
            palabras_clave = re.sub(r'\s+', ' ', palabras_clave.replace('.', '')).strip()
            data.append([cluster, cantidad, porcentaje, palabras_clave])

    # Crear el DataFrame
    df = pd.DataFrame(data, columns=[
        'cluster', 
        'cantidad_de_palabras_clave', 
        'porcentaje_de_palabras_clave', 
        'principales_palabras_clave'
    ])

    return df
