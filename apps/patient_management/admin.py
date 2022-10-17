from django.contrib import admin

from apps.core.services.filter_data_service import FilterDataService
from apps.financial_management.models.payment_plain import PaymentPlain
from apps.patient_management.forms import (
    PatientForm,
    TherapySessionForm,
    TherapySessionInLineForm,
)

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
    form = TherapySessionInLineForm


class ProntuaryInLine(admin.StackedInline):
    model = Prontuary
    extra = 0
    list_display = [
        "patient",
        "prontuary_number",
        "open_date",
        "close_date",
        "demand_description",
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
    form = PatientForm
    inlines = [
        ProntuaryInLine,
    ]


@admin.register(TherapySession)
class TherapySessionAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        _service = FilterDataService(request=request)
        return _service.therapy_sessions_by_psycologist()

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        _service = FilterDataService(request=request)
        if db_field.name == "prontuary":
            kwargs["queryset"] = Prontuary.objects.filter(
                patient__psychologist=_service.psychologist
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        obj.patient = obj.prontuary.patient
        super().save_model(request, obj, form, change)

    list_display = [
        "prontuary",
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
    form = TherapySessionForm
    autocomplete_fields = [
        "patient",
    ]
    list_per_page = 10


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
    inlines = [
        TherapySessionInLine,
    ]
