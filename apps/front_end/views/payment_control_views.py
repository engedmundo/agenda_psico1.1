from apps.core.models import Psychologist
from apps.financial_management.forms import PaymentControlRegisterForm
from apps.financial_management.models import PaymentControl
from apps.patient_management.models import Prontuary, TherapySession
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render


@login_required(login_url="login")
def payment_control_list(request):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    payments = PaymentControl.objects.filter(
        prontuary__patient__psychologist=psychologist,
        is_active=True,
    ).order_by("-date_of_pay")

    return render(
        request,
        "pages/financial/payment_control/payment_control.html",
        context={
            "psychologist": psychologist,
            "payments": payments,
        },
    )


@login_required(login_url="login")
def create_payment_control(request):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    prontuaries = Prontuary.objects.filter(
        patient__psychologist=psychologist,
        is_active=True,
    )
    register_form_data = request.session.get(
        "register_form_data",
        None,
    )
    form = PaymentControlRegisterForm(
        register_form_data,
    )
    return render(
        request,
        "pages/financial/payment_control/create_payment_control.html",
        context={
            "psychologist": psychologist,
            "prontuaries": prontuaries,
            "form": form,
        },
    )


@login_required(login_url="login")
def payment_control_save(request):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    if not request.POST:
        raise Http404()

    form = PaymentControlRegisterForm(
        data=request.POST or None,
        files=request.FILES or None,
    )

    if form.is_valid():
        payment = form.save(commit=False)
        payment.save()
        del request.session["register_form_data"]

    return redirect("payment_control")


@login_required(login_url="login")
def payment_control_update(request, id):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    payment_control = get_object_or_404(
        PaymentControl,
        pk=id,
    )
    prontuary = payment_control.prontuary
    if not payment_control:
        raise Http404()

    if payment_control.prontuary.patient.psychologist != psychologist:
        raise HttpResponseBadRequest

    form = PaymentControlRegisterForm(
        request.POST or None,
        request.FILES or None,
        instance=payment_control,
    )

    if form.is_valid():
        payment = form.save(commit=False)
        payment.prontuary = prontuary
        payment.save()
        return redirect("payment_control")

    return render(
        request,
        "pages/financial/payment_control/update_payment_control.html",
        context={
            "psychologist": psychologist,
            "form": form,
            "payment_control": payment_control,
        },
    )


"""
@login_required(login_url="login")
def service_modality_archive_confirm(request, id):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    service_modality = get_object_or_404(
        ServiceModalitiy,
        pk=id,
    )

    return render(
        request,
        "pages/patients_management/service_modalities/confirm_archive_service_modality.html",
        context={
            "psychologist": psychologist,
            "service_modality": service_modality,
        },
    )


@login_required(login_url="login")
def service_modality_archive(request, id):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    service_modality = get_object_or_404(
        ServiceModalitiy,
        pk=id,
    )

    if service_modality.psychologist != psychologist:
        raise HttpResponseBadRequest

    service_modality.is_active = False
    service_modality.save()

    return redirect("service_modalities")


@login_required(login_url="login")
def service_modalities_archived(request):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    service_modalities = ServiceModalitiy.objects.filter(
        psychologist=psychologist,
        is_active=False,
    )

    return render(
        request,
        "pages/patients_management/service_modalities/archived_service_modalities.html",
        context={
            "psychologist": psychologist,
            "service_modalities": service_modalities,
        },
    )


@login_required(login_url="login")
def service_modality_unarchive(request, id):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    service_modality = get_object_or_404(
        ServiceModalitiy,
        pk=id,
    )

    if service_modality.psychologist != psychologist:
        raise HttpResponseBadRequest

    service_modality.is_active = True
    service_modality.save()

    return redirect("service_modalities")


@login_required(login_url="login")
def service_modality_delete(request, id):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    service_modality = get_object_or_404(
        ServiceModalitiy,
        pk=id,
    )

    if service_modality.psychologist != psychologist:
        raise HttpResponseBadRequest

    service_modality.delete()
    return redirect("service_modalities")


@login_required(login_url="login")
def service_modality_delete_confirm(request, id):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    service_modality = get_object_or_404(
        ServiceModalitiy,
        pk=id,
    )

    return render(
        request,
        "pages/patients_management/service_modalities/confirm_delete_service_modality.html",
        context={
            "psychologist": psychologist,
            "service_modality": service_modality,
        },
    )
"""
