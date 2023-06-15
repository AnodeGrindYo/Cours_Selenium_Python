from imdb import IMDBScraper


def main():
    print("🍿 Popcorn Time: IMDB Top 50 Scraper 🍿")

    # Créer une instance de notre robot de scraping
    scraper = IMDBScraper()

    # Obtenir la liste des films du site IMDB
    print("🤖 Robot à l'oeuvre... scraping en cours...")
    films = scraper.get_top_50_films()

    # Afficher les informations des films récupérés
    print("\n🎬 Voici les 50 films les mieux notés sur IMDB: 🎬\n")
    for i, film in enumerate(films, start=1):
        print(f"{i}. {film.title} ({film.year})")
        print(f"   Note: {film.rating} ({film.votes} votes)")
        print(f"   Réalisateur: {film.director}")
        print(f"   Acteurs principaux: {', '.join(film.main_actors)}\n")

    print("🎉 C'est terminé! Maintenant, allons regarder un bon film! 🎉")

if __name__ == "__main__":
    main()
