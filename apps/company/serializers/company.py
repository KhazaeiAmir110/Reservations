from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from apps.company.models import Company, HolidaysDate, SansConfig, SansHolidayDateTime


class CreateORRetrieveCompanyBackofficeSerializer(serializers.ModelSerializer):
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


class ListORRetrieveCompanyBackofficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            'name', 'description', 'address', 'image', 'status'
        ]

        extra_kwargs = {
            'name': {'label': _('Name')},
            'description': {'label': _('Description')},
            'address': {'label': _('Address')},
            'image': {'label': _('Image')},
            'status': {'label': _('Status')}
        }
        read_only_fields = [
            'name', 'description', 'address', 'image', 'status'
        ]


class ListCompanySummaryBackofficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            'id', 'name',
        ]

        extra_kwargs = {
            'name': {'label': _('Name')},
        }


class HolidaysDateBaseSerializer(serializers.ModelSerializer):
    company = serializers.CharField(source='company.name')

    class Meta:
        model = HolidaysDate
        fields = [
            'date', 'company'
        ]

        extra_kwargs = {
            'date': {'label': _('Date')},
            'company': {'label': _('Company')},
        }


class CreateORUpdateHolidaysDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidaysDate
        fields = [
            'date', 'company'
        ]

        extra_kwargs = {
            'date': {'label': _('Date')},
            'company': {'label': _('Company')},
        }


class SansConfigBaseBackofficeSerializer(serializers.ModelSerializer):
    company = serializers.CharField(source='company.name')

    class Meta:
        model = SansConfig
        fields = [
            'start_time', 'end_time', 'duration', 'amount', 'company'
        ]
        read_only_fields = [
            'start_time', 'end_time', 'duration', 'amount', 'company'
        ]

        extra_kwargs = {
            'start_time': {'label': _('Start time')},
            'end_time': {'label': _('End time')},
            'duration': {'label': _('Duration')},
            'amount': {'label': _('Amount')},
            'company': {'label': _('Company')},
        }


class CreateORUpdateSansConfigBackofficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SansConfig
        fields = [
            'start_time', 'end_time', 'duration', 'amount', 'company'
        ]

        extra_kwargs = {
            'start_time': {'label': _('Start time')},
            'end_time': {'label': _('End time')},
            'duration': {'label': _('Duration')},
            'amount': {'label': _('Amount')},
            'company': {'label': _('Company')},
        }


class SansHolidayDateTimeBaseBackofficeSerializer(serializers.ModelSerializer):
    company = serializers.CharField(source='company.name')

    class Meta:
        model = SansHolidayDateTime
        fields = [
            'start_time', 'end_time', 'company'
        ]
        read_only_fields = [
            'start_time', 'end_time', 'company'
        ]


class CreateORUpdateSansHolidayDateTimeBackofficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SansHolidayDateTime
        fields = [
            'start_time', 'end_time', 'company'
        ]
