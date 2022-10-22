from random import randint

from apps.core.models import Psychologist
from apps.front_end.forms import LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect


def home(request):
    psychologists = Psychologist.objects.all()
    while len(psychologists) > 4:
        rand_drop = randint(0, len(psychologists))
        del psychologists[rand_drop]

    return render(
        request,
        "pages/index.html",
        context={
            "psychologists": psychologists,
        },
    )


def professional_description(request, id):
    psychologist = get_object_or_404(Psychologist, id=id)
    return render(
        request,
        "pages/profile_description.html",
        context={
            "psychologist": psychologist,
        },
    )


def login_view(request):
    form = LoginForm()
    return render(
        request,
        "pages/login.html",
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
