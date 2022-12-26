from apps.core.models import Psychologist
from apps.financial_management.forms import ExpenseControlRegisterForm
from apps.financial_management.models import ExpenseControl, ExpenseCategory
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render


@login_required(login_url="login")
def expense_control_list(request):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    expenses = ExpenseControl.objects.filter(
        psychologist=psychologist,
        is_active=True,
    ).order_by("-completion_date")

    return render(
        request,
        "sections/financial/expense_control/expense_control.html",
        context={
            "psychologist": psychologist,
            "expenses": expenses,
        },
    )


@login_required(login_url="login")
def create_expense_control(request):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    categories = ExpenseCategory.objects.filter(
        psychologist=psychologist,
        is_active=True,
    )
    register_form_data = request.session.get(
        "register_form_data",
        None,
    )
    form = ExpenseControlRegisterForm(
        register_form_data,
    )
    return render(
        request,
        "sections/financial/expense_control/create_expense_control.html",
        context={
            "psychologist": psychologist,
            "categories": categories,
            "form": form,
        },
    )


@login_required(login_url="login")
def expense_control_save(request):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    if not request.POST:
        raise Http404()

    form = ExpenseControlRegisterForm(
        data=request.POST or None,
    )

    if form.is_valid():
        expense = form.save(commit=False)
        expense.psychologist = psychologist
        expense.save()

    return redirect("expense_control")


@login_required(login_url="login")
def expense_control_update(request, id):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    expense_control = get_object_or_404(
        ExpenseControl,
        pk=id,
    )
    categories = ExpenseCategory.objects.filter(
        psychologist=psychologist,
        is_active=True,
    )
    selected_category = expense_control.category

    if not expense_control:
        raise Http404()

    if expense_control.psychologist != psychologist:
        raise HttpResponseBadRequest

    form = ExpenseControlRegisterForm(
        request.POST or None,
        instance=expense_control,
    )

    if form.is_valid():
        expense = form.save(commit=False)
        expense.psychologist = psychologist
        expense.save()
        return redirect("expense_control")

    return render(
        request,
        "sections/financial/expense_control/update_expense_control.html",
        context={
            "psychologist": psychologist,
            "form": form,
            "expense_control": expense_control,
            "selected_category": selected_category,
            "categories": categories,
        },
    )


@login_required(login_url="login")
def expense_control_delete(request, id):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    expense_control = get_object_or_404(
        ExpenseControl,
        pk=id,
    )

    if expense_control.psychologist != psychologist:
        raise HttpResponseBadRequest

    expense_control.delete()
    return redirect("expense_control")


@login_required(login_url="login")
def expense_control_delete_confirm(request, id):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    expense = get_object_or_404(
        ExpenseControl,
        pk=id,
    )

    return render(
        request,
        "sections/financial/expense_control/confirm_delete_expense_control.html",
        context={
            "psychologist": psychologist,
            "expense": expense,
        },
    )
