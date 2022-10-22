from dataclasses import fields
from django import forms

def add_attr(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing} {attr_new_val}'.strip()

def add_placeholder(field, placeholder_value):
    add_attr(field, 'placeholder', placeholder_value)

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Usuário:",
    )
    password = forms.CharField(
        label="Senha:",
        widget=forms.PasswordInput(),
    )
