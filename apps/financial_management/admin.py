from django import forms
from django.contrib import admin

from apps.core.services.filter_data_service import FilterDataService
from apps.patient_management.models import Patient

from .models import PaymentControl, PaymentPlain


class PaymentPlainForm(forms.ModelForm):
    class Meta:
        model = PaymentPlain
        fields = ["name_plain", "plain_value"]


@admin.register(PaymentPlain)
class PaymentPlainAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        _service = FilterDataService(request=request)
        return _service.payment_plain_by_psycologist()

    list_display = ["name_plain", "plain_value"]
    list_filter = [
        "name_plain",
        "plain_value",
    ]
    search_fields = [
        "name_plain",
    ]
    form = PaymentPlainForm

    def save_model(self, request, obj, form, change):
        _service = FilterDataService(request=request)
        obj.psychologist = _service.psychologist
        super().save_model(request, obj, form, change)


@admin.register(PaymentControl)
class PaymentControlAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        _service = FilterDataService(request=request)
        return _service.payment_control_by_psycologist()

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        _service = FilterDataService(request=request)
        if db_field.name == "patient":
            kwargs["queryset"] = Patient.objects.filter(
                psychologist=_service.psychologist
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = [
        "patient",
        "data_pay",
        "value_pay",
        "way_pay",
    ]
    list_filter = [
        ("patient", admin.RelatedOnlyFieldListFilter),
        "data_pay",
        "value_pay",
        "way_pay",
    ]
    search_fields = ["patient"]
    autocomplete_fields = ["patient", "therapy_session"]
