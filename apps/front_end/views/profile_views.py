from audioop import reverse
from random import randint

from apps.core.models import Psychologist
from apps.front_end.forms import PsychologistRegisterForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render


@login_required(login_url="login_view")
def my_profile(request, id):
    psychologist = get_object_or_404(Psychologist, id=id)

    return render(
        request,
        "pages/index.html",
        context={
            "psychologist": psychologist,
        },
    )


@login_required(login_url="login_view")
def my_profile_update(request):
    user = get_object_or_404(User, username=request.user)
    psychologist = get_object_or_404(Psychologist, psychologist=user)

    if not psychologist:
        raise Http404()

    psycho_form = PsychologistRegisterForm(
        request.POST or None,
        request.FILES or None,
        instance=psychologist,
    )
    user_form = UserRegisterForm(
        request.POST or None,
        instance=user,
    )

    if psycho_form.is_valid() and user_form.is_valid():
        user_form.save()
        psycho_form.save()
        messages.success(request, "Perfil atualizado com sucesso")
        return redirect("my_profile")

    return render(
        request,
        "pages/my_profile/my_profile.html",
        context={
            "psycho_form": psycho_form,
            "user_form": user_form,
            "psychologist": psychologist,
            "user": user,
        },
    )
