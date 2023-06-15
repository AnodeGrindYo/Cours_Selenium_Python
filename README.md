# Apprendre Selenium en python


## I. Introduction à Selenium

### 1. Qu'est-ce que Selenium ?

Tu n'as jamais eu envie d'avoir un assistant pour effectuer des actions sur le web à ta place pour récupérer des informations s, remplir des formulaires, cliquer sur des boutons... Selenium est cet assistant que tu as toujours désiré ! Il ne te préparera pas de café, mais il rendra ta vie tellement plus facile... Et il est obsédé par les navigateurs web.

**Qu'est-ce que Selenium, au juste ?**

Eh bien, Selenium n'est ni un nouvel aliment pour votre régime, ni une nouvelle marque de shampooing. C'est un outil puissant pour automatiser les navigateurs web ! Oui, c'est vrai, Selenium permet à votre code Python de contrôler un navigateur web, tout comme vous le feriez avec votre souris et votre clavier.

Ce n'est pas de la magie (même si ça y ressemble), c'est du pur génie logiciel. Vous écrivez un script Python qui dit à Selenium ce qu'il doit faire, et Selenium exécute ces actions dans un navigateur web. C'est comme avoir un robot miniature qui vit dans votre ordinateur et qui fait tout ce que vous lui dites de faire sur le web.

**Où est-ce que Selenium est utilisé ?**

Selenium est principalement utilisé pour tester les applications web, mais il peut aussi être utilisé pour faire du web scraping, automatiser les tâches répétitives, et bien plus encore. On peut dire que c'est un véritable couteau suisse de l'automatisation du web.

Alors, si vous en avez assez de cliquer manuellement sur des boutons, remplir des formulaires, ou si vous voulez créer un bot pour extraire des données du web, Selenium est fait pour vous. C'est comme donner des super-pouvoirs à votre code Python pour contrôler le web.

### 2. Pourquoi utiliser Selenium ?

#### a. Test d'application web :

Tu as développé une application web et tu es prêt à la lancer. Mais comment peux-tu être sûr qu'elle fonctionne correctement ? Tu pourrais passer des heures à cliquer sur chaque bouton et à remplir chaque formulaire... Ou tu pourrais laisser Selenium le faire pour toi ! Selenium est parfait pour automatiser les tests de bout en bout de ton application web. Il peut cliquer sur les boutons, remplir les formulaires, naviguer à travers les pages, tout comme le ferait un vrai utilisateur.

#### b. Web Scraping :

Tu as besoin de recueillir des données d'un site web ? Pas de problème, Selenium est là pour toi ! Selenium peut naviguer sur un site web et extraire les données dont tu as besoin. C'est particulièrement utile lorsque tu dois interagir avec le site web (par exemple, cliquer sur des boutons ou remplir des formulaires) pour accéder aux données.

#### c. Automatisation de tâches :

Tu en as marre de faire toujours les mêmes tâches répétitives sur le web ? Selenium peut les faire pour toi ! Que tu aies besoin de soumettre des formulaires tous les jours à la même heure, de vérifier régulièrement si une page web a changé, ou de te rappeler de souhaiter un joyeux anniversaire à ta belle-mère, Selenium peut le faire !

#### d. Support multi-navigateurs :

Peu importe si tu es un fan de Chrome, si tu préfères Firefox, ou si tu es nostalgique d'Internet Explorer, Selenium te soutient ! Il fonctionne avec tous les navigateurs principaux, ce qui signifie que tu peux tester ton application sur différents navigateurs pour t'assurer qu'elle fonctionne parfaitement partout.

#### e. Langage de programmation :

Tu adores Python ? Parfait, Selenium aussi ! Mais si un jour tu te sens aventureux et que tu veux essayer Java, C#, Ruby ou JavaScript, devine quoi ? Selenium fonctionne avec ces langages aussi !


### 3. Comment installer Selenium ?

#### Étape 1 : Installer Python

Avant de pouvoir installer Selenium, tu as besoin de Python sur ton ordinateur. Pourquoi ? Parce que Python est comme le carburant de Selenium. Sans Python, Selenium ne peut pas bouger. Si tu ne l'as pas encore installé, tu peux le télécharger sur le [site officiel de Python](https://www.python.org/).
Assure-toi de cocher la case "Add Python to PATH" lors de l'installation. Cela te permettra d'utiliser Python et pip (l'outil d'installation de paquets Python) depuis la ligne de commande.

#### Étape 2 : Créer et activer un environnement virtuel, puis installer Selenium

Les environnements virtuels sont comme des petites bulles isolées où tu peux installer des paquets Python sans affecter ton système global. Ils sont très utiles pour gérer les dépendances de différents projets. Si tu n'en as jamais utilisé auparavant, c'est comme avoir un petit univers personnel où tu es le maître suprême (du moins en ce qui concerne les paquets Python).

Pour créer un nouvel environnement virtuel, ouvre une fenêtre de commande et navigue vers le dossier où tu veux créer ton environnement. Ensuite, tape la commande suivante :

