from selenium.webdriver.common.by import By


class Film:

    def __init__(self, row):
        # Extraire les informations de la ligne (row) passée en paramètre
        self.title = self.extract_title(row)
        self.year = self.extract_year(row)
        self.rating = self.extract_rating(row)
        self.votes = self.extract_votes(row)
        self.url = self.extract_url(row)
        self.director, self.main_actors = self.extract_director_and_main_actors(row)

    @staticmethod
    def extract_title(row):
        title_element = row.find_element(By.CSS_SELECTOR, ".titleColumn a")
        return title_element.text

    @staticmethod
    def extract_year(row):
        year_element = row.find_element(By.CSS_SELECTOR, ".titleColumn span.secondaryInfo")
        return year_element.text.strip('()')

    @staticmethod
    def extract_rating(row):
        rating_element = row.find_element(By.CSS_SELECTOR, ".imdbRating strong")
        return rating_element.get_attribute("title").split(' based on')[0]

    @staticmethod
    def extract_votes(row):
        rating_element = row.find_element(By.CSS_SELECTOR, ".imdbRating strong")
        return rating_element.get_attribute("title").split(' based on ')[1].split(' user')[0].replace('\xa0', '')

    @staticmethod
    def extract_url(row):
        url_element = row.find_element(By.CSS_SELECTOR, ".titleColumn a")
        return url_element.get_attribute("href")

    @staticmethod
    def extract_director_and_main_actors(row):
        title_element = row.find_element(By.CSS_SELECTOR, ".titleColumn a")
        title_info = title_element.get_attribute("title")
        
        # Split the string into director and main actors
        director_info, main_actors_info = title_info.split(" (dir.), ", 1)
        director = director_info.strip()
        main_actors = [actor.strip() for actor in main_actors_info.split(",")]
        
        return director, main_actors
