from django.contrib import admin

from .models import Freelancer, Direction


@admin.register(Freelancer)
class FreelancerAdmin(admin.ModelAdmin):
    list_display = ('user', 'experience', 'contact_info')
    list_filter = ('experience',)
    search_fields = ('user__username', 'user__email')


@admin.register(Direction)
class FreelancerAdmin(admin.ModelAdmin):
    list_display = ('name',)