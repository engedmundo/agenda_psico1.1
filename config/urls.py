from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("meuconsultorio/", admin.site.urls),
    path("", include("apps.front_end.urls.home_urls")),
    path("my_profile", include("apps.front_end.urls.home_urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.AdminSite.site_header = "Meu Consultório"
admin.AdminSite.site_title = "psiqueAtiva"
admin.AdminSite.index_title = "Gerenciar meu consultório"
