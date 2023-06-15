from scraper import Scraper
from film import Film
from selenium.webdriver.common.by import By

class IMDBScraper(Scraper):
    def __init__(self):
        super().__init__()
        self.base_url = "https://www.imdb.com"

    def get_top_50_films(self):
        """
        Récupère les 50 films les mieux notés sur IMDB.
        """
        # Naviguer vers la page des films les mieux notés
        self.navigate_to_page(f"{self.base_url}/chart/top/")

        # Trouver les lignes du tableau contenant les films
        rows = self.find_elements((By.XPATH, "//table[contains(@class, 'chart')]//tr"))

        # Extraire les informations des films
        films = []
        for row in rows[1:51]:  # Ignorer l'en-tête du tableau (première ligne)
            films.append(Film(row))

        return films

# Code pour tester si ce fichier est exécuté en tant que script principal
if __name__ == "__main__":
    scraper = IMDBScraper()
    films = scraper.get_top_50_films()
    for film in films:
        print(f"{film.title} ({film.year}): {film.rating}")
    scraper.close()
