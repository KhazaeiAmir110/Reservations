from rest_framework import serializers

from apps.company.models import Company


class CompanyBackOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
