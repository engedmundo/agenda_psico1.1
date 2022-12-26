from apps.core.models import Psychologist
from apps.financial_management.forms import ExpenseCategoryRegisterForm
from apps.financial_management.models import ExpenseCategory
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render


@login_required(login_url="login")
def expense_categories_list(request):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    expense_categories = ExpenseCategory.objects.filter(
        psychologist=psychologist,
        is_active=True,
    )

    return render(
        request,
        "sections/financial/expense_categories/expense_categories.html",
        context={
            "psychologist": psychologist,
            "expense_categories": expense_categories,
        },
    )


@login_required(login_url="login")
def create_expense_category(request):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    register_form_data = request.session.get("register_form_data", None)

    form = ExpenseCategoryRegisterForm(register_form_data)
    return render(
        request,
        "sections/financial/expense_categories/create_expense_category.html",
        context={
            "psychologist": psychologist,
            "form": form,
        },
    )


@login_required(login_url="login")
def expense_category_save(request):
    psychologist = get_object_or_404(Psychologist, psychologist__username=request.user)
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session["register_form_data"] = POST
    form = ExpenseCategoryRegisterForm(POST)

    if form.is_valid():
        expense_category = form.save(commit=False)
        expense_category.psychologist = psychologist
        expense_category.save()
        del request.session["register_form_data"]

    return redirect("expense_categories")


@login_required(login_url="login")
def expense_category_update(request, id):
    psychologist = get_object_or_404(Psychologist, psychologist__username=request.user)
    expense_category = get_object_or_404(
        ExpenseCategory,
        pk=id,
    )

    if not expense_category:
        raise Http404()

    if expense_category.psychologist != psychologist:
        raise HttpResponseBadRequest

    form = ExpenseCategoryRegisterForm(
        data=request.POST or None,
        instance=expense_category,
    )

    if form.is_valid():
        expense_category = form.save(commit=False)
        expense_category.psychologist = psychologist
        expense_category.save()
        return redirect("expense_categories")

    return render(
        request,
        "sections/financial/expense_categories/update_expense_category.html",
        context={
            "psychologist": psychologist,
            "form": form,
        },
    )


@login_required(login_url="login")
def expense_category_archive_confirm(request, id):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    expense_category = get_object_or_404(
        ExpenseCategory,
        pk=id,
    )

    return render(
        request,
        "sections/financial/expense_categories/confirm_archive_expense_category.html",
        context={
            "psychologist": psychologist,
            "expense_category": expense_category,
        },
    )


@login_required(login_url="login")
def expense_category_archive(request, id):
    psychologist = get_object_or_404(Psychologist, psychologist__username=request.user)
    expense_category = get_object_or_404(
        ExpenseCategory,
        pk=id,
    )

    if expense_category.psychologist != psychologist:
        raise HttpResponseBadRequest

    expense_category.is_active = False
    expense_category.save()

    return redirect("expense_categories")


@login_required(login_url="login")
def expense_categories_archived(request):
    psychologist = get_object_or_404(Psychologist, psychologist__username=request.user)
    expense_categories = ExpenseCategory.objects.filter(
        psychologist=psychologist,
        is_active=False,
    )

    return render(
        request,
        "sections/financial/expense_categories/archived_expense_categories.html",
        context={
            "psychologist": psychologist,
            "expense_categories": expense_categories,
        },
    )


@login_required(login_url="login")
def expense_category_unarchive(request, id):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    expense_category = get_object_or_404(
        ExpenseCategory,
        pk=id,
    )

    if expense_category.psychologist != psychologist:
        raise HttpResponseBadRequest

    expense_category.is_active = True
    expense_category.save()

    return redirect("expense_categories")


@login_required(login_url="login")
def expense_category_delete(request, id):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    expense_category = get_object_or_404(
        ExpenseCategory,
        pk=id,
    )

    if expense_category.psychologist != psychologist:
        raise HttpResponseBadRequest

    expense_category.delete()
    return redirect("expense_categories")


@login_required(login_url="login")
def expense_category_delete_confirm(request, id):
    psychologist = get_object_or_404(
        Psychologist,
        psychologist__username=request.user,
    )
    expense_category = get_object_or_404(
        ExpenseCategory,
        pk=id,
    )

    return render(
        request,
        "sections/financial/expense_categories/confirm_delete_expense_category.html",
        context={
            "psychologist": psychologist,
            "expense_category": expense_category,
        },
    )
