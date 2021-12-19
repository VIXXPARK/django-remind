from django.urls import path
from .views import kakao_get_login, get_user_info

urlpatterns = [
    path('accounts/kakao/login/', kakao_get_login),
    path('user/kakao/callback/', get_user_info, name="kakao_callback"),
]
