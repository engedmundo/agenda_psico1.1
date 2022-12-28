from django.test import TestCase
from django.urls import reverse
from parameterized import parameterized


class HomeURLsTest(TestCase):
    @parameterized.expand(
        [
            ("home", "/"),
            ("login", "/login/"),
            ("login_create", "/login/create/"),
            ("logout", "/logout/"),
            ("my_profile", "/my_profile/"),
        ]
    )
    def test_home_urls_is_correct(self, url_name, expected_path):
        url = reverse(url_name)
        self.assertEqual(url, expected_path)

    def test_professional_description_url_is_correct(self):
        url = reverse("professional_description", kwargs={"id": 1})
        self.assertEqual(url, "/professional_description/1/")
