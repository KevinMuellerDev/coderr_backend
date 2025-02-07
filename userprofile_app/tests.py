from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile
from django.core.files.uploadedfile import SimpleUploadedFile

class ProfileModelTest(TestCase):

    def setUp(self):
        # Erstelle einen User, der später mit dem Profil verknüpft wird
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_user_directory_path(self):
        test_image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        profile = Profile.objects.create(user=self.user, username="Test", first_name="Test", last_name="User", file=test_image)
        
        expected_path_start = f'user/{self.user.id}/test_image'

        self.assertTrue(profile.file.name.startswith(expected_path_start))
        print(profile.file.name) 


class ProfileModelTest(TestCase):

    def setUp(self):
        # Erstelle einen User
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_profile_model(self):
        # Erstelle eine Beispiel-Datei
        test_image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        
        # Erstelle ein Profile-Objekt und weise ihm ein Bild sowie andere Felder zu
        profile = Profile.objects.create(
            user=self.user,
            username="Test",
            first_name="Test",
            last_name="User",
            file=test_image,
            location="Test Location",
            tel="1234567890",
            description="Test description",
            working_hours="9-5",
            type="business",
            email="testuser@example.com"
        )
        
        # Gib das ganze Profil aus, um es in der Konsole zu überprüfen
        print("Profile Model Output:")
        print(f"User ID: {profile.user.id}")
        print(f"Username: {profile.username}")
        print(f"First Name: {profile.first_name}")
        print(f"Last Name: {profile.last_name}")
        print(f"File: {profile.file.name}")
        print(f"Location: {profile.location}")
        print(f"Tel: {profile.tel}")
        print(f"Description: {profile.description}")
        print(f"Working Hours: {profile.working_hours}")
        print(f"Type: {profile.type}")
        print(f"Email: {profile.email}")
        print(f"Created At: {profile.created_at}")

        # Optional: Teste, ob der Pfad korrekt generiert wird
        expected_path_start = f'user/{self.user.id}/test_image'
        self.assertTrue(profile.file.name.startswith(expected_path_start))
