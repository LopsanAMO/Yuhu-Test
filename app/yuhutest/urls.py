from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)



urlpatterns = [
    path('admin/', admin.site.urls),


    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/doc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path('', include('yuhutest.apps.users.urls')),
    path('', include('yuhutest.apps.tasks.urls')),
    re_path(r"^$", RedirectView.as_view(url=reverse_lazy("api-root"), permanent=False)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)