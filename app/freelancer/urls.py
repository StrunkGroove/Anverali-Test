from django.urls import path

from .views import main, info, works


urlpatterns = [
    path('main/', main, name='freelancer-main'),
    path('works/', works, name='customer-works'),
    path('info/', info, name='freelancer-info'),
]