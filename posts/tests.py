from django.test import TestCase
from django.urls import reverse
from .models import Post


# Create your tests here.
class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(title="Just a test", content="Just a test")

    def test_model_title(self):
        self.assertEqual(self.post.title, "Just a test")

    def test_model_content(self):
        self.assertEqual(self.post.content, "Just a test")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "Just a test")
