from django import forms
from django.contrib import admin

from apps.core.models import Psychologist
from apps.core.services.filter_data_service import FilterDataService
from apps.financial_management.models.payment_plain import PaymentPlain

from .models import Patient, Prontuary, TherapySession


class TherapySessionInLine(admin.StackedInline):
    model = TherapySession
    extra = 0
    list_display = [
        "date_session",
        "hour_session",
        "fault",
        "justify_fault",
        "evolution",
        "forwarding",
        "payment",
    ]


class ProntuaryInLine(admin.StackedInline):
    model = Prontuary
    extra = 0
    list_display = [
        "patient",
        "open_date",
        "close_date",
        "demand_description",
    ]


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
            "responsable",
            "fone_resp",
            "session_week_day",
            "session_hour",
        ]


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        _service = FilterDataService(request=request)
        return _service.patients_by_psychologist()

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        _service = FilterDataService(request=request)
        if db_field.name == "plain":
            kwargs["queryset"] = PaymentPlain.objects.filter(
                psychologist=_service.psychologist
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        _service = FilterDataService(request=request)
        obj.psychologist = _service.psychologist
        super().save_model(request, obj, form, change)

    list_display = [
        "patient_name",
        "phone_number",
        "session_week_day",
        "session_hour",
        "plain",
    ]
    list_filter = [
        "session_week_day",
        ("plain", admin.RelatedOnlyFieldListFilter),
    ]
    search_fields = [
        "patient_name",
    ]
    inlines = [
        ProntuaryInLine,
        TherapySessionInLine,
    ]
    form = PatientForm  


@admin.register(TherapySession)
class TherapySessionAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        _service = FilterDataService(request=request)
        return _service.therapy_sessions_by_psycologist()

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        _service = FilterDataService(request=request)
        if db_field.name == "patient":
            kwargs["queryset"] = Patient.objects.filter(
                psychologist=_service.psychologist
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = [
        "patient",
        "session_number",
        "date_session",
        "hour_session",
        "payment",
    ]
    list_filter = [
        "payment",
    ]
    search_fields = [
        "patient_name",
    ]
    autocomplete_fields = [
        "patient",
    ]


@admin.register(Prontuary)
class ProntuaryAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        _service = FilterDataService(request=request)
        return _service.prontuaries_by_psycologist()

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        _service = FilterDataService(request=request)
        if db_field.name == "patient":
            kwargs["queryset"] = Patient.objects.filter(
                psychologist=_service.psychologist
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = [
        "patient",
        "open_date",
        "close_date",
    ]
    search_fields = [
        "patient",
    ]
    autocomplete_fields = [
        "patient",
    ]
