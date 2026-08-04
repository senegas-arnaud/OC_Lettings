from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Profile


class ProfileModelTest(TestCase):
    """Tests unitaires pour le modèle Profile."""

    def setUp(self):
        """Crée un utilisateur et un profil de test."""
        self.user = User.objects.create_user(
            username='johndoe',
            password='testpass123',
            first_name='John',
            last_name='Doe',
            email='john.doe@example.com',
        )
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city='Paris',
        )

    def test_profile_str(self):
        """Vérifie que __str__ retourne le username de l'utilisateur."""
        self.assertEqual(str(self.profile), 'johndoe')

    def test_profile_fields(self):
        """Vérifie que les champs sont correctement enregistrés."""
        self.assertEqual(self.profile.favorite_city, 'Paris')
        self.assertEqual(self.profile.user, self.user)

    def test_profile_user_relation(self):
        """Vérifie la relation OneToOne vers User."""
        self.assertEqual(self.profile.user.username, 'johndoe')
        self.assertEqual(self.profile.user.first_name, 'John')
        self.assertEqual(self.profile.user.email, 'john.doe@example.com')

    def test_profile_favorite_city_blank(self):
        """Vérifie que favorite_city peut être laissé vide (blank=True)."""
        user2 = User.objects.create_user(username='janedoe', password='testpass123')
        profile2 = Profile.objects.create(user=user2)
        self.assertEqual(profile2.favorite_city, '')


class ProfilesIndexViewTest(TestCase):
    """Tests unitaires pour la vue index (liste des profils)."""

    def setUp(self):
        """Crée un utilisateur et un profil de test."""
        self.user = User.objects.create_user(
            username='alicesmith',
            password='testpass123',
        )
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city='Lyon',
        )

    def test_index_status_code(self):
        """Vérifie que la page liste répond avec un statut 200."""
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)

    def test_index_uses_correct_template(self):
        """Vérifie que le bon template est utilisé."""
        response = self.client.get(reverse('profiles:index'))
        self.assertTemplateUsed(response, 'profiles/index.html')

    def test_index_contains_profile(self):
        """Vérifie que le profil créé apparaît bien dans le contexte."""
        response = self.client.get(reverse('profiles:index'))
        self.assertIn(self.profile, response.context['profiles_list'])

    def test_index_contains_username_in_content(self):
        """Vérifie que le username s'affiche dans la page."""
        response = self.client.get(reverse('profiles:index'))
        self.assertContains(response, 'alicesmith')


class ProfileDetailViewTest(TestCase):
    """Tests unitaires pour la vue profile (détail d'un profil)."""

    def setUp(self):
        """Crée un utilisateur et un profil de test."""
        self.user = User.objects.create_user(
            username='bobmartin',
            password='testpass123',
            first_name='Bob',
            last_name='Martin',
            email='bob.martin@example.com',
        )
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city='Marseille',
        )

    def test_profile_detail_status_code(self):
        """Vérifie que la page détail répond avec un statut 200."""
        response = self.client.get(
            reverse('profiles:profile', args=[self.user.username])
        )
        self.assertEqual(response.status_code, 200)

    def test_profile_detail_uses_correct_template(self):
        """Vérifie que le bon template est utilisé."""
        response = self.client.get(
            reverse('profiles:profile', args=[self.user.username])
        )
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_profile_detail_context(self):
        """Vérifie que le contexte contient bien le profil attendu."""
        response = self.client.get(
            reverse('profiles:profile', args=[self.user.username])
        )
        self.assertEqual(response.context['profile'], self.profile)

    def test_profile_detail_nonexistent_username_returns_404(self):
        """Vérifie qu'un username inexistant renvoie bien une 404."""
        response = self.client.get(
            reverse('profiles:profile', args=['nonexistent_user'])
        )
        self.assertEqual(response.status_code, 404)
