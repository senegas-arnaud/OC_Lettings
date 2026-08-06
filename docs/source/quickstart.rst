Guide de démarrage rapide
============================

Lancer le serveur de développement
--------------------------------------

.. code-block:: bash

   python manage.py runserver

Le site est alors accessible sur http://127.0.0.1:8000/

Lancer les tests
------------------

.. code-block:: bash

   pytest

Vérifier la couverture de tests
-----------------------------------

.. code-block:: bash

   pytest --cov=lettings --cov=profiles --cov=oc_lettings_site --cov-report=term-missing

Vérifier le linting
----------------------

.. code-block:: bash

   flake8

Lancer le projet avec Docker
--------------------------------

.. code-block:: bash

   docker build -t oc-lettings .
   docker run --rm -p 8000:8000 --env-file .env oc-lettings