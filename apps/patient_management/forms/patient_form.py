from django import forms
from apps.patient_management.models import Patient

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
