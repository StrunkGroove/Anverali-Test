from django.contrib import admin

from .models import Customer, Task


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'description', 'contact_method')
    search_fields = ('user__username', 'user__email')


@admin.register(Task)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'customer')
