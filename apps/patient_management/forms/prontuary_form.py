from apps.patient_management.models import Prontuary
from django import forms


class ProntuaryRegisterForm(forms.ModelForm):
    class Meta:
        model = Prontuary
        fields = [
            "patient",
            "prontuary_number",
            "open_date",
            "close_date",
            "type_of_service",
            "demand_description",
        ]

        labels = {
            "patient": "Paciente:",
            "prontuary_number": "Número do prontuário:",
            "open_date": "Data de abertura:",
            "close_date": "Data de fechamento:",
            "type_of_service": "Tipo de atendimento:",
            "demand_description": "Descrição da demanda:",
        }
