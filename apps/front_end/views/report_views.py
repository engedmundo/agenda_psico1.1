from datetime import date, datetime

from apps.core.models import Psychologist
from apps.patient_management.models import Patient, Prontuary, TherapySession
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render


@login_required(login_url="login_view")
def session_payments_report(request):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )

    start_date = (
        datetime.strptime(request.GET.get("start_date"), "%Y-%m-%d")
        if request.GET.get("start_date")
        else date(2020, 1, 1)
    )
    end_date = (
        datetime.strptime(request.GET.get("end_date"), "%Y-%m-%d")
        if request.GET.get("end_date") 
        else date.today()
    )

    therapy_sessions = TherapySession.objects.filter(
        prontuary__patient__psychologist=psychologist,
        created_at__range=[start_date, end_date],
    ).order_by(
        "patient",
        "-prontuary",
        "-date_session",
    )
    pending_sessions = therapy_sessions.filter(
        payment=False,
    )
    paid_sessions = therapy_sessions.filter(
        payment=True,
    )

    pendind_value = sum(
        [
            session.prontuary.patient.session_value
            if session.prontuary.patient.session_value
            else session.prontuary.patient.plain.plain_value
            for session in pending_sessions
        ]
    )
    paid_value = sum(
        [
            session.prontuary.patient.session_value
            if session.prontuary.patient.session_value
            else session.prontuary.patient.plain.plain_value
            for session in paid_sessions
        ]
    )

    return render(
        request,
        "pages/financial/reports/session_payments_report.html",
        context={
            "psychologist": psychologist,
            "pending_sessions": pending_sessions,
            "paid_sessions": paid_sessions,
            "pending_total": pendind_value,
            "paid_total": paid_value,
            "start_date": start_date,
            "end_date": end_date,
        },
    )
