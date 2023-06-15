import subprocess


def get_chrome_version():
    """
    Récupère la version de Google Chrome installée sur le système.

    Returns:
        str: La version de Google Chrome, ou None si Chrome n'est pas installé ou si la version ne peut pas être récupérée.

    Raises:
        FileNotFoundError: Si la clé de registre spécifiée n'est pas trouvée.
        OSError: En cas d'erreur lors de l'accès au registre Windows.
        winreg.WindowsError: En cas d'erreur lors de la récupération de la valeur de la clé de registre.

    Note:
        Cette fonction utilise le registre Windows pour obtenir la version de Google Chrome.
        Assurez-vous que la clé de registre 'HKEY_CURRENT_USER\SOFTWARE\Google\Chrome\BLBeacon' est présente sur le système.
    """
    try:
        # Mettre à jour pip
        subprocess.check_call(['pip', 'install', '--upgrade', 'pip'], stdout=subprocess.PIPE)

        # Installer les dépendances
        subprocess.check_call(['pip', 'install', 'selenium'], stdout=subprocess.PIPE)
        subprocess.check_call(['pip', 'install', 'webdriver_manager'], stdout=subprocess.PIPE)

        # Importer les modules requis
        from selenium import webdriver
        from webdriver_manager.chrome import ChromeDriverManager

        # Installer le webdriver avec ChromeDriverManager
        webdriver.Chrome(ChromeDriverManager().install())

        return True
    except (subprocess.CalledProcessError, ImportError) as e:
        print(f"Erreur lors de l'installation du webdriver : {str(e)}")
        return False

def install_webdriver():
    """
    Installe automatiquement le webdriver compatible avec la version de Google Chrome.

    Returns:
        bool: True si l'installation du webdriver est réussie, False sinon.
    """
    try:
        # Mettre à jour pip
        subprocess.check_call(['pip', 'install', '--upgrade', 'pip'])

        # Installer les dépendances
        subprocess.check_call(['pip', 'install', 'selenium'])
        subprocess.check_call(['pip', 'install', 'webdriver_manager'])

        # Importer les modules requis
        from selenium import webdriver
        from webdriver_manager.chrome import ChromeDriverManager

        # Installer le webdriver avec ChromeDriverManager
        webdriver.Chrome(ChromeDriverManager().install())

        return True
    except (subprocess.CalledProcessError, ImportError) as e:
        print(f"Erreur lors de l'installation du webdriver : {str(e)}")
        return False

chrome_version = get_chrome_version()
if chrome_version:
    success = install_webdriver()
    if success:
        print("Le webdriver a été installé avec succès.")
    else:
        print("Échec de l'installation du webdriver.")
else:
    print("Chrome n'est pas installé.")