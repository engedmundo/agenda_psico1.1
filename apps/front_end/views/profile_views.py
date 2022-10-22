from random import randint

from apps.core.models import Psychologist
from apps.front_end.forms import PsychologistRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render


@login_required(login_url="site_interface:login_view")
def my_profile(request, id):
    psychologist = get_object_or_404(Psychologist, id=id)

    return render(
        request,
        "pages/index.html",
        context={
            "psychologist": psychologist,
        },
    )


@login_required(login_url="site_interface:home")
def plains_update(request, id):
    psychologist = get_object_or_404(Psychologist, id=id)

    if not psychologist:
        raise Http404()

    form = PsychologistRegisterForm(
        data=request.POST or None,
        instance=psychologist,
    )

    if form.is_valid():
        form.save()
        messages.success(request, "Perfil atualizado com sucesso")
        return redirect("site_interface:home")

    return render(
        request,
        "pages/my_profile/my_profile.html",
        context={
            "form": form,
        },
    )
