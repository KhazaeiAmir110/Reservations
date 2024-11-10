from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from apps.company.models import Company, Reservation, Payment, SansConfig


class CompanyBackOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            'name', 'description', 'address', 'image'
        ]

        extra_kwargs = {
            'name': {'label': _('Name')},
            'description': {'label': _('Description')},
            'address': {'label': _('Address')},
            'image': {'label': _('Image')}
        }


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


class PaymentBackOfficeSerializer(serializers.ModelSerializer):
    company = serializers.CharField(source='reservation.company.name')
    date = serializers.DateField(source='reservation.date')
    time = serializers.TimeField(source='reservation.time')
    amount = serializers.SerializerMethodField()

    class Meta:
        model = Payment
        fields = [
            'company', 'date', 'time', 'status', 'amount'
        ]

        extra_kwargs = {
            'company': {'label': _('Company')},
            'date': {'label': _('Date')},
            'time': {'label': _('Time')},
            'status': {'label': _('Status')},
            'amount': {'label': _('Amount')}
        }

    def get_amount(self, obj):
        try:
            sans_config = SansConfig.objects.get(company=obj.reservation.company)
            return sans_config.amount
        except SansConfig.DoesNotExist:
            return None


class PaymentTotalBackofficeSerializer(serializers.ModelSerializer):
    amount = serializers.SerializerMethodField()

    class Meta:
        model = Payment
        fields = [
            'status', 'amount'
        ]

    def get_amount(self, obj):
        try:
            sans_config = SansConfig.objects.get(company=obj.reservation.company)
            return sans_config.amount
        except SansConfig.DoesNotExist:
            return None
