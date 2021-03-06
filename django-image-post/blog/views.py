from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.response import Response


class BlogViewSet(ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({'success': True})

    def get_queryset(self):
        return super().get_queryset()