```bash
python3 -m venv mon_env
```

Ici, "mon_env" est le nom de ton environnement virtuel. Tu peux le nommer comme tu le souhaites, mais essaie de choisir un nom qui a du sens pour ton projet.

Une fois l'environnement virtuel créé, tu peux l'activer avec la commande suivante :

Pour Windows:

```bash
mon_env\Scripts\activate
```

Pour Unix ou MacOS:

```bash
source mon_env/bin/activate
```

Félicitations, tu es maintenant dans ton univers personnel !

Maintenant, tu peux installer Selenium. Pour ce faire, tape la commande suivante :

```bash
pip install selenium
```

C'est tout ! Pip va télécharger et installer Selenium dans ton environnement virtuel.


#### Étape 3 : Installer et tester un WebDriver

Selenium a besoin d'un autre ingrédient pour fonctionner : un WebDriver. Le WebDriver est comme un traducteur entre Selenium et ton navigateur web. Il dit à ton navigateur ce que Selenium veut qu'il fasse.

Chaque navigateur a son propre WebDriver. Par exemple, Chrome a le ChromeDriver, Firefox a le GeckoDriver, et ainsi de suite. Pour ce cours, nous utiliserons Chrome et ChromeDriver.

Pour ce cours, nous utiliserons Chrome et ChromeDriver. Heureusement, avec Python, nous avons un outil merveilleux appelé webdriver_manager qui facilite grandement ce processus. webdriver_manager télécharge automatiquement le bon WebDriver pour toi (basé sur ton navigateur), donc pas besoin de jouer à "cherche l'erreur" avec différentes versions de WebDriver et de navigateur.

Pour l'installer, si tu es sur Windows, tu peux exécuter le script `install_webdriver.py` qui se trouve dans ce repository

Pour l'exécuter, utilise la fenêtre de commande dans laquelle ton environnement virtuel est activé et tape (ou copie-colle, tu fais bien ce que tu veux):

```bash
python install_webdriver.py
```

Félicitations, tu as maintenant le WebDriver installé sur ton système !

Pour tester si tout fonctionne comme prévu, nous allons créer un autre petit script Python. Ce script ouvrira une fenêtre Chrome et ira sur la page Google. Voici comment :

```python
# check_webdriver.py

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# créer un objet Service
s = Service(ChromeDriverManager().install())

# créer une nouvelle instance de chrome
driver = webdriver.Chrome(service=s)

# aller à la page Google
driver.get('https://www.google.com')

# pause pour garder la fenêtre ouverte
input("Appuyez sur n'importe quelle touche pour quitter...")
```

tu peux retrouver ce script dans le repository. Son nom est `check_webdriver.py`. Je ne vais pas te dire comment l'exécuter, maintenant tu sais faire 😉

Si tout se passe bien, une nouvelle fenêtre Chrome devrait s'ouvrir et aller sur la page Google. Si ce n'est pas le cas, il y a peut-être eu un problème avec l'installation du WebDriver. Assure-toi que le script install_webdriver.py a été exécuté avec succès et a installé le bon WebDriver.

⚠ **S'il y a un problème...**

Il se peut que tu rencontres des problèmes avec l'installation automatique du WebDriver. Si c'est le cas, ne t'inquiète pas, tu peux aussi installer le WebDriver manuellement.

Pour ce faire, suis les étapes suivantes :

  1. Rends-toi sur la page de téléchargement du ChromeDriver.

  2. Trouve la version du ChromeDriver qui correspond à ta version de Chrome. Tu peux trouver ta version de Chrome en ouvrant Chrome, en cliquant sur les trois points verticaux dans le coin supérieur droit, en allant dans "Aide", puis "À propos de Google Chrome".

  3. Télécharge le fichier correspondant à ton système d'exploitation (Windows, Mac, Linux).

Une fois téléchargé, décompresse le fichier et déplace l'exécutable (chromedriver.exe pour Windows, chromedriver pour Mac/Linux) dans un dossier de ton choix.

Ensuite, tu devras fournir le chemin vers l'exécutable lors de la création de l'instance de WebDriver. Par exemple :

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# chemin vers l'exécutable du pilote
webdriver_path = '/path/to/chromedriver'

# créer un objet Service
s = Service(webdriver_path)

# créer une nouvelle instance de chrome
driver = webdriver.Chrome(service=s)

# aller à la page Google
driver.get('https://www.google.com')

