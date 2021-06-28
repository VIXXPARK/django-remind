from django.urls import path
from .views import kakaoGetLogin,getTokenOAuth
urlpatterns=[
    path('accounts/kakao/login/',kakaoGetLogin),
    path('accounts/kakao/oauth/token/',getTokenOAuth)
]