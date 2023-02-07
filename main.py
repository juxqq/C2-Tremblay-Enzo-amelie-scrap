import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

session = requests.Session()

payload = {
    "type": "ps",
    "ps_profession": "34",
    "ps_profession_label": "Médecin généraliste",
    "ps_localisation": "HERAULT (34)",
    "localisation_category": "departements",
}

headers = {
    'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1'
}

url = "http://annuairesante.ameli.fr/recherche.html"

def get_datas():
    data = []
    pageNumber = 1
    for url in range(20):
        url = f"http://annuairesante.ameli.fr/professionnels-de-sante/recherche/liste-resultats-page-{pageNumber}-par_page-20-tri-aleatoire.html"
        pageNumber += 1
        page = session.post(url)

        soup = BeautifulSoup(page.content, "html.parser")

        medecins = soup.find_all('div', class_='item-professionnel-inner')
        
        for medecin in medecins:
            nom = medecin.find('h2').text.strip()
            num_div = medecin.find('div', class_='item left tel')
            if num_div:
                numero = num_div.text.strip()
            else:
                numero = None
            adresse = medecin.find('div', class_='item left adresse').text.strip()
            adresse_finale = ', '.join(re.split(r'(\d+)', adresse))
            data.append([nom, numero, adresse_finale])
            
    df = pd.DataFrame(data, columns=['Nom', 'Numéro', 'Adresse'])
    df.to_csv("medecins.csv", encoding='UTF-16', index=False, columns=['Nom', 'Numéro', 'Adresse'])
    
session.post(url, headers=headers, params=payload)
get_datas()