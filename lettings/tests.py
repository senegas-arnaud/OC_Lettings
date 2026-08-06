"""
Tests unitaires pour l'application lettings.

Couvre les modèles Address et Letting, ainsi que les vues
et URLs associées (liste et détail des locations).
"""

from django.test import TestCase
from .models import Address, Letting
from django.urls import reverse


class AddressModelTest(TestCase):
    """Tests unitaires pour le modèle Address."""

    def setUp(self):
        """Crée une adresse de test réutilisée dans chaque test."""
        self.address = Address.objects.create(
            number=10,
            street='Main Street',
            city='Los Angeles',
            state='CA',
            zip_code=90001,
            country_iso_code='USA',
        )

    def test_address_str(self):
        """Vérifie que __str__ retourne 'numéro rue'."""
        self.assertEqual(str(self.address), '10 Main Street')

    def test_address_fields(self):
        """Vérifie que les champs sont correctement enregistrés."""
        self.assertEqual(self.address.city, 'Los Angeles')
        self.assertEqual(self.address.state, 'CA')
        self.assertEqual(self.address.zip_code, 90001)
        self.assertEqual(self.address.country_iso_code, 'USA')

    def test_address_verbose_name_plural(self):
        """Vérifie que le pluriel affiché est bien 'Addresses'."""
        self.assertEqual(
            str(Address._meta.verbose_name_plural), 'Addresses'
        )


class LettingModelTest(TestCase):
    """Tests unitaires pour le modèle Letting."""

    def setUp(self):
        """Crée une adresse et une location de test."""
        self.address = Address.objects.create(
            number=25,
            street='Sunset Blvd',
            city='Hollywood',
            state='CA',
            zip_code=90028,
            country_iso_code='USA',
        )
        self.letting = Letting.objects.create(
            title='Cozy Studio',
            address=self.address,
        )

    def test_letting_str(self):
        """Vérifie que __str__ retourne le titre de la location."""
        self.assertEqual(str(self.letting), 'Cozy Studio')

    def test_letting_address_relation(self):
        """Vérifie que la relation OneToOne vers Address fonctionne."""
        self.assertEqual(self.letting.address, self.address)
        self.assertEqual(self.letting.address.city, 'Hollywood')


class LettingsIndexViewTest(TestCase):
    """Tests unitaires pour la vue index (liste des locations)."""

    def setUp(self):
        """Crée une adresse et une location de test."""
        self.address = Address.objects.create(
            number=5,
            street='Rodeo Drive',
            city='Beverly Hills',
            state='CA',
            zip_code=90210,
            country_iso_code='USA',
        )
        self.letting = Letting.objects.create(
            title='Luxury Villa',
            address=self.address,
        )

    def test_index_status_code(self):
        """Vérifie que la page liste répond avec un statut 200."""
        response = self.client.get(reverse('lettings:index'))
        self.assertEqual(response.status_code, 200)

    def test_index_uses_correct_template(self):
        """Vérifie que le bon template est utilisé."""
        response = self.client.get(reverse('lettings:index'))
        self.assertTemplateUsed(response, 'lettings/index.html')

    def test_index_contains_letting(self):
        """Vérifie que la location créée apparaît bien dans le contexte."""
        response = self.client.get(reverse('lettings:index'))
        self.assertIn(self.letting, response.context['lettings_list'])

    def test_index_contains_letting_title_in_content(self):
        """Vérifie que le titre de la location s'affiche dans la page."""
        response = self.client.get(reverse('lettings:index'))
        self.assertContains(response, 'Luxury Villa')


class LettingDetailViewTest(TestCase):
    """Tests unitaires pour la vue letting (détail d'une location)."""

    def setUp(self):
        """Crée une adresse et une location de test."""
        self.address = Address.objects.create(
            number=12,
            street='Ocean Avenue',
            city='Santa Monica',
            state='CA',
            zip_code=90401,
            country_iso_code='USA',
        )
        self.letting = Letting.objects.create(
            title='Beach House',
            address=self.address,
        )

    def test_letting_detail_status_code(self):
        """Vérifie que la page détail répond avec un statut 200."""
        response = self.client.get(
            reverse('lettings:letting', args=[self.letting.id])
        )
        self.assertEqual(response.status_code, 200)

    def test_letting_detail_uses_correct_template(self):
        """Vérifie que le bon template est utilisé."""
        response = self.client.get(
            reverse('lettings:letting', args=[self.letting.id])
        )
        self.assertTemplateUsed(response, 'lettings/letting.html')

    def test_letting_detail_context(self):
        """Vérifie que le contexte contient le bon titre et la bonne adresse."""
        response = self.client.get(
            reverse('lettings:letting', args=[self.letting.id])
        )
        self.assertEqual(response.context['title'], 'Beach House')
        self.assertEqual(response.context['address'], self.address)

    def test_letting_detail_nonexistent_id_returns_404(self):
        """Vérifie qu'un ID inexistant renvoie bien une 404."""
        response = self.client.get(
            reverse('lettings:letting', args=[9999])
        )
        self.assertEqual(response.status_code, 404)
