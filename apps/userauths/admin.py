from django.contrib import admin
from .models import User, Profile


class UserAdmin(admin.ModelAdmin):
    search_fields = ['full_name', 'email']
    list_display = ('username', 'email', 'full_name', 'phone')


class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['full_name']
    list_display = ('user', 'eitaa')


admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
