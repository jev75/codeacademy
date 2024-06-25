
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('learning/', include('learning.urls')),
    path('', RedirectView.as_view(url='/learning/')),
    path('library/', include('library.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('autoservice/', include('autoservice.urls')),
    path('users/', include('users.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Tinklapio valdymas'