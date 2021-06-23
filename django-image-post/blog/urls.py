from django.db import router
from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet
router = DefaultRouter()

blog_list = BlogViewSet.as_view({"get": "list", "post": "create"})
blog_detail = BlogViewSet.as_view(
    {"get": "retrieve", "patch": "partial_update", "delete": "destroy"})


urlpatterns = [
    path('upload', blog_list, name="blog_list"),
    path('blog/<int:pk>', blog_detail),
]
