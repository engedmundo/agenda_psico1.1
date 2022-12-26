from datetime import date, datetime

from apps.core.models import Psychologist
from apps.financial_management.models import (
    ExpenseCategory,
    ExpenseControl,
    PaymentControl,
)
from apps.patient_management.models import Patient, Prontuary, TherapySession
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render
from num2words import num2words


@login_required(login_url="login")
def therapy_session_payments_report(request):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    start_date, end_date = get_start_and_end_date(request=request)

    therapy_sessions = TherapySession.objects.filter(
        prontuary__patient__psychologist=psychologist,
        date_session__range=[start_date, end_date],
    ).order_by(
        "patient",
        "-prontuary",
        "-date_session",
    )
    payment_status = None

    if request.GET.get("payment_status"):
        payment_status = request.GET.get("payment_status")

        if payment_status == "pending":
            therapy_sessions = therapy_sessions.filter(
                payment=False,
            )
        elif payment_status == "paid":
            therapy_sessions = therapy_sessions.filter(
                payment=True,
            )
        else:
            raise Http404

    total_value = sum(
        [
            session.prontuary.patient.session_value
            if session.prontuary.patient.session_value
            else session.prontuary.patient.plain.plain_value
            for session in therapy_sessions
        ]
    )

    return render(
        request,
        "sections/financial/reports/session_payments_report.html",
        context={
            "psychologist": psychologist,
            "therapy_sessions": therapy_sessions,
            "total_value": total_value,
            "start_date": start_date,
            "end_date": end_date,
            "payment_status": payment_status,
        },
    )


@login_required(login_url="login")
def payment_control_report(request):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    start_date, end_date = get_start_and_end_date(request=request)
    payments = PaymentControl.objects.filter(
        prontuary__patient__psychologist=psychologist,
        date_of_pay__range=[start_date, end_date],
    ).order_by(
        "prontuary",
        "-date_of_pay",
    )
    patients = Patient.objects.filter(
        psychologist=psychologist,
        is_active=True,
    )
    if request.GET.get("patient"):
        try:
            patient = get_object_or_404(
                Patient,
                pk=request.GET.get("patient"),
            )
            if patient.psychologist != psychologist:
                raise HttpResponseBadRequest

            payments = payments.filter(
                prontuary__patient=patient,
            )
        except:
            raise Http404

    total_value = sum([payment.value_paid for payment in payments])

    return render(
        request,
        "sections/financial/reports/payment_control_report.html",
        context={
            "psychologist": psychologist,
            "payments": payments,
            "patients": patients,
            "total_value": total_value,
            "start_date": start_date,
            "end_date": end_date,
        },
    )


@login_required(login_url="login")
def payment_receipt(request, id):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    payment = get_object_or_404(
        PaymentControl,
        pk=id,
    )

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


@login_required(login_url="login")
def expense_control_report(request):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    start_date, end_date = get_start_and_end_date(request=request)

    expenses = ExpenseControl.objects.filter(
        psychologist=psychologist,
        completion_date__range=[start_date, end_date],
    ).order_by("-completion_date")

    categories = ExpenseCategory.objects.filter(
        psychologist=psychologist,
        is_active=True,
    )
    if request.GET.get("category"):
        try:
            category = get_object_or_404(
                ExpenseCategory,
                pk=request.GET.get("category"),
            )
            if category.psychologist != psychologist:
                raise HttpResponseBadRequest

            expenses = expenses.filter(
                category=category,
            )
        except:
            raise Http404

    total_value = sum([expense.expense_value for expense in expenses])

    return render(
        request,
        "sections/financial/reports/expense_control_report.html",
        context={
            "psychologist": psychologist,
            "expenses": expenses,
            "categories": categories,
            "total_value": total_value,
            "start_date": start_date,
            "end_date": end_date,
        },
    )


def get_start_and_end_date(request) -> tuple:
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
    return start_date, end_date
