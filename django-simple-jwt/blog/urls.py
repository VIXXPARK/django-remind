from django.urls import path,include
from .views import BlogView
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet
router = DefaultRouter()

blog_list = BlogViewSet.as_view({"get": "list", "post": "create"})
blog_detail = BlogViewSet.as_view(
    {"get": "retrieve", "patch": "partial_update", "delete": "destroy"})
urlpatterns=[
    path('blog',BlogView.as_view()),
    path('post',blog_list)
]