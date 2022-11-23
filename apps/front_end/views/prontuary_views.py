from datetime import datetime

from apps.core.models import Psychologist
from apps.financial_management.models import PaymentPlain
from apps.patient_management.forms import PatientRegisterForm, ProntuaryRegisterForm
from apps.patient_management.models import Patient, Prontuary
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render


@login_required(login_url="login_view")
def prontuaries_list(request):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    prontuaries = Prontuary.objects.filter(
        patient__psychologist=psychologist,
        patient__is_active=True,
        is_active=True,
    )

    return render(
        request,
        "pages/patients_management/prontuary/prontuaries.html",
        context={
            "psychologist": psychologist,
            "prontuaries": prontuaries,
        },
    )


@login_required(login_url="login_view")
def create_prontuary(request):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    register_form_data = request.session.get(
        "register_form_data",
        None,
    )
    patients = Patient.objects.filter(
        psychologist=psychologist,
    )

    form = ProntuaryRegisterForm(
        register_form_data,
    )
    return render(
        request,
        "pages/patients_management/prontuary/create_prontuary.html",
        context={
            "psychologist": psychologist,
            "form": form,
            "patients": patients,
        },
    )


@login_required(login_url="login_view")
def prontuary_save(request):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session["register_form_data"] = POST
    form = ProntuaryRegisterForm(POST)

    if form.is_valid():
        prontuary = form.save(commit=False)
        prontuary.psychologist = psychologist
        prontuary.save()
        messages.success(request, "Prontuário cadastrado com sucesso")
        del request.session["register_form_data"]

    return redirect("prontuaries_list")


@login_required(login_url="login_view")
def prontuary_update(request, id):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    prontuary = get_object_or_404(
        Prontuary,
        pk=id,
    )
    patient = prontuary.patient

    if not prontuary:
        raise Http404()

    if prontuary.patient.psychologist != psychologist:
        raise HttpResponseBadRequest

    form = ProntuaryRegisterForm(
        data=request.POST or None,
        instance=prontuary,
    )

    if form.is_valid():
        prontuary = form.save(commit=False)
        prontuary.save()
        messages.success(request, "Prontuário atualizado com sucesso")
        return redirect("prontuaries_list")

    return render(
        request,
        "pages/patients_management/prontuary/update_prontuary.html",
        context={
            "psychologist": psychologist,
            "form": form,
            "prontuary": prontuary,
        },
    )


@login_required(login_url="login_view")
def prontuary_archive_confirm(request, id):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    prontuary = get_object_or_404(
        Prontuary,
        pk=id,
    )

    return render(
        request,
        "pages/patients_management/prontuary/archive_prontuary.html",
        context={
            "psychologist": psychologist,
            "prontuary": prontuary,
        },
    )


@login_required(login_url="login_view")
def prontuary_archive(request, id):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    prontuary = get_object_or_404(
        Prontuary,
        pk=id,
    )

    if prontuary.patient.psychologist != psychologist:
        raise HttpResponseBadRequest

    prontuary.is_active = False
    if not prontuary.close_date:
        prontuary.close_date = datetime.today()
    prontuary.save()

    return redirect("prontuaries_list")


@login_required(login_url="login_view")
def prontuaries_archived(request):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    prontuaries = Prontuary.objects.filter(
        patient__psychologist=psychologist,
        is_active=False,
    )

    return render(
        request,
        "pages/patients_management/prontuary/archived_prontuaries.html",
        context={
            "psychologist": psychologist,
            "prontuaries": prontuaries,
        },
    )


@login_required(login_url="login_view")
def prontuary_unarchive(request, id):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    prontuary = get_object_or_404(
        Prontuary,
        pk=id,
    )

    if prontuary.patient.psychologist != psychologist:
        raise HttpResponseBadRequest

    prontuary.is_active = True
    prontuary.save()

    return redirect("prontuaries_list")


@login_required(login_url="login_view")
def prontuary_delete(request, id):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    prontuary = get_object_or_404(
        Prontuary,
        pk=id,
    )

    if prontuary.patient.psychologist != psychologist:
        raise HttpResponseBadRequest

    prontuary.delete()
    messages.success(request, "Prontuário excluído com sucesso")
    return redirect("prontuaries_list")


@login_required(login_url="login_view")
def prontuary_delete_confirm(request, id):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    prontuary = get_object_or_404(
        Prontuary,
        pk=id,
    )

    return render(
        request,
        "pages/patients_management/prontuary/delete_prontuary.html",
        context={
            "psychologist": psychologist,
            "prontuary": prontuary,
        },
    )
