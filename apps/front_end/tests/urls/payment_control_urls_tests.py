from django.test import TestCase
from django.urls import reverse
from parameterized import parameterized


class PaymentControlURLsTest(TestCase):
    @parameterized.expand(
        [
            ("payment_control", "/payment_control/"),
            ("create_payment_control", "/payment_control/create/"),
            ("payment_control_save", "/payment_control/save/"),
        ]
    )
    def test_payment_controls_urls_is_correct(self, url_name, expected_path):
        url = reverse(url_name)
        self.assertEqual(url, expected_path)

    @parameterized.expand(
        [
            ("payment_control_update", "/payment_control/1/update/"),
            ("payment_control_delete", "/payment_control/1/delete/"),
            ("payment_control_delete_confirm", "/payment_control/1/delete_confirm/"),
        ]
    )
    def test_payment_controls_with_id_url_is_correct(self, url_name, expected_path):
        url = reverse(url_name, kwargs={"id": 1})
        self.assertEqual(url, expected_path)
