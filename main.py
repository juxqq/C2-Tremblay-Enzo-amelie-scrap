import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

session = requests.Session()

# Payload for the session post request
payload = {
    "type": "ps",
    "ps_profession": "34",
    "ps_profession_label": "Médecin généraliste",
    "ps_localisation": "HERAULT (34)",
    "localisation_category": "departements",
}

# Headers for the session post request
headers = {
    'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1'
}

# URL for the session post request
url = "http://annuairesante.ameli.fr/recherche.html"

def get_datas():
    """
    Scrapes data from a website and stores the result in a CSV file.

    Returns:
        None
    """
    data = []
    pageNumber = 1
    # Loop through 20 pages of the website
    for url in range(20):
        # Create a URL for each page
        url = f"http://annuairesante.ameli.fr/professionnels-de-sante/recherche/liste-resultats-page-{pageNumber}-par_page-20-tri-aleatoire.html"
        pageNumber += 1
        # Send a POST request to the page
        page = session.post(url)

        # Parse the page content
        soup = BeautifulSoup(page.content, "html.parser")

        # Find all the doctors on the page
        medecins = soup.find_all('div', class_='item-professionnel-inner')
        
        # Extract data for each doctor
        for medecin in medecins:
            nom = medecin.find('h2').text.strip() # Name
            num_div = medecin.find('div', class_='item left tel') # Phone number
            if num_div:
                numero = num_div.text.strip()
            else:
                numero = None
            adresse = medecin.find('div', class_='item left adresse').text.strip() # Address
            adresse_finale = ', '.join(re.split(r'(\d+)', adresse)) # Final address
            data.append([nom, numero, adresse_finale])
            
    # Create a DataFrame from the data
    df = pd.DataFrame(data, columns=['Nom', 'Numéro', 'Adresse'])
    # Write the DataFrame to a CSV file
    df.to_csv("medecins.csv", encoding='UTF-16', index=False, columns=['Nom', 'Numéro', 'Adresse'])
    
# Send a POST request to the website
session.post(url, headers=headers, params=payload)
# Call the function to scrape the data
get_datas()