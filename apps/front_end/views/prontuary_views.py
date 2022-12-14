from datetime import datetime

from apps.core.models import Psychologist, ServiceModalitiy
from apps.patient_management.forms import ProntuaryRegisterForm
from apps.patient_management.models import Patient, Prontuary, TherapySession
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render


@login_required(login_url="login")
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
        "sections/patients_management/prontuaries/prontuaries.html",
        context={
            "psychologist": psychologist,
            "prontuaries": prontuaries,
        },
    )


@login_required(login_url="login")
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
        is_active=True,
    )
    types_of_service = ServiceModalitiy.objects.filter(
        psychologist=psychologist,
        is_active=True,
    )

    form = ProntuaryRegisterForm(
        register_form_data,
    )
    return render(
        request,
        "sections/patients_management/prontuaries/create_prontuary.html",
        context={
            "psychologist": psychologist,
            "form": form,
            "patients": patients,
            "types_of_service": types_of_service,
        },
    )


@login_required(login_url="login")
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
        messages.success(request, "Prontu??rio cadastrado com sucesso")
        del request.session["register_form_data"]

    return redirect("prontuaries_list")


@login_required(login_url="login")
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

    types_of_service = ServiceModalitiy.objects.filter(
        psychologist=psychologist,
        is_active=True,
    )
    active_service = prontuary.type_of_service

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
        messages.success(request, "Prontu??rio atualizado com sucesso")
        return redirect("prontuaries_list")

    return render(
        request,
        "sections/patients_management/prontuaries/update_prontuary.html",
        context={
            "psychologist": psychologist,
            "form": form,
            "prontuary": prontuary,
            "types_of_service": types_of_service,
            "active_service": active_service,
        },
    )


@login_required(login_url="login")
def prontuary_details(request, id):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    prontuary = get_object_or_404(
        Prontuary,
        pk=id,
    )
    therapy_sessions = TherapySession.objects.filter(
        prontuary=prontuary,
    ).order_by("-date_session", "-pk")

    if not prontuary:
        raise Http404()

    if prontuary.patient.psychologist != psychologist:
        raise HttpResponseBadRequest

    return render(
        request,
        "sections/patients_management/prontuaries/prontuary_details.html",
        context={
            "psychologist": psychologist,
            "prontuary": prontuary,
            "therapy_sessions": therapy_sessions,
        },
    )


@login_required(login_url="login")
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
        "sections/patients_management/prontuaries/confirm_archive_prontuary.html",
        context={
            "psychologist": psychologist,
            "prontuary": prontuary,
        },
    )


@login_required(login_url="login")
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


@login_required(login_url="login")
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
        "sections/patients_management/prontuaries/archived_prontuaries.html",
        context={
            "psychologist": psychologist,
            "prontuaries": prontuaries,
        },
    )


@login_required(login_url="login")
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


@login_required(login_url="login")
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
    messages.success(request, "Prontu??rio exclu??do com sucesso")
    return redirect("prontuaries_list")


@login_required(login_url="login")
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
        "sections/patients_management/prontuaries/confirm_delete_prontuary.html",
        context={
            "psychologist": psychologist,
            "prontuary": prontuary,
        },
    )
