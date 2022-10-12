from django.contrib import admin

from apps.core.services.filter_data_service import FilterDataService

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


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        _service = FilterDataService(request=request)
        return _service.patients_by_psychologist()

    list_display = [
        "patient_name",
        "phone_number",
        "session_week_day",
        "session_hour",
        "plain",
    ]
    list_filter = [
        "session_week_day",
        "plain",
    ]
    search_fields = [
        "patient_name",
    ]
    inlines = [
        ProntuaryInLine,
        TherapySessionInLine,
    ]


@admin.register(TherapySession)
class TherapySessionAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        _service = FilterDataService(request=request)
        return _service.therapy_sessions_by_psycologist()

    list_display = [
        "patient",
        "session_id",
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

    list_display = [
        "patient",
        "open_date",
        "close_date",
    ]
    search_fields = [
        "patient",
    ]
