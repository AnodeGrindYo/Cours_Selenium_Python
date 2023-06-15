"""
Cette classe Scraper est assez générique et peut être utilisée comme base 
pour des scrapers plus spécifiques. Elle utilise Selenium pour naviguer 
vers une URL, trouver des éléments sur la page, et fermer le navigateur.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Scraper:
    def __init__(self):
        # Utiliser Chrome WebDriver
        self.driver = webdriver.Chrome()

    def navigate_to_page(self, url):
        """
        Navigue vers une URL donnée.
        """
        self.driver.get(url)

    def find_element(self, locator, timeout=10):
        """
        Trouve et retourne un élément sur la page en utilisant un locator.
        Attend jusqu'à ce que l'élément soit présent (jusqu'à un certain timeout).
        """
        element_present = EC.presence_of_element_located(locator)
        WebDriverWait(self.driver, timeout).until(element_present)

        return self.driver.find_element(*locator)

    def find_elements(self, locator, timeout=10):
        """
        Trouve et retourne une liste d'éléments sur la page en utilisant un locator.
        Attend jusqu'à ce que les éléments soient présents (jusqu'à un certain timeout).
        """
        elements_present = EC.presence_of_all_elements_located(locator)
        WebDriverWait(self.driver, timeout).until(elements_present)

        return self.driver.find_elements(*locator)

    def close(self):
        """
        Ferme le WebDriver et la fenêtre du navigateur.
        """
        self.driver.quit()
