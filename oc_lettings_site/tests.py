"""
Tests unitaires pour l'application oc_lettings_site.

Couvre la vue index (page d'accueil) ainsi que les pages
d'erreur personnalisées 404 et 500.
"""

from django.test import TestCase
from django.urls import reverse


class IndexViewTest(TestCase):
    """Tests unitaires pour la vue index (page d'accueil)."""

    def test_index_status_code(self):
        """Vérifie que la page d'accueil répond avec un statut 200."""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_index_uses_correct_template(self):
        """Vérifie que le bon template est utilisé."""
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index.html')

    def test_index_content(self):
        """Vérifie que la page contient le texte de bienvenue attendu."""
        response = self.client.get(reverse('index'))
        self.assertContains(response, 'Welcome to Holiday Homes')
