from apps.patient_management.models import TherapySession
from django import forms


class TherapySessionForm(forms.ModelForm):
    class Meta:
        model = TherapySession
        fields = [
            "prontuary",
            "session_number",
            "date_session",
            "hour_session",
            "fault",
            "justify_fault",
            "evolution",
            "forwarding",
            "payment",
        ]


class TherapySessionInLineForm(forms.ModelForm):
    class Meta:
        model = TherapySession
        fields = [
            "session_number",
            "date_session",
            "hour_session",
            "fault",
            "justify_fault",
            "evolution",
            "forwarding",
            "payment",
        ]


class TherapySessionRegisterForm(forms.ModelForm):
    class Meta:
        model = TherapySession
        fields = [
            "prontuary",
            "session_number",
            "date_session",
            "hour_session",
            "fault",
            "justify_fault",
            "evolution",
            "forwarding",
            "payment",
        ]
        labels = {
            "patient": "Nome do paciente:",
            "prontuary": "Prontuário:",
            "session_number": "Número da sessão:",
            "date_session": "Data da sessão:",
            "hour_session": "Horário da sessão:",
            "fault": "Paciente faltou?",
            "justify_fault": "Justificativa da falta:",
            "evolution": "Evolução",
            "forwarding": "Encaminhamento:",
            "payment": "Pagamento:",
        }
