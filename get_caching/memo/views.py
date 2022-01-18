from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from memo.models import Memo


class MemoAPIView(APIView):
    @method_decorator(cache_page(60))
    def get(self, request, pk):
        memo = Memo.objects.get(id=pk)
        print('cache')
        return Response(str(memo))

