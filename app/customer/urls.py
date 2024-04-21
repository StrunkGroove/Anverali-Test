from django.urls import path

from .views import main, freelancers, profile, tasks, edit_task, delete_task


urlpatterns = [
    path('main/', main, name='customer-main'),
    path('freelancers/', freelancers, name='freelancers'),
    path('profile/', profile, name='customer-profile'),
    path('tasks/', tasks, name='tasks'),
    path('edit/<int:task_id>/', edit_task, name='edit-task'),
    path('delete/<int:task_id>/', delete_task, name='delete-task'),
]