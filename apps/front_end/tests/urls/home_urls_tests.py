import pytest
from django.test import TestCase
from django.urls import reverse


class HomeURLsTest(TestCase):
    def test_home_url_is_correct(self):
        url = reverse("home")
        self.assertEqual(url, "/")

    def test_professional_description_url_is_correct(self):
        url = reverse("professional_description", kwargs={"id": 1})
        self.assertEqual(url, "/professional_description/1/")

    def test_login_url_is_correct(self):
        url = reverse("login")
        self.assertEqual(url, "/login/")

    def test_login_create_url_is_correct(self):
        url = reverse("login_create")
        self.assertEqual(url, "/login/create/")

    def test_logout_url_is_correct(self):
        url = reverse("logout")
        self.assertEqual(url, "/logout/")

    def test_my_profile_url_is_correct(self):
        url = reverse("my_profile")
        self.assertEqual(url, "/my_profile/")
