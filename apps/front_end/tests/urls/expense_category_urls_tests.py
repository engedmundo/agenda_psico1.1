from django.test import TestCase
from django.urls import reverse
from parameterized import parameterized


class ExpenseCategoryURLsTest(TestCase):
    @parameterized.expand(
        [
            ("expense_category", "/expense_category/"),
            ("create_expense_category", "/expense_category/create/"),
            ("expense_category_save", "/expense_category/save/"),
            ("expense_category_archived", "/expense_category/archived/"),
        ]
    )
    def test_expense_categorys_urls_is_correct(self, url_name, expected_path):
        url = reverse(url_name)
        self.assertEqual(url, expected_path)

    @parameterized.expand(
        [
            ("expense_category_update", "/expense_category/1/update/"),
            ("expense_category_archive", "/expense_category/1/archive/"),
            (
                "expense_category_archive_confirm",
                "/expense_category/1/archive_confirm/",
            ),
            ("expense_category_unarchive", "/expense_category/1/unarchive/"),
            ("expense_category_delete", "/expense_category/1/delete/"),
            ("expense_category_delete_confirm", "/expense_category/1/delete_confirm/"),
        ]
    )
    def test_expense_categorys_with_id_url_is_correct(self, url_name, expected_path):
        url = reverse(url_name, kwargs={"id": 1})
        self.assertEqual(url, expected_path)
