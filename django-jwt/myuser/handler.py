from .serializers import UserSerializer
from rest_framework_jwt.settings import api_settings


def handler(token, user=None, request=None):
    return{
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }
