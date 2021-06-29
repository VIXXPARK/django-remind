import requests
url = "https://kauth.kakao.com/oauth/token"
res = {
    'grant_type': "authorization_code",
    'client_id': "af24b46746928ced4a24848039817dd0",
    'redirect_url': "http://localhost:8000/accounts/kakao/login/callback/",
    'code': "euVn6zUOcFgX_1B2w1KQsBJ9Z5SgSrnEBHDBSVtzYfnrt3X8aWOBjqV2OcOM0nxeKMDy-gopyNkAAAF6VR0dzg"
}
headers = {
    'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
}
response = requests.post(url, data=res)
token = response.json()
print(token)
