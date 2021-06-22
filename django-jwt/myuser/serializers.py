from rest_framework import fields, serializers
from .models import User
from rest_framework_jwt.settings import api_settings

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
