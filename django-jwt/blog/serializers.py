from rest_framework import fields, serializers
from .models import Image, Post


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model: Image
        fields = ['image']


class BlogSerailzer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model: Post
        fields = ('id', 'title', 'author', 'images',
                  'content', 'created_at', 'updated_at')

    def create(self, validated_data):
        images_data = self.context['request'].FILES
        post = Post.objects.create(**validated_data)
        for image_data in images_data.getlist('images'):
            Image.objects.create(postId=post, image=image_data)
        return post
