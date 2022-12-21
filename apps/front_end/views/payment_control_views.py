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
    )

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

    POST = request.POST
    request.session["register_form_data"] = POST
    form = PaymentControlRegisterForm(POST)

    if form.is_valid():
        payment = form.save(commit=False)
        payment.save()
        del request.session["register_form_data"]

    return redirect("create_payment_control")


"""
@login_required(login_url="login")
def service_modality_update(request, id):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    service_modality = get_object_or_404(
        ServiceModalitiy,
        pk=id,
    )
    if not service_modality:
        raise Http404()

    if service_modality.psychologist != psychologist:
        raise HttpResponseBadRequest

    form = ServiceModalitiesRegisterForm(
        data=request.POST or None,
        instance=service_modality,
    )

    if form.is_valid():
        service_modality = form.save(commit=False)
        service_modality.psychologist = psychologist
        service_modality.save()
        return redirect("service_modalities")

    return render(
        request,
        "pages/patients_management/service_modalities/update_service_modality.html",
        context={
            "psychologist": psychologist,
            "form": form,
        },
    )


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
