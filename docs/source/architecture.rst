Architecture et structure des données
========================================

Applications Django
----------------------

Le projet est découpé en trois applications, chacune responsable
d'un domaine métier distinct :

``oc_lettings_site``
   Projet principal : page d'accueil, configuration globale,
   fichiers statiques et gestion des erreurs 404/500.

``lettings``
   Gestion des locations immobilières.

``profiles``
   Gestion des profils utilisateurs.

Modèles de données
----------------------

**Address** (application ``lettings``)
   Représente une adresse postale : numéro, rue, ville, état,
   code postal, code ISO du pays.

**Letting** (application ``lettings``)
   Représente une location, associée à une ``Address`` via une
   relation one-to-one.

**Profile** (application ``profiles``)
   Représente le profil d'un utilisateur, associé à un ``User``
   Django via une relation one-to-one, avec un champ optionnel
   ``favorite_city``.

Voir la section :doc:`Référence de l'API <lettings>` pour le détail
complet des champs et méthodes de chaque modèle.