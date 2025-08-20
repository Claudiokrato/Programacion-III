import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import os
os.system ("clear")


# URL de CKWeb
url = "https://www.justiciachaco.gov.ar"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Timestamp del scraping
fecha_scraping = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Extraer título principal <h1>
titulo_h1 = soup.find("h1")
titulo_principal = titulo_h1.get_text(strip=True) if titulo_h1 else "No encontrado"

# Extraer subtítulos <h2>
subtitulos = [h2.get_text(strip=True) for h2 in soup.find_all("h2")]

# Extraer párrafos <p>
parrafos = [p.get_text(strip=True) for p in soup.find_all("p") if p.get_text(strip=True)]

# Extraer enlaces con texto visible
enlaces = [
    (a.get_text(strip=True), a.get("href"))
    for a in soup.find_all("a", href=True)
    if a.get_text(strip=True)
]

# Crear y guardar CSV
with open("justicia_scraping.csv", "w", newline="", encoding="utf-8") as archivo_csv:
    writer = csv.writer(archivo_csv)
    writer.writerow(["Fecha Scraping", fecha_scraping])
    writer.writerow(["Título Principal", titulo_principal])
    writer.writerow([])
    writer.writerow(["Subtítulos"])
    for subtitulo in subtitulos:
        writer.writerow([subtitulo])
    writer.writerow([])
    writer.writerow(["Párrafos"])
    for parrafo in parrafos:
        writer.writerow([parrafo])
    writer.writerow([])
    writer.writerow(["Enlaces", "URL"])
    for texto, href in enlaces:
        writer.writerow([texto, href])

print("✅ Contenido extraído y guardado en 'ckweb_scraping.csv'")
