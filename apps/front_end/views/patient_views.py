from apps.core.models import Psychologist
from apps.financial_management.models import PaymentPlain
from apps.patient_management.forms import PatientRegisterForm
from apps.patient_management.models import Patient, Prontuary
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render


@login_required(login_url="login_view")
def patients_list(request):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    patients = Patient.objects.filter(
        psychologist=psychologist,
        is_active=True,
    )

    return render(
        request,
        "pages/patients_management/patients/patients.html",
        context={
            "psychologist": psychologist,
            "patients": patients,
        },
    )


@login_required(login_url="login_view")
def create_patient(request):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    register_form_data = request.session.get(
        "register_form_data",
        None,
    )
    payment_plains = PaymentPlain.objects.filter(
        psychologist=psychologist,
    )

    form = PatientRegisterForm(
        register_form_data,
    )
    return render(
        request,
        "pages/patients_management/patients/create_patient.html",
        context={
            "psychologist": psychologist,
            "form": form,
            "payment_plains": payment_plains,
        },
    )


@login_required(login_url="login_view")
def patient_save(request):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session["register_form_data"] = POST
    form = PatientRegisterForm(POST)

    if form.is_valid():
        patient = form.save(commit=False)
        patient.psychologist = psychologist
        patient.save()
        messages.success(request, "Paciente cadastrado com sucesso")
        del request.session["register_form_data"]

    return redirect("patients_list")


@login_required(login_url="login_view")
def patient_update(request, id):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    patient = get_object_or_404(
        Patient,
        pk=id,
    )
    payment_plains = PaymentPlain.objects.filter(
        psychologist=psychologist,
    )

    if not patient:
        raise Http404()

    if patient.psychologist != psychologist:
        raise HttpResponseBadRequest

    form = PatientRegisterForm(
        data=request.POST or None,
        instance=patient,
    )

    if form.is_valid():
        patient = form.save(commit=False)
        patient.psychologist = psychologist
        patient.save()
        messages.success(request, "Paciente atualizado com sucesso")
        return redirect("patients_list")

    return render(
        request,
        "pages/patients_management/patients/update_patient.html",
        context={
            "psychologist": psychologist,
            "form": form,
            "payment_plains": payment_plains,
        },
    )


@login_required(login_url="login_view")
def patient_archive_confirm(request, id):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    patient = get_object_or_404(
        Patient,
        pk=id,
    )

    return render(
        request,
        "pages/patients_management/patients/archive_patient.html",
        context={
            "psychologist": psychologist,
            "patient": patient,
        },
    )


@login_required(login_url="login_view")
def patient_archive(request, id):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    patient = get_object_or_404(
        Patient,
        pk=id,
    )
    prontuaries = Prontuary.objects.filter(
        patient=patient,
    )

    if patient.psychologist != psychologist:
        raise HttpResponseBadRequest

    patient.is_active = False
    patient.save()

    for prontuary in prontuaries:
        prontuary.is_active = False
        prontuary.save()

    return redirect("patients_list")


@login_required(login_url="login_view")
def patients_archived(request):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    patients = Patient.objects.filter(
        psychologist=psychologist,
        is_active=False,
    )

    return render(
        request,
        "pages/patients_management/patients/archived_patients.html",
        context={
            "psychologist": psychologist,
            "patients": patients,
        },
    )


@login_required(login_url="login_view")
def patient_unarchive(request, id):
    psychologist = get_object_or_404(Psychologist, psychologist__username=request.user)
    patient = get_object_or_404(Patient, pk=id)

    if patient.psychologist != psychologist:
        raise HttpResponseBadRequest

    patient.is_active = True
    patient.save()

    return redirect("patients_list")


@login_required(login_url="login_view")
def patient_delete(request, id):
    psychologist = get_object_or_404(Psychologist, psychologist__username=request.user)
    patient = get_object_or_404(Patient, pk=id)

    if patient.psychologist != psychologist:
        raise HttpResponseBadRequest

    patient.delete()
    messages.success(request, "Paciente excluído com sucesso")
    return redirect("patients_list")


@login_required(login_url="login_view")
def patient_delete_confirm(request, id):
    psychologist = get_object_or_404(Psychologist, psychologist__username=request.user)
    patient = get_object_or_404(Patient, pk=id)

    return render(
        request,
        "pages/patients_management/patients/delete_patient.html",
        context={
            "psychologist": psychologist,
            "patient": patient,
        },
    )
