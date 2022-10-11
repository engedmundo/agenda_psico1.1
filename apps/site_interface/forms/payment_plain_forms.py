from django import forms
from apps.financial_management.models import PaymentPlain

def add_attr(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing} {attr_new_val}'.strip()

def add_placeholder(field, placeholder_value):
    add_attr(field, 'placeholder', placeholder_value)

class PaymentPlainRegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['name_plain'], 'Escreva o nome desejado para o plano aqui')

    class Meta:
        model = PaymentPlain
        fields = [
            'name_plain',
            'plain_value',
        ]

        labels = {
            'name_plain': 'Nome do plano/convênio',
            'plain_value': 'Valor do plano/convênio (R$)',
        }

        #help_texts = {}
        #error_messages = {}

        widgets = {
        #    'name_plain': forms.TextInput(attrs={
        #        'placeholder': 'Escreva o nome desejado para o plano aqui', 
        #    }),
            'plain_value': forms.TextInput(attrs={
                'placeholder': 'Escreva o valor do plano aqui', 
            }),
        }