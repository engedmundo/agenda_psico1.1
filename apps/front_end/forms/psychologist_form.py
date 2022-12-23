from dataclasses import fields

from apps.core.models import Psychologist
from django import forms


def add_attr(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, "")
    field.widget.attrs[attr_name] = f"{existing} {attr_new_val}".strip()


def add_placeholder(field, placeholder_value):
    add_attr(field, "placeholder", placeholder_value)


class PsychologistRegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Psychologist
        widgets = {
            "bio": forms.Textarea(attrs={"rows": 5}),
            "photo": forms.FileInput(),
        }
        fields = [
            "crp_register",
            "short_description",
            "professional_address",
            "city",
            "secondary_address",
            "phone_number",
            "cpf",
            "instagram_link",
            "twitter_link",
            "linkedin_link",
            "whatsapp_number",
            "bio",
            "schedule_description",
            "photo",
        ]
        required = [
            "crp_register",
            "short_description",
            "bio",
        ]

        labels = {
            "crp_register": "Registro profissional:",
            "short_description": "Descrição curta/titulação:",
            "professional_address": "Endereço profissional:",
            "city": "Cidade de atendimento:",
            "secondary_address": "Endereço secundário:",
            "phone_number": "Telefone profissional:",
            "cpf": "CPF/CNPJ:",
            "instagram_link": "Link perfil Instagram:",
            "twitter_link": "Link perfil Twitter:",
            "linkedin_link": "Link perfil LinkedIn:",
            "whatsapp_number": "WhatsApp:",
            "bio": "Biografia/Descrição longa:",
            "schedule_description": "Agenda/horários de atendimento:",
            "photo": "Foto de perfil:",
        }
