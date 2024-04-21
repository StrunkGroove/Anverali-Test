from django.conf.urls import url

from .views import user_login


urlpatterns = [
    url('login/', user_login, name='login'),
]