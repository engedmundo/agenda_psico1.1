from django.test import TestCase
from django.urls import reverse
from parameterized import parameterized


class PatientURLsTest(TestCase):
    @parameterized.expand(
        [
            ("patient", "/patient/"),
            ("create_patient", "/patient/create/"),
            ("patient_save", "/patient/save/"),
            ("patient_archived", "/patient/archived/"),
        ]
    )
    def test_patients_urls_is_correct(self, url_name, expected_path):
        url = reverse(url_name)
        self.assertEqual(url, expected_path)

    @parameterized.expand(
        [
            ("patient_update", "/patient/1/update/"),
            ("patient_archive", "/patient/1/archive/"),
            ("patient_archive_confirm", "/patient/1/archive_confirm/"),
            ("patient_unarchive", "/patient/1/unarchive/"),
            ("patient_delete", "/patient/1/delete/"),
            ("patient_delete_confirm", "/patient/1/delete_confirm/"),
        ]
    )
    def test_patients_with_id_url_is_correct(self, url_name, expected_path):
        url = reverse(url_name, kwargs={"id": 1})
        self.assertEqual(url, expected_path)
