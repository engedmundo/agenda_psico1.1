from dataclasses import fields
from django import forms
from apps.patient_management.models import Prontuary

class ProntuaryRegisterForm(forms.ModelForm):
    class Meta:
        model = Prontuary
        fields = [
            'patient',
            'open_date',
            'close_date',
            'demand_description',
        ]

        labels = {
            'patient': 'Paciente',
            'code': 'Código do prontuário',
            'open_date': 'Data de abertura',
            'close_date': 'Data de fechamento',
            'demand_description': 'Descrição da demanda',
        }