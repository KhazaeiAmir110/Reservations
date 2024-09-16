from rest_framework import serializers

from apps.company.models import Company, Reservation, Payment
from apps.userauths.serializers import UserSerializer


class CompanyBackOfficeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Company
        fields = [
            'name', 'description', 'address', 'slug', 'user'
        ]
        read_only_fields = [
            'user', 'slug'
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


class ReservationForPaymentSerializer(serializers.ModelSerializer):
    company = serializers.CharField(source='company.name')

    class Meta:
        model = Reservation
        fields = [
            'company', 'date', 'time'
        ]


class PaymentBackOfficeSerializer(serializers.ModelSerializer):
    reservation = ReservationForPaymentSerializer()

    class Meta:
        model = Payment
        fields = [
            'reservation', 'status'
        ]
