from apps import site_interface
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render

from ..forms import LoginForm


def home(request):
    return render(
        request,
        "pages/home/home.html",
    )


def login_view(request):
    form = LoginForm()
    return render(
        request,
        "pages/home/login.html",
        context={
            "form": form,
        },
    )


def login_create(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)

    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get("username", ""),
            password=form.cleaned_data.get("password", ""),
        )

        if authenticated_user is not None:
            messages.success(request, "Login realizado com sucesso!")
            login(
                request,
                user=authenticated_user,
            )
        else:
            messages.error(request, "Credenciais inválidas")

    else:
        messages.error(request, "Erro ao validar formulário")

    return redirect("site_interface:home")


@login_required(login_url="site_interface:login_view")
def logout_view(request):
    logout(request)
    return redirect("site_interface:home")
