from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from apps.company.models import Payment, SansConfig


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
