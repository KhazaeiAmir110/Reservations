from django.contrib import admin
from .models import Company, HolidaysDate, SansConfig, SansHolidayDateTime, Reservation


class CompanyAdmin(admin.ModelAdmin):
    search_fields = ['name', 'user']
    list_display = ('name', 'user', 'address')


class HolidaysDateyAdmin(admin.ModelAdmin):
    search_fields = ['date']
    list_display = ('date', 'company')


class SansConfigAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time', 'company')


class SansHolidayDateTimeAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time', 'company')


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'company')


admin.site.register(Company, CompanyAdmin)
admin.site.register(HolidaysDate, HolidaysDateyAdmin)
admin.site.register(SansConfig, SansConfigAdmin)
admin.site.register(SansHolidayDateTime, SansHolidayDateTimeAdmin)
admin.site.register(Reservation, ReservationAdmin)
