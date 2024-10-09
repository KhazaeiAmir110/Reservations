from rest_framework import serializers

from apps.userauths.models import User


def validate_username(attrs):
    if 'admin' in attrs:
        raise serializers.ValidationError('admin is not non !!!')
    return attrs


def validate_email(attrs):
    if '@gmail.com' in attrs:
        return attrs
    else:
        raise serializers.ValidationError('is not a valid email !!!')


def validate_phone(attrs):
    if (attrs is None) or (attrs is str):
        raise serializers.ValidationError('is not a valid phone number !!!')
    else:
        return attrs


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100, validators=[validate_username])
    password = serializers.CharField(max_length=100, write_only=True)
    email = serializers.EmailField(validators=[validate_email])
    phone = serializers.IntegerField(validators=[validate_phone])

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'phone']


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']


# Page 1
class UserDashboardHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username', 'image'
        ]


class UserDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'phone', 'email'
        ]
