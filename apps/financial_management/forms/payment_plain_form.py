from apps.financial_management.models import PaymentPlain
from django import forms


def add_attr(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, "")
    field.widget.attrs[attr_name] = f"{existing} {attr_new_val}".strip()


def add_placeholder(field, placeholder_value):
    add_attr(field, "placeholder", placeholder_value)


class PaymentPlainRegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = PaymentPlain
        fields = [
            "name_plain",
            "plain_value",
        ]
        required = [
            "name_plain",
            "plain_value",
        ]

        labels = {
            "name_plain": "Nome do plano:",
            "plain_value": "Valor do plano (R$)",
        }
