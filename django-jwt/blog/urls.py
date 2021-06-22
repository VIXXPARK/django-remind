from django.urls.conf import include
from . import views
from django.urls import path

# post_list=views.BlogViewSet.as_view({"get":"list","post":"create"})


urlpatterns = [
    path('posts/', views.posts, name='posts'),
    # path('posts/upload/',post_list,name="upload")
]
