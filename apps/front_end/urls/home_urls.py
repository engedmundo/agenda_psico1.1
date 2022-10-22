from django.urls import path

from ..views import home, professional_description

app_name = "site_interface"


urlpatterns = [
    path(
        "",
        home,
        name="home",
    ),
    path(
        "professional_description/<int:id>",
        professional_description,
        name="professional_description",
    ),
]
