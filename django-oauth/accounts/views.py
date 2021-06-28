from os import access
from django.shortcuts import redirect, render
import requests
from backend.settings import SOCIAL_OUTH_CONFIG
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import getCodeSerializer, getOAuthSerializer
CODE = ""


@api_view(['GET'])
@permission_classes([AllowAny, ])
def kakaoGetLogin(request):
    CLIENT_ID = SOCIAL_OUTH_CONFIG['KAKAO_REST_API_KEY']
    REDIRET_URL = SOCIAL_OUTH_CONFIG['KAKAO_REDIRECT_URI']
    print("CLIENT_ID", CLIENT_ID)
    print("REDIRET_URL", REDIRET_URL)
    url = "https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={0}&redirect_uri={1}".format(
        CLIENT_ID, REDIRET_URL)
    return redirect(url)


@api_view(['GET'])
@permission_classes([AllowAny, ])
def getCode(reqeust):
    CODE = reqeust.query_params['code']
    return Response({'code': CODE})


@api_view(['POST'])
@permission_classes([AllowAny, ])
def getOAuthRedirect(request):
    res = getOAuthSerializer(data=request.data)
    if res.is_valid():
        return Response(res.data)


@api_view(['POST'])
@permission_classes([AllowAny, ])
def getTokenOAuth(request):
    url = "https://kauth.kakao.com/oauth/token"
    value = getCodeSerializer(data=request.data)
    if value.is_valid():
        CODE = value.validated_data['code']
        print("CODE", CODE)
        res = {
            'grant_type': 'authorization_code',
            'client_code': SOCIAL_OUTH_CONFIG['KAKAO_REST_API_KEY'],
            'redirect_url': SOCIAL_OUTH_CONFIG['KAKAO_REDIRECT_URI'],
            'client_secret': SOCIAL_OUTH_CONFIG['KAKAO_SECRET_KEY'],
            'code': CODE
        }
        print("data : ", res)
        response = requests.post(url=url,data=res)
        return Response(response.text)
