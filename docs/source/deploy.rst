Déploiement
=============

Vue d'ensemble
------------------

Le déploiement est entièrement automatisé via un pipeline GitHub Actions,
déclenché à chaque push sur la branche ``main`` :

1. **Build & Test** : installation des dépendances, linting (flake8),
   exécution des tests avec vérification de la couverture (>80%).
2. **Containerisation** : construction de l'image Docker, taguée avec
   ``latest`` et le hash du commit, puis publiée sur Docker Hub.
3. **Déploiement** : appel du Deploy Hook Render, qui récupère la
   nouvelle image et redémarre le service.

Chaque étape ne s'exécute que si la précédente a réussi.

Configuration requise
--------------------------

Secrets GitHub Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``DOCKERHUB_USERNAME`` / ``DOCKERHUB_TOKEN`` : authentification Docker Hub
* ``DJANGO_SECRET_KEY`` : clé secrète Django de production
* ``SENTRY_DSN`` : DSN Sentry
* ``RENDER_DEPLOY_HOOK`` : URL du Deploy Hook Render

Variables d'environnement sur Render
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``SECRET_KEY``, ``SENTRY_DSN``, ``DEBUG=False``, ``ALLOWED_HOSTS``

Procédure de déploiement
------------------------------

Le déploiement est automatique : il suffit de pousser du code sur
``main``. Aucune action manuelle n'est requise sur Render, l'option
*Auto-Deploy* étant désactivée au profit du pilotage par le pipeline
GitHub Actions.

Limite connue
------------------

La base de données SQLite n'est pas persistée entre deux déploiements
sur le tier gratuit de Render (absence de disque persistant). Une
migration vers PostgreSQL (via un service externe comme Neon, gratuit
et permanent) serait nécessaire pour garantir la persistance des
données en production.