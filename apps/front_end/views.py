from django.shortcuts import render, get_object_or_404
from apps.core.models import Psychologist
from random import randint


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
        }
    )

def professional_description(request, id):
    psychologist = get_object_or_404(Psychologist, id=id)

    return render(
        request,
        "pages/profile_description.html",
        context={
            "psychologist": psychologist,
        }
    )
