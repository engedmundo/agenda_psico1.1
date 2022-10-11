from django import forms
from apps.patient_management.models import Patient

def add_attr(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing} {attr_new_val}'.strip()

def add_placeholder(field, placeholder_value):
    add_attr(field, 'placeholder', placeholder_value)

class PatientRegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Patient
        fields = [
            'patient_name',
            'psychologist',
            'birth_date',
            'cpf',
            'phone_number',
            'patient_address',
            'email',
            'occupation',
            'responsable',
            'fone_resp',
            'session_week_day',
            'session_hour',
            'plain',
        ]

        labels = {
            'patient_name': 'Nome do Paciente',
            'psychologist': 'Psicólogo',
            'birth_date': 'Data de nascimento',
            'cpf': 'CPF',
            'phone_number': 'Telefone',
            'patient_address': 'Endereço',
            'email': 'E-mail',
            'occupation': 'Profissão',
            'responsable': 'Responsável',
            'fone_resp': 'Telefone do responsável',
            'session_week_day': 'Dia fixo da sessão',
            'session_hour': 'Horário fixo da sessão',
            'plain': 'Convênio',
        }

        placeholder = {
            'patient_address': 'Endereço completo',
            'email': 'E-mail',
            'occupation': 'Profissão',
            'responsable': 'Responsável',
            'fone_resp': 'Telefone do responsável',
            'session_week_day': 'Dia fixo da sessão',
            'session_hour': 'Horário fixo da sessão',
            'plain': 'Convênio',
        }
