from django.test import TestCase
from django.urls import reverse
from parameterized import parameterized


class PaymentPlainURLsTest(TestCase):
    @parameterized.expand(
        [
            ("payment_plain", "/payment_plain/"),
            ("create_payment_plain", "/payment_plain/create/"),
            ("payment_plain_save", "/payment_plain/save/"),
            ("payment_plain_archived", "/payment_plain/archived/"),
        ]
    )
    def test_payment_plains_urls_is_correct(self, url_name, expected_path):
        url = reverse(url_name)
        self.assertEqual(url, expected_path)

    @parameterized.expand(
        [
            ("payment_plain_update", "/payment_plain/1/update/"),
            ("payment_plain_archive", "/payment_plain/1/archive/"),
            ("payment_plain_archive_confirm", "/payment_plain/1/archive_confirm/"),
            ("payment_plain_unarchive", "/payment_plain/1/unarchive/"),
            ("payment_plain_delete", "/payment_plain/1/delete/"),
            ("payment_plain_delete_confirm", "/payment_plain/1/delete_confirm/"),
        ]
    )
    def test_payment_plains_with_id_url_is_correct(self, url_name, expected_path):
        url = reverse(url_name, kwargs={"id": 1})
        self.assertEqual(url, expected_path)
