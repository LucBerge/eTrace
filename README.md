# eTrace

## Description

eTrace est un outil python fonctionnant sous Linux permettant de retracer tous les sites web sur lesquels vous avec un compte avec une adresse mail.

## Prérequis

Installation de pip :
```
sudo apt-get install python-pip
```

## Installation

Vous pouvez installer eTrace directement depuis le dépôt [PyPi](https://pypi.org/project/eTrace/) :
```
sudo pip install eTrace
```

**Mise à jour**
```
sudo pip install eTrace -U
```

## Désinstallation

Pour désinstaller eTrace :
```
sudo pip uninstall eTrace
```

## Utilisation

Pour lister tous les sites web sur lesquels vous avez un compte avec l'adresse mail `exemple@gmail.com`, utiliser la commande suivante :
```
eTrace exemple@gmail.com
```

Vous pouvez consulter la [liste des sites supportés]() et la [liste des sites non supportés]().

## Contribution

Pour contribuer au projet, vous devez réaliser un fork du projet vers votre espace personnel. Vous pourrez alors faire un pull request en temps voulu. Merci de contacter [@LucBerge](https://github.com/LucBerge) pour plus d'informations sur les tâches à réaliser.


## Issue

File "/usr/lib/python2.7/subprocess.py", line 1343, in _execute_child
- mv geckodrive /usr/local/bin/geckodriver
- driver = webdriver.Firefox(executable_path='/path/to/geckodriver')

https://selenium-python.readthedocs.io/locating-elements.html