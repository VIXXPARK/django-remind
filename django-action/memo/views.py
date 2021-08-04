from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .models import Memo
from .serializers import MemoSerializer


class MemoModelViewSet(ModelViewSet):
    queryset = Memo.objects.all()
    serializer_class = MemoSerializer

    @action(detail=False, methods=['GET'])
    def recent_memo(self, request):
        recent_memo = Memo.objects.all().order_by('-updated_at')
        serializer = self.get_serializer(recent_memo, many=True)
        return Response(serializer.data)
