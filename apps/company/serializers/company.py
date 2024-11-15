from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from apps.company.models import Company


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


class ListORDestroyCompanyBackofficeSerializer(serializers.ModelSerializer):
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
