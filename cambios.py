import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.bportugal.pt/taxas-cambio"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

f = open('cambios.csv', 'w')
writer = csv.writer(f)
writer.writerow(['País', 'Valor', 'Data'])

tabela_cambios = soup.find(id="rates-full")
cambios = tabela_cambios.find_all("div", class_="rates-row")
for cambio in cambios:
    pais = cambio.find("div", class_="rates-country-name")
    if pais.get_text() == "":
        continue

    valor = cambio.find("div", class_="rates-rate")
    data = cambio.find("div", class_="rates-date")
    pais_final = str(pais.get_text())
    valor_final = valor.get_text()
    data_final = str(data).replace('<div class="rates-date">', '').replace('</div>','')

    writer.writerow([pais_final]+[valor_final]+[data_final])

f.close()
