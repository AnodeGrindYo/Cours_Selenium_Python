from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# créer un objet Service
s = Service(ChromeDriverManager().install())

# créer une nouvelle instance de chrome
driver = webdriver.Chrome(service=s)

# aller à la page Google
driver.get('https://www.google.com')

# pause pour garder la fenêtre ouverte
input("Appuyez sur n'importe quelle touche pour quitter...")
