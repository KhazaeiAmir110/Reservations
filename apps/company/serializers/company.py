from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from apps.company.models import Company, HolidaysDate


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


class CreateORUpdateHolidaysDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidaysDate
        fields = [
            'date', 'company'
        ]
