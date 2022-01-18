from rest_framework.serializers import ModelSerializer

from memo.models import Memo


class MemoSerializer(ModelSerializer):
    class Meta:
        model = Memo
        fields = '__all__'
