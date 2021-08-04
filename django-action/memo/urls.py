from django.urls import path
from .views import MemoModelViewSet
memo_list = MemoModelViewSet.as_view({"get": "list", "post": "create"})
memo_detail = MemoModelViewSet.as_view(
    {"get": "retrieve", "patch": "partial_update", "delete": "destroy"})


urlpatterns = [
    path("memo", memo_list),
    path("memo/<int:pk>", memo_detail),
    path("memo/recent", MemoModelViewSet.as_view({"get": "recent_memo"}))
]
