from apps.core.models import Psychologist
from apps.financial_management.models import PaymentControl, PaymentPlain
from apps.patient_management.models import Patient, Prontuary, TherapySession
from django.shortcuts import get_object_or_404


class FilterDataService:
    def __init__(self, request) -> None:
        self.request = request
        self.psychologist = get_object_or_404(
            Psychologist, psychologist=self.request.user
        )

    def patients_by_psychologist(self):
        queryset = Patient.objects.all()
        if self.request.user.is_superuser:
            return queryset.filter(psychologist=None)

        return queryset.filter(psychologist=self.psychologist)

    def therapy_sessions_by_psycologist(self):
        queryset = TherapySession.objects.all()
        if self.request.user.is_superuser:
            return queryset.filter(patient=None)

        return queryset.filter(prontuary__patient__psychologist=self.psychologist)

    def prontuaries_by_psycologist(self):
        queryset = Prontuary.objects.all()
        if self.request.user.is_superuser:
            return queryset.filter(patient=None)

        return queryset.filter(patient__psychologist=self.psychologist)

    def payment_plain_by_psycologist(self):
        queryset = PaymentPlain.objects.all()
        if self.request.user.is_superuser:
            return queryset.filter(psychologist=None)

        return queryset.filter(psychologist=self.psychologist)

    def payment_control_by_psycologist(self):
        queryset = PaymentControl.objects.all()
        if self.request.user.is_superuser:
            return queryset.filter(patient=None)

        return queryset.filter(patient__psychologist=self.psychologist)

    def patients_by_prontuary(
        self,
    ):
        queryset = Prontuary.objects.all()
        if self.request.user.is_superuser:
            return queryset.filter(psychologist=None)

        return queryset.filter(psychologist=self.psychologist)
