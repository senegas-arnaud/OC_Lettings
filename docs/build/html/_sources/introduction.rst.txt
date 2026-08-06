Introduction
============

Description du projet
----------------------

OC Lettings est une application web développée avec Django, permettant de
consulter une liste de locations immobilières (*lettings*) ainsi que les
profils des utilisateurs associés (*profiles*).

Le projet est structuré en trois applications Django :

* ``oc_lettings_site`` : le projet principal, gérant la page d'accueil
  et la configuration globale.
* ``lettings`` : gestion des locations et de leurs adresses.
* ``profiles`` : gestion des profils utilisateurs.

Technologies et langages utilisés
-----------------------------------

* **Langage** : Python 3.13
* **Framework web** : Django 6.0
* **Base de données** : SQLite
* **Serveur applicatif (production)** : Gunicorn
* **Fichiers statiques** : WhiteNoise
* **Monitoring** : Sentry
* **Conteneurisation** : Docker
* **Intégration continue** : GitHub Actions
* **Hébergement** : Render
* **Tests** : pytest, pytest-django, pytest-cov
* **Qualité de code** : flake8
* **Documentation** : Sphinx, Read The Docs