# pause pour garder la fenêtre ouverte
input("Appuyez sur n'importe quelle touche pour quitter...")
```

Voilà, maintenant tu as un plan de secours si l'installation automatique ne fonctionne pas.

## II. Bases de Selenium avec python

### 1.1. Premiers pas avec Selenium WebDriver

#### a. Qu'est-ce que Selenium WebDriver ?

D'accord, alors qu'est-ce que Selenium WebDriver exactement? Eh bien, il fait partie de la famille Selenium, qui est un ensemble d'outils pour l'automatisation du navigateur web. Selenium WebDriver est spécifiquement conçu pour fournir une interface de programmation simple et concise pour naviguer et interagir avec les pages web.

Il est important de noter que Selenium WebDriver est différent des autres outils de Selenium comme Selenium IDE ou Selenium Grid. Alors que Selenium IDE est un outil de record-playback qui n'a pas besoin de connaissances en programmation, et Selenium Grid est utilisé pour l'exécution de tests parallèles sur différentes machines et navigateurs, Selenium WebDriver est utilisé pour écrire des scripts d'automatisation plus sophistiqués et personnalisables.


#### b. Comment Selenium WebDriver fonctionne-t-il ?

Selenium WebDriver interagit avec le navigateur de la même manière qu'un utilisateur le ferait. Il peut cliquer sur des boutons, remplir des formulaires, lire le texte sur la page, et bien plus encore. Mais comment fait-il tout cela?

C'est là que le WebDriver entre en jeu. Le WebDriver est comme un pilote qui conduit Selenium à travers le site web. Chaque navigateur a son propre WebDriver. Par exemple, Chrome a ChromeDriver, Firefox a GeckoDriver, etc.

Lorsque tu écris un script Selenium, tu donnes des instructions à Selenium sur ce que tu veux qu'il fasse. Ces instructions sont ensuite passées au WebDriver. Le WebDriver traduit ces instructions en commandes spécifiques au navigateur, puis les envoie au navigateur pour exécution.

C'est pourquoi le WebDriver est une composante si importante de Selenium. Sans lui, Selenium ne saurait pas comment interagir avec le navigateur.

Dans les prochaines leçons, nous verrons comment utiliser Selenium WebDriver pour accomplir diverses tâches, de la navigation sur un site web à l'interaction avec les éléments d'une page. Prépare-toi à plonger dans le monde fascinant de l'automatisation du web !


#### c. Les différences entre Selenium WebDriver et d'autres outils de Selenium

Selenium est une suite d'outils d'automatisation du navigateur, qui comprend Selenium IDE, Selenium WebDriver et Selenium Grid. Même si tous ces outils font partie de la même suite et visent à faciliter l'automatisation du navigateur, ils ont des différences clés en termes de capacités, de complexité et de cas d'utilisation.

- **Selenium IDE :** C'est l'outil le plus simple de la suite Selenium. C'est une extension de navigateur qui enregistre et rejoue les actions que tu effectues dans ton navigateur. C'est parfait pour les débutants ou pour des tests simples, mais il n'offre pas autant de flexibilité ou de contrôle que WebDriver.

- **Selenium WebDriver :** C'est l'outil que nous allons explorer en profondeur dans ce cours. Contrairement à Selenium IDE, WebDriver te permet d'écrire tes scripts de test dans plusieurs langages de programmation comme Java, C#, Python, etc. Cela signifie que tu peux intégrer tes tests Selenium dans tes projets existants, quelle que soit la langue que tu utilises. De plus, WebDriver te donne plus de contrôle sur tes tests, te permettant de manipuler les éléments de la page, de gérer les fenêtres et les onglets, et bien plus encore.

- **Selenium Grid :** C'est l'outil que tu utiliserais si tu devais exécuter tes tests sur plusieurs machines ou navigateurs simultanément. Selenium Grid te permet de créer une infrastructure de test distribuée où plusieurs instances de WebDriver peuvent exécuter des tests en parallèle. Cela peut être très utile pour les tests à grande échelle ou pour les tests de compatibilité sur plusieurs navigateurs ou systèmes d'exploitation.

**Selenium WebDrive**r se situe entre **Selenium IDE** et **Selenium Grid** en termes de complexité et de flexibilité. C'est un outil puissant qui, lorsqu'il est utilisé correctement, peut grandement améliorer la qualité et l'efficacité de tes tests d'automatisation du navigateur.

### 1.2. Les bases de Selenium WebDriver

Dans cette section, nous allons explorer comment utiliser Selenium WebDriver pour interagir avec les éléments d'une page web, naviguer à travers celle-ci et extraire des informations. Ensuite, nous allons voir quelques exemples concrets de ces actions.


#### a. Comment utiliser Selenium WebDriver pour interagir avec les éléments d'une page web

Interagir avec les éléments d'une page web est au cœur de l'automatisation avec Selenium WebDriver. Voici comment tu peux le faire :

  1. **Trouver des éléments :** Avant de pouvoir interagir avec un élément sur une page web, tu dois d'abord le trouver. Selenium WebDriver fournit plusieurs méthodes pour cela, comme `find_element_by_id`, `find_element_by_name`, `find_element_by_class_name`, `find_element_by_css_selector`, et `find_element_by_xpath`.

  ```python
  # trouver un élément par son ID
  element = driver.find_element_by_id('element_id')
  ```

  2. **Interagir avec des éléments :** Une fois que tu as trouvé un élément, tu peux interagir avec lui de plusieurs façons. Tu peux cliquer dessus (`click`), saisir du texte (`send_keys`), lire son texte (`text`), et bien plus encore.

  ```python
  # cliquer sur un élément
  element.click()

  # saisir du texte dans un champ de texte
  element.send_keys('Hello, World!')
  ```


#### b. Comment utiliser les méthodes de Selenium WebDriver pour naviguer dans une page web

Naviguer dans une page web est une autre fonctionnalité clé de Selenium WebDriver. Tu peux le faire de plusieurs façons :

   1. **Aller à une URL :** La méthode la plus simple pour naviguer à une page web est d'utiliser la méthode `get` de WebDriver avec l'URL de la page.

   ```python
   # aller à Google
  driver.get('https://www.google.com')
   ```

   2. **Naviguer en arrière et en avant :** Tu peux également naviguer en arrière et en avant dans l'historique du navigateur avec les méthodes `back` et `forward`.

   ```python
  # aller en arrière
  driver.back()

  # aller en avant
  driver.forward()
   ```

   3. **Rafraîchir la page :** Tu peux rafraîchir la page actuelle avec la méthode `refresh`.

   ```python
   # rafraîchir la page
  driver.refresh()
   ```

#### c. Comment utiliser les méthodes de Selenium WebDriver pour extraire des informations d'une page web

Extraire des informations d'une page web est un autre aspect essentiel de l'automatisation avec Selenium WebDriver. Tu peux le faire de plusieurs façons :

  1. **Lire le texte d'un élément :** Tu peux lire le texte d'un élément en utilisant la propriété `text`.

  ```python
  # lire le texte d'un élément
  text = element.text
  ```

  2. **Obtenir l'attribut d'un élément :** Tu peux obtenir la valeur d'un attribut d'un élément avec la méthode `get_attribute`.

  ```python
  # obtenir la valeur de l'attribut href d'un lien
  href = element.get_attribute('href')
  ```

  3. **Obtenir l'URL actuelle :** Tu peux obtenir l'URL de la page actuelle avec la propriété `current_url` du WebDriver.

  ```python
  # obtenir l'URL de la page actuelle
  current_url = driver.current_url
  ```

  4. **Obtenir le titre de la page :** Tu peux obtenir le titre de la page actuelle avec la propriété `title` du WebDriver.

  ```python
  # obtenir le titre de la page actuelle
  title = driver.title
  ```

  Maintenant, contrairement à ce que dit [ce type](https://www.youtube.com/watch?v=2bjk26RwjyU), tu as les bases pour utiliser le WebDriver 💪

### 1.3 Exemples de base avec Selenium WebDriver

Dans cette section, nous allons explorer trois exemples de base avec Selenium WebDriver : ouvrir une page web, naviguer dans une page web, et extraire des informations d'une page web.


#### a. Exemple de script pour ouvrir une page web

Voici un script simple pour ouvrir la page d'accueil de Google :

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Instancier le WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Aller à Google
driver.get('https://www.google.com')

# Fermer le navigateur
driver.quit()
```


