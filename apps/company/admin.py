from django.contrib import admin
from .models import Company, Category, WorkDate, WorkTime


class CompanyAdmin(admin.ModelAdmin):
    search_fields = ['name', 'user']
    list_display = ('name', 'user', 'status')


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'is_subb')


class WorkDateAdmin(admin.ModelAdmin):
    list_display = ('date', 'company', 'active')


class WorkTimeAdmin(admin.ModelAdmin):
    list_display = ('work_date', 'active')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(WorkDate, WorkDateAdmin)
admin.site.register(WorkTime, WorkTimeAdmin)
