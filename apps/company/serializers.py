from rest_framework import serializers

from apps.company.models import Company, Reservation


class CompanyBackOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CreateCompanyBackOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            'name', 'description', 'address'
        ]


class UpdateCompanyBackOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            'name', 'description', 'address'
        ]


class ReservationBackOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = [
            'first_name', 'last_name', 'phone_number', 'email', 'company', 'date', 'time'
        ]
