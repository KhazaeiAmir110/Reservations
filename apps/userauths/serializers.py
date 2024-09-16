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


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'phone']
        extra_kwargs = {
            'password': {
                'write_only': True
            },
            'username': {
                'validators': [validate_username]
            },
            'email': {
                'validators': [validate_email]
            }
        }


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'password']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'full_name', 'phone'
        ]