### b. Exemple de script pour naviguer dans une page web

Voici un script qui va à Google, recherche "cat bounce", clique sur le premier lien, puis navigue en arrière et en avant :

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Instancier le WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Aller à Google
driver.get('https://www.google.com')

# Trouver la barre de recherche
search_bar = driver.find_element(By.NAME, 'q')

# Saisir "OpenAI" et appuyer sur Entrée
search_bar.send_keys('cat bounce' + Keys.RETURN)

# Attendre que la page de résultats se charge
time.sleep(2)

# Cliquer sur le premier lien
first_link = driver.find_element(By.XPATH, '(//h3)[1]')
first_link.click()

# Attendre que la page se charge
time.sleep(2)

# Aller en arrière
driver.back()

# Attendre que la page de résultats se charge à nouveau
time.sleep(2)

# Aller en avant
driver.forward()

# Fermer le navigateur
driver.quit()
```

#### c. Exemple de script pour extraire des informations d'une page web

Voici un script qui va à une vidéo spécifique sur YouTube, extrait le titre de la vidéo et le texte du premier commentaire :

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Instancier le WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Aller à une vidéo spécifique sur YouTube
driver.get('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

# Attendre que la page se charge
time.sleep(2)

# Extraire le titre de la vidéo
title = driver.find_element(By.XPATH, '//*[@id="container"]/h1/yt-formatted-string').text
print(f'Title: {title}')

# Attendre que les commentaires se chargent
time.sleep(2)

# Extraire le texte du premier commentaire
first_comment = driver.find_element(By.XPATH, '//*[@id="content-text"]').text
print(f'First Comment: {first_comment}')

# Fermer le navigateur
driver.quit()

```

#### d. Gérer les onglets et les fenêtres
En utilisant Selenium, tu peux également gérer les onglets et les fenêtres de ton navigateur. Parfois, tu auras besoin d'ouvrir de nouveaux onglets ou fenêtres, de passer d'un onglet à un autre ou de fermer un onglet.

Voici comment tu peux faire tout cela :

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Instancier le WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Aller à une page web
driver.get('https://www.google.com')

# Ouvrir un nouvel onglet
driver.execute_script("window.open('');")

# Passer au nouvel onglet (l'index des onglets commence à 0)
driver.switch_to.window(driver.window_handles[1])

