from operator import mod
from django.db.models import fields
from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('title',)


class checkSerializer(serializers.Serializer):
    title=serializers.CharField()
    userId=serializers.CharField()
