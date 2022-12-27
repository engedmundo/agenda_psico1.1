import pytest
from apps.front_end.forms import LoginForm
from apps.front_end.tests.fixtures.core_test_fixtures import CoreTestFixtures
from apps.front_end.views import *
from django.test import TestCase
from django.urls import resolve, reverse


class HomeViewsTests(CoreTestFixtures, TestCase):
    def test_home_view_function_is_correct(self):
        view = resolve(reverse("home"))

        self.assertIs(view.func, home)

    def test_home_view_return_status_code_200(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)

    def test_home_view_render_correct_template(self):
        response = self.client.get(reverse("home"))

        self.assertTemplateUsed(response, "pages/home/index.html")

    def test_home_view_returns_correct_context(self):
        self.make_psychologist()
        response = self.client.get(reverse("home"))
        psycho_query = response.context["psychologists"]

        self.assertEqual(len(psycho_query), 1)

    def test_professional_description_function_is_correct(self):
        view = resolve(
            reverse(
                "professional_description",
                kwargs={"id": 1},
            )
        )
        self.assertIs(view.func, professional_description)

    def test_professional_description_view_return_status_code_404(self):
        response = self.client.get(
            reverse(
                "professional_description",
                kwargs={"id": 1},
            )
        )
        self.assertEqual(response.status_code, 404)

    def test_professional_description_view_return_status_code_200(self):
        psycho = self.make_psychologist()

        response = self.client.get(
            reverse(
                "professional_description",
                kwargs={"id": 1},
            )
        )

        self.assertEqual(response.status_code, 200)

    def test_professional_description_view_return_correct_context(self):
        psycho = self.make_psychologist()
        service = self.make_service_modality(psychologist=psycho)

        response = self.client.get(
            reverse(
                "professional_description",
                kwargs={"id": 1},
            )
        )
        response_psycho = response.context["psychologist"]
        response_services = response.context["types_of_service"]

        self.assertIsInstance(response_psycho, Psychologist)
        self.assertEqual(len(response_services), 1)

    def test_professional_description_view_render_correct_template(self):
        psycho = self.make_psychologist()

        response = self.client.get(
            reverse(
                "professional_description",
                kwargs={"id": psycho.id},
            )
        )
        self.assertTemplateUsed(response, "pages/home/profile_description.html")

    def test_login_view_function_is_correct(self):
        view = resolve(reverse("login"))
        self.assertIs(view.func, login_view)

    def test_login_view_return_status_code_200(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/home/index.html")

    def test_login_view_render_correct_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "pages/home/index.html")

    def test_login_view_return_correct_context(self):
        response = self.client.get(reverse("login"))
        response_context = response.context["form"]

        self.assertIsInstance(response_context, LoginForm)

    def test_login_create_function_is_correct(self):
        view = resolve("/login/create/")
        self.assertIs(view.func, login_create)

    def test_logout_view_function_is_correct(self):
        view = resolve(reverse("logout"))
        self.assertIs(view.func, logout_view)
