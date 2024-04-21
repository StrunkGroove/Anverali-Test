from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('home.urls')),
    path('freelancer/', include('freelancer.urls')),
    path('customer/', include('customer.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