# Aller à une autre page web dans le nouvel onglet
driver.get('https://www.youtube.com')

# Passer de nouveau à l'onglet initial
driver.switch_to.window(driver.window_handles[0])

# Fermer l'onglet initial
driver.close()

# Passer à l'onglet qui reste (qui est maintenant à l'index 0)
driver.switch_to.window(driver.window_handles[0])
```

Dans cet exemple, nous utilisons plusieurs méthodes pour gérer les onglets :

- `execute_script("window.open('');")` : cette méthode permet d'ouvrir un nouvel onglet.
- `window_handles` : cette propriété donne une liste de tous les onglets ouverts. Tu peux passer à un onglet en utilisant son index dans cette liste.
- `switch_to.window(handle)` : cette méthode permet de passer à l'onglet spécifié par sa poignée (qui est son index dans window_handles).
- `close()` : cette méthode permet de fermer l'onglet actuel.

Ces méthodes fonctionnent également pour les fenêtres, pas seulement pour les onglets. Dans Selenium, un "onglet" et une "fenêtre" sont traités de la même manière.

### 1.4 Conseils et astuces pour aller plus loin avec Selenium WebDriver

  1. **Patience :** Selenium nécessite parfois un peu de temps pour charger les éléments ou les pages. Utilise time.sleep() pour laisser le temps à la page de se charger.

  2. **Documentation :** Consulte toujours la documentation officielle de Selenium si tu es bloqué ou si tu veux approfondir une fonctionnalité particulière.

  3. **Inspecter les éléments :** Apprend à inspecter les éléments sur une page web pour trouver leurs attributs et savoir comment les cibler avec Selenium.

  4. **Gestion des exceptions :** Envisage d'ajouter des blocs try/except pour gérer les exceptions et éviter que ton script ne s'arrête brusquement en cas d'erreur.



Félicitations, tu as fait tes premiers pas avec Selenium WebDriver ! Tu sais maintenant comment installer Selenium et un WebDriver, comment utiliser Selenium pour interagir avec des pages web, et tu as même écrit quelques scripts toi-même.

Mais ce n'est que la pointe de l'iceberg ! Selenium a encore beaucoup à offrir. Dans les prochaines parties de ce cours, nous allons explorer des fonctionnalités plus avancées de Selenium, comme les attentes explicites pour gérer les éléments qui prennent du temps à charger, comment interagir avec des éléments plus complexes comme les menus déroulants et les pop-ups, et bien plus encore.

### 2. Aller plus loin avec Selenium : Interagir avec des éléments plus complexes et gérer les attentes

#### 2.1 Interactions avancées vec Selenium

Les listes déroulantes sont des éléments courants sur les sites web. Elles permettent à l'utilisateur de choisir une option parmi plusieurs disponibles. Selenium fournit la classe `Select` pour manipuler de tels éléments.

Voici un exemple de la façon dont tu peux interagir avec une liste déroulante :

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

# Instancier le WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Aller à une page web qui contient une liste déroulante
driver.get('http://www.example.com')

# Trouver la liste déroulante
dropdown = driver.find_element(By.ID, 'dropdown_id')

# Créer une instance de Select
select = Select(dropdown)

# Sélectionner une option par son texte visible
select.select_by_visible_text('Option')

# Sélectionner une option par sa valeur
select.select_by_value('value')

# Sélectionner une option par son index (0-based)
select.select_by_index(1)
```

Dans cet exemple, nous utilisons plusieurs méthodes pour sélectionner une option :

- `select_by_visible_text(text)` : sélectionne l'option par son texte visible.
- `select_by_value(value)` : sélectionne l'option par sa valeur.
- `select_by_index(index)` : sélectionne l'option par son index (0-based).

**Remarque :** *Remplace 'http://www.example.com' et 'dropdown_id' par l'URL de la page web que tu veux visiter et l'identifiant de la liste déroulante que tu veux manipuler. Remplace également `Option`, `value` et `1` par le texte, la valeur ou l'index de l'option que tu veux sélectionner.*


### 2.2  Interagir avec les pop-ups et les alertes

Les pop-ups et les alertes sont des fenêtres qui apparaissent au-dessus du contenu de la page. Elles peuvent être déclenchées par différentes actions, comme un clic sur un bouton. Selenium peut gérer ces fenêtres grâce à sa capacité à passer le contrôle entre les fenêtres et les cadres.

Voici comment tu peux interagir avec les pop-ups et les alertes en utilisant Selenium :

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Instancier le WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Aller à une page web qui déclenche une alerte
driver.get('http://www.example.com')

# Clique sur le bouton qui déclenche l'alerte
button = driver.find_element_by_id('alert_button')
button.click()

# Passer à l'alerte
alert = driver.switch_to.alert

# Obtenir le texte de l'alerte
alert_text = alert.text
print(f'Texte de l\'alerte : {alert_text}')

# Accepter l'alerte
alert.accept()

