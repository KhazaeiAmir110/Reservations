from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    search_fields = ['full_name', 'email']
    list_display = ('username', 'email', 'phone')


admin.site.register(User, UserAdmin)
