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
        fields = [
            "psychologist",
            # "psychologist__first_name",
            # "psychologist__last_name",
            # "psychologist__email",
            "crp_register",
            "short_description",
            "professional_address",
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

        labels = {
            "psychologist__first_name": "Primeiro nome",
            "psychologist__last_name": "Sobrenome",
            "psychologist__email": "Email profissional",
            "crp_register": "Registro profissional",
            "short_description": "Descrição curta/titulação",
            "professional_address": "Endereço profissional",
            "secondary_address": "Endereço secundário",
            "phone_number": "Telefone profissional",
            "cpf": "CPF/CNPJ",
            "instagram_link": "Link perfil Instagram",
            "twitter_link": "Link perfil Twitter",
            "linkedin_link": "Link perfil LinkedIn",
            "whatsapp_number": "WhatsApp",
            "bio": "Biografia/Descrição longa",
            "schedule_description": "Agenda/horários de atendimento",
            "photo": "Foto de perfil",
        }