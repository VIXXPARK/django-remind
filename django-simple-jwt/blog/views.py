import blog
from os import stat
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from .serializers import BlogSerializer,checkSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Blog
from rest_framework.viewsets import ModelViewSet

class BlogView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        res = BlogSerializer(data=request.data)
        if not res.is_valid():
            return Response({'succsess': False}, status=status.HTTP_400_BAD_REQUEST)
        title= res.validated_data['title']
        Blog.objects.create(userId=request.user,title=title)
        return Response({'success': True}, status=status.HTTP_200_OK)

    def get(self,request):
        blog_list = checkSerializer(Blog.objects.all(),many=True)
        return Response({'data':blog_list.data},status=status.HTTP_200_OK)
        
class BlogViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset=Blog.objects.all()
    serializer_class=checkSerializer
