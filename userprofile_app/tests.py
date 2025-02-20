from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile
from django.core.files.uploadedfile import SimpleUploadedFile

class ProfileModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_user_directory_path(self):
        test_image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        profile = Profile.objects.create(user=self.user, username="Test", first_name="Test", last_name="User", file=test_image)
        
        expected_path_start = f'user/{self.user.id}/test_image'

        self.assertTrue(profile.file.name.startswith(expected_path_start))


class ProfileModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_profile_model(self):
        test_image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        
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

        expected_path_start = f'user/{self.user.id}/test_image'
        self.assertTrue(profile.file.name.startswith(expected_path_start))
