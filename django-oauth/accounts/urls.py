from django.urls import path
from .views import kakao_get_login, get_user_info
urlpatterns=[
    path('accounts/kakao/login/', kakao_get_login),
    path('user/kakao/callback/', get_user_info, name="kakao_callback"),
    """
    두 번째 URL 은 kakao developers redirect url에 추가해주시면 됩니다. 
    """
]