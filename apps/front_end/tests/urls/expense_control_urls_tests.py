from django.test import TestCase
from django.urls import reverse
from parameterized import parameterized


class ExpenseControlURLsTest(TestCase):
    @parameterized.expand(
        [
            ("expense_control", "/expense_control/"),
            ("create_expense_control", "/expense_control/create/"),
            ("expense_control_save", "/expense_control/save/"),
        ]
    )
    def test_expense_controls_urls_is_correct(self, url_name, expected_path):
        url = reverse(url_name)
        self.assertEqual(url, expected_path)

    @parameterized.expand(
        [
            ("expense_control_update", "/expense_control/1/update/"),
            ("expense_control_delete", "/expense_control/1/delete/"),
            ("expense_control_delete_confirm", "/expense_control/1/delete_confirm/"),
        ]
    )
    def test_expense_controls_with_id_url_is_correct(self, url_name, expected_path):
        url = reverse(url_name, kwargs={"id": 1})
        self.assertEqual(url, expected_path)
