from django.urls import path
from .views import MyTokenObtainPairView
urlpatterns=[
    path('user/token/',MyTokenObtainPairView.as_view())
]