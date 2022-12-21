from django import forms
from django.contrib import admin

from apps.core.services.filter_data_service import FilterDataService
from apps.patient_management.models import Patient, Prontuary

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
        if db_field.name == "prontuary":
            kwargs["queryset"] = Prontuary.objects.filter(
                psychologist=_service.psychologist
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = [
        "prontuary",
        "date_of_pay",
        "value_paid",
        "payment_method",
    ]
    list_filter = [
        ("prontuary", admin.RelatedOnlyFieldListFilter),
        "date_of_pay",
        "value_paid",
        "payment_method",
    ]
    search_fields = ["prontuary"]
    autocomplete_fields = ["prontuary"]
