from django.http.response import HttpResponse
from django.shortcuts import render
import jwt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserSerializer
from django.core import serializers
from rest_framework.response import Response

# Create your views here.


