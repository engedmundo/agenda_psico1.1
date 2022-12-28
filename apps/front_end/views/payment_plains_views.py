from apps.core.models import Psychologist
from apps.financial_management.forms import PaymentPlainRegisterForm
from apps.financial_management.models import PaymentPlain
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render


@login_required(login_url="login")
def payment_plains_list(request):
    psychologist = get_object_or_404(Psychologist, psychologist__username=request.user)
    payment_plains = PaymentPlain.objects.filter(
        psychologist=psychologist,
        is_active=True,
    )

    return render(
        request,
        "sections/financial/payment_plains/payment_plains.html",
        context={
            "psychologist": psychologist,
            "payment_plains": payment_plains,
        },
    )


@login_required(login_url="login")
def create_payment_plain(request):
    psychologist = get_object_or_404(Psychologist, psychologist__username=request.user)
    register_form_data = request.session.get("register_form_data", None)

    form = PaymentPlainRegisterForm(register_form_data)
    return render(
        request,
        "sections/financial/payment_plains/create_payment_plain.html",
        context={
            "psychologist": psychologist,
            "form": form,
        },
    )


@login_required(login_url="login")
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


@login_required(login_url="login")
def payment_plain_update(request, id):
    psychologist = get_object_or_404(Psychologist, psychologist__username=request.user)
    payment_plain = get_object_or_404(PaymentPlain, pk=id)

    if not payment_plain:
        raise Http404()

    if payment_plain.psychologist != psychologist:
        raise HttpResponseBadRequest

    form = PaymentPlainRegisterForm(
        data=request.POST or None,
        instance=payment_plain,
    )

    if form.is_valid():
        payment_plain = form.save(commit=False)
        payment_plain.psychologist = psychologist
        payment_plain.save()
        messages.success(request, "Plano de pagamento cadastrado com sucesso")
        return redirect("payment_plains")

    return render(
        request,
        "sections/financial/payment_plains/update_payment_plain.html",
        context={
            "psychologist": psychologist,
            "form": form,
        },
    )


@login_required(login_url="login")
def payment_plain_archive_confirm(request, id):
    psychologist = get_object_or_404(Psychologist, psychologist__username=request.user)
    payment_plain = get_object_or_404(PaymentPlain, pk=id)

    return render(
        request,
        "sections/financial/payment_plains/confirm_archive_plain.html",
        context={
            "psychologist": psychologist,
            "payment_plain": payment_plain,
        },
    )


@login_required(login_url="login")
def payment_plain_archive(request, id):
    psychologist = get_object_or_404(Psychologist, psychologist__username=request.user)
    payment_plain = get_object_or_404(PaymentPlain, pk=id)

    if payment_plain.psychologist != psychologist:
        raise HttpResponseBadRequest

    payment_plain.is_active = False
    payment_plain.save()

    return redirect("payment_plains")


@login_required(login_url="login")
def payment_plains_archived(request):
    psychologist = get_object_or_404(Psychologist, psychologist__username=request.user)
    payment_plains = PaymentPlain.objects.filter(
        psychologist=psychologist,
        is_active=False,
    )

    return render(
        request,
        "sections/financial/payment_plains/payment_plains_arquived.html",
        context={
            "psychologist": psychologist,
            "payment_plains": payment_plains,
        },
    )


@login_required(login_url="login")
def payment_plain_unarchive(request, id):
    psychologist = get_object_or_404(Psychologist, psychologist__username=request.user)
    payment_plain = get_object_or_404(PaymentPlain, pk=id)

    if payment_plain.psychologist != psychologist:
        raise HttpResponseBadRequest

    payment_plain.is_active = True
    payment_plain.save()

    return redirect("payment_plains")


@login_required(login_url="login")
def payment_plain_delete(request, id):
    psychologist = get_object_or_404(Psychologist, psychologist__username=request.user)
    payment_plain = get_object_or_404(PaymentPlain, pk=id)

    if payment_plain.psychologist != psychologist:
        raise HttpResponseBadRequest

    payment_plain.delete()
    messages.success(request, "Deletado com sucesso")
    return redirect("payment_plains")


@login_required(login_url="login")
def payment_plain_delete_confirm(request, id):
    psychologist = get_object_or_404(Psychologist, psychologist__username=request.user)
    payment_plain = get_object_or_404(PaymentPlain, pk=id)

    return render(
        request,
        "sections/financial/payment_plains/confirm_delete_plain.html",
        context={
            "psychologist": psychologist,
            "payment_plain": payment_plain,
        },
    )
