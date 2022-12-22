from datetime import datetime

from apps.core.models import Psychologist
from apps.patient_management.forms import TherapySessionRegisterForm
from apps.patient_management.models import Patient, Prontuary, TherapySession
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render


@login_required(login_url="login_view")
def create_therapy_session(request, id):
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
    register_form_data = request.session.get(
        "register_form_data",
        None,
    )
    form = TherapySessionRegisterForm(
        register_form_data,
    )

    if not prontuary:
        raise Http404()

    if prontuary.patient.psychologist != psychologist:
        raise HttpResponseBadRequest

    return render(
        request,
        "sections/patients_management/therapy_sessions/create_therapy_session.html",
        context={
            "psychologist": psychologist,
            "prontuary": prontuary,
            "therapy_sessions": therapy_sessions,
            "form": form,
        },
    )


@login_required(login_url="login_view")
def therapy_session_save(request, id):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    prontuary = get_object_or_404(
        Prontuary,
        pk=id,
    )
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session["register_form_data"] = POST
    form = TherapySessionRegisterForm(POST)

    if form.is_valid():
        session = form.save(commit=False)
        session.prontuary = prontuary
        session.patient = prontuary.patient
        session.save()
        messages.success(request, "Sessão cadastrada com sucesso")
        del request.session["register_form_data"]

    return redirect("prontuary_details", id)


@login_required(login_url="login_view")
def therapy_session_update(request, id):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    therapy_session = get_object_or_404(
        TherapySession,
        pk=id,
    )
    prontuary = therapy_session.prontuary

    if not prontuary:
        raise Http404()

    if prontuary.patient.psychologist != psychologist:
        raise HttpResponseBadRequest

    form = TherapySessionRegisterForm(
        data=request.POST or None,
        instance=therapy_session,
    )

    if form.is_valid():
        session = form.save(commit=False)
        session.patient = prontuary.patient
        session.prontuary = prontuary
        session.save()
        messages.success(request, "Sessão atualizada com sucesso")
        return redirect("prontuary_details", prontuary.pk)

    return render(
        request,
        "sections/patients_management/therapy_sessions/update_therapy_session.html",
        context={
            "psychologist": psychologist,
            "prontuary": prontuary,
            "therapy_session": therapy_session,
            "form": form,
        },
    )


@login_required(login_url="login_view")
def therapy_session_update_payment(request, id):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    therapy_session = get_object_or_404(
        TherapySession,
        pk=id,
    )

    if not therapy_session.payment:
        therapy_session.payment = True
    else:
        therapy_session.payment = False

    therapy_session.save()

    return redirect("prontuary_details", therapy_session.prontuary.id)


@login_required(login_url="login_view")
def therapy_session_update_fault(request, id):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    therapy_session = get_object_or_404(
        TherapySession,
        pk=id,
    )

    if not therapy_session.fault:
        therapy_session.fault = True
    else:
        therapy_session.fault = False

    therapy_session.save()

    return redirect("prontuary_details", therapy_session.prontuary.id)


@login_required(login_url="login_view")
def therapy_session_delete(request, id):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    therapy_session = get_object_or_404(
        TherapySession,
        pk=id,
    )
    prontuary_id = therapy_session.prontuary.id

    if therapy_session.prontuary.patient.psychologist != psychologist:
        raise HttpResponseBadRequest

    therapy_session.delete()
    messages.success(request, "Sessão excluída com sucesso")
    return redirect("prontuary_details", prontuary_id)


@login_required(login_url="login_view")
def therapy_session_delete_confirm(request, id):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    therapy_session = get_object_or_404(
        TherapySession,
        pk=id,
    )

    return render(
        request,
        "sections/patients_management/therapy_sessions/confirm_delete_therapy_session.html",
        context={
            "psychologist": psychologist,
            "therapy_session": therapy_session,
        },
    )
