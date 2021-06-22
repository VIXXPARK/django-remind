from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.parsers import MultiPartParser,FormParser,JSONParser
from rest_framework.viewsets import ModelViewSet
from .models import Post
from .serializers import BlogSerailzer
from rest_framework.status import(
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_502_BAD_GATEWAY,
    HTTP_500_INTERNAL_SERVER_ERROR
)
from rest_framework.response import Response
from rest_framework.exceptions import APIException
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
def posts(request):
    posts = Post.objects.filter(
        published_at__isnull=False).order_by('-published_at')
    post_list = serializers.serialize('json', posts)
    return HttpResponse(post_list, content_type="text/json-comment-filtered")


class BlogViewSet(ModelViewSet):
    permission_classes=(permissions.AllowAny,)
    queryset=Post.objects.all()
    serializer_class=BlogSerailzer
    parser_classes = (MultiPartParser,FormParser)
    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
        except APIException as e:
            return Response({"success":False,'err':e.detail},status=HTTP_404_NOT_FOUND)
        context = {
            'success' : True,
        }
        instance = response.data
        return Response(context,HTTP_201_CREATED)