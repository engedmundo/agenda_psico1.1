from dataclasses import fields

from django import forms
from django.contrib.auth.models import User


def add_attr(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, "")
    field.widget.attrs[attr_name] = f"{existing} {attr_new_val}".strip()


def add_placeholder(field, placeholder_value):
    add_attr(field, "placeholder", placeholder_value)


class UserRegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
        ]

        labels = {
            "first_name": "Primeiro nome",
            "last_name": "Sobrenome",
            "email": "Email profissional",
        }
