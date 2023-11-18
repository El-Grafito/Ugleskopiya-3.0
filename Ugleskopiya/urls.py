from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from Ugleskopiya.settings.base import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

urlpatterns = [
    path('batya/', admin.site.urls),
    path('', include('apps.app.urls')),
    path('', include('apps.authorization.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 