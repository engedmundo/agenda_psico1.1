from apps.core.models.psychologist import Psychologist
from apps.financial_management.models import PaymentPlain
from apps.patient_management.models import Patient
from django import forms
from django.shortcuts import get_object_or_404


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            "patient_name",
            "plain",
            "birth_date",
            "cpf",
            "phone_number",
            "patient_address",
            "email",
            "occupation",
            "school",
            "responsable",
            "phone_resp",
            "father",
            "phone_father",
            "mother",
            "phone_mother",
            "session_week_day",
            "session_hour",
        ]


class PatientRegisterForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            "patient_name",
            "plain",
            "birth_date",
            "cpf",
            "phone_number",
            "patient_address",
            "email",
            "occupation",
            "school",
            "responsable",
            "phone_resp",
            "father",
            "phone_father",
            "mother",
            "phone_mother",
            "session_week_day",
            "session_hour",
        ]

        labels = {
            "patient_name": "Nome do paciente:",
            "plain": "Plano de pagamento:",
            "birth_date": "Data de nascimento:",
            "cpf": "CPF:",
            "phone_number": "Telefone do paciente:",
            "patient_address": "Endereço:",
            "email": "E-mail:",
            "occupation": "Profissão:",
            "school": "Escola:",
            "responsable": "Responsável:",
            "phone_resp": "Telefone do responsável:",
            "father": "Nome do Pai:",
            "phone_father": "Telefone do Pai:",
            "mother": "Nome da Mãe:",
            "phone_mother": "Telefone da Mãe",
            "session_week_day": "Dia da sessão:",
            "session_hour": "Horário da sessão",
        }
