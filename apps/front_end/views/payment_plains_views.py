from apps.core.models import Psychologist
from apps.financial_management.models import PaymentPlain
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render


@login_required(login_url="login_view")
def payment_plains_list(request):
    psychologist = get_object_or_404(Psychologist, psychologist__username=request.user)
    payment_plains = PaymentPlain.objects.filter(
        psychologist=psychologist,
        is_active=True,
        )

    return render(
        request,
        "pages/financial/payment_plains.html",
        context={
            "psychologist": psychologist,
            "payment_plains": payment_plains,
        },
    )

@login_required(login_url="login_view")
def create_payment_plain(request):
    psychologist = get_object_or_404(Psychologist, psychologist__username=request.user)
    # payment_plains = PaymentPlain.objects.filter(
    #     psychologist=psychologist,
    #     is_active=True,
    #     )

    return render(
        request,
        "pages/financial/create_payment_plain.html",
        context={
            "psychologist": psychologist,
        },
    )

@login_required(login_url="login_view")
def payment_plains_list_archived(request):
    psychologist = get_object_or_404(Psychologist, psychologist__username=request.user)
    payment_plains = PaymentPlain.objects.filter(
        psychologist=psychologist,
        is_active=False,
        )

    return render(
        request,
        "pages/financial/payment_plains_list.html",
        context={
            "psychologist": psychologist,
            "payment_plains": payment_plains,
        },
    )
