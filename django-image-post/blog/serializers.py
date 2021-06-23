from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Image, Blog


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']


class BlogSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ('id', 'title', 'images')
        depth = 1

    def create(self, validated_data):
        images_data = self.context['request'].FILES
        blog = Blog.objects.create(**validated_data)
        for image_data in images_data.getlist('images'):
            Image.objects.create(blogId=blog, image=image_data)
        return blog