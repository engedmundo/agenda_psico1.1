
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from apps.financial_management.models import PaymentPlain

from ..forms import PaymentPlainRegisterForm
from apps.financial_management.models import PaymentPlain


@login_required(login_url='site_interface:home')
def plains(request):
    plains = PaymentPlain.objects.all()
    return render(request, 'pages/plains.html',
                  context={
                      "plains": plains,
                  })


@login_required(login_url='site_interface:home')
def plains_register(request):
    register_form_data = request.session.get(
        'register_form_data',
        None
    )
    form = PaymentPlainRegisterForm(register_form_data)
    return render(request, 'pages/plain_register.html', {
        'form': form,
    }
    )


@login_required(login_url='site_interface:home')
def plains_register_save(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = PaymentPlainRegisterForm(POST)

    if form.is_valid():
        form.save()
        messages.success(request, 'Plano criado com sucesso')

        del(request.session['register_form_data'])

    return redirect('plains:plains')


@login_required(login_url='site_interface:home')
def plains_update(request, id):
    queryset = PaymentPlain.objects.filter(pk=id)
    plain = get_object_or_404(queryset)

    if not plain:
        raise Http404()

    form = PaymentPlainRegisterForm(
        data=request.POST or None,
        instance=plain,
    )

    if form.is_valid():
        form.save()
        messages.success(request, 'Plano atualizado com sucesso')
        return redirect('plains:plains')

    return render(
        request,
        'pages/plain_update.html',
        context={
            "form": form,
        }
    )


@login_required(login_url='site_interface:home')
def plains_delete_confirm(request, id):
    queryset = PaymentPlain.objects.filter(pk=id)
    plain = get_object_or_404(queryset)

    if not plain:
        raise Http404()

    return render(
        request,
        'pages/plain_delete_confirm.html',
        context={
            "plain": plain,
        }
    )


@login_required(login_url='site_interface:home')
def plains_delete(request, id):
    queryset = PaymentPlain.objects.filter(pk=id)
    plain = get_object_or_404(queryset)

    plain.delete()
    messages.success(request, 'Deletado com sucesso')
    return redirect('plains:plains')
