from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('author/', include('author.urls')),
    path('publisher/', include('publisher.urls')),
    path('users/', include('users.urls')),
    path('service_fees/', include('service_fees.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
