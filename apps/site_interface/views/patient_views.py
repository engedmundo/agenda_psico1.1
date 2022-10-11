from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from apps.patient_management.models import Patient

from ..forms import PatientRegisterForm


@login_required(login_url='site_interface:home')
def patients(request):
    patients = Patient.objects.all().order_by('-id')
    return render(request, 'pages/patients.html',
                  context={
                      "patients": patients,
                  })


@login_required(login_url='site_interface:home')
def patient_details(request, id):
    queryset = Patient.objects.filter(pk=id)
    patient = get_object_or_404(queryset)
    return render(
        request,
        'pages/patient_details.html',
        context={
            "patient": patient,
        }
    )


@login_required(login_url='site_interface:home')
def patient_register(request):
    register_form_data = request.session.get(
        'register_form_data',
        None
    )
    form = PatientRegisterForm(register_form_data)
    return render(
        request,
        'pages/patient_register.html',
        {
            "form": form,
        }
    )


@login_required(login_url='site_interface:home')
def patient_register_save(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = PatientRegisterForm(POST)

    if form.is_valid():
        form.save()
        messages.success(request, 'paciente cadastrado com sucesso')

        del(request.session['register_form_data'])

    return redirect('patients:patients')


@login_required(login_url='site_interface:home')
def patient_update(request, id):
    queryset = Patient.objects.filter(pk=id)
    patient = get_object_or_404(queryset)

    form = PatientRegisterForm(
        instance=patient,
    )

    if request.method == 'POST':
        form = PatientRegisterForm(
            request.POST,
            instance=patient,
        )

    if form.is_valid():
        form.save()
        messages.success(
            request,
            'paciente atualizado com sucesso',
        )
        return redirect('patients:patients')

    return render(
        request,
        'pages/patient_update.html',
        context={
            'form': form,
        }
    )


@login_required(login_url='site_interface:home')
def patient_delete_confirm(request, id):
    queryset = Patient.objects.filter(pk=id)
    patient = get_object_or_404(queryset)

    if not patient:
        raise Http404()

    return render(
        request,
        'pages/patient_delete_confirm.html',
        context={
            'patient': patient,
        }
    )


@login_required(login_url='site_interface:home')
def patient_delete(request, id):
    queryset = patient.objects.filter(pk=id)
    patient = get_object_or_404(queryset)

    patient.delete()
    messages.success(request, 'paciente excluído com sucesso')
    return redirect('patients:patients')
