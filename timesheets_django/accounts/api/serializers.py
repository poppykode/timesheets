from rest_framework import serializers
from accounts.models import User
from django.conf import settings

class RegistrationSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('first_name','last_name','email','designation',)

class PasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class loginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

