from email import message

from apps.financial_management.models import PaymentControl
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from ..forms import PaymentControlRegisterForm


@login_required(login_url="site_interface:home")
def payments(request):
    payments = PaymentControl.objects.all().order_by("-id")
    return render(
        request,
        "pages/payments.html",
        context={
            "payments": payments,
        },
    )


@login_required(login_url="site_interface:home")
def payment_details(request, id):
    queryset = PaymentControl.objects.filter(pk=id)
    payment = get_object_or_404(queryset)
    return render(
        request,
        "pages/payment_details.html",
        context={
            "payment": payment,
        },
    )


@login_required(login_url="site_interface:home")
def payment_register(request):
    register_form_data = request.session.get("register_form_data", None)
    form = PaymentControlRegisterForm(register_form_data)
    return render(
        request,
        "pages/payment_register.html",
        {
            "form": form,
        },
    )


@login_required(login_url="site_interface:home")
def payment_register_save(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session["register_form_data"] = POST
    form = PaymentControlRegisterForm(POST)

    if form.is_valid():
        form.save()
        messages.success(request, "Pagamento cadastrado com sucesso")
        del request.session["register_form_data"]

    return redirect("payments:payments")


@login_required(login_url="site_interface:home")
def payment_update(request, id):
    payment = get_object_or_404(PaymentControl, id=id)

    form = PaymentControlRegisterForm(
        instance=payment,
    )

    if request.method == "POST":
        form = PaymentControlRegisterForm(
            request.POST,
            instance=payment,
        )

        if form.is_valid():
            form.save()
            messages.success(request, "Pagamento atualizado com sucesso")
            return redirect("payments:payments")

    return render(
        request,
        "pages/payment_update.html",
        context={
            "form": form,
        },
    )


@login_required(login_url="site_interface:home")
def payment_delete_confirm(request, id):
    queryset = PaymentControl.objects.filter(pk=id)
    payment = get_object_or_404(queryset)

    if not payment:
        raise Http404()

    return render(
        request,
        "pages/payment_delete_confirm.html",
        context={
            "payment": payment,
        },
    )


@login_required(login_url="site_interface:home")
def payment_delete(request, id):
    queryset = PaymentControl.objects.filter(pk=id)
    payment = get_object_or_404(queryset)

    payment.delete()
    messages.success(request, "Deletado com sucesso")
    return redirect("payments:payments")
