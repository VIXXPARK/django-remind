from django.template.defaulttags import url
from django.urls import include, path
from memo.views import MemoAPIView

urlpatterns = [
    path('<int:pk>', MemoAPIView.as_view()),
]
