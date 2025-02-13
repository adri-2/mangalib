from django.test import TestCase

import requests

url = "http://localhost:8000/api/manga/"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Convertir la réponse en JSON
    
    # Afficher les mangas
    for manga in data["results"]:
        print(f"ID: {manga['id']}, Titre: {manga['title']}, Auteur ID: {manga['author']}")

    # Afficher les liens de pagination
    next_page = data.get("next")
    prev_page = data.get("previous")

    print(f"\nPage suivante: {next_page if next_page else 'Aucune'}")
    print(f"Page précédente: {prev_page if prev_page else 'Aucune'}")

else:
    print(f"Erreur {response.status_code}: {response.text}")



