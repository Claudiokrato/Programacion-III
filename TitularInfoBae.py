


import requests
from bs4 import BeautifulSoup
import csv
import os
os.system ("clear")

# Paso 1: Hacer la solicitud a Clarín
url = 'https://www.infobae.com/'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

# Paso 2: Parsear HTML con BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Paso 3: Buscar titulares en etiquetas <h2> (puedes probar con <h1>, <h3> si deseas)
titulares = soup.find_all('h2')

# Paso 4: Extraer texto y guardar en lista
lista_titulares = []
for i, t in enumerate(titulares, 1):
    texto = t.get_text(strip=True)
    if texto:
        lista_titulares.append([i, texto])  # Número + titular

# Paso 5: Guardar en archivo CSV
with open('titulares_infobae.csv', 'w', newline='', encoding='utf-8') as archivo_csv:
    writer = csv.writer(archivo_csv)
    writer.writerow(['Nº', 'Titular'])  # Encabezado
    writer.writerows(lista_titulares)

print("✅ Titulares guardados en 'titulares_infobae.csv'")
