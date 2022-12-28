from apps.front_end.forms import LoginForm
from apps.core.tests.fixtures.core_models_fixtures import CoreModelFixtures
from apps.core.tests.fixtures.core_form_fixtures import CoreFormFixtures
from apps.front_end.views import *
from django.test import TestCase
from django.urls import resolve, reverse
from parameterized import parameterized


class HomeViewsUnitTests(CoreModelFixtures, TestCase):
    @parameterized.expand(
        [
            ("home", home),
            ("login", login_view),
            ("login_create", login_create),
            ("logout", logout_view),
        ]
    )
    def test_home_views_functions_is_correct(self, url_name, expected_function_name):
        view = resolve(reverse(url_name))
        self.assertIs(view.func, expected_function_name)

    @parameterized.expand(
        [
            ("home"),
            ("login"),
        ]
    )
    def test_home_views_return_status_code_200(self, url_name):
        response = self.client.get(reverse(url_name))

        self.assertEqual(response.status_code, 200)

    @parameterized.expand(
        [
            ("home", "pages/home/index.html"),
            ("login", "pages/home/login.html"),
        ]
    )
    def test_home_views_render_correct_templates(self, url_name, expected_template):
        response = self.client.get(reverse(url_name))

        self.assertTemplateUsed(response, expected_template)

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

    def test_login_view_return_correct_context(self):
        response = self.client.get(reverse("login"))
        response_context = response.context["form"]

        self.assertIsInstance(response_context, LoginForm)


class HomeViewsIntegratedTests(CoreFormFixtures, TestCase):
    def test_login_create_successfully(self):
        form_data = self.make_login_form_data()
        url = reverse("login_create")
        response = self.client.post(
            path=url,
            data=form_data,
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
