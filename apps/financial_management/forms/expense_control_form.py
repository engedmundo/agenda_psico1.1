from apps.financial_management.models import ExpenseControl
from django import forms


class ExpenseControlRegisterForm(forms.ModelForm):
    class Meta:
        model = ExpenseControl
        fields = [
            "category",
            "expense_value",
            "completion_date",
            "description",
            "cpf_cnpj",
        ]

        labels = {
            "category": "Categoria de despesa:",
            "expense_value": "Valor (R$):",
            "completion_date": "Data do pagamento:",
            "description": "Descrição da despesa:",
            "cpf_cnpj": "CPF/CNPJ do Recebedor:",
        }
