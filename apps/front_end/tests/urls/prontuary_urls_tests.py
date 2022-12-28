from django.test import TestCase
from django.urls import reverse
from parameterized import parameterized


class ProntuaryURLsTest(TestCase):
    @parameterized.expand(
        [
            ("prontuary", "/prontuary/"),
            ("create_prontuary", "/prontuary/create/"),
            ("prontuary_save", "/prontuary/save/"),
            ("prontuary_archived", "/prontuary/archived/"),
        ]
    )
    def test_prontuaries_urls_is_correct(self, url_name, expected_path):
        url = reverse(url_name)
        self.assertEqual(url, expected_path)

    @parameterized.expand(
        [
            ("prontuary_update", "/prontuary/1/update/"),
            ("prontuary_details", "/prontuary/1/"),
            ("prontuary_archive", "/prontuary/1/archive/"),
            ("prontuary_archive_confirm", "/prontuary/1/archive_confirm/"),
            ("prontuary_unarchive", "/prontuary/1/unarchive/"),
            ("prontuary_delete", "/prontuary/1/delete/"),
            ("prontuary_delete_confirm", "/prontuary/1/delete_confirm/"),
        ]
    )
    def test_prontuaries_with_id_url_is_correct(self, url_name, expected_path):
        url = reverse(url_name, kwargs={"id": 1})
        self.assertEqual(url, expected_path)