# Ou refuser l'alerte (si c'est une confirmation)
# alert.dismiss()
```

Dans cet exemple, nous utilisons plusieurs méthodes pour interagir avec l'alerte :

- `switch_to.alert` : cette méthode permet à Selenium de passer le contrôle à l'alerte.
- `alert.text` : cette propriété donne le texte de l'alerte.
- `alert.accept()` : cette méthode permet d'accepter l'alerte (comme si tu cliquais sur "OK")`.
- `alert.dismiss()` : cette méthode permet de refuser l'alerte (comme si tu cliquais sur "Annuler" ou "Fermer"). Note que cette méthode ne fonctionne que pour les alertes de confirmation qui ont une option pour refuser.

**Remarque :** *Remplace 'http://www.example.com' et `alert_button` par l'URL de la page web que tu veux visiter et l'ID du bouton qui déclenche l'alerte.*

### 2.3 Interagir avec les cadres (frames) et les iframes
Les cadres (ou frames) sont des pages web dans la page web. Ils sont couramment utilisés pour incorporer du contenu provenant d'autres sources. Avec Selenium, tu peux passer d'un cadre à un autre en utilisant la méthode `switch_to.frame`.

Voici comment tu peux interagir avec les cadres et les iframes en utilisant Selenium :

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Instancier le WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Aller à une page web qui contient un cadre
driver.get('http://www.example.com')

# Passer au cadre en utilisant son nom ou son ID
driver.switch_to.frame('frame_name')

# Ou passer au cadre en utilisant un élément WebElement
frame = driver.find_element(By.ID, 'frame_id')
driver.switch_to.frame(frame)

# Interagir avec les éléments dans le cadre
element_in_frame = driver.find_element(By.ID, 'element_id')

