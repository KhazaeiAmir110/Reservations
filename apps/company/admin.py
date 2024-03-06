from django.contrib import admin
from .models import Company, Category


class CompanyAdmin(admin.ModelAdmin):
    search_fields = ['name', 'user']
    list_display = ('name', 'user', 'status')


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'is_subb')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Category, CategoryAdmin)