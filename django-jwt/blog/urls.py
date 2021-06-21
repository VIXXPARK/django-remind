from . import views
from django.urls import path


urlpatterns=[
    path('posts/',views.posts,name='posts')
]