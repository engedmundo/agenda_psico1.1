from datetime import date, datetime

from apps.core.models import Psychologist
from apps.financial_management.models import PaymentControl
from apps.patient_management.models import Patient, Prontuary, TherapySession
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render
from num2words import num2words


@login_required(login_url="login_view")
def pending_session_payments_report(request):
    payment_sessions_info = session_payments_report(
        request=request,
        payment_status="pending",
    )
    payment_sessions_info["pending"] = True

    return render(
        request,
        "sections/financial/reports/session_payments_report.html",
        context=payment_sessions_info,
    )


@login_required(login_url="login_view")
def paid_session_payments_report(request):
    payment_sessions_info = session_payments_report(
        request=request,
        payment_status="paid",
    )
    payment_sessions_info["paid"] = True

    return render(
        request,
        "sections/financial/reports/session_payments_report.html",
        context=payment_sessions_info,
    )


@login_required(login_url="login_view")
def therapy_session_payments_report(request):
    payment_sessions_info = session_payments_report(
        request=request,
    )
    payment_sessions_info["therapy"] = True

    return render(
        request,
        "sections/financial/reports/session_payments_report.html",
        context=payment_sessions_info,
    )


def session_payments_report(request, payment_status: str = None) -> dict:
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
        date_session__range=[start_date, end_date],
    ).order_by(
        "patient",
        "-prontuary",
        "-date_session",
    )
    if payment_status == "pending":
        therapy_sessions = therapy_sessions.filter(
            payment=False,
        )
    elif payment_status == "paid":
        therapy_sessions = therapy_sessions.filter(
            payment=True,
        )

    total_value = sum(
        [
            session.prontuary.patient.session_value
            if session.prontuary.patient.session_value
            else session.prontuary.patient.plain.plain_value
            for session in therapy_sessions
        ]
    )

    return {
        "psychologist": psychologist,
        "therapy_sessions": therapy_sessions,
        "total_value": total_value,
        "start_date": start_date,
        "end_date": end_date,
    }


@login_required(login_url="login_view")
def payment_control_report(request):
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
    payments = PaymentControl.objects.filter(
        prontuary__patient__psychologist=psychologist,
        date_of_pay__range=[start_date, end_date],
    ).order_by(
        "prontuary",
        "-date_of_pay",
    )
    total_value = sum([payment.value_paid for payment in payments])

    return render(
        request,
        "sections/financial/reports/payment_control_report.html",
        context={
            "psychologist": psychologist,
            "payments": payments,
            "total_value": total_value,
            "start_date": start_date,
            "end_date": end_date,
        },
    )


@login_required(login_url="login_view")
def payment_receipt(request, id):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    payment = get_object_or_404(
        PaymentControl,
        pk=id,
    )
    today = datetime.today()

    value_in_words = num2words(
        number=payment.value_paid,
        lang="pt_BR",
        to="currency",
    )
    signature_line = "_" * (
        (
            len(psychologist.psychologist.first_name)
            + len(psychologist.psychologist.last_name)
        )
        + 20
    )

    return render(
        request,
        "sections/financial/reports/payment_receipt.html",
        context={
            "psychologist": psychologist,
            "payment": payment,
            "value_in_words": value_in_words,
            "signature_line": signature_line,
        },
    )
