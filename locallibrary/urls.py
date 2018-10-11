from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.conf.urls import url, include


urlpatterns = [
    url('admin/', admin.site.urls),
    url('catalog/', include('catalog.urls')),
    #url('', RedirectView.as_view(url='/catalog/', permanent=True)),
    url(r'^accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



