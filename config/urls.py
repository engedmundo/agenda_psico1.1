from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('pannel/', admin.site.urls),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('api/plains', include('apps.plains.api.urls')),
    # path('api/pacient_sessions', include('apps.pacient_sessions.api.urls')),
    # path('api/pacients', include('apps.pacients.api.urls')),
    # path('api/payments', include('apps.payments.api.urls')),
    # path('api/prontuaries', include('apps.prontuaries.api.urls')),
    # path('', include('apps.site_interface.urls')),
    path('', include('apps.site_interface.urls')),
    path('', include('apps.financial_management.urls')),
    path('', include('apps.patient_management.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)