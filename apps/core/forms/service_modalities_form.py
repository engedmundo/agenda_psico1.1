from apps.core.models import ServiceModalitiy
from django import forms


class ServiceModalitiesRegisterForm(forms.ModelForm):
    class Meta:
        model = ServiceModalitiy
        fields = [
            "name",
            "description",
        ]

        labels = {
            "name": "Nome da modalidade:",
            "description": "Descrição da modalidade:",
        }
