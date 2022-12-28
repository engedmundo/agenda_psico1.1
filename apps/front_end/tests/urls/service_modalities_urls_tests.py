from django.test import TestCase
from django.urls import reverse
from parameterized import parameterized


class ServiceModalityURLsTest(TestCase):
    @parameterized.expand(
        [
            ("service_modality", "/service_modality/"),
            ("create_service_modality", "/service_modality/create/"),
            ("service_modality_save", "/service_modality/save/"),
            ("service_modality_archived", "/service_modality/archived/"),
        ]
    )
    def test_service_modalits_urls_is_correct(self, url_name, expected_path):
        url = reverse(url_name)
        self.assertEqual(url, expected_path)

    @parameterized.expand(
        [
            ("service_modality_update", "/service_modality/1/update/"),
            ("service_modality_archive", "/service_modality/1/archive/"),
            (
                "service_modality_archive_confirm",
                "/service_modality/1/archive_confirm/",
            ),
            ("service_modality_unarchive", "/service_modality/1/unarchive/"),
            ("service_modality_delete", "/service_modality/1/delete/"),
            ("service_modality_delete_confirm", "/service_modality/1/delete_confirm/"),
        ]
    )
    def test_service_modalits_with_id_url_is_correct(self, url_name, expected_path):
        url = reverse(url_name, kwargs={"id": 1})
        self.assertEqual(url, expected_path)
