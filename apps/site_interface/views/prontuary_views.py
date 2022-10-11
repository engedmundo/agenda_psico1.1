from apps.patient_management.models import Prontuary, TherapySession
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from ..forms import ProntuaryRegisterForm


@login_required(login_url="site_interface:home")
def prontuaries(request):
    queryset = Prontuary.objects.all()
    return render(
        request,
        "pages/prontuaries.html",
        context={
            "prontuaries": queryset,
        },
    )


@login_required(login_url="site_interface:home")
def prontuary_details(request, id):
    queryset = Prontuary.objects.filter(pk=id)
    prontuary = get_object_or_404(queryset)
    sessions = TherapySession.objects.filter(pacient__id=prontuary.pacient.id)
    return render(
        request,
        "pages/prontuary_details.html",
        context={
            "prontuary": prontuary,
            "pacient_sessions": sessions,
        },
    )


@login_required(login_url="site_interface:home")
def prontuary_register(request):
    register_form_data = request.session.get("register_form_data", None)
    form = ProntuaryRegisterForm(register_form_data)
    return render(
        request,
        "pages/prontuary_register.html",
        context={
            "form": form,
        },
    )


@login_required(login_url="site_interface:home")
def prontuary_register_save(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session["register_form_data"] = POST
    form = ProntuaryRegisterForm(POST)

    if form.is_valid():
        form.save()
        messages.success(request, "Prontuário registrado com sucesso")

        del request.session["register_form_data"]

    return redirect("prontuaries:prontuaries")


@login_required(login_url="site_interface:home")
def prontuary_update(request, id):
    queryset = Prontuary.objects.filter(pk=id)
    prontuary = get_object_or_404(queryset)

    form = ProntuaryRegisterForm(
        instance=prontuary,
    )

    if request.method == "POST":
        form = ProntuaryRegisterForm(
            request.POST,
            instance=prontuary,
        )

    if form.is_valid():
        form.save()
        messages.success(request, "Prontuário atualizado com sucesso")
        return redirect("prontuaries:prontuaries")

    return render(
        request,
        "pages/prontuary_update.html",
        context={
            "form": form,
        },
    )


@login_required(login_url="site_interface:home")
def prontuary_delete_confirm(request, id):
    queryset = Prontuary.objects.filter(pk=id)
    prontuary = get_object_or_404(queryset)

    if not prontuary:
        raise Http404()

    return render(
        request,
        "pages/prontuary_delete_confirm.html",
        context={
            "prontuary": prontuary,
        },
    )


@login_required(login_url="site_interface:home")
def prontuary_delete(request, id):
    queryset = Prontuary.objects.filter(pk=id)
    prontuary = get_object_or_404(queryset)

    prontuary.delete()
    messages.success(request, "Deletado com sucesso!")
    return redirect("prontuaries:prontuaries")
