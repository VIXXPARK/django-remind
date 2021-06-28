from rest_framework import serializers

class getCodeSerializer(serializers.Serializer):
    code = serializers.CharField()

class getOAuthSerializer(serializers.Serializer):
    token_type = serializers.CharField()
    access_token = serializers.CharField()
    expires_in = serializers.IntegerField()
    refresh_token = serializers.CharField()
    refresh_token_expires_in =serializers.IntegerField()
    scope =serializers.CharField()