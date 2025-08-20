import requests
from bs4 import BeautifulSoup

import os
os.system ("clear")

# Paso 1: Solicitud HTTP
url = "https://www.ckweb.com.ar"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

# Paso 2: Crear objeto BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Paso 3: Extraer información

# Título principal <h1>
titulo_h1 = soup.find("h1")
texto_h1 = titulo_h1.get_text(strip=True) if titulo_h1 else "No encontrado"

# Subtítulos <h2>
subtitulos = [h2.get_text(strip=True) for h2 in soup.find_all("h2")]

# Párrafos <p>
parrafos = [p.get_text(strip=True) for p in soup.find_all("p") if p.get_text(strip=True)]

# Enlaces <a> con texto e href
enlaces = [
    (a.get_text(strip=True), a.get("href"))
    for a in soup.find_all("a", href=True)
    if a.get_text(strip=True)
]

# Paso 4: Mostrar resultados
print("Título H1:", texto_h1)
print("\nSubtítulos H2:")
for st in subtitulos:
    print("-", st)

print("\nPárrafos:")
for p in parrafos:
    print("-", p[:60], "...")  # Mostramos los primeros 60 caracteres

print("\nEnlaces:")
for texto, href in enlaces:
    print(f"- {texto}: {href}")
