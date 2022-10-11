
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q

from apps.patient_management.models import TherapySession

from ..forms import TherapySessionRegisterForm


@login_required(login_url='site_interface:home')
def pacient_sessions(request):
    pacient_sessions = TherapySession.objects.all().order_by('-date_session', 'hour_session')
    return render(request, 'pages/pacient_sessions.html',
                  context={
                      "pacient_sessions": pacient_sessions,
                  })


@login_required(login_url='site_interface:home')
def pacient_sessions_details(request, id):
    pacient_sessions = TherapySession.objects.filter(pk=id).first()
    return render(request, 'pages/pacient_session_details.html',
                  context={
                      "pacient_sessions": pacient_sessions,
                  })


@login_required(login_url='site_interface:home')
def pacient_session_register(request):
    register_form_data = request.session.get('register_form_data', None)
    form = TherapySessionRegisterForm(register_form_data)
    return render(
        request,
        'pages/pacient_sessions_register.html',
        {
            'form': form,
        }
    )


@login_required(login_url='site_interface:home')
def pacient_session_register_save(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = TherapySessionRegisterForm(POST)

    if form.is_valid():
        form.save()
        messages.success(request, 'Sessão registrada com sucesso')

        del(request.session['register_form_data'])

    return redirect('pacient_sessions:pacient_sessions')


@login_required(login_url='site_interface:home')
def pacient_session_update(request, id):
    queryset = TherapySession.objects.filter(pk=id)
    pacient_session = get_object_or_404(queryset)

    form = TherapySessionRegisterForm(
        instance=pacient_session,
    )

    if request.method == 'POST':
        form = TherapySessionRegisterForm(
            request.POST,
            instance=pacient_session,
        )

        if form.is_valid():
            form.save()
            messages.success(request, 'Sessão atualizada com sucesso!')
            return redirect('pacient_sessions:pacient_sessions')

    return render(
        request,
        'pages/pacient_sessions_update.html',
        context={
            'form': form,
        }
    )


@login_required(login_url='site_interface:home')
def pacient_session_delete_confirm(request, id):
    queryset = TherapySession.objects.filter(pk=id)
    pacient_session = get_object_or_404(queryset)

    if not pacient_session:
        raise Http404()

    return render(
        request,
        'pages/pacient_session_delete_confirm.html',
        context={
            'pacient_session': pacient_session,
        }
    )


@login_required(login_url='site_interface:home')
def pacient_session_delete(request, id):
    queryset = TherapySession.objects.filter(pk=id)
    pacient_session = get_object_or_404(queryset)

    pacient_session.delete()
    messages.success(request, 'Deletado com sucesso!')
    return redirect('pacient_sessions:pacient_sessions')

@login_required(login_url='site_interface:home')
def pacient_session_search(request):
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404()

    pacient_sessions = TherapySession.objects.filter(
        Q(pacient__pacient_name__icontains=search_term),
    ).order_by('-id')

    return render(request, 'pages/pacient_sessions_search.html',
                context={
                    "pacient_sessions": pacient_sessions,
                    "search_term": search_term,
                })