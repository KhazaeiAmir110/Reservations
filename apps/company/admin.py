from django.contrib import admin
from .models import Company, Category, WorkDate, WorkTime, Booking


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


class BookingAdmin(admin.ModelAdmin):
    search_fields = ['full_name', 'company']
    list_display = ('full_name', 'company', 'active')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(WorkDate, WorkDateAdmin)
admin.site.register(WorkTime, WorkTimeAdmin)
admin.site.register(Booking, BookingAdmin)
