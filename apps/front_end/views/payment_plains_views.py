from apps.core.models import Psychologist
from apps.financial_management.forms import PaymentPlainRegisterForm
from apps.financial_management.models import PaymentPlain
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render


@login_required(login_url="login_view")
def payment_plains_list(request):
    psychologist = get_object_or_404(Psychologist, psychologist__username=request.user)
    payment_plains = PaymentPlain.objects.filter(
        psychologist=psychologist,
        is_active=True,
    )

    return render(
        request,
        "pages/financial/payment_plains.html",
        context={
            "psychologist": psychologist,
            "payment_plains": payment_plains,
        },
    )


@login_required(login_url="login_view")
def create_payment_plain(request):
    psychologist = get_object_or_404(Psychologist, psychologist__username=request.user)
    register_form_data = request.session.get("register_form_data", None)

    form = PaymentPlainRegisterForm(register_form_data)
    return render(
        request,
        "pages/financial/create_payment_plain.html",
        context={
            "psychologist": psychologist,
            "form": form,
        },
    )


@login_required(login_url="site_interface:home")
def payment_plain_save(request):
    psychologist = get_object_or_404(Psychologist, psychologist__username=request.user)
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session["register_form_data"] = POST
    form = PaymentPlainRegisterForm(POST)

    if form.is_valid():
        payment_plain = form.save(commit=False)
        payment_plain.psychologist = psychologist
        payment_plain.save()
        messages.success(request, "Plano de pagamento cadastrado com sucesso")
        del request.session["register_form_data"]

    return redirect("payment_plains")


@login_required(login_url="login_view")
def payment_plains_list_archived(request):
    psychologist = get_object_or_404(Psychologist, psychologist__username=request.user)
    payment_plains = PaymentPlain.objects.filter(
        psychologist=psychologist,
        is_active=False,
    )

    return render(
        request,
        "pages/financial/payment_plains_list.html",
        context={
            "psychologist": psychologist,
            "payment_plains": payment_plains,
        },
    )
