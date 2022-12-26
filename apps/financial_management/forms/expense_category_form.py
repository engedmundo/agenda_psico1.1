from apps.financial_management.models import ExpenseCategory
from django import forms


class ExpenseCategoryRegisterForm(forms.ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = [
            "name",
            "description",
        ]
        required = [
            "name",
            "description",
        ]

        labels = {
            "name": "Nome do categoria:",
            "description": "Descrição da categoria:",
        }
