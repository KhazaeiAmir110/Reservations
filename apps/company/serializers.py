from rest_framework import serializers

from apps.company.models import Company, Reservation, Payment


class CompanyBackOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            'name', 'description', 'address'
        ]


class ReservationBackOfficeSerializer(serializers.ModelSerializer):
    company = serializers.CharField(source='company.name')

    class Meta:
        model = Reservation
        fields = [
            'first_name', 'last_name', 'phone_number', 'email', 'company', 'date', 'time'
        ]
        read_only_fields = [
            'first_name', 'last_name', 'phone_number', 'email',
        ]


class PaymentBackOfficeSerializer(serializers.ModelSerializer):
    company = serializers.CharField(source='reservation.company.name')
    date = serializers.DateField(source='reservation.date')
    time = serializers.TimeField(source='reservation.time')

    class Meta:
        model = Payment
        fields = [
            'company', 'date', 'time', 'status'
        ]