# Revenir au contenu principal
driver.switch_to.default_content()
```

Dans cet exemple, nous utilisons plusieurs méthodes pour interagir avec les cadres :

- `switch_to.frame(name_or_id)` : cette méthode permet à Selenium de passer le contrôle au cadre spécifié par son nom ou son ID.
- `switch_to.frame(WebElement)` : cette méthode permet à Selenium de passer le contrôle au cadre spécifié par un élément WebElement. C'est utile si le cadre n'a pas de nom ou d'ID, ou si tu as déjà un WebElement pour le cadre.
- `switch_to.default_content()` : cette méthode permet à Selenium de revenir au contenu principal (hors des cadres).

**Remarque :** *Remplace 'http://www.example.com', `frame_name`, `frame_id` et `element_id` par l'URL de la page web que tu veux visiter, le nom ou l'ID du cadre auquel tu veux passer, et l'ID de l'élément avec lequel tu veux interagir*.

### 3. Utilisation de Selenium pour extraire des données du web

#### 3.1 Introduction au web scraping avec Selenium

##### 3.1.1 Qu'est-ce que le web scraping ?

**Définition du web scraping**

Le web scraping, ou "grattage du web", est une méthode utilisée pour extraire des informations à partir de sites web. C'est un peu comme faire de la collecte de données, mais au lieu de collecter des données à partir de fichiers ou de bases de données, tu les collectes à partir de sites web.

**Applications courantes du web scraping**

Le web scraping est souvent utilisé dans une grande variété d'applications, comme :

- Collecter des données pour la recherche : les chercheurs peuvent utiliser le web scraping pour collecter des données sur les tendances sociales, les habitudes de consommation, etc.
- Analyser les sentiments : le web scraping peut être utilisé pour collecter des commentaires ou des critiques sur les réseaux sociaux et analyser les sentiments du public à l'égard d'un produit, d'une marque ou d'un événement.
- Veille concurrentielle : les entreprises peuvent utiliser le web scraping pour surveiller les prix de leurs concurrents, les nouvelles sorties de produits, etc.
- SEO : les spécialistes du marketing peuvent utiliser le web scraping pour analyser le classement des mots clés, les backlinks, etc.

**Les défis du web scraping**

Cependant, le web scraping pose également certains défis :

- Respect de la vie privée : le web scraping doit être réalisé de manière éthique et respecter la vie privée des utilisateurs. Certaines données peuvent être protégées par des lois sur la protection des données.
- Dynamisme des sites web : les sites web sont constamment mis à jour et modifiés, ce qui peut rendre le web scraping difficile si tu te bases sur une structure spécifique de la page.
- Blocage : certains sites web peuvent bloquer les scrapers, soit en limitant le nombre de requêtes que tu peux faire, soit en bloquant ton IP si tu en fais trop.
C'est pourquoi il est essentiel de comprendre les bases du web scraping et de connaître les bonnes pratiques à adopter, ce que nous aborderons dans les prochaines sections de ce cours. Alors, prépare-toi pour une aventure de web scraping avec Selenium !


##### 3.1.2 Pourquoi utiliser Selenium pour le web scraping ?

**Avantages de Selenium pour le web scraping**

Selenium a plusieurs avantages qui le rendent approprié pour le web scraping :

- **Interactions complexes :** Contrairement à d'autres outils de web scraping, Selenium peut gérer des interactions complexes avec un site web. Par exemple, il peut remplir des formulaires, cliquer sur des boutons, naviguer entre les pages, etc. Cela peut être très utile pour les sites web qui nécessitent une interaction de l'utilisateur pour afficher certaines données.

- **Prise en charge du JavaScript :** De nombreux sites web modernes utilisent JavaScript pour charger du contenu de manière dynamique. Selenium peut interagir avec ce contenu dynamique car il charge les pages web de la même manière qu'un navigateur web humain le ferait.

- **Automatisation :** Avec Selenium, tu peux automatiser tout le processus de web scraping. Tu peux programmer ton script pour qu'il se connecte à un site web à des moments précis, collecte des données, les analyse et les stocke.

**Limitations de Selenium pour le web scraping**

Cependant, Selenium a aussi quelques limitations :

- **Performance :** Selenium peut être plus lent que d'autres outils de web scraping car il doit charger toute la page web, y compris les images, les CSS et les scripts JavaScript.

- **Complexité :** Selenium peut être plus complexe à utiliser que d'autres outils de web scraping qui sont spécifiquement conçus pour cette tâche.

**Comparaison de Selenium avec d'autres outils de web scraping**

Il existe de nombreux autres outils de web scraping, comme Beautiful Soup, Scrapy, etc. Ces outils peuvent être plus rapides et plus faciles à utiliser que Selenium pour le web scraping de sites web simples et statiques. Cependant, pour les sites web modernes et dynamiques qui utilisent beaucoup de JavaScript, Selenium est souvent le meilleur choix.


#### 3.2 Les bases du web scraping avec Selenium

##### 3.2.1 Trouver des éléments sur une page web

L'une des tâches les plus courantes en web scraping est de trouver des éléments sur une page web. Selenium offre plusieurs méthodes pour cela, qui peuvent être utilisées en fonction de la nature de l'élément que tu recherches.

**Par ID :** Si l'élément que tu recherches a un attribut id, tu peux le trouver rapidement avec la méthode `find_element_by_id()`. Par exemple :

```python
element = driver.find_element_by_id("mon_id")
```
**Par nom :** Si l'élément a un attribut `name`, tu peux le trouver avec la méthode `find_element_by_name()`. Par exemple :

```python
element = driver.find_element_by_name("mon_nom")
```

**Par classe :** Si tu veux trouver tous les éléments d'une certaine classe, tu peux utiliser la méthode `find_elements_by_class_name()`. Par exemple :

```python
elements = driver.find_elements_by_class_name("ma_classe")
```

**Par sélecteur CSS :** Si tu es familier avec les sélecteurs CSS, tu peux utiliser la méthode `find_element_by_css_selector()` pour trouver un élément. Par exemple :

```python
element = driver.find_element_by_css_selector("div.content > p.first_paragraph")
```

**Par XPath :** XPath est un langage qui peut être utilisé pour naviguer dans les éléments d'un document XML. Comme le HTML peut être considéré comme un type de document XML, tu peux utiliser XPath pour trouver des éléments sur une page web. Par exemple :

```python
element = driver.find_element_by_xpath("//div[@id='mon_id']/p[1]")
```
Chacune de ces méthodes renvoie le premier élément qui correspond à tes critères de recherche. Si tu veux trouver tous les éléments qui correspondent à tes critères, tu peux utiliser les versions "elements" de ces méthodes, comme `find_elements_by_id()`, `find_elements_by_name()`, etc.

Note que ces méthodes renvoient un objet `WebElement`, qui représente un élément sur la page web et qui a ses propres méthodes et attributs pour interagir avec l'élément ou extraire des informations de celui-ci.


##### 3.2.2 Extraire le texte et les attributs d'un élément

Une fois que tu as trouvé un élément sur une page web avec Selenium, tu peux extraire des informations à partir de cet élément. Les informations les plus courantes que tu voudras peut-être extraire sont le texte de l'élément et la valeur de ses attributs.

**Extraire le texte d'un élément**

Tu peux obtenir le texte d'un élément avec la propriété `text` de l'objet WebElement. Par exemple :

```python
element = driver.find_element_by_id("mon_id")
text = element.text
print(text)
```

Ceci affichera le texte de l'élément avec l'ID "mon_id".

**Extraire la valeur d'un attribut**

Tu peux obtenir la valeur d'un attribut d'un élément avec la méthode `get_attribute()` de l'objet `WebElemen`t. Par exemple, si tu veux obtenir la valeur de l'attribut `href` d'un lien, tu peux faire :

```python
element = driver.find_element_by_id("mon_lien")
href = element.get_attribute("href")
print(href)
```

**Attention :** *Note que la méthode `get_attribute()` renvoie toujours une chaîne de caractères, même si la valeur de l'attribut est un nombre. Si tu as besoin d'utiliser cette valeur comme un nombre, tu devras la convertir toi-même avec les fonctions `int()` ou `float()`.*


##### 3.2.3 Naviguer dans la structure d'une page web

Parfois, tu souhaiteras peut-être naviguer dans la structure d'une page web. Par exemple, tu pourrais vouloir trouver le parent d'un élément, ou ses enfants, ou ses frères et sœurs. Selenium te permet de faire cela.

**Trouver le parent d'un élément**

Tu peux trouver le parent d'un élément en utilisant la relation d'axe parent en XPath. Par exemple :

```python
element = driver.find_element_by_id("mon_id")
parent = element.find_element_by_xpath("..")
```

Ceci trouve le parent de l'élément avec l'ID "mon_id".

**Trouver les enfants d'un élément**

Tu peux trouver les enfants d'un élément en utilisant les méthodes de recherche que nous avons vues précédemment, mais en les appelant sur l'objet `WebElement` plutôt que sur l'objet `WebDriver`. Par exemple :


```python
element = driver.find_element_by_id("mon_id")
children = element.find_elements_by_tag_name("p")
```

Ceci trouve tous les éléments <p> qui sont des enfants directs de l'élément avec l'ID "mon_id".

**Trouver les frères et sœurs d'un élément**

Trouver les frères et sœurs d'un élément est un peu plus compliqué, car Selenium n'a pas de méthode directe pour cela. Cependant, tu peux le faire en utilisant XPath. Par exemple :

```python
element = driver.find_element_by_id("mon_id")
siblings = element.find_elements_by_xpath("../child::*")
```

Ceci trouve tous les frères et sœurs de l'élément avec l'ID "mon_id".

Note que ces méthodes renvoient des objets `WebElement`, donc tu peux utiliser toutes les méthodes et propriétés que nous avons vues précédemment pour interagir avec ces éléments ou extraire des informations d'eux.

### 4.3 Exemple de projet : Création d'un robot de web scraping

#### 4.3.1 Planification du projet

Maintenant que tu as les bases du web scraping avec Selenium, il est temps de réaliser un projet ! Nous allons créer un petit robot de web scraping. Pour rendre les choses plus amusantes, nous allons choisir un site web qui a des données intéressantes et un peu de complexité, disons... IMDB, le site web de référence pour les informations sur les films.

##### Objectif du projet

Notre objectif sera de scraper les informations suivantes pour les 50 films les mieux notés de tous les temps :

1. Le titre du film
2. L'année de sortie
3. La note IMDB
4. Le nombre de votes
5. Le réalisateur
6. La liste des acteurs principaux

##### Planification des étapes

1. **Inspection du site web :** Nous devrons d'abord inspecter la structure de la page web pour comprendre où se trouvent les informations que nous voulons extraire.

2. **Création du script de scraping :** Ensuite, nous créerons un script Python qui utilisera Selenium pour naviguer sur la page web, trouver les éléments contenant les informations que nous voulons et les extraire.

3. **Test et débogage :** Nous testerons notre script et corrigerons les problèmes qui pourraient survenir.

4. **Extraction des données **: Enfin, nous exécuterons notre script pour extraire les données que nous voulons.

5. **Analyse des données :** Avec les données en main, nous pourrons les analyser pour répondre à des questions intéressantes, comme "Quelle est la note moyenne des 50 films les mieux notés ?", "Quel réalisateur apparaît le plus souvent dans la liste ?", etc.

6. **Améliorations :** Nous pourrons améliorer notre robot de scraping pour lui faire faire des choses plus sophistiquées, comme naviguer sur plusieurs pages, gérer les erreurs de manière plus robuste, etc.


#### 4.3.2 Mise en place du projet

Maintenant que nous avons notre projet bien planifié, commençons à mettre tout en place. Pour faciliter la gestion du projet, nous allons structurer notre code dans différents fichiers. Suivez les étapes suivantes :

##### **Étape 1: Créer un nouvel environnement virtuel**

Si tu n'as pas déjà un environnement virtuel pour ce projet, crée-en un nouveau. Cela aidera à garder notre espace de travail propre et organisé.

```bash
python -m venv venv_imdb_scraper
source venv_imdb_scraper/bin/activate  # Sur Linux/macOS
venv_imdb_scraper\Scripts\activate     # Sur Windows
```

##### **Étape 2: Installer les dépendances nécessaires**

Nous allons avoir besoin de Selenium pour ce projet. Installe-le en utilisant pip :

```bash
pip install selenium
```

Si tu n'as pas déjà installé le WebDriver pour ton navigateur, fais-le maintenant.

##### **Étape 3: Créer les fichiers du projet**

Nous allons avoir besoin de plusieurs fichiers pour ce projet. Voici une proposition de structure :

- **main.py :** le script principal qui exécutera le robot de scraping.
- **scraper.py :** une classe Python qui encapsulera toutes les fonctionnalités de scraping.
- **imdb.py :** une classe Python qui définira comment scraper le site IMDB.
- **film.py :** une classe Python qui représentera un film.

Crée ces fichiers dans ton répertoire de projet. Ils peuvent tous être vides pour l'instant.

Et maintenant, c'est à toi de jouer !

Tu pourras ensuite regarder ma version du scraper dans ce repository, dans le dossier `IMDB_Scraper`
