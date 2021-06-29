from django.urls import path
from .views import kakaoGetLogin
urlpatterns=[
    path('accounts/kakao/login/',kakaoGetLogin),
]