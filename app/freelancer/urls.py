from django.urls import path

from .views import main, profile, works


urlpatterns = [
    path('main/', main, name='freelancer-main'),
    path('works/', works, name='customer-works'),
    path('profile/', profile, name='freelancer-profile'),
]