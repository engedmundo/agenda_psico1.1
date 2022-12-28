from django.test import TestCase
from django.urls import reverse
from parameterized import parameterized


class ReportURLsTest(TestCase):
    @parameterized.expand(
        [
            ("therapy_session_payment_report", "/therapy_session_payment_report/"),
            ("payment_control_report", "/payment_control_report/"),
            ("expense_control_report", "/expense_control_report/"),
        ]
    )
    def test_reports_url_is_correct(self, url_name, expected_path):
        url = reverse(url_name)
        self.assertEqual(url, expected_path)

    def test_payment_receipt_url_is_correct(self):
        url = reverse("payment_receipt", kwargs={"id": 1})
        self.assertEqual(url, "/payment_receipt/1/")
