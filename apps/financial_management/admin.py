from django.contrib import admin
from apps.core.services.filter_data_service import FilterDataService
from .models import PaymentControl, PaymentPlain


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


@admin.register(PaymentControl)
class PaymentControlAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        _service = FilterDataService(request=request)
        return _service.payment_control_by_psycologist()

    list_display = ["patient", "data_pay", "value_pay", "way_pay"]
    list_filter = ["patient", "data_pay", "value_pay", "way_pay"]
    search_fields = ["patient"]
