from dataclasses import fields
from django import forms
from apps.patient_management.models import TherapySession

def add_attr(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing} {attr_new_val}'.strip()

def add_placeholder(field, placeholder_value):
    add_attr(field, 'placeholder', placeholder_value)

class TherapySessionRegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['num_session'], 'Indique o número da sessão')
        add_placeholder(self.fields['evolution'], 'Insira a evolução do caso aqui')
        add_placeholder(self.fields['forwarding'], 'Insira o encaminhamento dado aqui')

    class Meta:
        model = TherapySession
        fields = [
            'patient',
            'date_session',
            'hour_session',
            'fault',
            'justify_fault',
            'evolution',
            'forwarding',
            'payment',
        ]

        labels = {
            'patient': 'Nome do paciente:',
            'num_session': 'Número da seção:',
            'date_session': 'Data da sessão:',
            'hour_session': 'Hora da sessão:',
            'fault': 'Paciente faltou?',
            'justify_fault': 'Justificativa da falta:',
            'evolution': 'Evolução:',
            'forwarding': 'Encaminhamento:',
            'payment': 'Status de pagamento:',
        }

        help_texts = {
            'fault': 'Marque em caso de falta do paciente',
            'payment': 'Marque se o pagamento da sessão for efetuado',
        }