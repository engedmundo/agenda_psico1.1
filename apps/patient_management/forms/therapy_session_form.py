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
