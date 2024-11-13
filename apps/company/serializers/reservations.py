from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from apps.company.models import Company, Reservation


class ReservationBackOfficeSerializer(serializers.ModelSerializer):
    company = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = Reservation
        fields = [
            'first_name', 'last_name', 'phone_number', 'email', 'company', 'date', 'time'
        ]

        extra_kwargs = {
            'first_name': {'label': 'First Name'},
            'last_name': {'label': 'Last Name'},
            'phone_number': {'label': _("Phone Number")},
            'email': {'label': _("Email")},
            'company': {'label': _("Company")},
            'date': {'label': _("Date")},
            'time': {'label': _("Time")},
        }


class ListReservationBackOfficeSerializer(serializers.ModelSerializer):
    company = serializers.CharField(source='company.name')
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Reservation
        fields = ['full_name', 'phone_number', 'email', 'company', 'date', 'time']
        read_only_fields = ['full_name', 'phone_number', 'email', 'company', 'date', 'time']

        extra_kwargs = {
            'full_name': {'label': _('Full Name')},
            'phone_number': {'label': _("Phone Number")},
            'email': {'label': _("Email")},
            'company': {'label': _("Company")},
            'date': {'label': _("Date")},
            'time': {'label': _("Time")},
        }

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


# List Filters
class ListItemsFilterReservationsBackofficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            'id', 'name',
        ]

        extra_kwargs = {
            'name': {'label': _('Name')},
        }
