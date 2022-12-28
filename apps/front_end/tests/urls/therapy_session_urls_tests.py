from django.test import TestCase
from django.urls import reverse
from parameterized import parameterized


class TherapySessionURLsTest(TestCase):
    @parameterized.expand(
        [
            ("create_session", "/prontuary/1/create_session/"),
            ("therapy_session_save", "/prontuary/1/create_session/save/"),
            ("therapy_session_update", "/therapy_session/1/update/"),
            ("therapy_session_update_payment", "/therapy_session/1/update_payment/"),
            ("therapy_session_update_fault", "/therapy_session/1/update_fault/"),
            ("therapy_session_delete", "/therapy_session/1/delete/"),
            ("therapy_session_delete_confirm", "/therapy_session/1/delete_confirm/"),
        ]
    )
    def test_therapy_sessions_with_id_url_is_correct(self, url_name, expected_path):
        url = reverse(url_name, kwargs={"id": 1})
        self.assertEqual(url, expected_path)
