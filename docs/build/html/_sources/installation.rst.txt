Installation
============

Prérequis
---------

* Python 3.13 ou supérieur
* Git

Cloner le projet
------------------

.. code-block:: bash

   git clone https://github.com/senegas-arnaud/OC_Lettings.git
   cd OC_Lettings

Créer et activer un environnement virtuel
-------------------------------------------

.. code-block:: bash

   python -m venv .venv
   .venv\Scripts\activate

Installer les dépendances
----------------------------

.. code-block:: bash

   pip install -r requirements.txt

Configurer les variables d'environnement
-------------------------------------------

Créez un fichier ``.env`` à la racine du projet, contenant :

.. code-block:: text

   SECRET_KEY=votre_cle_secrete
   DEBUG=True
   ALLOWED_HOSTS=127.0.0.1,localhost
   SENTRY_DSN=votre_dsn_sentry

Une nouvelle clé secrète peut être générée avec :

.. code-block:: bash

   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

Appliquer les migrations
----------------------------

.. code-block:: bash

   python manage.py migrate

Créer un compte administrateur
----------------------------------

.. code-block:: bash

   python manage.py createsuperuser